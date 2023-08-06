import argparse
import logging
import traceback
import requests
import yaml
import openpyxl
import pkg_resources

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

queries_path = pkg_resources.resource_filename('newrelic_data_exporter', 'queries.yml')
resources_path = pkg_resources.resource_filename('newrelic_data_exporter', 'resources.yml')

# Load queries from the configuration file
with open(queries_path, 'r') as file:
    queries = yaml.safe_load(file)

# Load resource headers and keys from the configuration file
with open(resources_path, 'r') as file:
    resources = yaml.safe_load(file)


def get_nested_value(item, key):
    keys = key.split('.')
    value = item
    for key in keys:
        value = value.get(key, None)
        if value is None:
            break
    return value


def send_nerdgraph_request(api_key, query):
    headers = {
        'Api-Key': api_key,
        'Content-Type': 'application/json'
    }
    url = 'https://api.newrelic.com/graphql'
    payload = {
        'query': query
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        response_json = response.json()
        if 'data' in response_json and 'actor' in response_json['data']:
            return response_json
        else:
            logger.error(f"Unexpected response structure: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"HTTP error occurred: {e}")
        return None


def export_data(api_key, tag_name, tag_value, workbook, domain):
    # Select the query, headers and keys based on the domain argument
    query_template = queries[domain]
    query = query_template.format(tag_name=tag_name, tag_value=tag_value)
    headers = resources[domain]['headers']
    keys = resources[domain]['keys']

    data = send_nerdgraph_request(api_key, query)

    if data and 'data' in data:
        data = data['data']['actor']['entitySearch']['results']['entities']

    else:
        data = []
        logger.error(f"No data received for tag: {tag_name}:{tag_value}")

    sheet_name = f"{tag_name}_{tag_value}"
    sheet = workbook.create_sheet(sheet_name)
    sheet.append(headers)

    for item in data:
        row = [get_nested_value(item, key) for key in keys]
        sheet.append(row)

    logger.info(f"Exported data for tag: {tag_name}:{tag_value}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', choices=['all', 'apm', 'synth'], required=True, help='the domain of the resources')
    parser.add_argument('-o', '--output', default='newrelic_export.xlsx', help='the output Excel file name')
    parser.add_argument('-c', '--config',  help='Path to the configuration file', required=True)

    args = parser.parse_args()

    # Load account data from the configuration file
    with open(args.config, 'r') as file:
        account_data = yaml.safe_load(file)

    workbook = openpyxl.Workbook()

    for account in account_data:
        for tag in account['tags']:
            tag_name = tag['name']
            tag_value = tag['value']
            export_data(account['api_key'], tag_name, tag_value, workbook, args.domain)

    try:
        workbook.save(args.output)
        logger.info(f"Data exported successfully. Output file: {args.output}")
    except Exception as e:
        logger.error(f"Error occurred while saving the Excel file: {str(e)}\n{traceback.format_exc()}")


if __name__ == '__main__':
    main()

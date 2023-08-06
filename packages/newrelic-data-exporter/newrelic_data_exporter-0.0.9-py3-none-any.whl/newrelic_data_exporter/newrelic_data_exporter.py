"""
Script to fetch and export New Relic data based on specific tags.
"""

import argparse
import logging
import traceback
from typing import Dict, Any, Optional

import openpyxl
import pkg_resources
import requests
import yaml
import os

# Constants
API_ENDPOINT = 'https://api.newrelic.com/graphql'
DEFAULT_OUTPUT = 'newrelic_export.xlsx'

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load queries and resources from the configuration files
QUERIES_PATH = pkg_resources.resource_filename('newrelic_data_exporter', 'queries.yml')
RESOURCES_PATH = pkg_resources.resource_filename('newrelic_data_exporter', 'resources.yml')


def load_yaml_file(path: str) -> Dict[str, Any]:
    """
    Load YAML file and return its contents.

    Parameters:
        path (str): Path of the YAML file.

    Returns:
        dict: Contents of the YAML file.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"No such file or directory: {path}")
    with open(path, 'r') as file:
        return yaml.safe_load(file)


QUERIES = load_yaml_file(QUERIES_PATH)
RESOURCES = load_yaml_file(RESOURCES_PATH)


def get_nested_value(item: Dict[str, Any], key: str) -> Any:
    """
    Get nested dictionary value using dot-separated key.

    Parameters:
        item (dict): Dictionary from which value needs to be fetched.
        key (str): Dot-separated key to fetch value.

    Returns:
        any: Value fetched from the dictionary.
    """
    keys = key.split('.')
    for key in keys:
        if not isinstance(item, dict):
            return None
        item = item.get(key)
    return item


def send_nerdgraph_request(api_key: str, query: str) -> Optional[Dict[str, Any]]:
    """
    Send a POST request to the New Relic GraphQL API.

    Parameters:
        api_key (str): API key for New Relic.
        query (str): Query to send in the request body.

    Returns:
        dict: Response from the API.
    """
    headers = {
        'Api-Key': api_key,
        'Content-Type': 'application/json'
    }
    payload = {'query': query}

    try:
        response = requests.post(API_ENDPOINT, headers=headers, json=payload)
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


def create_excel_sheet(workbook: openpyxl.Workbook, data: Dict[str, Any], domain: str, tag_name: str, tag_value: str):
    """
    Create an Excel sheet with data for a specific tag.

    Parameters:
        workbook (openpyxl.Workbook): Workbook to which the sheet will be added.
        data (dict): Data to add to the sheet.
        domain (str): Domain of the resources.
        tag_name (str): Name of the tag.
        tag_value (str): Value of the tag.
    """
    headers = RESOURCES[domain]['headers']
    keys = RESOURCES[domain]['keys']

    sheet_name = f"{tag_name}_{tag_value}"
    sheet = workbook.create_sheet(sheet_name)
    sheet.append(headers)

    for item in data:
        row = [get_nested_value(item, key) for key in keys]
        sheet.append(row)

    logger.info(f"Exported data for tag: {tag_name}:{tag_value}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', choices=['all', 'apm', 'synth'], required=True,
                        help='The domain of the resources')
    parser.add_argument('-o', '--output', default=DEFAULT_OUTPUT, help='The output Excel file name')
    parser.add_argument('-c', '--config', help='Path to the configuration file', required=True)

    args = parser.parse_args()
    account_data = load_yaml_file(args.config)

    workbook = openpyxl.Workbook()

    for account in account_data:
        for tag in account['tags']:
            tag_name = tag['name']
            tag_value = tag['value']

            query_template = QUERIES[args.domain]
            query = query_template.format(tag_name=tag_name, tag_value=tag_value)

            data = send_nerdgraph_request(account['api_key'], query)
            if data and 'data' in data:
                data = data['data']['actor']['entitySearch']['results']['entities']
                create_excel_sheet(workbook, data, args.domain, tag_name, tag_value)
            else:
                logger.error(f"No data received for tag: {tag_name}:{tag_value}")

    try:
        workbook.save(args.output)
        logger.info(f"Data exported successfully. Output file: {args.output}")
    except Exception as e:
        logger.error(f"Error occurred while saving the Excel file: {str(e)}\n{traceback.format_exc()}")


if __name__ == '__main__':
    main()

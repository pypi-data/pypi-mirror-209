# NewRelic Data Exporter

NewRelic Data Exporter is a Python tool designed to streamline the process of extracting data from NewRelic.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Configuration](#configuration)
5. [License](#license)
6. [Contributing](#contributing)

## Getting Started

This tool requires Python 3.7 or newer. Before installing and using this tool, ensure that you have the correct Python version installed.

## Installation

You can install the NewRelic Data Exporter package from PyPI:

```bash
pip install newrelic-data-exporter
```

## Usage

After installation, you can run the NewRelic Data Exporter from the command line:

```bash
newrelic_data_exporter --domain <domain> --output <output file> --config <configuration file>
```

Here, `<domain>` can be `all`, `apm`, or `synth`; `<output file>` is the name of the Excel file to which the data will be exported; and `<configuration file>` is the path to the user-provided YAML configuration file.

## Configuration

The configuration file must be in YAML format. It should contain account data, queries, and resource headers and keys as per the requirements of the NewRelic API. For example:

```yaml
accounts:
  - api_key: "<your-api-key>"
    tags:
      - name: "<tag-name>"
        value: "<tag-value>"
```

You will need to replace `<your-api-key>`, `<tag-name>`, and `<tag-value>` with your own data.

## License

This project is licensed under the MIT License. This allows you to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software under certain conditions. For more information, see the `LICENSE` file in the project root.

## Contributing

Contributions are welcome! Please read the `CONTRIBUTING.md` file for details on our code of conduct, and the process for submitting pull requests to us.

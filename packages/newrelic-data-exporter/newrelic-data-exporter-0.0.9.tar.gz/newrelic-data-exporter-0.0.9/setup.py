from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="newrelic-data-exporter",
    version="0.0.9",
    author="Atheeque Ahmed",
    author_email="hello@atheeque.com",
    description="A tool to export data from New Relic using GraphQL API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atheeque-ahmed/newrelic-data-exporter",
    packages=find_packages(),
    package_data={
        'newrelic_data_exporter': ['queries.yml', 'resources.yml'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'PyYAML',
        'openpyxl'
    ],
    entry_points={
        'console_scripts': [
            'newrelic-data-exporter=newrelic_data_exporter.newrelic_data_exporter:main',
        ],
    },
)

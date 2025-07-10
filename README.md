# Avalara-Platform-Engineer-Take-Home

# Merriam-Webster Dictionary CLI Tool

This is a simple CLI tool that allows users to query the Merriam-Webster dictionary and receive a formatted response with the word definition.

Table of Contents

*   Overview
*   Requirements
*   Installation
*   Usage
*   Build Pipeline
*   Testing
*   Continuous Integration
*   Contributing

Overview

This project is a command-line tool that queries the Merriam-Webster dictionary API and returns a formatted response with the word definition.

Requirements

*   Python 3.9+
*   requests library
*   argparse library

Installation

To install the tool, run the following command:

#pip install -r requirements.txt

Usage

To use the tool, run the following command:

#python merriam_webster_cli.py -k YOUR_API_KEY exercise

Replace "YOUR_API_KEY" with your actual Merriam-Webster API key.

Build Pipeline

The build pipeline is configured using a GNU Makefile. To build the tool, run:

make build

Testing

The test suite is written using the unittest framework. To run the tests, execute:

make test

Continuous Integration

The continuous integration pipeline is set up using GitLab CI/CD. The pipeline consists of the following stages:

*   Build: builds the tool using the Makefile
*   Test: runs the test suite
*   Deploy: produces a runtime artifact

Contributing

Contributions are welcome! To contribute to this project, please fork the repository and submit a pull request with your changes.

API Documentation

The Merriam-Webster API documentation can be found https://dictionaryapi.com/products/api-collegiate-dictionary

Acknowledgments

This project uses the following libraries:

*   [requests](https://requests.readthedocs.io/en/master/)
*   [argparse](https://docs.python.org/3/library/argparse.html)

This `README.md` file provides a comprehensive overview of the project, including installation instructions, usage examples, and information about the build pipeline and testing.

Additional Sections

You can add additional sections to the README.md file as needed, such as:

*   Changelog(CHANGELOG.md)
*   Authors(AUTHORS.md)
*   Acknowledgments(ACKNOWLEDGMENTS.md)

# Data Extractor App

This Python script is designed to extract structured data from PDF files containing information such as Company Identification Number (CIN), email addresses, PAN (Permanent Account Number), phone numbers, dates, and websites. The script utilizes the PyPDF2 library for PDF processing and multiprocessing for efficient extraction from multiple PDFs.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Prerequisites

- Python 3.x
- Required Python libraries (install via `pip install -r requirements.txt`):
  - `selenium`
  - `PyPDF2`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NotShrirang/Data-Extractor-App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Data-Extractor-App
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Edit the `config.json` file to configure URLs for PDFs.

2. Run the main script:

   ```bash
   python main.py
   ```

3. The extracted data will be saved as `output.json` in the project directory.

## Configuration

- **config.json**: This file contains the configuration for the script. It includes the list of URLs for PDFs and page_count.

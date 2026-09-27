# Web Scraping Project — CodeAlpha Task 1
## Overview
This repository contains a Python-based Web Scraping application developed as part of the **CodeAlpha Data Analytics Internship** program. The goal of this project is to automatically extract structured data from a target website and export it into a clean CSV format for analysis.

## Features
- Scrapes product/book information (Titles and Prices) from [Books to Scrape](http://books.toscrape.com/).
- Parses HTML content using `BeautifulSoup`.
- Handles HTTP requests using the `requests` library.
- Structures and exports the collected data into `scraped_data.csv` using `pandas`.

## Technologies & Tools Used
- **Language:** Python 3.13
- **Libraries:** `requests`, `beautifulsoup4`, `pandas`
- **Environment:** Visual Studio Code

## Project Structure
- `scraper.py` — Main Python script containing the web scraping logic.
- `scraped_data.csv` — Extracted dataset containing titles and prices.
- `README.md` — Project documentation and overview.

## How to Run the Project
1. Clone this repository or download the files.
2. Install the required Python packages:
   ```bash
   pip install requests beautifulsoup4 pandas

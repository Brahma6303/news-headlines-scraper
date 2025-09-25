# news-headlines-scraper
A simple Python script that scrapes top news headlines from a public website using requests and BeautifulSoup, and saves them to a .txt file. Great for learning web scraping, HTML parsing, and automation.

#  News Headlines Web Scraper

##  Overview
This Python script automates the process of collecting top news headlines from a public news website. It uses HTTP requests and HTML parsing to extract headline tags and saves them into a `.txt` file for easy access and analysis.

##  Features
- Fetches live HTML content using `requests`
- Parses headline tags (`<h2>`, `<h3>`, etc.) using `BeautifulSoup`
- Saves clean, readable headlines to `headlines.txt`
- Includes error handling for failed requests

##  Tools & Technologies
- Python 3
- `requests` for HTTP GET requests
- `BeautifulSoup` from `bs4` for HTML parsing

##  Files Included
- `news_scraper.py`: Main Python script
- `headlines.txt`: Output file with scraped headlines
- `README.md`: Project documentation

##  How to Run

1. **Install dependencies**:
   ```bash
   pip install requests beautifulsoup4

 2 - **Run the script**:
                python news_scraper.py
  - Check the output:
  - Headlines will be saved in headlines.txt

# QS University Rankings Scraper

## Introduction
This Python web scraping tool allows users to retrieve subject ranking data from the QS World University Rankings website without the need for using Selenium. It offers flexibility in specifying subjects and provides options for fetching comprehensive ranking data, including detailed indicator information.


## Usage
```python
# Import the scraper module
from qs_scraper import get_qs_ranking_data

# Retrieve QS ranking data for Engineering & Technology subject
df = get_qs_ranking_data(subject='engineering-technology', full_view=True)

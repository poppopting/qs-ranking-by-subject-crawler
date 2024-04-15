# QS University Rankings By Subject Cralwer

## Introduction
This Python web scraping tool allows users to retrieve subject ranking data from the QS World University Rankings website without the need for using Selenium. It offers flexibility in specifying subjects and provides options for fetching comprehensive ranking data, including detailed indicator information.


## Usage
This tool can be used in two ways:

1. Importing as a module:

```python
# Import the scraper module
from qs_ranking_crawler import get_qs_ranking_data

# Retrieve QS ranking data for Engineering & Technology subject
df = get_qs_ranking_data(subject='engineering-technology', full_view=True)
```

2. Running as a script:
```python
python qs_ranking_crawler.py --subject='engineering-technology' --full-view      
```

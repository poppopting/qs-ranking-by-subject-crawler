# 2024 QS World University Rankings by Subject Crawler

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

## Result
1. Under Quick-View (without --full-view)
   
|      city      |     country    | overall_score | rank | rank_display |   region    |                                        title                                       |
|:--------------:|:--------------:|:-------------:|:----:|:------------:|:-----------:|:----------------------------------------------------------------------------------:|
|   Cambridge    | United States  |      96.8     |  1   |      1       | North America |                               Massachusetts Institute of Technology (MIT)                                |
|    Stanford    | United States  |      93.8     |  2   |      2       | North America |                                        Stanford University                                        |
|    Berkeley    | United States  |      92.2     |  5   |      5       | North America |                          University of California, Berkeley (UCB)                          |
|   Cambridge    | United States  |      89.8     |  8   |      8       | North America |                                            Harvard University                                            |
|   Pasadena     | United States  |      88.8     |  9   |      9       | North America |                            California Institute of Technology (Caltech)                     
2. Under Full-View (with --full-view)
   
| Academic Reputation Score | Citations per Paper Score | Employer Reputation Score | H-index Citations Score | International Research Network Score | city      | country       | overall_score | rank | rank_display | region       | title                                     |
|--------------------------|---------------------------|---------------------------|-------------------------|---------------------------------------|-----------|---------------|---------------|------|--------------|--------------|-------------------------------------------|
| 100                      | 96.2                      | 97.9                      | 96                      | 81.9                                  | Cambridge | United States | 96.8          | 1    | 1            | North America | Massachusetts Institute of Technology (MIT) |
| 96.1                     | 100                       | 95.3                      | 99                      | 68.5                                  | Stanford  | United States | 93.8          | 2    | 2            | North America | Stanford University                        |
| 94.4                     | 99.4                      | 89.7                      | 97.1                    | 78.9                                  | Berkeley  | United States | 92.2          | 5    | 5            | North America | University of California, Berkeley (UCB)   |
| 82.6                     | 95.1                      | 100                       | 91.1                    | 80.9                                  | Cambridge | United States | 89.8          | 8    | 8            | North America | Harvard University                         |
| 98.9                     | 89.3                      | 86.5                      | 80.9                    | 62.4                                  | Pasadena  | United States | 88.8          | 9    | 9            | North America | California Institute of Technology (Caltech) |



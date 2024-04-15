import pandas as pd
import requests
from bs4 import BeautifulSoup

def parse_indicators(indicators):
  """
    Parse indicators column from JSON format into a DataFrame.

    Parameters:
        Indicators (list): List of indicators in JSON format. 
        For exmaple: 
            "scores": [
                {
                  "indicator_id": "76",
                  "indicator_name": "Academic Reputation",
                  "rank": "1",
                  "score": "100"
                },
                {
                  "indicator_id": "77",
                  "indicator_name": "Employer Reputation",
                  "rank": "1",
                  "score": "100"
                },
                ...
              ]

    Returns:
        Series: Series containing indicator scores.

  """
  info = pd.DataFrame()
  for indicator in indicators:
    # info[indicator["indicator_name"] + " Rank"] = [indicator["rank"]]
    info[indicator["indicator_name"] + " Score"] = [indicator["score"]]
  return info.squeeze()

def get_qs_ranking_data(subject='engineering-technology', full_view=False, **kwargs):
  """
    Get QS World University Rankings data for a specific subject. Ref: from https://www.topuniversities.com/university-subject-rankings

    Args:
        subject (str): The subject for which you want to retrieve rankings. Default is 'engineering-technology'.
        full_view (bool): Whether to retrieve full view data, including score details like Academic Reputation, Employer Reputation, Citations per Paper, H-index Citations, and International Research Network. Default is False.
        **kwargs: Additional keyword arguments for customization. 

    Returns:
        DataFrame: DataFrame containing QS rankings data.

    Example:
        # Retrieve QS ranking data for Engineering & Technology subject
        df = get_qs_ranking_data(subject='engineering-technology', full_view=True)
  """
  subject_url = f'https://www.topuniversities.com/university-subject-rankings/{subject}'

  subject_response = requests.get(subject_url)
  subject_soup = BeautifulSoup(subject_response.content, 'html.parser')
  subject_nid = subject_soup.find('article').get('data-history-node-id')

  query_info = {
      'nid': subject_nid,
      'page': kwargs.get('page', ''),
      'items_per_page': kwargs.get('items_per_page', '15'),
      'tab': 'indicators' if full_view else '',
      'region': kwargs.get('region', ''),
      'countries': kwargs.get('countries', ''),  # please use country code aplha-2 code, ex:us, ca. Ref:https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
      'cities': kwargs.get('cities', ''),   
      'search': kwargs.get('search', ''),
      'star': kwargs.get('star', ''),
      'sort_by': 'overallscore',
      'order_by': 'asc',
      'program_type': ''
  }

  ranking_endpoint = 'https://www.topuniversities.com/rankings/endpoint'
  ranking_response = requests.get(ranking_endpoint, params=query_info)
  ranking_data = pd.DataFrame(ranking_response.json()['score_nodes'])


  if full_view:
    indicators_data = ranking_data['scores'].apply(parse_indicators)
    ranking_data = pd.concat([ranking_data, indicators_data], axis=1)
    ranking_data.drop(columns=['scores'], inplace=True)

  return ranking_data


if __name__ == '__main__':

    SUBJECT = 'data-science-artificial-intelligence'
    REGION = 'North America'
    COUNTRIES = 'us,ca'
    FULL_VIEW = False

    df = get_qs_ranking_data(subject=SUBJECT, region=REGION, countries=COUNTRIES, full_view=FULL_VIEW)
    unrelated_cols = ['score_nid', 'nid', 'advanced_profile', 'core_id', 'path', 'logo', 'stars', 'dagger', 'redact']
    df = df[df.columns.difference(unrelated_cols)]
    df.to_csv('{0}-{1}-{2}.csv'.format(SUBJECT, REGION, COUNTRIES.replace(',', '')), index=False)
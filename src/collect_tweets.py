# Arman Izadi
from os import path
import datetime
import requests
import pandas as pd
import argparse


# Hardcoded bearer_token for now
bearer_token = "AAAAAAAAAAAAAAAAAAAAAB%2FKVgEAAAAAuvlm7K%2BW7FW9nJhP82%2FOM%2BMYsXc" \
               "%3D6Tiv1QcsJuH5L4T2DPBbxRcVb33G8EsaSs2i02qTGjGt9aouxS"
# bearer_token = os.environ.get("BEARER_TOKEN")
date_today = datetime.datetime.fromisoformat((datetime.date.today() - datetime.timedelta(days=3)).isoformat()).isoformat(timespec="seconds")+'Z'

# Hardcoded domain and entity key for news.covid19
query_params = {'query': '(COVID OR COVID 19 OR #covid OR #covid-19 OR #covid19) -(tortilla blanket)'
                         'context:123.1220701888179359745 -is:reply -is:retweet -is:quote -has:links lang:en',
                'tweet.fields': 'created_at,geo',
                'expansions': 'geo.place_id',
                'place.fields': 'country',
                'max_results': 100,
                'start_time': date_today}

search_url = "https://api.twitter.com/2/tweets/search/recent"


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    # json_obj = json.dumps(json_response, indent=4, sort_keys=True)
    json_response = run_pagination(json_response, search_url)
    dump_to_csv(json_response)


def run_pagination(first_response, url):
    """
    Method to call the defined query 10 times using Twitter API pagination to avoid duplicates
    :param first_response: [dict] of the initial query result
    :param url: API endpoint URL
    :return: [dict] new value for json_response
    """
    next_query = query_params
    for i in range(9):
        if 'next_token' in first_response['meta']:
            next_query['next_token'] = first_response['meta']['next_token']
            next_json_response = connect_to_endpoint(url, next_query)
            for tweet in next_json_response['data']:
                first_response['data'].append(tweet)
            if 'next_token' in next_json_response['meta']:
                first_response['meta']['next_token'] = next_json_response['meta']['next_token']
            else:
                first_response['meta'].pop('next_token', None)

    return first_response


def get_output_path():
    """
    Basic argparse method for output filepath
    :return: Absolute Path of the output csv file
    """
    # Set up for CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Output filepath", required=True)
    args = parser.parse_args()
    return path.abspath(args.output)


def dump_to_csv(json_dict):
    """
    Added by me to parse twitter api response and format to csv using pandas
    :param json_dict: py dict of the json response of twitter api (before json.dumps
    :return: null
    """
    output_path = get_output_path()
    pandas_dict = {
        'id': [],
        'created_at': [],
        'text': [],
        'topic': [],
        'sentiment': []
    }
    for tweet in json_dict['data']:
        pandas_dict['id'].append(tweet['id'])
        pandas_dict['created_at'].append(tweet['created_at'])
        tweet['text'] = tweet['text'].replace('\n', ' ')
        pandas_dict['text'].append(tweet['text'])

    df = pd.DataFrame(pandas_dict)
    df.to_csv(output_path, mode='w', encoding='utf-8', line_terminator="")


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    Straight from Twitter API example code
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "COMP598_Final_Project_1"
    return r


def connect_to_endpoint(url, params):
    """
    From Twitter API Example code
    :param url: search url endpoint - hardcoded to search/recent
    :param params: parameters incl. query, tweet.fields, etc.
    :return: json response
    """
    response = requests.get(url, auth=bearer_oauth, params=params)
    # print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


if __name__ == '__main__':
    main()

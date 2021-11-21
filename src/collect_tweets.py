# Arman Izadi
import json
from os import path, walk
import datetime
import requests
import pandas as pd
import argparse


# Hardcoded bearer_token for now
bearer_token = "AAAAAAAAAAAAAAAAAAAAAB%2FKVgEAAAAAuvlm7K%2BW7FW9nJhP82%2FOM%2BMYsXc" \
               "%3D6Tiv1QcsJuH5L4T2DPBbxRcVb33G8EsaSs2i02qTGjGt9aouxS"
# bearer_token = os.environ.get("BEARER_TOKEN")
date_today = datetime.datetime.fromisoformat(datetime.date.today().isoformat()).isoformat(timespec="seconds")+'Z'

# Hardcoded domain and entity key for news.covid19
query_params = {'query': 'Canada (COVID OR COVID 19 OR #covid OR #covid-19 OR #covid19) '
                         'context:123.1220701888179359745 -is:retweet lang:en',
                'tweet.fields': 'created_at,geo',
                'expansions': 'geo.place_id',
                'place.fields': 'country',
                'max_results': 100,
                'start_time': date_today}

search_url = "https://api.twitter.com/2/tweets/search/recent"


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    json_obj = json.dumps(json_response, indent=4, sort_keys=True)
    dump_to_csv(json_response, json_obj)


def get_output_path():
    # Set up for CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Output filepath", required=True)
    args = parser.parse_args()
    return path.abspath(args.output)


def dump_to_csv(json_dict, json_object):
    output_path = get_output_path()
    pandas_dict = {
        'id': [],
        'created_at': [],
        'text': []
    }
    for tweet in json_dict['data']:
        pandas_dict['id'].append(tweet['id'])
        pandas_dict['created_at'].append(tweet['created_at'])
        pandas_dict['text'].append(tweet['text'])

    df = pd.DataFrame(pandas_dict)
    print(df.head())
    df.to_csv(output_path, mode='w', encoding='utf-8', line_terminator="")


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "COMP598_Final_Project_1"
    return r


def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


if __name__ == '__main__':
    main()

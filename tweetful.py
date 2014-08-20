import requests
import argparse
import sys
 
import authorization
from urls import *
 
def main():
    """ Main function """
    auth = authorization.authorize()
 
    response = requests.get(TIMELINE_URL, auth=auth)
    print json.dumps(response.json(), indent=4)
 
if __name__ == "__main__":
    main()

# Sets up argparse input
parser = argparse.ArgumentParser()
parser.add_argument(username="Twitter Handle", help="enter the TWitter Handle you want data on",type=len)
args = parser.parse_args()


def twittertimeline():
	""" Calls Twitter API to get most recent user mentions on Twitter """
	timeline = https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=username

    print timeline

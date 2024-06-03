import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_user_tweets(username, num_tweets=5, mock: bool = True):
    """scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (related to now), "text", and "url"
    """

    if mock:
        twitter_url = "https://gist.githubusercontent.com/emarco177/827323bb599553d0f0e662da07b9ff68/raw/57bf38cf8acce0c87e060f9bb51f6ab72098fbd6/eden-marco-twitter.json"
        response = requests.get(
            twitter_url,
            timeout=10
        )

    # else:
    #     # todo : implement this

    tweets = response.json()
    tweet_list = []
    for tweet in tweets:
        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet['id']}"
        tweet_list.append(tweet_dict)
        
            
    return tweet_list

if __name__ == "__main__":
    tweets  = scrape_user_tweets(username="EdenEmarco177")
    print(tweets)
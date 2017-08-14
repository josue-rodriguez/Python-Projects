import requests
import time
import tweepy


def get_api(vals):
  auth = tweepy.OAuthHandler(vals['consumer_key'], vals['consumer_secret'])
  auth.set_access_token(vals['access_token'], vals['access_token_secret'])
  return tweepy.API(auth)


def tweet(title):
  vals = {
    "consumer_key"        : "VALUES",
    "consumer_secret"     : "VALUES",
    "access_token"        : "VALUES",
    "access_token_secret" : "VALUES"
    }

  api = get_api(vals)
  tweet = title
  status = api.update_status(status=tweet)

  
def check_new(check):
    while True:
        try:
            r = requests.get(r"https://www.reddit.com/r/todayilearned/new/.json")

            title = data['data']['children'][0]['data']['title']

            if title == check:
                time.sleep(30)
                continue
            else:
                break
        except:
            continue


def tweet_til():
    while True:
        try:
            r = requests.get(r"https://www.reddit.com/r/todayilearned/new/.json")

            data = r.json()

            title = data['data']['children'][0]['data']['title']
            check = title

            title = title.split()

            for word in title[0:2]:
                if word.lower() in ['til', 'that', 'about']:
                    title.remove(word)

            title = ' '.join(title)

            if len(title) <= 140:
                tweet(title)
            else:
                pass

            time.sleep(60*15)

            check_new(check)

        except KeyError:
            continue


tweet_til()

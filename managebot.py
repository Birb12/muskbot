consumer_key = "woomp"
consumer_secret = "wamp"

access_token = "gloop"
access_secret = "glop"

def tweets():
    tweet = generate_tweet()
    return tweet

def format_tweet(tweet):
    return {"text": "{}".format(tweet)}

def connect_to_oauth(consumerkey, consumersecret, accesstoken, accesssecret):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(consumerkey, consumersecret, accesstoken, accesssecret)
    return url, auth

def hello_pubsub():
   tweet = tweets()
   payload = format_tweet(tweet)
   url, auth = connect_to_oauth(
       consumer_key, consumer_secret, access_token, access_secret
   )
   request = requests.post(
       auth=auth, url=url, json=payload, headers={"Content-Type": "application/json"}
   )

   print(request)

hello_pubsub()

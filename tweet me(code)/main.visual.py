import sys
try:
  import tweepy
except:
  print("Please open the Shell and run 'social_install' script")
  sys.exit(1)

from wyliodrin import *

import random
from threading import Timer

previousRead = None
item = None

twitter_key = 'UpavQfaridl0wQx9qySAI9Uad'
twitter_secret = 'pR32xNAXJS2d22tWxZiRiS7Jw2BCW5wRNdYJJkWHZeYEyzYxSb'
twitter_token = '718371405616820225-T8Eonb9E185onRWfEDqAafQRDDFlfcT'
twitter_secretToken = 'kDFz8olPLTdq3ncKhBWtQupKOLmrvjcItNsZ6xnQsY46A'

pinMode (2, 0)

def twitterFunction(cKey, cSecret, aToken, aTSecret):
  auth = tweepy.OAuthHandler(cKey, cSecret)
  auth.set_access_token(aToken, aTSecret)
  twitter_tweet = tweepy.API(auth)
  return twitter_tweet


previousRead = 1
def loopCode():
  global previousRead, item
  sendSignal('Water_sensor', digitalRead (2))
  if (digitalRead (2)) == 0:
    if previousRead == 1:
      item = 'I\'m empty 99'
      item = str(item) + str(random.randint(1, 100))
      twitter_tweet = twitterFunction(twitter_key, twitter_secret, twitter_token, twitter_secretToken)
      twitter_tweet.update_status(str(item))
      print('Empty')
  elif (digitalRead (2)) == 1:
    if previousRead == 0:
      twitter_tweet = twitterFunction(twitter_key, twitter_secret, twitter_token, twitter_secretToken)
      twitter_tweet.update_status(str('im full 6'))
      print('Full')
  previousRead = digitalRead (2)
  Timer(10, loopCode).start()
loopCode()

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:28:33 2019

This script sets up tweepy and hears twitter streams
Before launching the streaming, a sqlite database is created
All the tweets listened is pushed into the database

Note:
    this script is initialized for running in Docker containers, if you tend to run this script locally
    uncomment line 47-52 to create a database

@author: Shihao Ran
         shihao1007@gmail.com
         STIM Laboratory
"""

# import packages
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from slistener import SListener
from urllib3.exceptions import ProtocolError
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from keys_secret import consumer_key, consumer_secret
from keys_secret import access_token, access_token_secret

# consumer key authentication
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# set up the API with the authentication handler
api = API(auth)

# set up words to hear
keywords_to_hear = ['#Fortnite',
                    '#LeagueOfLegends',
                    '#ApexLegends',
                    ]

# instantiate the SListener object
listen = SListener(api)

# instantiate the stream object
stream = Stream(auth, listen)

# # create a engine to the database
# engine = create_engine("sqlite:///tweets.sqlite")
# # if the database does not exist
# if not database_exists(engine.url):
#     # create a new database
#     create_database(engine.url)

# begin collecting data
while True:
    # maintian connection unless interrupted
    try:
        stream.filter(track=keywords_to_hear)
    # reconnect automantically if error arise
    # due to unstable network connection
    except (ProtocolError, AttributeError):
        continue

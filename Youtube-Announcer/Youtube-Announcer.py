import discord
from discord.ext import commands


#!/usr/bin/python

import httplib2
import os
import sys

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = "client_secrets.json"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the {{ Cloud Console }}
{{ https://cloud.google.com/console }}

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))
#import gdata.youtube
#import gdata.youtube.service

#yt_service = gdata.youtube.service.YouTubeService()

# Turn on HTTPS/SSL access.
# Note: SSL is not available at this time for uploads.
#yt_service.ssl = True

#yt_service.developer_key = 'AIzaSyAie7tXECe8LZlvVfQGeq-pyj3G3J4hHM0'
#yt_service.client_id = 'youtube-api-185317'

#def GetAndPrintUserUploads(username):
  #yt_service = gdata.youtube.service.YouTubeService()
  #uri = 'http://gdata.youtube.com/feeds/api/users/%s/uploads' % username
  #PrintVideoFeed(yt_service.GetYouTubeVideoFeed(uri))


class Youtube_Announcer: #Here
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
    def youtube(username):
      pass
      
    @commands.command()
    async def update(self):
        """This does stuff!"""

        #Your code will go here
        username = 'GrimBOMB'
        #printThis = GetAndPrintUserUploads(username)
        #await self.bot.say(printThis)
        await self.bot.say(username)
        #await self.bot.say("I can do stuff!")

def setup(bot):
    bot.add_cog(Youtube_Announcer(bot)) #Here

import os
from slack import RTMClient
from slack.errors import SlackApiError
from scraper import *

REPLY = ""
INTEXT = False

def handleMensCricket(data):
    global INTEXT
    global REPLY
    REPLY = ""
    if 'test ranking' in data['text']:
        INTEXT = True
        rankings = cricketRankings("https://www.icc-cricket.com/rankings/mens/team-rankings/test")
        REPLY = "Test Rankings: \n"
    elif 'odi ranking' in data['text']:
        INTEXT = True
        rankings = cricketRankings("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
        REPLY = "ODI Rankings: \n"
    elif 't20 ranking' in data['text']:
        INTEXT = True
        rankings = cricketRankings("https://www.icc-cricket.com/rankings/mens/team-rankings/t20i")
        REPLY = "T20 Rankings: \n"
    if (INTEXT):
        for element in rankings[:25]:
            REPLY += '{:<22}{:<22}{:<22}{:<22}{:<22}'.format(element[0], element[1], element[2], element[3], element[4]) + '\n'

def handleNews(data):
    global INTEXT
    global REPLY
    pass


@RTMClient.run_on(event='message')
def say_hello(**payload):
    global INTEXT
    global REPLY
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    channel_id = data['channel']
    handleMensCricket(data)
    if INTEXT == True:
        INTEXT = False
        try:
            response = web_client.chat_postMessage(
                channel=channel_id,
                text=REPLY,
            )
        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            assert e.response["ok"] is False
            assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
            print(f"Got an error: {e.response['error']}")

rtm_client = RTMClient(token=(os.environ["CLASSIC_SLACK_BOT_TOKEN"][1:]))
rtm_client.start()
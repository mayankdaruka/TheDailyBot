import os
from slack import RTMClient
from slack.errors import SlackApiError
from scraper import *


ICCurl = "https://www.icc-cricket.com/rankings/womens/team-rankings/odi"

@RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    channel_id = data['channel']
    reply = ""
    inText = False
    if 'test ranking' in data['text']:
        inText = True
        test_rankings = cricketRankings("https://www.icc-cricket.com/rankings/mens/team-rankings/test")
        reply = "Test Rankings: \n"
        for element in test_rankings:
            reply += '{:>22}  {:>22}  {:>22}  {:>22}  {:>22}'.format(element[0], element[1], element[2], element[3], element[4]) + '\n'
    elif 'odi ranking' in data['text']:
        inText = True
        odi_rankings = cricketRankings("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
        reply = "ODI Rankings: \n"
        for element in odi_rankings:
            reply += '{:>22}  {:>22}  {:>22}  {:>22}  {:>22}'.format(element[0], element[1], element[2], element[3], element[4]) + '\n'

    if inText == True:   
        user = data['user']
        try:
            response = web_client.chat_postMessage(
                channel=channel_id,
                text=reply,
            )
        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            assert e.response["ok"] is False
            assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
            print(f"Got an error: {e.response['error']}")

rtm_client = RTMClient(token=(os.environ["CLASSIC_SLACK_BOT_TOKEN"][1:]))
rtm_client.start()
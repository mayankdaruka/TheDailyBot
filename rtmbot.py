import os
from slack import RTMClient
from slack.errors import SlackApiError
from bs4 import BeautifulSoup

base_url = "https://www.icc-cricket.com/rankings"

print(os.environ)
@RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    if 'text' in data and 'Hello' in data.get('text', []):
        channel_id = data['channel']
        user = data['user']
        try:
            response = web_client.chat_postMessage(
                channel=channel_id,
                text=f"Hi <@{user}>!",
            )
        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            assert e.response["ok"] is False
            assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
            print(f"Got an error: {e.response['error']}")

rtm_client = RTMClient(token=os.environ["SLACK_BOT_TOKEN"])
rtm_client.start()
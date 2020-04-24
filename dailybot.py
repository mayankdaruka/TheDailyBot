import slack
from slackeventsapi import SlackEventAdapter
import os

slack_bot_token = os.environ['SLACK_BOT_TOKEN']
slack_signing_secret = os.environ['SLACK_SIGNING_SECRET']
client = slack.WebClient(slack_bot_token)
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

# # To handle received message
# @slack_events_adapter.on("message")
# def handle_message(event_data):
#     message = event_data["event"]
#     # Check if message contains a subtype
#     # Examples of subtype: Member joined a channel, file was mentioned in channel, 
#     # group was renamed, message was deleted, group topic was updated etc.
#     if message["subtype"] is None:
#         if "test rankings" in message["text"]:
#             response = "Here are the test rankings: ***insert web scraped data***"
#             client.chat_postMessage(channel=message["channel"], text=response)

# @slack_events_adapter.on("error")
# def error_handler(error):
#     print("Error: " + str(error))


slack_events_adapter.start(port=3000)
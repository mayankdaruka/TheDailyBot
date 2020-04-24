import slack
from slackeventsapi import SlackEventAdapter
import os

slack_bot_token = os.environ['SLACK_BOT_TOKEN']
slack_signing_secret = os.environ['SLACK_SIGNING_SECRET']
client = slack.WebClient(slack_bot_token)
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

@slack_events_adapter.on("message")
def handle_message(event_data):
    pass
import slack
import os

client = slack.WebClient(os.environ['SLACK_BOT_TOKEN'], timeout=30)

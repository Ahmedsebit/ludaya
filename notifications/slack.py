from slackclient import SlackClient
import os
from decorators import async

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

@async
def async_create_channel(name):
    sc.api_call(
    "channels.create",
    name=name,
    is_private=True
    )

def create_channel(name):
    async_create_channel(name)


@async
def async_add_user_to_channel(channel,name):
    sc.api_call(
    "channels.invite",
    channel=channel,
    user=name
    )

def add_user_to_channel(channel,name):
    async_add_user_to_channel(channel, name)

@async
def async_send_channel_messages(channel, message):
    sc.api_call(
    "chat.postMessage",
    channel="#"+channel,
    text=message
    )

def send_channel_messages(channel, message):
    async_send_channel_messages(channel, message)


@async
def asyn_send_dm(email, message):
    user_slack_id = get_user(email)
    if user_slack_id:
        sc.api_call(
        "chat.postMessage",
        channel=user_slack_id,
        text=message
        ) 

def send_dm(email, message):
    asyn_send_dm(email, message)


def get_user(email):
    all_users = sc.api_call('users.list')
    if 'member' in all_users:
        for user in all_users['members']:
            if 'email' in user['profile']:
                if user['profile']['email'] == email:
                    return user['id']


def get_channel_id(name):
    all_channels = sc.api_call('channels.list')
    for channel in all_channels['channels']:
        if channel['name'] == name:
            return channel['id']


message = ">>> Testing *right now!"

send_dm('ahmedamedy@gmail.com', 'test')
send_channel_messages('ludayatesting9', message)

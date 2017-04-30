import json
from channels.channel import Group

LIVESTREAM = 'livestream'

# Connected to websocket.connect
def ws_connect(message):
    # Accept connection
    message.reply_channel.send({"accept": True})
    # Add to our broadcast stats group
    Group(LIVESTREAM).add(message.reply_channel)

# Connected to websocket.receive
def ws_message(message):
    pass
    #Group(LIVESTREAM).send({'text': json.dumps({'message': message.content['text'],
    #                                        'sender': message.reply_channel.name})})

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group(LIVESTREAM).discard(message.reply_channel)
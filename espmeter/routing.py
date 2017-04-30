from channels.routing import route

channel_routing = {
    'websocket.connect': 'meter.consumers.ws_connect',
    'websocket.receive': 'meter.consumers.ws_message',
    'websocket.disconnect': 'meter.consumers.ws_disconnect',
}
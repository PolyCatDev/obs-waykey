from . import keybind
from . import client

def record(name: str):
    if keybind == name:
        client.toggle_record()

def record_pause(name: str):
    if keybind == name:
        client.toggle_record_pause()

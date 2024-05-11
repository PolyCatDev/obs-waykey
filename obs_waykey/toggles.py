import obsws_python as obs
import sys

keybind = sys.argv[1]
client = obs.ReqClient()

def record(name: str):
    if keybind == name:
        client.toggle_record()

def record_pause(name: str):
    if keybind == name:
        client.toggle_record_pause()

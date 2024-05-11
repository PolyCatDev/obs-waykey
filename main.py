import obsws_python as obs
import sys

keybind = sys.argv[1]

client = obs.ReqClient()

if keybind == "toggle-rec":
    client.toggle_record()
elif keybind == "toggle-rec-pause":
    client.toggle_record_pause()
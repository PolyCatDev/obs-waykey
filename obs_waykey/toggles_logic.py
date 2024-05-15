###############################################################################
# This is the main file with functions for each toggle.                       #
# Quick Tip: "name" is a variable passed in by the toggle_ignition.py script. #
###############################################################################

import obsws_python as obs
import argparse

# Sets up argumet parser
parser = argparse.ArgumentParser(description="Global hotkey workaround for obs")
parser.add_argument("-t", "--toggle", type=str, help="Flag for specyfing triggers")
parser.add_argument("-w", "--password", type=str, help="Flag for setting password")
args = parser.parse_args()

# Sets up needed variables
client = obs.ReqClient(host='localhost', port=4455, password=args.password, timeout=3)
toggle = args.toggle

def record(name: str):
    if toggle == name:
        client.toggle_record()

def record_pause(name: str):
    if toggle == name:
        client.toggle_record_pause()

# TODO add more toggles
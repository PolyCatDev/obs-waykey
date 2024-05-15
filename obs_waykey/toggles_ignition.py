###############################################################
# This file is first ran when using the obs-waykey command    #
# This file is where you can change the name of the triggers. #
###############################################################

from .toggles_logic import *

def ignite():
    record("toggle-record")
    record_pause("toggle-record-pause")

# TODO Add more triggers
import obs_waykey as obs

# Modify action names here
def ignite():
    obs.record("toggle-rec")
    obs.record_pause("toggle-rec-pause")
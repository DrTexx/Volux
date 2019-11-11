from cpaudio import MixerController
from time import sleep

mixer = MixerController()

old_vol = mixer.gvol()
old_mute_state = mixer.gmute()

print("old volume: {}".format(old_vol))
print("old mute state: {}".format(old_mute_state))

print(); sleep(1)

print("setting volume to 80%")
mixer.svol(80)
print("volume reported: {}".format(mixer.gvol()))

print(); sleep(1)

print("setting mute...")
mixer.smute(True)
print("mute state reported: {}".format(mixer.gmute()))

print(); sleep(1)

print("reverting to original values...")

print(); sleep(1)

mixer.svol(old_vol)
mixer.smute(old_mute_state)
print("volume reported: {}".format(mixer.gvol()))
print("mute state reported: {}".format(mixer.gmute()))

print(); sleep(1)

print("finished!")

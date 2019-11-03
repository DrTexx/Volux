import cpaudio

# create mixer object
mixer = cpaudio.MixerController()

# print volume
print("volume:",mixer.gvol())

# print mute state
print("mute state:",mixer.gmute())

# loop for set volume or mute
while True:
    print("v = change volume, m = change mute state, e = exit")
    option = str(input("which would you like to change? [v/m/e]:")).lower()
    if option == "v":
        newvol = int(input("new volume?:"))
        mixer.svol(newvol)
    elif option == "m":
        newmute = str(input("muted?:"))

        print(type(newmute))
        mixer.smute(newmute)
    elif option == "e":
        print("exiting...")
        break
    else:
        print("invalid option!")

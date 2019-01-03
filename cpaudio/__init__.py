# determine the platform

import platform
platform = platform.system()

# load the necessary classes / packages / whatever

if platform == "Windows":
    from cpaudio.Platforms.Windows import MixerController

elif platform == "Darwin":
    from cpaudio.Platforms.Darwin import MixerController

elif platform == "Linux":
    from cpaudio.Platforms.Linux import MixerController

else:
    raise Exception("Platform not recognised!")

# create common aliases for them all regardless of platform
    # tool 1
    # tool 2
    # tool 3
    # etc.
# determine the platform

import platform

platform = platform.system()

# load the necessary classes / packages / whatever

if platform == "Windows":

    pass
    # from cpaudio.Platforms.Windows import #[ADD ME]

elif platform == "Darwin":

    pass
    # from cpaudio.Platforms.Darwin import [ADD ME]

elif platform == "Linux":

    pass
    # from cpaudio.Platforms.Linux import [ADD ME]

else:
    raise Exception("Platform not recognised!")

# create common aliases for them all regardless of platform
# tool 1
# tool 2
# tool 3
# etc.

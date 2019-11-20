import logging
import volux

# create logger with 'spam_application'
log = logging.getLogger("volux")
log.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler("volux.log")
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
log.addHandler(fh)
log.addHandler(ch)

log.info("creating an instance of volux.Auxiliary")
vlx = volux.VoluxOperator()
log.info("created an instance of volux.Auxiliary")
log.info("calling volux.Auxiliary.do_something")

try:
    vlx.start_sync()
except:
    log.error("it screwed up...")

log.info("finished volux.Auxiliary.do_something")
log.info("calling volux.some_function()")
try:
    volux.add_module("kek it's a string")
except:
    log.error("that didn't work :(")
log.info("done with volux.some_function()")


# FORMAT = '[%(asctime)-15s][%(levelname)s] %(message)s'
# logging.basicConfig(level=logging.DEBUG)

# log = logging.getLogger('volux')
# log.setLevel(logging.INFO)
#
# log.debug("here's something for debugging")
# log.info("here's some info")
# log.warning("here's a warning!")
# log.error("an error :(")
# log.critical("HERE'S SOME REAL CRITICAL STUFF!")

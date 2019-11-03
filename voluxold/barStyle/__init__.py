barstyles = {
    "Volume": {
        "name": "volume",
        "kwargs": {"background": "GREEN"}
    },
    "Muted": {
        "name": "muted",
        "kwargs": {"background": "RED"}
    },
    "Brightness": {
        "name": "brightness",
        "kwargs": {"background": "BLUE"}
    },
    "Unknown": {
        "name": "unknown",
        "kwargs": {"background": "GREY"}
    }
}

def add_bar_styles(tkstyleObject, bstyles):

    for bstyle in bstyles:
        bstyle_id = bstyles[bstyle]["name"] + ".TFrame"
        print(bstyle_id,"style added!")
        tkstyleObject.configure(bstyle_id,**bstyles[bstyle]["kwargs"])



# def _add_styles(tkstyle_object):
#     tkstyle_object.configure("volume.TFrame", background="GREEN")
#
# class barMode:
# 
#     def __init__(self, tkstyleObject, name, color):
#         
#         tkstyleObject.configure(name,background=color)
# 
#         "volume.TFrame",background="GREEN"


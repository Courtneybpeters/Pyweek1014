import json, os
CONFIGFILE = "config.json"

class Config(object):
    def __init__(self):
        if os.path.exists(CONFIGFILE):
            self.settings = self._load(CONFIGFILE)
        else:
            #define default config here
            self.settings = dict()
            self.settings["display_width"] = 1920
            self.settings["display_height"] = 1080
            self.settings["width"] = 1920
            self.settings["height"] = 1080
            self.settings["fullscreen"] = False
            self.settings['show_fps'] = True
            self.settings["fps"] = 60

            colors = dict()
            colors["textcolor"] = (255, 255, 255)
            colors["bgcolor"] = (25, 0, 51)
            colors["hovercolor"] = (0, 255, 0)
            self.settings["colors"] = colors
            self.save()

    def _load(self, filename):
        with open(CONFIGFILE, "r") as myfile:
            return json.loads(myfile.read())

    def _save(self, filename):
        f = file(filename, "w")
        f.write(json.dumps(self.settings))
        f.close()


    def save(self):
        self._save(CONFIGFILE)

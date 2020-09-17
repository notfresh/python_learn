import yaml
import os
class ConfigManager:

    def __init__(self):
        self.file = os.path.join(os.environ['HOME'], ".md-tool-config.yml")
        if not os.path.exists(self.file):
            file = open(self.file, "w")
            file.close()
        self.dataMap = {}

    def read(self, key):
        f = open(self.file)
        self.dataMap = yaml.load(f)
        f.close()
        return self.dataMap.get(key, '')

    def write(self, key, value):
        f = open(self.file, "w+")
        self.dataMap[key] = value
        yaml.dump(self.dataMap, f,default_flow_style=False)
        f.close()


if __name__ == '__main__':
    configer = ConfigManager()
    configer.write("a", 111)
    configer.write("b", 232)

    configer.write("c", 1114)
    configer.write("d", {"d": 111})
    print(configer.read("a"))
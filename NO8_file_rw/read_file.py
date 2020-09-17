import os
file = os.path.join(os.environ['HOME'], ".md-tool-config.yml")
with open(file, "w+") as f:
    f.write("111")

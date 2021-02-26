#This file was somthing i made quickly to help format JSON files whan I was first strting out
#You can use it if you want, just know it won't do anything in the program

import os
import json
list = []
for root, dirs, files in os.walk(""):
    for file in files:
        if file.endswith(".json"):
            path = (os.path.join(root, file))
            if os.path.exists(path):
                with open(path) as f:
                    data = json.load(f)
            with open(path, 'w') as f:
                f.write(json.dumps(data))
print("done")

import json

with open("avatar.json") as f:
    data = json.load(f)

for avatar in data["avatars"]:
    if "Gl".lower() in avatar["name"].lower():
        print(avatar["name"])

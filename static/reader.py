import json

with open("avatar.json") as f:
    data = json.load(f)

# file = open("avatar.json")
# _data = json.load(file)

print(data["avatars"][0])

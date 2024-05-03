from web3 import Web3
import json

file = open("./data.json","r")

data = json.load(file)

a = {}
for i in data:
    cur = data[i]["from"]
    a[cur] = a.get(cur,0) + 1
    cur = data[i]["to"]
    a[cur] = a.get(cur,0) + 1
print(a)
print(len(a))
print(len(data))

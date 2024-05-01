from web3 import Web3
import json

apifile = open("./APIURI.txt")
APIURI = apifile.read().splitlines()[0];

w3 = Web3(Web3.HTTPProvider(APIURI))
print(w3.is_connected())

tokenaddress = Web3.to_checksum_address('0x68749665ff8d2d112fa859aa293f07a622782f38')
tokenabi = []
with open("./erc20abi.json", "r" ) as f:
    tokenabi = json.load(f)

tokencontract = w3.eth.contract(address=tokenaddress, abi=tokenabi)


file = open("./data.json","r")
data = json.load(file)

out = {}

count = 0
for i in data:
    t = (data[i]["from"],data[i]["to"])
    for cur in t:
        if cur not in out:
            out[cur] = tokencontract.functions.balanceOf(cur).call()
    if count % 100 == 0:
        print(str(cur) + ' ' + str(out[cur]))
    count += 1

print(str(out))
with open("./balances.json", "w") as f:
    json.dump(out,f)



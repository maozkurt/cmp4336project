from web3 import Web3
import json
from web3.datastructures import AttributeDict

# get api url from APIURI.txt
apifile = open("./APIURI.txt")
APIURI = apifile.read().splitlines()[0];


w3 = Web3(Web3.HTTPProvider(APIURI))
print(w3.is_connected())

tokenaddress = Web3.to_checksum_address('0x68749665ff8d2d112fa859aa293f07a622782f38')
tokenabi = []
with open("./erc20abi.json", "r" ) as f:
    tokenabi = json.load(f)

tokencontract = w3.eth.contract(address=tokenaddress, abi=tokenabi)

#event_filter = tokencontract.events.Transfer.create_filter(fromBlock=0x0, toBlock=0xffffffffff)
#transactions = event_filter.get_new_entries()

with open("./data.json", "w") as output:
    # api limits us to 10K logs per request.
    transactions = tokencontract.events.Transfer().get_logs(fromBlock=hex(18300000), toBlock=hex(19776867))
    out = {}
    size = len(transactions)
    for i in range(0,size):
        out[str(i)] = dict(transactions[i]["args"])
    jsonout = json.dumps(out)
    output.write(jsonout)

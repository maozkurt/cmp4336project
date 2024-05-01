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

with open("./data.", "w") as output:
    # Get first third of the data, since api limits response size to 10K logs at one request.
    transactions = tokencontract.events.Transfer().get_logs(fromBlock=0x1169F8B, toBlock=0x11E5BB7)
    """for i in transactions:
        output.write(str(i))
        output.write("\n")
    """
    # Second third
    transactions += tokencontract.events.Transfer().get_logs(fromBlock=0x11E5BB8, toBlock=0x1260BC7)
    """for i in transactions:
        output.write(str(i))
       output.write("\n")
    """
    # Last third
    transactions += tokencontract.events.Transfer().get_logs(fromBlock=0x1260BC8, toBlock=0x12DC1E6)
    """for i in transactions:
        output.write(str(i))
        output.write("\n")
    """
    
    #transactions = json.dumps(dict(transactions))
    transactionsjson = Web3.toJson(transactions) # ERROR
    output.write(transactionsjson)

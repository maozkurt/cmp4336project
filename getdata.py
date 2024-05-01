from web3 import Web3

# get api url from APIURI.txt
apifile = open("./APIURI.txt")
APIURI = apifile.readline();


w3 = Web3(Web3.HTTPProvider(APIURI))

tokenaddress = Web3.to_checksum_address('0x68749665ff8d2d112fa859aa293f07a622782f38')
tokenabi = []
tokencontract = w3.eth.contract(address=tokenaddress, abi=tokenabi)

transactions = tokencontract.events.Transfer().getLogs()

with open("./data", "w") as output:
    output.write(transactions)


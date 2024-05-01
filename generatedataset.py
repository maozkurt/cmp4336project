#Generates dataset using data.json & balances.json
import json
from math import sqrt

headers = {"Volume" : 0, "Number_of_Transactions" : 1,
           "Number_of_Received_Transactions" : 2, "Number_of_Sent_Transactions" : 3,
           "Amount Received" : 4, "Amount_Sent" : 5,
           "Mean_of_Received" : 6, "Mean_of_Sent" : 7,
           "Stddev_of_Received" : 8, "Stddev_of_Sent" : 9,
           "Maximum_Amount_of_Sent_&_Received" : 10, "Last_Balance" : 11}

datafile = open("./data.json","r")
rawdata = json.load(datafile)
data2file = open("./balances.json","r")
rawdata2 = json.load(data2file)

address = {}

for i in rawdata:
    if rawdata[i]["from"] not in address:
        address[rawdata[i]["from"]] = len(address)
    if rawdata[i]["to"] not in address:
        address[rawdata[i]["to"]] = len(address)


dataset = {j: [0 for i in headers] for j in address}

for i in rawdata:
    fr = rawdata[i]["from"]
    to = rawdata[i]["to"]
    vol = int(rawdata[i]["value"])
    
    #Volume
    dataset[fr][0] += vol
    dataset[to][0] += vol

    #Number of Transactions
    dataset[fr][1] += 1
    dataset[to][1] += 1

    #Number of Received Transactions
    dataset[to][2] += 1

    #Number of Sent Transactions
    dataset[fr][3] += 1

    #Amount Received
    dataset[to][4] += vol

    #Amount Sent
    dataset[fr][5] += vol
    
    #Maximum Amount of Sent & Received
    dataset[fr][10] = max(dataset[fr][10], vol)
    dataset[to][10] = max(dataset[to][10], vol)

for i in address:
    #Mean of Received
    if dataset[i][2] != 0:
        dataset[i][6] = dataset[i][4] / dataset[i][2]
    #Mean of Sent
    if dataset[i][3] != 0:
        dataset[i][7] = dataset[i][5] / dataset[i][3]


for i in rawdata: 
    fr = rawdata[i]["from"]
    to = rawdata[i]["to"]
    vol = int(rawdata[i]["value"])
    
    #Stddev of Received preparation
    dataset[to][8] += (vol - dataset[to][6])**2

    #Stddev of Sent preparation
    dataset[fr][9] += (vol - dataset[fr][7])**2

for i in address:
    #Stddevs completed
    if dataset[i][2] != 0:
        dataset[i][8] = sqrt(dataset[i][8]/dataset[i][2])
    if dataset[i][3] != 0:
        dataset[i][9] = sqrt(dataset[i][9]/dataset[i][3])

#Balances
for i in rawdata2:
    try:
        dataset[i][11] = rawdata2[i]
    except KeyError:
        print("Balance's address doesn't exist in dataset? How???")


#Generate CSV

with open("./dataset.csv","w") as datasetfile:
    datasetfile.write("Address,")
    count = 0
    for i in headers:
        datasetfile.write(i)
        if count != len(headers)-1 :
            datasetfile.write(",")
        else:
            datasetfile.write("\n")
        count += 1

    for i in dataset:
        datasetfile.write(i + ",")
        count = 0
        for j in dataset[i]:
            datasetfile.write(str(j))
            if count != len(dataset[i])-1 :
                datasetfile.write(",")
            else:
                datasetfile.write("\n")
            count += 1



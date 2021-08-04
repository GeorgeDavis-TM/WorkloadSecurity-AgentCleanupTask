import json
import urllib3

def httpRequest(c1wsApiKey, httpMethod, uri, data):

    headers = {
        "Content-Type": "application/json",
        "api-version": "v1",
        "api-secret-key": c1wsApiKey
    }

    url = "https://cloudone.trendmicro.com/api" + uri

    http = urllib3.PoolManager()

    if data != None:
        r = http.request(httpMethod, url, headers=headers, body=json.dumps(data))
    else:
        r = http.request(httpMethod, url, headers=headers)
    
    return json.loads(r.data)
    
def deleteComputer(c1wsApiKey, computerId):

    return httpRequest(c1wsApiKey, "DELETE", "/computers/" + str(computerId), data=None)

def getComputers(c1wsApiKey):

    return httpRequest(c1wsApiKey, "GET", "/computers", data=None)

def main():

    f = open("config.json", "r+")
    configObj = json.loads(f.read())
    f.close()

    targetComputerStatusList = configObj["targetComputerStatusList"]

    computersDict = getComputers(configObj["c1wsApiKey"])

    for computer in computersDict["computers"]:
        for status in computer["computerStatus"]["agentStatusMessages"]:
            if status in targetComputerStatusList:
                print("\n" + str(computer["ID"]) + " - " + str(computer["computerStatus"]["agentStatusMessages"][0]))

                # if computer["ID"] == 4225:
                print("\n\t" + str(deleteComputer(configObj["c1wsApiKey"], computer["ID"])))

    # f = open("computers.json", "w+")
    # f.write(str(computersDict))
    # f.close()

if __name__ == "__main__":
    main()
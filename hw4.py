import requests
import json
def printRepos(un):
    if not isinstance(un, str):
        return "Not a String"
    urlString = "https://api.github.com/users/" + un + "/repos"
    test = requests.get(urlString)
    obj = test.json()
    if not isinstance(obj,list):
        return "User Does not Exist"
    listOfNames = []
    listOfNumbers = []
    finalList = []
    for i in range(len(obj)):
        listOfNames.append(obj[i]["name"])
    for i in range(len(obj)):
        newUrl = "https://api.github.com/repos/" + un + "/" + obj[i]["name"] + "/commits"
        oy = requests.get(newUrl)
        yo = oy.json()
        listOfNumbers.append(len(yo))
    for i in range(len(obj)):
        #print("Repo: " + listOfNames[i] + " Number of commits: " + str(listOfNumbers[i]))
        finalList.append("Repo: " + listOfNames[i] + " Number of commits: " + str(listOfNumbers[i]))
    return finalList

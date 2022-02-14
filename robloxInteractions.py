import requests
from bisect import bisect_left
from functionTools import *

class userInventory:
    def __init__(self, playerID):
        self.playerID = playerID
        self.inventory = ""


    def getInventory(assetType):
        params = {
            'assetTypes': assetType,
            'limit': '100',
            'sortOrder': 'Asc'
        }
        response = requests.get('https://inventory.roblox.com/v2/users/41086276/inventory', params=params)

        jsonResponse = response.json()
        return jsonResponse

    def findAsset(self, assetName, assetType):
        playerInventory = self.getInventory(assetType)
        asset = SearchJSONList(playerInventory, assetName, "name")
        if asset == None:
            return None
        else:
            return asset
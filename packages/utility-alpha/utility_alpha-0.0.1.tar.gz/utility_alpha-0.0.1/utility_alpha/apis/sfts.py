from utility_alpha.apis import constants



"""
* PUT
* /sfts/resync
* Resync Sfts
"""
def updateresyncnfts(self, address = None, network = None, owner = None, token_ids = None):
    if address == None or address == "":
        return "address is required"
    if network == None or network == "":
        return "network is required"
    if network == 0:
         return "network should be greater than zero"
    if owner == None or owner == "":
        return "owner is required"
    if token_ids == None or token_ids == "":
        return "token_ids is required"
  
    body = {
        "address": address,
        "network": network,
        "owner": owner,
        "token_ids": token_ids
      }

    url = "sfts/resync"
    try:
        res = constants.PUT_RESPONSE(url, body, self.apikey)
        print("constants.PUT_RESPONSE")
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res

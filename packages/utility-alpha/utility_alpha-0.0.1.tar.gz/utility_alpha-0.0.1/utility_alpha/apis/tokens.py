from utility_alpha.apis import constants



"""
* PUT
* /tokens/resync
* Resync Tokens
"""
def resynctokens(self, address = None, network = None, owner = None):
    if address == None or address == "":
        return "address is required"
    if network == None or network == "":
        return "network is required"
    if owner == None or owner == "":
        return "owner is required"

    url = "tokens/resync"
    body = {
        "address": address,
        "network": network,
        "owner": owner
    }

    try:
        res = constants.PUT_RESPONSE(url, body, self.apikey)
        print("constants.PUT_RESPONSE")
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res
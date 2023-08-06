from utility_alpha.apis import constants


"""
* GET
* /nfts/{token_id}
* Get Non Fungible Token
"""


def getnfts(self, token_id=None, contract_address=None, network_id=None):
    if token_id == None or token_id == "":
        return "token_id is required"
    if network_id == None or network_id == "":
        return "network_id is required"
    if contract_address == None or contract_address == "":
        return "contract_address is required"

    url = f"nfts/{token_id}?contract_address={contract_address}&network_id={network_id}"
    try:
        res = constants.GET_RESPONSE(url, self.apikey)
        print("constants.GET_RESPONSE")
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res


"""
* PUT
* /nfts/resync
* Resync Nfts
"""


def resyncnfts(self, address=None, network=None, token_ids=None):
    if address == None or address == "":
        return "address is required"
    if network == None or network == "":
        return "network is required"
    if network == 0:
        return "network should be greater than zero"
    if token_ids == None or token_ids == "":
        return "token_ids is required"
    if token_ids.length == 0:
        return "token_ids should be greater than zero"

    body = {
        "address": address,
        "network": network,
        "token_ids": token_ids
    }

    url = "nfts/resync"
    try:
        res = constants.PUT_RESPONSE(url, body, self.apikey)
        print("constants.POST_RESPONSE")
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res
from utility_alpha.apis import constants



"""
* GET
* /wallets/{wallet_address}/nfts
* Get Nfts For Wallet
"""
def nftforwallet(self, wallet_address, network_id, contract_address=None, page=None, limit=None):
    url = f"wallets/{wallet_address}/nfts"
    query = f"?network_id={network_id}"

    if contract_address != None and contract_address != "":
        query += f"&contract_address={contract_address}"
    if page != None and page != "":
        query += "&page={page}"
    if limit != None and limit != "":
        query += "&limit={limit}"
    try:
        res = constants.GET_RESPONSE(url + query, self.apikey)
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res


"""
* GET
* /wallets/{wallet_address}/sfts
* Get Sfts For Wallet
"""
def sftforwallet(self, wallet_address, network_id, contract_address = None, page = None, limit = None):
    url = f"wallets/{wallet_address}/sfts"
    query = f"?network_id={network_id}"

    if contract_address != None and contract_address != "":
        query += f"&contract_address={contract_address}"
    if page != None and page != "":
        query += "&page={page}"
    if limit != None and limit != "":
        query += "&limit={limit}"
    try:
        res = constants.GET_RESPONSE(url + query, self.apikey)
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res


"""
* GET
* /wallets/{wallet_address}/tokens
* Get Tokens For Wallet
"""
def tokensforwallet(self, wallet_address, network_id, contract_address = None, page = None, limit = None):
    url = f"wallets/{wallet_address}/tokens"
    query = f"?network_id={network_id}"

    if contract_address != None and contract_address != "":
        query += f"&contract_address={contract_address}"
    if  page != None and page != "":
        query += f"&page={page}"
    if  limit != None and limit != "":
        query += f"&limit={limit}"

    try:
        res = constants.GET_RESPONSE(url + query, self.apikey)
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res



"""
* GET
* /wallets/{address}
* Get Wallet
"""
def getwallet(self, address):
    url = f"wallets/{address}"
    try:
        res = constants.GET_RESPONSE(url, self.apikey)
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res



"""
* GET
* /wallets
* Get Wallets
"""
def getwallets(self, network_id = None, page = None, limit = None):
    url = f"wallets"
    query = "?"
    if network_id != None and network_id != "":
        query += f"&network_id={network_id}"
    if  page != None and page != "":
        query += f"&page={page}"
    if  limit != None and limit != "":
         query += f"&limit={limit}"

    try:
        res = constants.GET_RESPONSE(url + query, self.apikey)
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res


"""
* POST
* /wallets
* Create Wallet
"""
def createwallet(self, network_id = None, name = None):
    if network_id == None and network_id == "":
        return "network_id required"
    if name == None and name == "":
        return "name required"
    url = "wallets"
    body = {
        "network_id": network_id,
        "name": name
    }
    try:
        res = constants.POST_RESPONSE(url, body, self.apikey)
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res




"""
* PUT
* /wallets/{wallet_id}
* Update Wallet
"""
def updatewallet(self, wallet_id = None, name = None, is_forwarder = None):
    if wallet_id == None and wallet_id == "":
        return "wallet_id required"
    if name == None and name == "":
        return "name required"
    if is_forwarder == None and is_forwarder == "":
        return "is_forwarder required"

    url = f"wallets/{wallet_id}"
    body = {
        "name": name,
        "is_forwarder": is_forwarder
    }

    try:
        res = constants.PUT_RESPONSE(url, body, self.apikey)
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res



"""
* DELETE
* /wallets/{wallet_id}
* Delete Wallet
"""
def deletewallet(self, wallet_id = None):
    if (wallet_id == None and wallet_id == ""): 
        return "wallet_id required"

    url = f"wallets/{wallet_id}"
    try:
        res = constants.DELETE_RESPONSE(url, self.apikey)
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res



"""
* POST
* /wallets/{wallet_address}/signature
* Sign Message
"""
def signature(self, wallet_address = None, message = None):
    if (wallet_address == None and wallet_address == ""): 
        return "wallet_address required"
    if (message == None and message == ""): 
        return "message required"

    url = f"wallets/{wallet_address}/signature"
    body = { "message": message };    

    try:
        res = constants.POST_RESPONSE(url, body, self.apikey)
        # print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res
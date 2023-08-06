from utility_alpha.apis import constants


"""
* POST
* /contracts/{address}/resync
* Resync Contract Metadata
"""
def resynccontractmetadata(self, address = None, network_id = None):
    if address == None or address == "": 
        return "address is required"
    if network_id == None or network_id == "": 
        return "network_id is required"

    url = f"contracts/{address}?network_id={network_id}"
    try:
        res = constants.POST_RESPONSE(url, {}, self.apikey)
        print("constants.POST_RESPONSE")
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res


"""
* GET
* /contracts/{contract_address}/tokens
* Get Contract Nfts
"""
def getcontractnfts(self, contract_address = None, network_id = None, page = None, limit = None):
    url = f"contracts/{contract_address}/tokens"
    query = f"?network_id={network_id}"

    if contract_address == None or contract_address == "": 
        return "contract_address is required"
    if network_id == None or network_id == "": 
        return "network_id is required"
    if page != None and page != "": 
        query += f"&page={page}"
    if limit != None and limit != "":
        query += f"&limit={limit}"
  
    try:
        res = constants.GET_RESPONSE(url + query, self.apikey)
        print("constants.GET_RESPONSE")
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res
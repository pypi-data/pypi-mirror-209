from utility_alpha.apis import constants



"""
* POST
* /transactions/read
* Read Contract View Function
"""
def readtx(self, chain_id = None, params = None, contract_address = None, abi = None, contract_function_name = None):
    if (chain_id == None or chain_id == ""):
        return "chain_id is required"
    if (params == None or params == ""):
        return "params is required"
    if (contract_address == None or contract_address == ""):
        return "contract_address is required"
    if (abi == None or abi == ""):
        return "abi is required"
    if (contract_function_name == None or contract_function_name == ""):
        return "function name is required"

    body = {
        "chain_id": chain_id,
        "params": params,
        "contract_address": contract_address,
        "abi": abi,
        "contract_function_name": contract_function_name,
    }
    url = "transactions/read"
    
    try:
        res = constants.POST_RESPONSE(url, body, self.apikey)
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res



"""
* POST
* /transactions
* Create Transaction
"""
def createtx(self, chain_id = None, from_address = None, to_address = None, params = None, contract_address = None, abi = None, contract_function_name = None, gas_limit = None, gas_strategy = "SLOW"):
    if (chain_id == None or chain_id == ""):
        return "chain_id is required"
    if (from_address == None or from_address == ""):
        return "from_address is required"
    if (to_address == None or to_address == ""):
        return "to_address is required"
    if (params == None or params == ""):
        return "params is required"
    if (contract_address == None or contract_address == ""):
        return "contract_address is required"
    if (abi == None or abi == ""):
        return "abi is required"
    if (contract_function_name == None or contract_function_name == ""):
        return "function name is required"
    if (gas_limit == None or gas_limit == ""):
        return "gas_limit is required"
    if (gas_strategy == None or gas_strategy == ""):
        return "gas_strategy is required"

    body = {
        "chain_id": chain_id,
        "type": "TRANSFER",
        "from_address": from_address,
        "to_address": to_address,
        "params": params,
        "contract": contract_address,
        "abi": abi,
        "contract_function_name": contract_function_name,
        "gas_limit": gas_limit,
        "gas_strategy": gas_strategy
    }
    url = "transactions"
    
    try:
        res = constants.POST_RESPONSE(url, body, self.apikey)
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res


"""
* POST
* /transactions/meta
* Create Meta Transaction
"""
def createmetatx(self, chain_id = None, from_address = None, to_address = None, forwarder_address = None, params = None, abi = None, contract_function_name = None, gas_limit = None, gas_strategy = "SLOW"):
    if (chain_id == None or chain_id == ""):
        return "chain_id is required"
    if (from_address == None or from_address == ""):
        return "from_address is required"
    if (to_address == None or to_address == ""):
        return "to_address is required"
    if (forwarder_address == None or forwarder_address == ""):
        return "forwarder_address is required"
    if (params == None or params == ""):
        return "params is required"
    if (abi == None or abi == ""):
        return "abi is required"
    if (contract_function_name == None or contract_function_name == ""):
        return "function name is required"
    if (gas_limit == None or gas_limit == ""):
        return "gas_limit is required"
    if (gas_strategy == None or gas_strategy == ""):
        return "gas_strategy is required"

    body = {
        "chain_id": chain_id,
        "from_address": from_address,
        "to_address": to_address,
        "forwarder_address": forwarder_address,
        "params": params,
        "abi": abi,
        "contract_function_name": contract_function_name,
        "gas_limit": gas_limit,
        "gas_strategy": gas_strategy
    }

    url = "transactions/meta"
    
    try:
        res = constants.POST_RESPONSE(url, body, self.apikey)
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res



"""
* GET
* /transactions/{transaction_id}
* Get Transactions
"""
def getsingletx(self, transaction_id = None):
    if (transaction_id == None or transaction_id == ""):
        return "transaction_id is required"

    url = f"transactions/{transaction_id}"
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
* /transactions/group_by_wallet/{wallet_id}
* Get Wallet Transactions
"""
def gettxofwallet(self, wallet_id = None, page = None, limit = None):
    query = "?"
    if wallet_id == None or wallet_id == "":
        return "wallet_id  is required"
    if page != None and page != "":
        query += "&page={page}"
    if limit != None and limit != "":
        query += "&limit={limit}"
  
    url = "transactions/group_by_wallet/{wallet_id}"
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
* /transactions/{transaction_id}/status
* Get Transaction Status
"""
def gettxstatus(self, transaction_id = None):
    if (transaction_id == None or transaction_id == ""):
        return "transaction_id is required"
  
    url = "transactions/{transaction_id}/status"
    try:
        res = constants.GET_RESPONSE(url, self.apikey)
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res
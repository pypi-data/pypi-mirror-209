from utility_alpha.apis import constants



"""
* GET
* /metadata
* Get Namespaces
"""
def getnamespaces(self, page = None, limit = None):
    url = "metadata"
    query = "?"

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



"""
* POST
* /metadata
* Create Namespace
"""
def createnamespaces(self, namespace = None, description = None):
    if namespace == None or namespace == "": 
        return "namespace is required"
    if description == None or description == "": 
        return "description is required"
    
    url = "metadata"
    body = {
        "namespace": namespace,
        "description": description
    }
    
    try:
        res = constants.POST_RESPONSE(url, body, self.apikey)
        print("constants.POST_RESPONSE")
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res



"""
* GET
* /metadata/{namespace}
* Get Metadata Items
"""
def getmetadataitems(self, namespace = None, page = None, limit = None):
    url = "metadata/{namespace}"
    query = "?"

    if namespace == None or namespace == "": 
        return "namespace is required"
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



"""
* PUT
* /metadata/{namespace}
* Update Metadata Item
"""
def updatemetadataitem(self, namespace = None, id = None, name = None, image = None, description = None, attributes = None):
    if namespace == None or namespace == "": 
        return "namespace required"
    if id == None or id == "": 
        return "id required"
    if name == None or name == "": 
        return "name required"
    if image == None or image == "": 
        return "image required"
    if description == None or description == "": 
        return "description required"
    if attributes == None or attributes == "": 
        return "attributes required"
    if attributes.length == 0: 
        return "attributes should be in JSON format e.g. array of objects"

    url = f"metadata/{namespace}"
    body = {
        "id": id,
        "name": name,
        "image": image,
        "description": description,
        "attributes": attributes
    }

    try:
        res = constants.PUT_RESPONSE(url, body, self.apikey)
        print("constants.POST_RESPONSE")
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res




"""
* POST
* /metadata/{namespace}
* Create Metadata Item
"""
def createmetadataitem(self, namespace = None, id = None, name = None, image = None, description = None, attributes = None):
    if namespace == None or namespace == "": 
        return "namespace is required"
    if id == None or id == "": 
        return "id required"
    if name == None or name == "": 
        return "name required"
    if image == None or image == "": 
        return "image required"
    if description == None or description == "": 
        return "description required"
    if attributes == None or attributes == "": 
        return "attributes required"
    if attributes.length == 0:
        return "attributes should be in JSON format e.g. array of objects"

    
    url = f"metadata/{namespace}"
    body = {
        "id": id,
        "name": name,
        "image": image,
        "description": description,
        "attributes": attributes
    }
    
    try:
        res = constants.POST_RESPONSE(url, body, self.apikey)
        print("constants.POST_RESPONSE")
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res



"""
* GET
* /metadata/{namespace}/{id}
* Token Uri
"""
def getsinglemetadataitem(self, namespace = None, id = None):
    if id == None or id == "": 
        return "id is required"
    if namespace == None or namespace == "": 
        return "namespace is required"
    
    url = f"metadata/{namespace}/{id}"
   
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
* DELETE
* /metadata/{namespace}/{id}
* Delete Metadata Item
"""
def deletemetadataitem(self, namespace = None, id = None):
    if id == None or id == "": 
        return "id is required"
    if namespace == None or namespace == "": 
        return "namespace is required"

    url = f"metadata/{namespace}/{id}"
    try:
        res = constants.DELETE_RESPONSE(url, self.apikey)
        print("constants.Delete_RESPONSE")
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res
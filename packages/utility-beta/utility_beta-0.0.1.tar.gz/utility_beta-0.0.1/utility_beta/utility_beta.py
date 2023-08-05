# # Import sys and append path for access directory as a module
# import sys
# sys.path.append('./apis')

# import file as a module from a directory
# import wallets
# import transactions
import requests

URL = "https://api.utiliti.ai"
headers = {
    # 'X-API-Key': 'f253d57f-1740-4603-9697-2dc1399eef73',
    "Accept": "*/*",
}

# print(myUtility.apikey)


def GET_RESPONSE(url, apikey):
    headers['X-API-Key'] = apikey
    try:
        _url = f'{URL}/{url}'
        response = requests.get(_url, headers=headers)
        response.raise_for_status()  # raise an HTTPError for 4xx and 5xx status codes
        data = {
            "status_code": response.status_code,
            "status_text": response.reason,
            "details": response.json()      # parse the response data as JSON
            }  

    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  

    except ValueError as e:
        print("Error parsing JSON response:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  
    else:
        print("API response:", data)
        return data


def POST_RESPONSE(url, body, apikey):
    headers['X-API-Key'] = apikey
    try:
        _url = f'{URL}/{url}'
        response = requests.post(_url, headers=headers, json=body)
        response.raise_for_status()  # raise an HTTPError for 4xx and 5xx status codes
        data = {
            "status_code": response.status_code,
            "status_text": response.reason,
            "details": response.json()      # parse the response data as JSON
            }  

    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  

    except ValueError as e:
        print("Error parsing JSON response:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  
    else:
        print("API response:", data)
        return data


def PUT_RESPONSE(url, body, apikey):
    headers['X-API-Key'] = apikey
    try:
        _url = f'{URL}/{url}'
        response = requests.put(_url, headers=headers, json=body)
        response.raise_for_status()  # raise an HTTPError for 4xx and 5xx status codes
        data = {
            "status_code": response.status_code,
            "status_text": response.reason,
            "details": response.json()      # parse the response data as JSON
            }  

    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  

    except ValueError as e:
        print("Error parsing JSON response:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  
    else:
        print("API response:", data)
        return data


def DELETE_RESPONSE(url, apikey):
    headers['X-API-Key'] = apikey
    try:
        _url = f'{URL}/{url}'
        response = requests.delete(_url, headers=headers)
        response.raise_for_status()  # raise an HTTPError for 4xx and 5xx status codes
        data = {
            "status_code": response.status_code,
            "status_text": response.reason,
            "details": response.json()      # parse the response data as JSON
            }  

    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  

    except ValueError as e:
        print("Error parsing JSON response:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  
    else:
        print("API response:", data)
        return data



# wallets
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
        res = GET_RESPONSE(url + query, self.apikey)
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
        res = GET_RESPONSE(url + query, self.apikey)
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
        res = GET_RESPONSE(url + query, self.apikey)
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
        res = GET_RESPONSE(url, self.apikey)
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
        res = GET_RESPONSE(url + query, self.apikey)
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
        res = POST_RESPONSE(url, body, self.apikey)
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
        res = PUT_RESPONSE(url, body, self.apikey)
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
        res = DELETE_RESPONSE(url, self.apikey)
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
        res = POST_RESPONSE(url, body, self.apikey)
        # print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res


# transactions

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
        res = POST_RESPONSE(url, body, self.apikey)
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
        res = POST_RESPONSE(url, body, self.apikey)
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
        res = POST_RESPONSE(url, body, self.apikey)
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
        res = GET_RESPONSE(url, self.apikey)
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
        res = GET_RESPONSE(url + query, self.apikey)
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
        res = GET_RESPONSE(url, self.apikey)
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res


# tokens

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
        res = PUT_RESPONSE(url, body, self.apikey)
        print("PUT_RESPONSE")
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res

# contracts
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
        res = POST_RESPONSE(url, {}, self.apikey)
        print("POST_RESPONSE")
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
        res = GET_RESPONSE(url + query, self.apikey)
        print("GET_RESPONSE")
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res

# metadata
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
        res = GET_RESPONSE(url + query, self.apikey)
        print("GET_RESPONSE")
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
        res = POST_RESPONSE(url, body, self.apikey)
        print("POST_RESPONSE")
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
        res = GET_RESPONSE(url + query, self.apikey)
        print("GET_RESPONSE")
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
        res = PUT_RESPONSE(url, body, self.apikey)
        print("POST_RESPONSE")
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
        res = POST_RESPONSE(url, body, self.apikey)
        print("POST_RESPONSE")
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
        res = GET_RESPONSE(url, self.apikey)
        print("GET_RESPONSE")
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
        res = DELETE_RESPONSE(url, self.apikey)
        print("Delete_RESPONSE")
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res

# nfts
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
        res = GET_RESPONSE(url, self.apikey)
        print("GET_RESPONSE")
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
        res = PUT_RESPONSE(url, body, self.apikey)
        print("POST_RESPONSE")
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res

# sfts
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
        res = PUT_RESPONSE(url, body, self.apikey)
        print("PUT_RESPONSE")
        print(res)
    except ValueError as e:
        print(f"ERROR =>=>=> {e}")
        return e
    else:
        return res

class Utility:
    def __init__(self, apikey):
        self.apikey = apikey

    def nftForWallet(self, *params):
        return nftforwallet(self, *params)

    def sftForWallet(self, *params):
        return sftforwallet(self, *params)

    def tokensForWallet(self, *params):
        return tokensforwallet(self, *params)

    def getWallet(self, *params):
        return getwallet(self, *params)

    def getWallets(self, *params):
        return getwallets(self, *params)

    def createWallet(self, *params):
        return createwallet(self, *params)

    def updateWallet(self, *params):
        return updatewallet(self, *params)

    def deleteWallet(self, *params):
        return deletewallet(self, *params)

    def getSignature(self, *params):
        return signature(self, *params)

    # Transaction APIs
    def readTx(self, *params):
        return readtx(self, *params)
    
    def createTx(self, *params):
        return createtx(self, *params)
    
    def createMetaTx(self, *params):
        return createmetatx(self, *params)
    
    def getSingleTx(self, *params):
        return getsingletx(self, *params)
    
    def getTxOfWallet(self, *params):
        return gettxofwallet(self, *params)
    
    def getTxStatus(self, *params):
        return gettxstatus(self, *params)

    # Tokens APIs
    def resyncTokens(self, *params):
        return resynctokens(self, *params)

    # Contracts APIs
    def resyncContractMetadata(self, *params):
        return resynccontractmetadata(self, *params)
    
    def getContractNfts(self, *params):
        return getcontractnfts(self, *params)


    # Metadata APIs
    def getNamespaces(self, *params):
        return getnamespaces(self, *params)
    
    def createNamespaces(self, *params):
        return createnamespaces(self, *params)
    
    def getMetadataItems(self, *params):
        return getmetadataitems(self, *params)
    
    def updateMetadataItem(self, *params):
        return updatemetadataitem(self, *params)
    
    def createMetadataItem(self, *params):
        return createmetadataitem(self, *params)
    
    def getSingleMetadataItem(self, *params):
        return getsinglemetadataitem(self, *params)
    
    def deleteMetadataItem(self, *params):
        return deletemetadataitem(self, *params)

    #  Nfts APIs
    def getNfts(self, *params):
        return getnfts(self, *params)

    def resyncNfts(self, *params):
        return resyncnfts(self, *params)

    #  Sfts APIs
    def updateResyncnfts(self, *params):
        return updateresyncnfts(self, *params)


    


    


# myUtility = Utility("588defcd-92ad-4891-93c8-ddd5bf41ea9d")
# myUtility = Utility("f253d57f-1740-4603-9697-2dc1399eef73")

# res = myUtility.nftForWallet("0xf7f9e7be5971dd17563dcbaa745975c0fb919669", 1)
# print(f" Response ===>>> {res}")

# res = myUtility.sftForWallet("0xf7f9e7be5971dd17563dcbaa745975c0fb919669", 1)
# print(f" Response ===>>> {res}")

# res = myUtility.tokensForWallet("0xf7f9e7be5971dd17563dcbaa745975c0fb919669", 1)
# print(f" Response ===>>> {res}")

# res = myUtility.getWallet("address")
# print(f" Response ===>>> {res}")

# res = myUtility.getWallets(1)
# print(f" Response ===>>> {res}")

# res = myUtility.createWallet(1, "python wallet")
# print(f" Response ===>>> {res}")

# res = myUtility.updateWallet("42e9e745-fb71-4515-8f0a-db43ba8ec7fe", "test-420", True)
# print(f" Response ===>>> {res}")

# res = myUtility.deleteWallet("42e9e745-fb71-4515-8f0a-db43ba8ec7fe")
# print(f" Response ===>>> {res}")

# res = myUtility.getSignature("0xda8d71c98b395d6ab86959bd64ece07cd2274411", "hello")
# print(f" Response ===>>> {res}")




# res = myUtility.readTx("0","hello","0xda8d71c98b395d6ab86959bd64ece07cd2274411","[]","hello")
# print(f" Response ===>>> {res}")

# res = myUtility.createTx("0","0xda8d71c98b395d6ab86959bd64ece07cd2274411","0xda8d71c98b395d6ab86959bd64ece07cd2274411","ppp","0xda8d71c98b395d6ab86959bd64ece07cd2274411","[]","ppp","120","678687")
# print(f" Response ===>>> {res}")

# res = myUtility.createMetaTx("0","0xda8d71c98b395d6ab86959bd64ece07cd2274411","0xda8d71c98b395d6ab86959bd64ece07cd2274411","0xda8d71c98b395d6ab86959bd64ece07cd2274411","ppp","[]","iii","1231","9798")
# print(f" Response ===>>> {res}")

# res = myUtility.getSingleTx("transaction_id")
# print(f" Response ===>>> {res}")

# res = myUtility.getTxOfWallet("42e9e745-fb71-4515-8f0a-db43ba8ec7fe","1","8")
# print(f" Response ===>>> {res}")

# res = myUtility.getTxStatus("transaction_id")
# print(f" Response ===>>> {res}")




# res = myUtility.resyncTokens("0xda8d71c98b395d6ab86959bd64ece07cd2274411", "1", "0xda8d71c98b395d6ab86959bd64ece07cd2274411")
# print(f" Response ===>>> {res}")




# res = myUtility.resyncContractMetadata("0xda8d71c98b395d6ab86959bd64ece07cd2274411", "1")
# print(f" Response ===>>> {res}")

# res = myUtility.getContractNfts("0xda8d71c98b395d6ab86959bd64ece07cd2274411", "1", "1", "1")
# print(f" Response ===>>> {res}")




# res = myUtility.getNamespaces("1", "2")
# print(f" Response ===>>> {res}")
# res = myUtility.createNamespaces("namespace = null", "description")
# res = myUtility.getMetadataItems("namespace = null", "page = null", "limit")
# res = myUtility.updateMetadataItem("namespace = null", "id = null", "name = null", "image = null", "description = null", "attributes = null")
# res = myUtility.createMetadataItem("namespace = null", "id = null", "name = null", "image = null", "description = null", "attributes = null")
# res = myUtility.getSingleMetadataItem("namespace = null", "id = null")
# res = myUtility.deleteMetadataItem("namespace = null", "id = null")




# res = myUtility.getNfts("token_id = null", "contract_address = null", "network_id = null")
# print(f" Response ===>>> {res}")
# res = myUtility.resyncNfts("address = null", "network = null", "token_ids = null")




# res = myUtility.updateResyncnfts("address", "network", "owner", "token_ids")
# print(f" Response ===>>> {res}")
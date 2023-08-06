from utility_alpha.apis import wallets
from utility_alpha.apis import transactions
from utility_alpha.apis import tokens
from utility_alpha.apis import contracts
from utility_alpha.apis import metadata
from utility_alpha.apis import nfts
from utility_alpha.apis import sfts

class Utility:
    def __init__(self, apikey):
        self.apikey = apikey

    def nftForWallet(self, *params):
        return wallets.nftforwallet(self, *params)

    def sftForWallet(self, *params):
        return wallets.sftforwallet(self, *params)

    def tokensForWallet(self, *params):
        return wallets.tokensforwallet(self, *params)

    def getWallet(self, *params):
        return wallets.getwallet(self, *params)

    def getWallets(self, *params):
        return wallets.getwallets(self, *params)

    def createWallet(self, *params):
        return wallets.createwallet(self, *params)

    def updateWallet(self, *params):
        return wallets.updatewallet(self, *params)

    def deleteWallet(self, *params):
        return wallets.deletewallet(self, *params)

    def getSignature(self, *params):
        return wallets.signature(self, *params)



    # Transaction APIs
    def readTx(self, *params):
        return transactions.readtx(self, *params)
    
    def createTx(self, *params):
        return transactions.createtx(self, *params)
    
    def createMetaTx(self, *params):
        return transactions.createmetatx(self, *params)
    
    def getSingleTx(self, *params):
        return transactions.getsingletx(self, *params)
    
    def getTxOfWallet(self, *params):
        return transactions.gettxofwallet(self, *params)
    
    def getTxStatus(self, *params):
        return transactions.gettxstatus(self, *params)

    

    # Tokens APIs
    def resyncTokens(self, *params):
        return tokens.resynctokens(self, *params)
    


    # Contracts APIs
    def resyncContractMetadata(self, *params):
        return contracts.resynccontractmetadata(self, *params)
    
    def getContractNfts(self, *params):
        return contracts.getcontractnfts(self, *params)
    


    # Metadata APIs
    def getNamespaces(self, *params):
        return metadata.getnamespaces(self, *params)
    
    def createNamespaces(self, *params):
        return metadata.createnamespaces(self, *params)
    
    def getMetadataItems(self, *params):
        return metadata.getmetadataitems(self, *params)
    
    def updateMetadataItem(self, *params):
        return metadata.updatemetadataitem(self, *params)
    
    def createMetadataItem(self, *params):
        return metadata.createmetadataitem(self, *params)
    
    def getSingleMetadataItem(self, *params):
        return metadata.getsinglemetadataitem(self, *params)
    
    def deleteMetadataItem(self, *params):
        return metadata.deletemetadataitem(self, *params)
    


    #  Nfts APIs
    def getNfts(self, *params):
        return nfts.getnfts(self, *params)
    

    def resyncNfts(self, *params):
        return nfts.resyncnfts(self, *params)
    


    #  Sfts APIs
    def updateResyncnfts(self, *params):
        return sfts.updateresyncnfts(self, *params)


    


    


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
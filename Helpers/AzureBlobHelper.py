from azure.storage.blob import BlobServiceClient
from Configs.Config import Config

class AzureBlobHelper:
    def __init__(self):
        config = Config()
        self.serviceClient = BlobServiceClient.from_connection_string(config.storageConnectionString)
        self.containerName = config.containerName;
    
    def SaveTextToBlob(self, request, answer, type):
        blobClient = self.serviceClient.get_blob_client(self.containerName, f"History/{type}.txt")
        try:
            currentContent = blobClient.download_blob().content_as_text()
        except:
            currentContent = ""

        newContent = currentContent + request + '\n' + answer + '\n' + "====================================" + '\n'
        blobClient.upload_blob(newContent, overwrite=True)

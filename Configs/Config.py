import os

class Config:
     def __init__(self):
          self.frontendUrls = ["http://localhost:4200", "https://portfolio.codieorberson.com"]
          self.storageName = "codieportfolio"
          self.containerName = "chatgpt"

          self.storageKey = os.environ.get("STORAGE_KEY")
          self.chatGptApiKey = os.environ.get("CHATGPT_API_KEY")
          self.orgId = os.environ.get("ORG_ID")
          self.storageConnectionString = os.environ.get("STORAGE_CONNECTION_STRING")
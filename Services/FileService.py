
import requests
import random
import string
import datetime
from Helpers.AzureBlobHelper import AzureBlobHelper

class FileService:

    def __init__(self):
        self.imageUrlFile = 'History/Images/ImageHistory.txt'
        self.answerFile = 'History/Answers/AnswerHistory.txt'
        self.imagesFolder = 'History/Images/'
        self.azureBlob = AzureBlobHelper()

    def SaveImage(self, url):
        response = requests.get(url)
        fileName = f"{self.GenerateCurrentDateString()}-{self.GenerateRandomNumber()}"
        outputPath = f"{self.imagesFolder}{fileName}.png"
        if(response.status_code==200):
            with open(outputPath, 'wb') as file:
                file.write(response.content)

    def SaveImageUrl(self, request, url):
        self.SaveImage(url)
        imageHistoryFile = 'History/Images/ImageHistory.txt'
        with open(imageHistoryFile, 'a') as file:
            file.write(f"{request}\n{url}\n{'='*40}\n")

        self.azureBlob.SaveTextToBlob(request, url, "Images")

    def SaveAnswer(self, request, answer):
        answerHistoryFile = 'History/Answers/AnswerHistory.txt'
        
        with open(answerHistoryFile, 'a') as file:
            file.write(f"{request}\n{answer}\n{'='*40}\n")
        self.azureBlob.SaveTextToBlob(request, answer, "Generic")


    def SaveFineTunedAnswer(self, request, answer):
        answerHistoryFile = 'History/FineTuneAnswers/AnswerHistory.txt'
        with open(answerHistoryFile, 'a') as file:
            file.write(f"{request}\n{answer}\n{'='*40}\n")
        self.azureBlob.SaveTextToBlob(request, answer, "FineTuned")

    def GenerateCurrentDateString(self):
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d-%H-%M-%S")
        return now
    
    def GenerateRandomString(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))
    
    def GenerateRandomNumber(self):
        return str(random.randint(0,9999999))
    

    
    

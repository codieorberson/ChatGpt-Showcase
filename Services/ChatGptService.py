
import openai
from Services.FileService import FileService

class ChatGptService:

    def __init__(self, apiKey, orgId):
        self.apiKey = apiKey
        self.orgId = orgId
        self.roles = ["user", "system", "assistant"]
        self.model = "gpt-3.5-turbo"
        openai.organization = self.orgId
        openai.api_key = self.apiKey
        
        self.conversation_history = []
        self.pictureSizes = {
            "S": "256x256", 
            "M" : "512x512", 
            "L": "1024x1024"
        }
        self.chatCgptFile = FileService()

    def GetAnswer(self, question):
        self.conversation_history.append({"role": "user", "content": question})
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages= self.conversation_history
            
        )
        answer = completion.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": answer})
        self.chatCgptFile.SaveAnswer(question, answer)
        return answer
    
    def GetFineTuneAnswer(self, question, modelId, systemPrompt):
        self.conversation_history.append({"role": "user", "content": question})
        self.conversation_history.append({"role": "system", "content": systemPrompt})
        completion = openai.ChatCompletion.create(
            model=modelId,
            messages=self.conversation_history
        )
        
        answer = completion.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": answer})
        self.chatCgptFile.SaveFineTunedAnswer(question, answer)
        return completion
    
    def CreatePicture(self, prompt, count, size):
        responses = []
        pictureSize = self.pictureSizes[size.capitalize()]
        completion = openai.Image.create(
            prompt=prompt,
            n=count,
            size = pictureSize
        )
        for i in range(count):
            response = completion["data"][i]["url"]
            self.chatCgptFile.SaveImageUrl(prompt, response)
            responses.append(response)
        return responses
    
    def CreateFineTune(self, id):

        completion = openai.FineTuningJob.create(
            training_file = id,
            model=self.model
        )
        return completion
    
    def UploadFile(self, fileName):
        file = f'TrainingData/{fileName}.jsonl'
        completion = openai.File.create(
            file=open(file, "rb"),
            purpose='fine-tune',
            user_provided_filename=f'{fileName}'
        )
        return completion

    
    def ListFiles(self):
        return openai.File.list()
    
    def ListModels(self):
        return openai.Model.list()
    
    def GetModel(self, model):
        return openai.Model.retrieve(model)

    def ListFineTunes(self):
        completion = openai.FineTuningJob.list()
        return completion
    
    def GetFineTune(self, id):
        completion = openai.FineTuningJob.retrieve(id = id)
        return completion
    
    def DeleteFineTune(self, id):
        completion = openai.Model.delete(id)
        return completion
    
    def CancelFineTune(self, id):
        completion = openai.FineTuningJob.cancel(id=id)
        return completion
    
    def DeleteFile(self, id):
        completion = openai.File.delete(id)
        return completion
    
    def DownloadFile(self, id):
        completion = openai.File.download(id)
        return True

    def RetrieveFile(self, id):
        completion = openai.File.retrieve(id)
        return completion
    
    

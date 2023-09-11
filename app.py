from Controllers.ChatGptController import ChatGptController
from Controllers.HealthController import HealthController
from flask import Flask, jsonify
from flask_cors import CORS
from Configs.Config import Config
import sys

print("Starting Project")
app = Flask(__name__)
app.config['TIMEOUT'] = 3600
config = Config()

cors = CORS(app, resources={r"/*": {"origins": "*"}})
HealthController.register(app, route_base='/api/v1/Health')
ChatGptController.register(app, route_base='/api/v1/ChatGpt')

print("Completing Setup Project")
if __name__ == '__main__':      
   app.run(debug=True)



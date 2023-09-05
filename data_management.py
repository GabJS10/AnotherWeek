import os
import json

def create_json():
     with open("weeks.json","w") as j:
          json.dump([{}],j)

def read():
     data = None

     if not os.path.isfile("weeks.json"):
          create_json()

     with open("weeks.json","r") as j:
          data = json.load(j)     

     return data

def write(data):
     if not os.path.isfile("weeks.json"):
          create_json()

     with open("weeks.json","w") as j:
          json.dump(data,j)

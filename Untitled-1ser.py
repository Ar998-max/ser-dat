# mongodb+srv://ashmitrajvansh70:<password>@cluster0.mbqicmt.mongodb.net/?retryWrites=true&w=majority
# mongo cluster pass lKFH6ztUjrOQmYK0

from flask import Flask, request, jsonify
import pymongo
from pymongo import MongoClient
import urllib
import requests


app = Flask(__name__)
cluster = MongoClient('mongodb+srv://'+"ashmitrajvansh70"+':'+urllib.parse.quote("lKFH6ztUjrOQmYK0")+'@cluster0.zwhyqjr.mongodb.net/?retryWrites=true&w=majority')
db = cluster['Cluster0']
collection = db['chat.chat-1']

post = {'_id': '0', 'name': "ancd", 'score': 5}

@app.route('/mongo_retrieve', methods=['GET'])
def get_docs():
  cursor = collection.find({})
  chat = []
  for document in cursor:
    print(document)
    chat.append(document)
  return chat

@app.route('/mongo', methods=['GET'])
def post_docs():
  d = {}

  inputpro = str(request.args.get('id', None))
  name = str(request.args.get('name', None))
  score = str(request.args.get('score', None))
  id = str(request.args.get('id', None))
  post = {'_id': str(inputpro), 'name': str(name), 'score': str(score)}

  collection.insert_one(post)
  print('mpmgp')
  return post
if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request, jsonify
from flask_cors import CORS
import string
import random

app = Flask(__name__)
CORS(app)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

def generate_id():
    return "".join(random.choices(
        [c for c in string.printable if not c in string.whitespace], k=6))


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')

      if search_username and search_job:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict

      if search_job :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict

      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users

   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = generate_id()
      users['users_list'].append(userToAdd)
      resp = jsonify(userToAdd)
      resp.status_code = 201 #optionally, you can always set a response code. 
      return resp

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if request.method== 'GET' and id :
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})

   if request.method=='DELETE' and id:
      new = [user for user in users['users_list'] if user['id'] != id]
      if new != users['users_list']:
         users['users_list'] = new
         return ('', 204)
      else:
         return ('poo', 404)
   else:
      return ('', 404)

   return users

import markdown
import os
import shelve
import psutil
import json
import datetime
import requests

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse
from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")


def getService(name):
	for i in name
		service = None
		try:
		service = psutil.win_service_get(i)
		service = service.as_dict()
		except Exception as ex:
       print(str(ex))
   return service


serviceList = ["httpd","rabbitmq","postgresql"]

servicesMointor = getService(serviceList)
json.dumps(servicesMointor)
filename = servicesMointor['display_name']+'-'+servicesMointor['status']+'-'+str(datetime.datetime.now())+'.json'
print(filename)
with open("{filename}", 'w') as outfile:
   json.dump(servicesMointor, outfile)
print(servicesMointor)

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

@app.route("/")
def index():
   """Present some documentation"""

   # Open the README file
   with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

       # Read the content of the file
       content = markdown_file.read()

       # Convert to HTML
       return markdown.markdown(content)


class ServicesRunningList(Resource):
   def get(id):
       res = es.get(index="services", doc_type="json", id="{id}")
       return {'message': 'Success', 'data': servicesMointor['status']}, 200

   def post(id):
       parser = reqparse.RequestParser()

       parser.add_argument('display_name', required=True)
       parser.add_argument('status', required=True)
       parser.add_argument('host_name', required=True)

       # Parse the arguments into an object
       args = parser.parse_args()
es.index(index="services", doc_type="json", id="{id}", body=servicesMointor)

       shelf[args['identifier']] = args

       return {'message': 'Device registered', 'data': args}, 201


class ServiceMointor(Resource):
   def get(self, identifier):

       # If the key does not exist in the data store, return a 404 error.
       if not (identifier in shelf):
           return {'message': 'Device not found', 'data': {}}, 404

       return {'message': 'Device found', 'data': servicesMointor}, 200


api.add_resource(ServicesRunningList, '/servicesrunning')
api.add_resource(Device, '/device/id')
api.add_resource(healthcheck, '/device/id?status')

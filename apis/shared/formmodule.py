import os
import pymongo
import json
import copy
import re
from bson import ObjectId

class form:

    def __init__(self, provider):
        self.provider = provider
        self.db = self.getDB()
        self.collection = self.db.forms
        print('form class initialized')

    def getDB(self):
        from pymongo import MongoClient
        client = MongoClient(os.environ['MONGO_CONNECTION_STRING'])
        db = client.simpleForm
        return db

    def getForms(self, event):

        searchTerm = self.provider.getQueryStringParam(event, 'title')
        rgx = re.compile('.*' + searchTerm + '.*', re.IGNORECASE) 
        cursor = self.collection.find({'title' : rgx})

        # create a dictionary of form items
        forms = {}

        for doc in cursor:
            item = {
                "id" : str(doc.get('_id')),
                "title" : doc.get('title'),
                "fields" : doc.get('fields'),
                "entries" : doc.get('entries')
            }
            forms[str(doc.get('_id'))] = item

        # return response
        body = {
            "forms" : forms
        }

        return self.provider.buildResponse(body)

    def getFormById(self, event):
        # get form id from route
        id = self.provider.getRouteParam(event, 'id')

        # find form in collection matching form id
        cursor = self.collection.find({'_id' : ObjectId(id)})
        fields = cursor[0]['fields']

        # return response
        return self.provider.buildResponse(fields)

    def createForm(self, event):
        # get form data
        formData = self.provider.getPostData(event, 'form')

        # insert new form into collection
        self.collection.insert_one(formData)

        # return response
        body = {
            "message" : "new form successfully created"
        }
        return self.provider.buildResponse(body)

    def deleteForm(self, event):
        # get form id from route
        id = self.provider.getRouteParam(event, 'id')

        # delete form from collection
        self.collection.delete_one({'_id' : ObjectId(id)})
        
        # return response
        body = {
            "message" : f"form {id} successfully deleted"
        }
        return self.provider.buildResponse(body)

    def submitFormData(self, event):
        # get post data
        data = self.provider.getPostData(event, 'data')
        fid = self.provider.getRouteParam(event, 'id')
        
        # find form by id
        cursor = self.collection.find({'_id' : ObjectId(fid)})
        entries = cursor[0]['entries']
        data.pop('form_id')
        
        # add new entry to selected form object
        entries.append(data)
        
        # update form
        self.collection.update_one({"_id" : ObjectId(fid)}, { "$set" : { "entries" : entries }})
        
        # return response
        body = {
            "message" : "form data successfully submitted"
        }
        return self.provider.buildResponse(body)
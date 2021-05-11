import logging
import time
import uuid
from shared.formmodule import form
from shared.provider import AWSProvider

def getForms(event, context):
    return form(AWSProvider()).getForms(event)

def getFormById(event, context):
    return form(AWSProvider()).getFormById(event)

def createForm(event, context):
    return form(AWSProvider()).createForm(event)

def deleteForm(event, context):
    return form(AWSProvider()).deleteForm(event)

def submitFormData(event, context):
    return form(AWSProvider()).submitFormData(event)
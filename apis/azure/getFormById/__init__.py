import logging
import json
from shared.formmodule import form
from shared.provider import AzureProvider
import azure.functions as func

def main(req: func.HttpRequest):
    return form(AzureProvider()).getFormById(req)


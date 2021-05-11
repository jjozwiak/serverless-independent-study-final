import logging
import os
import json
import azure.functions as func
from shared.formmodule import form
from shared.provider import AzureProvider


def main(req: func.HttpRequest):
    return form(AzureProvider()).getForms(req)
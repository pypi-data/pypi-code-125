# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import
import os
import sys
import unittest
import warnings
import shutil

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)
import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
from asposecellscloud.models import MatchConditionRequest
from asposecellscloud.models import BatchConvertRequest
from asposecellscloud.models import ImportIntArrayOption
from asposecellscloud.models import CalculationOptions
from asposecellscloud.models import WorkbookSettings
from asposecellscloud.models import PasswordRequest
from datetime import datetime
global_api = None

class TestOne(unittest.TestCase):
    """ CellsWorkbookApi unit test stubs """

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_one_call(self):
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, 'Book1.xlsx', folder)
        result = AuthUtil.Ready(self.api, 'myDocument.xlsx', folder)
        match_condition_request = MatchConditionRequest()
        match_condition_request.full_match_conditions =['Book1.xlsx','myDocument.xlsx'] 
        
        match_convert_request =  BatchConvertRequest()
        match_convert_request.source_folder = 'PythonTest'
        match_convert_request.format ='PDF'
        match_convert_request.match_condition = match_condition_request
        
        result = self.api.post_batch_convert( match_convert_request)
        self.assertTrue(len(result)>0) 
        pass


if __name__ == '__main__':
    unittest.main()

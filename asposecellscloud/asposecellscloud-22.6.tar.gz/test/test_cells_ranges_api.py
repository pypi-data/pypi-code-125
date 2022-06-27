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

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)
import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
from asposecellscloud.models import Range
from asposecellscloud.models import RangeSetOutlineBorderRequest
from asposecellscloud.models import Color
from asposecellscloud.models import Font
from asposecellscloud.models import Style
from asposecellscloud.models import RangeSetStyleRequest
from asposecellscloud.models import RangeCopyRequest
from asposecellscloud.models import PasteOptions
global_api = None

class TestCellsRangesApi(unittest.TestCase):
    """ CellsRangesApi unit test stubs """

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_ranges_get_worksheet_cells_range_value(self):
        """
        Test case for cells_ranges_get_worksheet_cells_range_value

        Get cells list in a range by range name or row column indexes  
        """
        name ='Book1.xlsx'  
        sheet_name ='Sheet1'    
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        firstRow = 0
        firstColumn = 0
        rowCount = 3
        columnCount = 2
        response = self.api.cells_ranges_get_worksheet_cells_range_value(name, sheet_name, first_row=firstRow, first_column=firstColumn, row_count=rowCount, column_count=columnCount, folder=folder)
        assert(len(response.cells_list) > 0)

        range_name = "A1:B3"
        response = self.api.cells_ranges_get_worksheet_cells_range_value(name, sheet_name, namerange=range_name, folder=folder)
        # assert(len(response.cells_list) > 0)

        range_name = "Name_2"
        response = self.api.cells_ranges_get_worksheet_cells_range_value(name, sheet_name, namerange=range_name, folder=folder)
        assert(len(response.cells_list) > 0)
        pass

    def test_cells_ranges_post_worksheet_cells_range_column_width(self):
        """
        Test case for cells_ranges_post_worksheet_cells_range_column_width

        Set column width of range
        """
        name ='Book1.xlsx'  
        sheet_name ='Sheet1'    
        value = 10.01
        range = Range(column_count=1, column_width = 10.1, first_column = 1, first_row = 1, row_count = 10, row_height=10)
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_ranges_post_worksheet_cells_range_column_width(name, sheet_name, value,range=range,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_ranges_post_worksheet_cells_range_merge(self):
        """
        Test case for cells_ranges_post_worksheet_cells_range_merge

        Combines a range of cells into a single cell.              
        """
        name ='Book1.xlsx'  
        sheet_name ='Sheet1'    
        range = Range(column_count=1, column_width = 10.1, first_column = 1, first_row = 1, row_count = 10, row_height=10)
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_ranges_post_worksheet_cells_range_merge(name, sheet_name,range=range,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_ranges_post_worksheet_cells_range_move_to(self):
        """
        Test case for cells_ranges_post_worksheet_cells_range_move_to

        Move the current range to the dest range.             
        """
        name ='Book1.xlsx'  
        sheet_name ='Sheet1'  
        destRow =1
        destColumn = 1  
        range = Range(column_count=1, column_width = 10.1, first_column = 1, first_row = 1, row_count = 10, row_height=10)
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_ranges_post_worksheet_cells_range_move_to(name, sheet_name,destRow, destColumn,range=range,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_ranges_post_worksheet_cells_range_outline_border(self):
        """
        Test case for cells_ranges_post_worksheet_cells_range_outline_border

        Sets outline border around a range of cells.
        """
        name ='Book1.xlsx'  
        sheet_name ='Sheet1'  
        rangeOperate = RangeSetOutlineBorderRequest()
        rangeOperate.border_edge = "LeftBorder"
        rangeOperate.border_style = "Dotted"
        color = Color(0, 255, 0, 0)
        rangeOperate.border_color = color
        range = Range(column_count=1, column_width = 10.1, first_column = 1, first_row = 1, row_count = 10, row_height=10)
        rangeOperate.range = range
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_ranges_post_worksheet_cells_range_outline_border(name, sheet_name,range_operate=rangeOperate,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_ranges_post_worksheet_cells_range_row_height(self):
        """
        Test case for cells_ranges_post_worksheet_cells_range_row_height

        set row height of range
        """
        name ='Book1.xlsx'  
        sheet_name ='Sheet1'    
        value = 10.01
        range = Range(column_count=1, column_width = 10.1, first_column = 1, first_row = 1, row_count = 10, row_height=10)
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_ranges_post_worksheet_cells_range_row_height(name, sheet_name, value,range=range,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_ranges_post_worksheet_cells_range_style(self):
        """
        Test case for cells_ranges_post_worksheet_cells_range_style

        Sets the style of the range.             
        """
        name ='Book1.xlsx'  
        sheet_name ='Sheet1'    
        rangeOperate = RangeSetStyleRequest()
        style = Style()
        font = Font()
        font.size = 10
        style.font = font
        rangeOperate.style = style
        range = Range(column_count=1, column_width = 10.1, first_column = 1, first_row = 1, row_count = 10, row_height=10)
        rangeOperate.range = range
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_ranges_post_worksheet_cells_range_style(name, sheet_name,range_operate=rangeOperate,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_ranges_post_worksheet_cells_range_unmerge(self):
        """
        Test case for cells_ranges_post_worksheet_cells_range_unmerge

        Unmerges merged cells of this range.             
        """
        name ='Book1.xlsx'  
        sheet_name ='Sheet1'    
        range = Range(column_count=1, column_width = 10.1, first_column = 1, first_row = 1, row_count = 10, row_height=10)
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_ranges_post_worksheet_cells_range_unmerge(name, sheet_name,range=range,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_ranges_post_worksheet_cells_range_value(self):
        """
        Test case for cells_ranges_post_worksheet_cells_range_value

        Puts a value into the range, if appropriate the value will be converted to other data type and cell's number format will be reset.             
        """
        name ='Book1.xlsx'  
        sheet_name ='Sheet1' 
        value = "null"   
        range = Range(column_count=1, column_width = 10.1, first_column = 1, first_row = 1, row_count = 10, row_height=10)
        isConverted = True
        setStyle = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_ranges_post_worksheet_cells_range_value(name, sheet_name,value,range=range,is_converted=isConverted, set_style = setStyle,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_ranges_post_worksheet_cells_ranges(self):
        """
        Test case for cells_ranges_post_worksheet_cells_ranges

        copy range in the worksheet
        """
        name ='Book1.xlsx'  
        sheet_name ='Sheet1' 
        rangeOperate = RangeCopyRequest()
        rangeOperate.operate = "copydata"
        pasteOptions = PasteOptions()
        pasteOptions.only_visible_cells = True
        rangeOperate.paste_options = pasteOptions
        range = Range(column_count=1, column_width = 10.1, first_column = 1, first_row = 1, row_count = 10, row_height=10)
        range2 = Range(column_count=1, column_width = 10.1, first_column = 10, first_row = 10, row_count = 10, row_height=10)
        rangeOperate.source = range
        rangeOperate.target = range2
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_ranges_post_worksheet_cells_ranges(name, sheet_name, range_operate=rangeOperate,folder=folder)
        self.assertEqual(result.code,200)
        pass
    def test_cells_ranges_put_worksheet_cells_range(self):
        """
        Test case for cells_ranges_put_worksheet_cells_range

        copy range in the worksheet
        """
        name ='Book1.xlsx'  
        sheet_name ='Sheet1' 
        range = 'A1:B5'
        shift = 'Down'
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_ranges_put_worksheet_cells_range(name, sheet_name, range,shift,folder=folder)
        self.assertEqual(result.code,200)
        pass
    def test_cells_ranges_delete_worksheet_cells_range(self):
        """
        Test case for cells_ranges_delete_worksheet_cells_range

        copy range in the worksheet
        """
        name ='Book1.xlsx'  
        sheet_name ='Sheet1' 
        range = 'A1:B5'
        shift = 'Up'
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_ranges_delete_worksheet_cells_range(name, sheet_name, range,shift,folder=folder)
        self.assertEqual(result.code,200)
        pass

if __name__ == '__main__':
    unittest.main()

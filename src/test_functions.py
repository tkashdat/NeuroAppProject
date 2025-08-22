# unit tests for functions
import data_loading_functions as dlf
import app_functions as af
from unittest import mock
from unittest import TestCase

class TestFileLoading(TestCase):
    def test_file_keys(self):
        dlf.loadStudy()
        self.assertTrue("('SAG 3D T1 SPGR','20100204',(184,256,256))")

    def test_file_size(self):
        dlf.loadStudy()
        self.assertTrue("('SAG 3D T1 SPGR','20100204',(184,255,256))")

class TestUserInputFunctions(TestCase):
    @mock.patch('app_functions.sliceColor.input', create=True)
    def test_slice_color(self, mocked_input):
        mocked_input= 'gray'
        result = af.sliceColor("Please enter a color ('jet', 'gray', or 'bone')")
        self.assertEqual(result, 'gray')
    
    @mock.patch('app_functions.sliceColor.input', create=True)
    def test_slice_color2(self, mocked_input):   
        mocked_input= 'rainbow'
        result = af.sliceColor("Please enter a color ('jet', 'gray', or 'bone')")
        self.assertEqual(result, 'bone')


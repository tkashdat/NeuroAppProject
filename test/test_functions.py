# unit tests for functions in src/functions.py
import data_loading_functions as dlf
import unittest

class TestFileLoading(unittest.TestCase):
    def test_file_keys(self):
        dlf.loadStudy()
        self.assertTrue('SAG 3D T1 SPGR','20100204',(256,256))
    
    def test_file_type(self):
        dlf.loadStudy()
        self.assertRaises(TypeError)

    def test_file_size(self):
        dlf.loadStudy()
        self.assertTrue('SAG 3D T1 SPGR','20100204',(256,256))
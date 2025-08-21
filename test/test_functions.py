# unit tests for functions in src/functions.py

class TestFileLoading(unittest.TestCase):
    def test_file_keys(self):
        loadStudy()
        self.assertTrue('SAG 3D T1 SPGR','20100204',(256,256))
    
    def test_file_type(self):
        loadStudy()
        self.assertRaises(TypeError)

    def test_file_size(self):
        loadStudy()
        self.assertTrue()
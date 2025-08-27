# unit tests for functions
import data_loading_functions as dlf
import app_functions as af
from unittest.mock import MagicMock, patch
from unittest import TestCase

class TestUserInputFunctions(TestCase):
    @patch('builtins.input', )
    def test_slice_color(self, mocked_input):
        mocked_input= 'gray'
        result = af.sliceColor()
        self.assertEqual(result, 'gray')
    
    @patch('app_functions.sliceColor.input')
    def test_slice_color2(self, mocked_input):   
        mocked_input= 'rainbow'
        result = af.sliceColor()
        self.assertEqual(result, "That is not a valid entry")
    
    @patch('app_functions.sliceColor.input')
    def test_slice_color2(self, mocked_input):   
        mocked_input= 'rainbow'
        result = af.sliceColor()
        self.assertEqual(result, "rainbow")

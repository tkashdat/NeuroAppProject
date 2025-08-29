# unit tests for functions
import app_functions as af
from unittest.mock import patch
from unittest import TestCase

class TestUserInputFunctions(TestCase):
    @patch('matplotlib.pyplot.imshow')
    @patch('matplotlib.pyplot.title')
    @patch('matplotlib.pyplot.axis')
    @patch('matplotlib.pyplot.show')
    @patch('builtins.input', side_effect=['5'])
    def test_show_slice_valid(self, mock_input, mock_show, mock_axis, mock_title, mock_imshow):
        """Test showing a valid slice against a mock DICOM class instance."""
        class MockDicom:
            def __init__(self, shape):
                self.shape = shape
            def __getitem__(self, idx):
                return [[0]]
        mock_file = MockDicom((10, 10, 10))
        af.showSlice(mock_file)
        mock_imshow.assert_called()
        mock_title.assert_called()
        mock_axis.assert_called_with('off')
        mock_show.assert_called()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['100', '5'])
    def test_show_slice_out_of_bounds(self, mock_input, mock_print):
        """Test showing an out-of-bounds slice number against a mock DICOM class instance."""
        class MockDicom:
            def __init__(self, shape):
                self.shape = shape
            def __getitem__(self, idx):
                return [[0]]
        mock_file = MockDicom((10, 10, 10))
        af.showSlice(mock_file)
        mock_print.assert_any_call('Not a valid slice number')

    def test_meta_data(self):
        """Test retrieving metadata keys from a mock DICOM class instance."""
        class MockDicom:
            def __init__(self, meta):
                self.meta = meta
        mock_file = MockDicom({'foo': 1, 'bar': 2})
        result = af.metaData(mock_file)
        self.assertEqual(set(result), {'foo', 'bar'})

    def test_meta_data_invalid(self):
        """Test metaData function with invalid mock DICOM No Meta instances."""
        # Case 1: meta attribute missing
        class MockDicomNoMeta:
            pass
        mock_file_missing = MockDicomNoMeta()
        with self.assertRaises(AttributeError):
            af.metaData(mock_file_missing)

        # Case 2: meta attribute wrong type
        class MockDicomWrongMeta:
            def __init__(self):
                self.meta = 123
        mock_file_wrong = MockDicomWrongMeta()
        with self.assertRaises(AttributeError):
            af.metaData(mock_file_wrong)

    def test_print_slices(self):
        """Test printing slice counts from a mock DICOM class instance."""
        class MockDicom:
            def __init__(self, shape):
                self.shape = shape
        mock_file = MockDicom((12, 34, 56))
        result = af.printSlices(mock_file)
        self.assertEqual(result, "Number of slices per view: Saggital: 12, Axial: 34, Coronal: 56")

    def test_print_slices_invalid(self):
        """Test printSlices function with invalid mock DICOM No Shape instances."""
        # Case 1: shape attribute missing
        class MockDicomNoShape:
            pass
        mock_file_missing = MockDicomNoShape()
        with self.assertRaises(AttributeError):
            af.printSlices(mock_file_missing)

        # Case 2: shape attribute wrong type
        class MockDicomWrongShape:
            def __init__(self):
                self.shape = 123
        mock_file_wrong = MockDicomWrongShape()
        with self.assertRaises(TypeError):
            af.printSlices(mock_file_wrong)
    
    def test_num_slices(self):
        """Test numSlices function with a valid mock DICOM class instance."""
        class MockDicom:
            def __init__(self, shape):
                self.shape = shape
        mock_file = MockDicom((12, 34, 56))
        result = af.numSlices(mock_file)
        self.assertEqual(result, (12, 34, 56))

    def test_num_slices_invalid(self):
        """Test numSlices function with invalid mock DICOM No Shape instances."""
        # Case 1: shape attribute missing
        class MockDicomNoShape:
            pass
        mock_file_missing = MockDicomNoShape()
        with self.assertRaises(AttributeError):
            af.numSlices(mock_file_missing)

        # Case 2: shape attribute wrong type
        class MockDicomWrongShape:
            def __init__(self):
                self.shape = 123
        mock_file_wrong = MockDicomWrongShape()
        with self.assertRaises(TypeError):
            af.numSlices(mock_file_wrong)

    @patch('builtins.print')
    @patch('matplotlib.pyplot.imshow')
    @patch('matplotlib.pyplot.title')
    @patch('matplotlib.pyplot.axis')
    @patch('matplotlib.pyplot.show')
    @patch('builtins.input', side_effect=['saggital', '5'])
    def test_pick_slice_axis_valid(self, mock_input, mock_show, mock_axis, mock_title, mock_imshow, mock_print):
        """Test picking a valid slice axis and number against a mock DICOM class instance."""
        class MockDicom:
            def __init__(self, shape):
                self.shape = shape
            def __getitem__(self, idx):
                return [[0]]
        mock_file = MockDicom((10, 10, 10))
        af.pickSliceAxis(mock_file)
        mock_imshow.assert_called()
        mock_title.assert_called()
        mock_axis.assert_called_with('off')
        mock_show.assert_called()
        mock_print.assert_not_called()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['invalid_axis', '0'])
    def test_pick_slice_axis_invalid_axis(self, mock_input, mock_print):
        """Test picking a slice with an invalid axis against a mock DICOM class instance."""
        class MockDicom:
            def __init__(self, shape):
                self.shape = shape
        mock_file = MockDicom((10, 10, 10))
        af.pickSliceAxis(mock_file)
        mock_print.assert_any_call('Invalid entry')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['axial', '100'])
    def test_pick_slice_axis_out_of_bounds(self, mock_input, mock_print):
        """Test picking a slice with an out-of-bounds number against a mock DICOM class instance."""
        class MockDicom:
            def __init__(self, shape):
                self.shape = shape
        mock_file = MockDicom((10, 10, 10))
        af.pickSliceAxis(mock_file)
        mock_print.assert_any_call('Invalid entry')

    @patch('builtins.print')
    @patch('matplotlib.pyplot.imshow')
    @patch('matplotlib.pyplot.title')
    @patch('matplotlib.pyplot.axis')
    @patch('matplotlib.pyplot.show')
    @patch('builtins.input', side_effect=['saggital', '5'])
    def test_complete_slice_valid(self, mock_input, mock_show, mock_axis, mock_title, mock_imshow, mock_print):
        """Test completing a slice with a valid axis, number, and color against a mock DICOM class instance."""
        class MockDicom:
            def __init__(self, shape):
                self.shape = shape
            def __getitem__(self, idx):
                return [[0]]
        mock_file = MockDicom((10, 10, 10))
        af.completeSlice(mock_file, 'gray')
        mock_imshow.assert_called()
        mock_title.assert_called()
        mock_axis.assert_called_with('off')
        mock_show.assert_called()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['invalid_axis', '0'])
    def test_complete_slice_invalid_axis(self, mock_input, mock_print):
        """Test completing a slice with an invalid axis against a mock DICOM class instance."""
        class MockDicom:
            def __init__(self, shape):
                self.shape = shape
                # For __getitem__ support if needed
                self.data = [[[0]]*shape[2]]*shape[1]*shape[0]
            def __getitem__(self, idx):
                return 0
        mock_file = MockDicom((10, 10, 10))
        af.completeSlice(mock_file, 'gray')
        mock_print.assert_any_call('Invalid entry')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['axial', '100'])
    def test_complete_slice_out_of_bounds(self, mock_input, mock_print):
        """Test completing a slice with an out-of-bounds number against a mock DICOM class instance."""
        class MockDicom:
            def __init__(self, shape):
                self.shape = shape
                self.data = [[[0]]*shape[2]]*shape[1]*shape[0]
            def __getitem__(self, idx):
                return 0
        mock_file = MockDicom((10, 10, 10))
        af.completeSlice(mock_file, 'gray')
        mock_print.assert_any_call('Invalid entry')

    @patch('builtins.input', side_effect=['gray', 'jet', 'bone'])
    def test_slice_color_true_values(self, mocked_input):
        """Test valid color inputs."""
        self.assertEqual(af.sliceColor(), 'gray')
        self.assertEqual(af.sliceColor(), 'jet')
        self.assertEqual(af.sliceColor(), 'bone')

    @patch('builtins.input', return_value='GRAY')
    def test_slice_color_all_caps(self, mocked_input):
        """Test sliceColor function with valid input 'GRAY' in all caps."""
        result = af.sliceColor()
        self.assertEqual(result, 'gray')

    @patch('builtins.input', return_value='rainbow')
    def test_slice_color_not_valid_entry(self, mocked_input):   
        """Test sliceColor function with invalid input 'rainbow'."""
        result = af.sliceColor()
        self.assertEqual(result, "That is not a valid entry")

    def test_get_aspect_ratio(self):
        """Test getAspectRatio function with a valid mock DICOM class instance."""
        class MockDicom:
            def __init__(self, sampling):
                self.meta = {'sampling': sampling}
        # Example sampling values
        sampling = (2.0, 4.0, 8.0)
        mock_file = MockDicom(sampling)
        saggital_asp, coronal_asp, axial_asp = af.getAspectRatio(mock_file)
        self.assertAlmostEqual(saggital_asp, 2.0/4.0)
        self.assertAlmostEqual(coronal_asp, 2.0/8.0)
        self.assertAlmostEqual(axial_asp, 4.0/8.0)

    def test_get_aspect_ratio_invalid(self):
        """Test getAspectRatio function with invalid mock DICOM No Sampling instances."""
        class MockDicom:
            def __init__(self, sampling):
                self.meta = {'sampling': sampling}
        # Case 1: sampling key missing
        class MockDicomNoSampling:
            def __init__(self):
                self.meta = {}
        mock_file_missing = MockDicomNoSampling()
        with self.assertRaises(KeyError):
            af.getAspectRatio(mock_file_missing)

        # Case 2: sampling tuple has wrong length
        mock_file_short = MockDicom((1.0, 2.0))
        with self.assertRaises(ValueError):
            af.getAspectRatio(mock_file_short)

#This function loads the dicom image data for one study containing an image stack for one individual
import imageio as iio

def loadVolume():
    """
    Prompts user to input the path to the location of the study folder. 
    Must be a folder containing DICOM MRI images.
    """
    filename = input("Enter path to study folder: ")
    vol = iio.volread(filename, 'DICOM')
    print(f"Description: {vol.meta['SeriesDescription']}, Date: {vol.meta['SeriesDate']}, Size: {vol.shape}")
    return(vol)
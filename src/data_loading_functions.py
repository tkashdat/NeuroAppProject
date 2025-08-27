#This function loads the dicom image data for one study containing an image stack for one individualimpo
import imageio as iio

def loadStudy():
    filename = input("Enter path to study folder: ")
    vol = iio.volread(filename, 'DICOM')
    
    return(vol.meta['SeriesDescription'],vol.meta['SeriesDate'],vol.shape)

def loadVolume():
    vol = iio.volread("/Users/tiffanykashima/NeuroAppProject/data/DICOM")
    return(vol)
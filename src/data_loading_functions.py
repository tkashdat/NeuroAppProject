#This function loads the dicom image data for one study containing an image stack for one individualimpo
import imageio as iio

def loadVolume():
    filename = input("Enter path to study folder: ")
    vol = iio.volread(filename, 'DICOM')
    print(f"Description: {vol.meta['SeriesDescription']}, Date: {vol.meta['SeriesDate']}, Size: {vol.shape}")
    return(vol)
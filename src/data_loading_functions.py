#This function loads the dicom image data for one study containing an image stack for one individualimpo
import imageio as iio

def loadStudy():
    filename = input("Enter path to study folder: ")
    try:
        vol = iio.volread(filename)
        vol.meta['Modality'] == 'MR'
    except TypeError:
        print("Not the correct modality type.  Uploaded study should be MRI image data")
    
    return(vol.meta['SeriesDescription'],vol.meta['Series Date'],vol.shape)


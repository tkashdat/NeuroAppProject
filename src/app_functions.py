#custom functions for use across the project in notebook
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

def showSlice(fileName):
    """
     Takes user input (integer value) for a single slice in the saggital plane to display (default cmap).  
     Input must be an integer in range of the available slices in the saggital plane for specified study.
    """
    while True: 
        printSlices(fileName)
        sliceNum = int(input("What number slice would you like in saggital view?"))
        #sliceNum = int(sliceNum)
        if sliceNum <= fileName.shape[0]:
            plt.imshow(fileName[sliceNum,:,:])
            plt.axis('off')
            plt.title(f"This is slice number {sliceNum} in saggital view in standard color tone")
            plt.show()
            break
        else:
            print("Not a valid slice number")
            return "Not a valid slice number"
            continue

def metaData(fileName):
    """
    Takes a processed DICOM file (from loadVolume() method).
    """
    return(fileName.meta.keys())

def printSlices(fileName):
    """
    Takes a processed DICOM file (from loadVolume() method). 
    Uses the shape method to store the number of slices (integer) in the study by plane 
    (saggital, coronal, axial) into three variables, respectively, and returns a print statement.
    """
    x,y,z = fileName.shape
    return(f"Number of slices per view: Saggital: {x}, Axial: {y}, Coronal: {z}")

def numSlices(fileName):
    """
    Takes a processed DICOM file (from loadVolume() method). 
    Uses the shape method to store the number of slices (integer) in the study by plane 
    (saggital, coronal, axial) into three variables, respectively.
    """
    x,y,z = fileName.shape
    return(x,y,z)

def pickSliceAxis(fileName):
    """
        Takes a processed DICOM file (from loadVolume() method).  
        Takes user input (axis: string value) for one specific plane (axis): saggital, coronal, or axial.  
        Takes additional user input (sliceNum: integer value) for the number slice to view.  
        Value must be less than or equal to the number of slices (n0, n1, n2).  
        Uses matplotlib to create a slice graphic based on the user input in the 'bone' color map.
    """
    n0, n1, n2 = fileName.shape
    #printSlices(fileName)
    axis = input("Specify which axis you would like to view (saggital, axial, coronal: ").lower() #prevent capitalization issues
    sliceNum = int(input("Specifiy the slice number you would like to view: "))
    
    if axis == "saggital" and sliceNum <= n0:
        plt.imshow(fileName[sliceNum,:,:], cmap='bone')
        plt.axis('off')
        plt.title(f"This is slice number {sliceNum} in {axis} view in bone color map")
        plt.show()

    elif axis == "axial" and sliceNum <= n1:
        plt.imshow(ndi.rotate(fileName[:,sliceNum,:],270), cmap='bone') #rotates image 270 degrees for standard orientation
        plt.axis('off')
        plt.title(f"This is slice number {sliceNum} in {axis} view in bone color map")
        plt.show()

    elif axis == "coronal" and sliceNum <= n2:
        plt.imshow(ndi.rotate(fileName[:,:,sliceNum],270), cmap='bone') #rotates image 270 degrees for standard orientation
        plt.axis('off')
        plt.title(f"This is slice number {sliceNum} in {axis} view in bone color map")
        plt.show()

    else:
        print("Invalid entry")

def completeSlice(fileName, color): #color argument can use sliceColor method
    """
        Takes a processed DICOM file (from loadVolume() method).  
        Takes user input (sliceNum: string value) for one specific plane (axis): saggital, coronal, or axial.  
        Takes user input (axis: integer value) for the number slice to view.  
        Takes user input (color argument) for cmap value.
        Value must be less than or equal to the number of slices (n0, n1, n2).  
        Uses matplotlib to create a slice graphic based on the user input in the specified color map.
    """
    n0, n1, n2 = fileName.shape
    #printSlices(fileName)
    axis = input("Specify which axis you would like to view (saggital, axial, coronal): ").lower()
    sliceNum = int(input("Specifiy the slice number you would like to view: "))
    #sliceNum = int(sliceNum)
    
    if axis == "saggital" and sliceNum <= n0:
        plt.imshow(fileName[sliceNum,:,:], cmap=color)
        plt.title(f"This is slice number {sliceNum} in {axis} view in color map {color}")
        plt.axis('off')
        plt.show()

    elif axis == "axial" and sliceNum <= n1:
        plt.imshow(ndi.rotate(fileName[:,sliceNum,:],270), cmap=color) #rotates image 270 degrees for standard orientation
        plt.title(f"This is slice number {sliceNum} in {axis} view in color map {color}")
        plt.axis('off')
        plt.show()

    elif axis == "coronal" and sliceNum <= n2:
        plt.imshow(ndi.rotate(fileName[:,:,sliceNum],270), cmap=color) #rotates image 270 degrees for standard orientation
        plt.title(f"This is slice number {sliceNum} in {axis} view in color map {color}")
        plt.axis('off')
        plt.show()

    else:
        print("Invalid entry")

def sliceColor():
    """
        Prompts the user to input the name of a color map to use in matplotlib methods in generating 
        MRI image figures.  Must be 'jet' (color), 'bone' (darker greyscale), or 'gray' (light grayscale).  
        Input must be a string value.
    """
    colors = ('gray', 'jet', 'bone')
    user_input = input("Choose color: gray, jet, or bone").lower() #prevent issues with capitalization
    if user_input in colors:
        return(user_input)
    else:
        print("That is not a valid entry")
        return "That is not a valid entry"

def getAspectRatio(fileName):
    """
    Takes a processed DICOM file (from loadVolume() method). 
    Stores the float values from the 'sampling' key from the metadata dictionary for fileName into 
    three variables(d0, d1, d2), respectively.  These values represent physical distances used in the MRI scan process.  
    These values can be used to re-create the correct aspect ratios in each plane (saggital, coronal, axial) 
    for viewing slices.
    """
    d0, d1, d2 = fileName.meta['sampling']
    axial_asp = d1/d2
    saggital_asp = d0/d1
    coronal_asp = d0/d2
    return (saggital_asp, coronal_asp, axial_asp)




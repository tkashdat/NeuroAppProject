#custom functions for use across the project
import matplotlib.pyplot as plt

def showSlice(fileName,sliceNum):
    plt.imshow(fileName[sliceNum,:,:], smap='gray')
    plt.axis('off')
    plt.shw()

def metaData(fileName):
    return(fileName.meta.keys())

def numSlices(fileName):
    x,y,z = fileName.shape
    print("Number of slices per view:nt", "Axial: ",x," nt","Coronal: ", y, " nt", "Saggital: ", z, " nt")

def pickSliceAxis(fileName):

    n0, n1, n2 = fileName.shape

    try:
        sliceNum = input("Specifiy the slice number you would like to view: ")
    except TypeError:
        print("Slice number is not an integer")
    
    try:
        axis = input("Specify which axis you would like to view (axial, coronal, transverse): ")
    except:
        print("Not a valid axis selection, please try again.")
    
    if axis == "axial" and sliceNum <= n0:
        plt.imshow(fileName[sliceNum,:,:], cmap='gray')
        plt.axis('off')
        plt.shw()

    if axis == "coronal" and sliceNum <= n1:
        plt.imshow(fileName[:,sliceNum,:], cmap='gray')
        plt.axis('off')
        plt.shw()

    if axis == "transverse" and sliceNum <= n2:
        plt.imshow(fileName[:,:,sliceNum], cmap='gray')
        plt.axis('off')
        plt.shw()


def sliceColor(promptMessage):
    colors = ('gray', 'jet', 'bone')
    while True:
        user_input = input(promptMessage)
        if user_input in colors:
            return(user_input)
        else:
            print("That is not a valid entry")
            continue

    

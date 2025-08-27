#custom functions for use across the project
import matplotlib.pyplot as plt

def showSlice(fileName,sliceNum):
    plt.imshow(fileName[sliceNum,:,:], cmap='gray')
    plt.axis('off')
    plt.title(f"This is slice number {sliceNum} in axial view in gray tone")
    plt.shw()

def metaData(fileName):
    return(fileName.meta.keys())

def numSlices(fileName):
    x,y,z = fileName.shape
    print(f"Number of slices per view: Axial: {x}, Coronal: {y}, Transverse: {z}")

def pickSliceAxis(fileName):

    n0, n1, n2 = fileName.shape

    sliceNum = input("Specifiy the slice number you would like to view: ")

    axis = input("Specify which axis you would like to view (axial, coronal, transverse): ")
    
    
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

    else:
        print("Invalid entry")

def sliceColor(promptMessage):
    colors = ('gray', 'jet', 'bone')
    while True:
        user_input = input(promptMessage)
        if user_input in colors:
            return(user_input)
        else:
            print("That is not a valid entry")
            continue

    

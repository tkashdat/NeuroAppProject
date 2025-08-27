#custom functions for use across the project
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

def showSlice(fileName):
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
            continue

def metaData(fileName):
    return(fileName.meta.keys())

def printSlices(fileName):
    x,y,z = fileName.shape
    return(f"Number of slices per view: Saggital: {x}, Axial: {y}, Coronal: {z}")

def numSlices(fileName):
    x,y,z = fileName.shape
    return(x,y,z)

def pickSliceAxis(fileName):
    n0, n1, n2 = fileName.shape
    printSlices(fileName)
    axis = input("Specify which axis you would like to view (saggital, axial, coronal: ").lower()
    sliceNum = int(input("Specifiy the slice number you would like to view: "))
    
    if axis == "saggital" and sliceNum <= n0:
        plt.imshow(fileName[sliceNum,:,:], cmap='bone')
        plt.axis('off')
        plt.title(f"This is slice number {sliceNum} in {axis} view in bone color map")
        plt.show()

    elif axis == "axial" and sliceNum <= n1:
        plt.imshow(ndi.rotate(fileName[:,sliceNum,:],270), cmap='bone')
        plt.axis('off')
        plt.title(f"This is slice number {sliceNum} in {axis} view in bone color map")
        plt.show()

    elif axis == "coronal" and sliceNum <= n2:
        plt.imshow(ndi.rotate(fileName[:,:,sliceNum],270), cmap='bone')
        plt.axis('off')
        plt.title(f"This is slice number {sliceNum} in {axis} view in bone color map")
        plt.show()

    else:
        print("Invalid entry")

def completeSlice(fileName, color):
    n0, n1, n2 = fileName.shape
    printSlices(fileName)
    axis = input("Specify which axis you would like to view (saggital, axial, coronal): ").lower()
    sliceNum = int(input("Specifiy the slice number you would like to view: "))
    #sliceNum = int(sliceNum)
    
    if axis == "saggital" and sliceNum <= n0:
        plt.imshow(fileName[sliceNum,:,:], cmap=color)
        plt.title(f"This is slice number {sliceNum} in {axis} view in color map {color}")
        plt.axis('off')
        plt.show()

    elif axis == "axial" and sliceNum <= n1:
        plt.imshow(ndi.rotate(fileName[:,sliceNum,:],270), cmap=color)
        plt.title(f"This is slice number {sliceNum} in {axis} view in color map {color}")
        plt.axis('off')
        plt.show()

    elif axis == "coronal" and sliceNum <= n2:
        plt.imshow(ndi.rotate(fileName[:,:,sliceNum],270), cmap=color)
        plt.title(f"This is slice number {sliceNum} in {axis} view in color map {color}")
        plt.axis('off')
        plt.show()

    else:
        print("Invalid entry")

def sliceColor():
    colors = ('gray', 'jet', 'bone')
    user_input = input("Choose color: gray, jet, or bone").lower()
    if user_input in colors:
        return(user_input)
    else:
        print("That is not a valid entry")

def getAspectRatio(fileName):
    d0, d1, d2 = fileName.meta['sampling']
    axial_asp = d1/d2
    saggital_asp = d0/d1
    coronal_asp = d0/d2
    return (saggital_asp, coronal_asp, axial_asp)




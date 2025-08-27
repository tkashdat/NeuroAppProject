#custom functions for use across the project
import matplotlib.pyplot as plt

def showSlice(fileName):
    sliceNum = input("What slice would you like to view?")
    sliceNum = int(sliceNum)
    while True:
        if sliceNum <= fileName.shape[0]:
            plt.imshow(fileName[sliceNum,:,:])
            plt.axis('off')
            plt.title(f"This is slice number {sliceNum} in axial view in standard color tone")
            plt.show()
            break
        else:
            print("Not a valid slice number")
            continue

def metaData(fileName):
    return(fileName.meta.keys())

def numSlices(fileName):
    x,y,z = fileName.shape
    print(f"Number of slices per view: Axial: {x}, Coronal: {y}, Transverse: {z}")
    return(x, y, z)

def pickSliceAxis(fileName):

    n0, n1, n2 = fileName.shape
    sliceNum = input("Specifiy the slice number you would like to view: ")
    sliceNum = int(sliceNum)
    axis = input("Specify which axis you would like to view (axial, coronal, transverse): ")
    
    if axis == "axial" and sliceNum <= n0:
        plt.imshow(fileName[sliceNum,:,:], cmap='bone')
        plt.axis('off')
        plt.show()

    if axis == "coronal" and sliceNum <= n1:
        plt.imshow(fileName[:,sliceNum,:], cmap='bone')
        plt.axis('off')
        plt.show()

    if axis == "transverse" and sliceNum <= n2:
        plt.imshow(fileName[:,:,sliceNum], cmap='bone')
        plt.axis('off')
        plt.show()

    else:
        print("Invalid entry")

def completeSlice(fileName, color):

    n0, n1, n2 = fileName.shape
    sliceNum = input("Specifiy the slice number you would like to view: ")
    sliceNum = int(sliceNum)
    axis = input("Specify which axis you would like to view (axial, coronal, transverse): ")
    
    if axis == "axial" and sliceNum <= n0:
        plt.imshow(fileName[sliceNum,:,:], cmap=color)
        plt.axis('off')
        plt.show()

    if axis == "coronal" and sliceNum <= n1:
        plt.imshow(fileName[:,sliceNum,:], cmap=color)
        plt.axis('off')
        plt.show()

    if axis == "transverse" and sliceNum <= n2:
        plt.imshow(fileName[:,:,sliceNum], cmap=color)
        plt.axis('off')
        plt.show()

    else:
        print("Invalid entry")

def sliceColor():
    colors = ('gray', 'jet', 'bone')
    user_input = input("Choose color: gray, jet, or bone")
    if user_input in colors:
        return(user_input)
    else:
        print("That is not a valid entry")

def getAspectRatio(fileName):
    d0, d1, d2 = fileName.meta['sampling']
    axial_asp = d1/d2
    saggital_asp = d0/d1
    coronal_asp = d0/d2
    return (axial_asp, coronal_asp, saggital_asp)




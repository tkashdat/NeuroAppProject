# Neuroscience MRI Application Project

*Author: Tiffany Kashima

*Arizona State University

*CAS502: Computation (Professor Julia Damerow) Spring 2025

## Project Description

This project explores the basic skills and considerations in displaying MRI images from DICOM files in a way that is useful to a user without coding experience, such as a medical researcher or clinician.  This provides the opportunity to consider and select the correct features and packages available in python, explore options in image display and study reconstruction, as well as creating a basic application to dynamically view and interact with the images.

MRI data is stored in a variety of files formats, typically depending on the context in which the data is being used.  For example, in most medical and healthcare settings, MRI image data is in DICOM (Digital Imaging and Communications in Medicine) format, while in the reserach setting, a common format is NIFTI (Neuroimaging Informatics Technology Initiative).  Metadata for the images is stored in a separate header, which can be in TSV or JSON, as well. 

Written in Python 3.11 using Jupyter Notebook.  

Adapted from Neural Data Science in Python (Aaron Newman) 

## Features

Demonstration of study upload and basic file features, including number of images, meta data, uploaded object type, slice thickness and aspect ratio.  Graphic features include using matplotlib to display individual images with correct orientation in 3 viewing planes and 3 color map options.  Finally, all of these skills are put together in one cohesive ipywidget "application" that allows the user to dynamicaly move through the slices in axial, coronal, and saggital planes with the option to choose three different color maps.  

## Dataset

The dataset for this notebook is located in the folder data_public (in this repository) as "DICOM." You may download the dataset folder and unzip it, making note of the location and path as you will need this information to run the notebook.  The zipped file is 16.5 MB.  The unzipped folder is 26 MB and contains 186 files, representing the stacked MRI images captured for a single subject in 3 planes.  Do not modify, add, or delete the files within the folder and keep them "as is" in the folder named "DICOM."  This is essential to how imageio reads and constructs a study volume.  You can optionally use any properly structured DICOM study folder (single study only).  

## Dependencies 

The notebook and python files were written and tested in Python 3.11 with the following dependencies: 

  - ipywidgets
  - imageio
  - matplotlib.pyplot
  - Ipython.display
  - scipy.ndimage
  - unittest

## Installation

Download all files in src folder as well as dataset in data_public folder.  Download environment file (neuro_dataascience_env.yml) from envs folder.  Store in the same local or cloud directory.  Ensure python and dependencies are installed in notebook environment before running scripts and jupyter notebook.  Ensure dataset path is accessible to notebook. 

## User Guide

1. data_loading_functions
    - loadVolume()
        Prompts user to input the path to the location of the study folder. Must be a folder containing DICOM MRI images. Uses imageio library. 
        No arguments.
        Example input: "Users/usr/folder/data/DICOM"
        Output: A numpy array, a dictionary of meta data from its 'meta' attributes.
2. app_functions
    - showSlice(fileName: string)
        Takes user input (integer value) for a single slice in the saggital plane to display (default cmap).  Input must be an integer in range of the available slices in the saggital plane for specified study (fileName).  Uses matplotlib.
        Example usage: showSlice(myStudy)
    - metaData(fileName: string)
        Takes a processed DICOM file (from loadVolume() method).  
        Example usage: metaData(myStudy)
        Output: Returns the key values from the meta data dictionary for the study volume.
    - printSlices(fileName: string)
        Takes a processed DICOM file (from loadVolume() method). Uses the shape method to store the number of slices (integer) in the study by plane (saggital, coronal, axial) into three variables, respectively.  
        Example usage: printSlices(myStudy)
        Output: A print statement displaying the number of slices per plane.
    - numSlices(fileName: string)
        Takes a processed DICOM file (from loadVolume() method). Uses the shape method to store the number of slices (integer) in the study by plane (saggital, coronal, axial) into three variables, respectively.
        Example usage: numSlices(myStudy)
        Output: Three variables: x, y, z assigned to the number of slices in the (saggital, coronal, axial) plane.
    - pickSliceAxis (fileName: string)
        Takes a processed DICOM file (from loadVolume() method).  Takes user input (string value) for one specific plane (axis): saggital, coronal, or axial.  Takes additional user input (integer value) for the number slice to view.  Value must be less than or equal to the number of slices.  Uses matplotlib to create a slice graphic based on the user input in the 'bone' color map.
        Example usage: pickSliceAxis(myStudy)
        Output: matplotlib figure of selected slice and plane.
    - completeSlice(fileName: string)
        Takes a processed DICOM file (from loadVolume() method).  Takes user input (string value) for one specific plane (axis): saggital, coronal, or axial.  Takes user input (integer value) for the number slice to view.  Value must be less than or equal to the number of slices.  Takes user input (string value) for one color map (cmap) option ('jet', 'bone', 'gray') to use in rendering the slice figure.  Uses matplotlib to create a slice graphic based on the user input in the specified color map.
        Example usage: completeSlice(myStudy)
        Output: matplotlib figure of selected slice and plane and cmap choice.
    - sliceColor()
        Prompts the user to input the name of a color map to use in matplotlib methods in generating MRI image figures.  Must be 'jet' (color), 'bone' (darker greyscale), or 'gray' (light grayscale).  Input must be a string value.
        No arguments.
        Output: Valis user colormap choice as a string value.
    - getAspectRatio(fileName: string)
        Takes a processed DICOM file (from loadVolume() method). Stores the float values from the 'sampling' key from the metadata dictionary for fileName into three variables, respectively.  These values represent physical distances used in the MRI scan process.  These values can be used to re-create the correct aspect ratios in each plane (saggital, coronal, axial) for viewing slices.
        Example usage: getAspectRatio(myStudy)
        Output: Three variables (float values) that store the correct aspect ratio for the saggital, coronal, and axial planes, respectively.
3. Ipywidget in neuroapp.ipynb
    - imageViewer(color='bone':string, saggital=50: integer, axial=175: integer, coronal=150: integer)
        This function is passed into the ipywidget.interactive method to create an example of a dynamically updated image viewer "application."  Takes three arguments: color (storing, default='bone'), saggital (integer, default=50), coronal (integer, default=150, axial (integer, default=150)). The default values of the arguments render a slice at these values when the widget is loaded.  This is hard coded example using the DICOM study uplaoded by loadVolume() and stored into the myStudy variable in the example notebook. Uses matplotlib to generate three ax objects for a selected slice and color map in the three different planes to be viewed simutaneously.
    - widget
        Allows user to select from a drop down menu of color map options and to select a slice from a slider in each plane.  Three MRI images are displated and dynamically updated based on these inputs.

## Unit Testing

The test_functions.py file contains example unit tests on the app methods in app_functions.py.  Requires unittest library.  

## Feature Requests and Bugs

Please submit feature requests and bugs as an issue in the project repository.  

Please submit any individual questions or concerns to Tiffany Kashima @ tkashima@asu dot edu.

## Known Issues

The ipynotebook application in the notebook is hard coded to dataset and its assigned variable, as an example to show functionality.  In the future version, this function would also take user input for a study file. 

## Challenges anticipated
 MRI data is stored in a variety of files formats, typically depending on the context in which the data is being used.  For example, in most medical and healthcare settings, MRI image data is in DICOM (Digital Imaging and Communications in Medicine) format, while in the reserach setting, a common format is NIFTI (Neuroimaging Informatics Technology Initiative).  Metadata for the images is stored in a separate header, which can be in TSV or JSON, as well.  Thus, allowing user input allows first a validation of the data type since it is only reasonable in the scope of this project to allow only one or two formats, and then a further check on the integrity of the data set itself.  The degree of data validation could be quite complex in applications in the "real-world," so a major part of the challenge will be controlling scope creep in this area and documenting the trade-offs and decision making process in implementing this feature.

## Communication Plan
 All feature requests, potential and actual bugs, testing, research, and documentation will be added as issues and tagged appropraitely.  While there is only one person authoring this project, there is collaboration with outside sources such as the course Professor, authors of the resources being used, etc.  I will assign myself to each ticket, but also note any outside resources also being consulted.  This creates a system of transparent and fair attribution.  I will use a lite version of agile inspired project management, utlizing a kanban board in Trello to organize, track, and and assign status with pull requests, issues, and commits from git hub (using GitHub Power-Up).

## Branches 
For each ticket on Trello, I will create a branch.  When each ticket is complete, I will create a pull request into main with the same good software egineering practices of code review and testing.  It is important to demonstrate that changes are not directly merged into main without a pull request.  

## Dataset used
 A high-density diffuse optical tomography dataset of naturalistic viewing (Arefeh Sherafati*, Aahana Bajracharya*, Michael S. Jones, Emma Speh, Monalisa Munsi, Chen Hao Lin, Andrew K. Fishell, Tamara Hershey, Adam Eggebrecht, Joseph P. Culver, Jonathan E. Peelle, 2023)

### References
Arefeh Sherafati* and Aahana Bajracharya* and Michael S. Jones and Emma Speh and Monalisa Munsi and Chen Hao Lin and Andrew K. Fishell and Tamara Hershey and Adam Eggebrecht and Joseph P. Culver and Jonathan E. Peelle (2023). A high-density diffuse optical tomography dataset of naturalistic viewing. OpenNeuro. [Dataset] doi: doi:10.18112/openneuro.ds004569.v1.0.0

DOI: [doi:10.18112/openneuro.ds004569.v1.0.0](doi:10.18112/openneuro.ds004569.v1.0.0)

Data obtained from OpenNEURO [https://openneuro.org/datasets/ds004569/versions/1.0.0](https://openneuro.org/datasets/ds004569/versions/1.0.0)
under a Creative Commons license.  

Data downloaded and managed from OpenNEURO using Datalad (v1.1.4) package for Python (v 3.12)
[https://www.datalad.org/](https://www.datalad.org/)

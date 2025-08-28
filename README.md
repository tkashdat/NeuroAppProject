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

## User Guide

1. data_loading_functions
    - loadVolume()
        Prompts user to input the path to the location of the study folder. Must be a folder containing DICOM MRI images. Uses imageio library. 
        No arguments.
        Example input: "Users/usr/folder/data/DICOM"
        Output: A numpy array, a dictionary of meta data from its 'meta' attributes.
2. app_functions
    - showSlice(fileName (string: name of object assigned from loadVolume()))
        Takes user input (integer value) for a single slice in the saggital plane to display (default cmap).  Input must be an integer in range of the available slices in the saggital plane for specified study (fileName).  Uses matplotlib.
        Example usage: showSlice(myStudy)
    - 


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

# Neuroscience MRI Application Project

Author: Tiffany Kashima

Arizona State University

CAS502: Computation (Professor Julia Damerow) Spring 2025

This project produces MRI images from a dataset and allows the user to control the plane of view, orientation, contrast, and smoothing algorithm.  Future feature set includes the ability to allow user upload of a dataset with data validation.

Written in Python 3.11 using Jupyter Notebooks, Voila, and Binder.  

Adapted from Neural Data Science in Python (Aaron Newman) and Building Complex Web Applications with Jupyter Notebooks (Nicole Brewer, Juan Cabenela,  Matt Craig, SciPy 2024) 

Challenges anticipated: MRI data is stored in a variety of files formats, typically depending on the context in which the data is being used.  For example, in most medical and healthcare settings, MRI image data is in DICOM (Digital Imaging and Communications in Medicine) format, while in the reserach setting, a common format is NIFTI (Neuroimaging Informatics Technology Initiative).  Metadata for the images is stored in a separate header, which can be in TSV or JSON, as well.  Thus, allowing user input allows first a validation of the data type since it is only reasonable in the scope of this project to allow only one or two formats, and then a further check on the integrity of the data set itself.  The degree of data validation could be quite complex in applications in the "real-world," so a major part of the challenge will be controlling scope creep in this area and documenting the trade-offs and decision making process in implementing this feature.  

Communication Plan: All feature requests, potential and actual bugs, testing, research, and documentation will be added as issues and tagged appropraitely.  While there is only one person authoring this project, there is collaboration with outside sources such as the course Professor, authors of the resources being used, etc.  I will assign myself to each ticket, but also note any outside resources also being consulted.  This creates a system of transparent and fair attribution.  I will use a lite version of agile inspired project management, utlizing a kanban board in Trello to organize, track, and and assign status with pull requests, issues, and commits from git hub (using GitHub Power-Up).

Branches: For each ticket on Trello, I will create a branch.  When each ticket is complete, I will create a pull request into main with the same good software egineering practices of code review and testing.  It is important to demonstrate that changes are not directly merged into main without a pull request.  

Dataset used: A high-density diffuse optical tomography dataset of naturalistic viewing (Arefeh Sherafati*, Aahana Bajracharya*, Michael S. Jones, Emma Speh, Monalisa Munsi, Chen Hao Lin, Andrew K. Fishell, Tamara Hershey, Adam Eggebrecht, Joseph P. Culver, Jonathan E. Peelle, 2023)

Arefeh Sherafati* and Aahana Bajracharya* and Michael S. Jones and Emma Speh and Monalisa Munsi and Chen Hao Lin and Andrew K. Fishell and Tamara Hershey and Adam Eggebrecht and Joseph P. Culver and Jonathan E. Peelle (2023). A high-density diffuse optical tomography dataset of naturalistic viewing. OpenNeuro. [Dataset] doi: doi:10.18112/openneuro.ds004569.v1.0.0

DOI: [doi:10.18112/openneuro.ds004569.v1.0.0](doi:10.18112/openneuro.ds004569.v1.0.0)

Data obtained from OpenNEURO [https://openneuro.org/datasets/ds004569/versions/1.0.0](https://openneuro.org/datasets/ds004569/versions/1.0.0)
under a Creative Commons license.  

Data downloaded and managed from OpenNEURO using Datalad (v1.1.4) package for Python (v 3.12)
[https://www.datalad.org/](https://www.datalad.org/)


# Neuroscience MRI Application Project

Author: Tiffany Kashima
Arizona State University

This project produces MRI images from a dataset and allows the user to control the plane of view, orientation, contrast, and smoothing algorithm.  Future feature set includes the ability to allow user upload of a dataset with data validation.

Written in Python 3.11 using Jupyter Notebooks, Voila, and Binder.  

Adapted from Neural Data Science in Python (Aaron Newman) and Building Complex Web Applications with Jupyter Notebooks (Nicole Brewer, Juan Cabenela,  Matt Craig, SciPy 2024) 

Challenges anticipated: MRI data is stored in a variety of files formats, typically depending on the context in which the data is being used.  For example, in most medical and healthcare settings, MRI image data is in DICOM (Digital Imaging and Communications in Medicine) format, while in the reserach setting, a common format is NIFTI (Neuroimaging Informatics Technology Initiative).  Metadata for the images is stored in a separate header, which can be in TSV or JSON, as well.  Thus, allowing user input allows first a validation of the data type since it is only reasonable in the scope of this project to allow only one or two formats, and then a further check on the integrity of the data set itself.  The degree of data validation could be quite complex in applications in the "real-world," so a major part of the challenge will be controlling scope creep in this area and documenting the trade-offs and decision making process in implementing this feature.  

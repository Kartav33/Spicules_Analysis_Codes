# This repository contains all the codes necessary for the handling and producing the required results as per our article.
# We suggest the user to kindly use 16 GB RAM SSD System to run these codes as it might crash the reular 8 GB SSD or HDD systems due to the grid size of our data.
# We also recommend the use of Paraview software in parallel to the program to ensure the uniformity of the run.
# We recommend the use of VS code interpreter for our repo. 
# Using the command below, one can load all the codes into their system.

git clone https://github.com/Kartav33/Spicules_Analysis_Codes

# Load the data as well in your offline folder to ensure proper paths in accordance with the code.

# Producing the horizontal slices (x-t)
# For these plots, use the code vtkpython_heightcuts.ipynb 
# specify the height coordinates on which you want to produce the image and simply run the code.
# The code is pretty much self explanatory with proper documentation in each cell. Documentations are either in the comments or in a markdown cell

# Producing the vertical slices (z-t)
# For these plots, use the code vtkpython_x_cuts.ipynb 
# specify the height coordinates on which you want to produce the image and simply run the code.
# The code is pretty much self explanatory with proper documentation in each cell. Documentations are either in the comments or in a markdown cell

# Cumulative Distribution functions plots and study can be created using the CDF_PDF_code.ipynb

# Next step is to fit the parabola on the created vertical cuts.
# Here we have two codes parabola_fit.py and improved_parabola_fit.py The key difference is tht the latter code keeps on produing the plot until you ask the code to break the loop. If only a single run is required, then we recommend using the former one.
# Note that you have to give the x coordinates as an array in form [x-2 : x+2] because a technique known as Maximum intenstity projection has been used which makes use of the adjacent slices along the target slice to produce the image.

# The deceleration plot can be created using the deceleration ration plots.

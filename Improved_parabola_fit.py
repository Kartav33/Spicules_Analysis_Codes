import vtk
from vtkmodules.util.numpy_support import vtk_to_numpy
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Load the VTK file
reader = vtk.vtkStructuredPointsReader()
reader.SetFileName("200G_lndem_3D.vtk") # set the path file
reader.Update()

# Get the data from the VTK file
data = reader.GetOutput()
dims = data.GetDimensions()
vtk_array = data.GetPointData().GetScalars()
np_array = vtk_to_numpy(vtk_array)
np_array = np_array.reshape(dims[2], dims[1], dims[0])
Origin = data.GetOrigin()
Spacing = data.GetSpacing()

# Index at which the vertical slice has to be made
id=508

# Here we have took 5 consecutive slices assuming the id to be the center slide
selected_slices = np_array[:,:,id-2:id+3] 

# Define the custom grayscale color scheme
colors_list = [(i / 255.0, i / 255.0, i / 255.0) for i in range(256)]
values_list = [i for i in range(256)]
colors = ListedColormap(colors_list)

# Define the reversed grayscale color scheme
colors_list = [(i / 255.0, i / 255.0, i / 255.0) for i in range(255, -1, -1)]
values_list = [i for i in range(255, -1, -1)]
colors_2 = ListedColormap(colors_list)

# Define the parabolic function
def parabola(y, a, b, c):
    return -a * y ** 2 + b * y + c

while True:
    # Calculate the Maximum Intensity Projection (MIP) along the Z-axis of the 3D image
    mip_image = selected_slices.max(axis=2)

    # Create a figure to show the 2D MIP image
    fig, ax = plt.subplots()

    # Show the 2D MIP image with the customized color scheme
    image = ax.imshow(
        mip_image,
        #cmap=colors,
        cmap=colors_2,
        vmin=0,
        vmax=2,
        extent=[
            Origin[1],
            Origin[1] + Spacing[1] * (dims[1] - 1),
            Origin[2],
            Origin[2] + Spacing[2] * (dims[2] - 1),
        ]
    )

    # Prompt user to select a patch
    print("Please select a patch by clicking seven points on the image.")

    # Get three points from the user
    points = plt.ginput(7)

    # Extract x and y coordinates of the selected points
    x_coords, y_coords = zip(*points)

    # Extract the patch data
    patch_data = mip_image[
        round(min(y_coords)) : round(max(y_coords)) + 1,
        round(min(x_coords)) : round(max(x_coords)) + 1,
    ]

    # Fit the parabola to the patch data
    popt, pcov = curve_fit(parabola, y_coords, x_coords)

    # Generate y-values for plotting the fitted parabola
    y_fit = np.linspace(min(y_coords), max(y_coords), 100)

    # Compute x-values using the fitted parameters
    x_fit = parabola(y_fit, *popt)

    # Plot the patch and the fitted parabola
    ax.plot(x_coords, y_coords, "r", marker="o")  # Mark the patch coordinates
    ax.plot(x_fit, y_fit, "b", linewidth=2)  # Plot the fitted parabola

    # Print the equation of the fitted parabola
    equation = f"Parabola Equation: x = {-popt[0]:.4f}y^2 + {popt[1]:.4f}y + {popt[2]:.4f}"

    # Create the title for the plot including the equation
    plot_title = f"{equation}"

    # Refresh the plot
    fig.canvas.draw()

    # Set the title of the plot
    plt.title(plot_title, fontsize=15, color="blue")


    # Show the plot
    plt.ylabel("Height (Mm)", fontsize=15)
    plt.xlabel("Time (min)", fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.show()

    # Prompt the user to fit another parabola
    answer = input("Fit another parabola? (yes/no): ")
    if answer.lower() == "no":
        break
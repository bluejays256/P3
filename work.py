import numpy as np
import matplotlib.pyplot as plt
import os

# Define a function to generate heatmap from a text file and save the image
def generate_heatmap_from_file(file_path, output_folder):
    # Load the data from the text file assuming the numbers are separated by commas
    data = np.loadtxt(file_path, delimiter=',')
    
    # Create the heatmap
    plt.figure(figsize=(8, 6))
    plt.imshow(data, cmap='viridis', interpolation='nearest')  # Use 'viridis' colormap, can be changed
    plt.colorbar(label='local electron density')  # Add a color bar to represent the values

    # Add title and labels (optional)
    plt.title(f"Heatmap from {os.path.basename(file_path)}")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save the image to the output folder
    output_path = os.path.join(output_folder, os.path.basename(file_path).replace('.txt', '.png'))
    plt.savefig(output_path)

    # Close the plot to free memory
    plt.close()

# Folder containing the text files
input_folder = '/root/Desktop/host/p3/Local_density_of_states_near_band_edge-main/Local_density_of_states_near_band_edge-main'  # Replace with your folder path
output_folder = '/root/Desktop/host/p3/Local_density_of_states_near_band_edge/local_density_of_states_heatmap'  # Replace with your desired output folder path

# Get a list of text files in the input folder
file_paths = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.txt')]

# Loop through each file, generate a heatmap, and save the image
for file_path in file_paths:
    generate_heatmap_from_file(file_path, output_folder)

print(f"Heatmaps saved to {output_folder}")

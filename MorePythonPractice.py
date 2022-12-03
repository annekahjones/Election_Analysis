# Using the open() function with the "w" mode we will write data to the file.
# Create a filename variable to a direct or indirect path to the file.
import os

file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")

    # Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")
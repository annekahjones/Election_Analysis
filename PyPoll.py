# Assign a variable for the file to load and the path directly
file_to_upload = 'Resources/election_results.csv'

# Open the election results 
with open(file_to_upload) as election_data:
    print(election_data)

# Using an indirect path
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Get the header row.
    headers = next(file_reader)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")

    # Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")


###---------------------------------------------------------------------------------------------------###
###---------------------------------------------------------------------------------------------------###
###---------------------------------------------------------------------------------------------------###
###---------------------------------------------------------------------------------------------------###
###---------------------------------------------------------------------------------------------------###

# Pseudocode of things we want to accomplish/retrieve
# 1. The total number of votes cast
# 2. A complete list of the candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes of each candidate
# 5. The winner of the election based on popular vote


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")



# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Candidate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""

winning_count = 0

winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
# Save the results to our text file.        
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    # Print election results to the terminal
    print(election_results, end="")

    # Save election results to the file
    txt_file.write(election_results)


    # The percentage of votes each candidate won
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)



    # The winner of the election based on popular vote
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name


    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the candidate results to our text file.
    txt_file.write(winning_candidate_summary)
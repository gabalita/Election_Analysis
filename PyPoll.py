#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote


# Add dependencies/modules
import csv
import os

# Assign a variable to load and save a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize the total votes to 0
total_votes = 0

# Intialize an empty list to keep track of candidates
candidate_options = []

# Declare an empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open files and read them
with open(file_to_load) as election_data:

    # Save as an object file to read
    file_reader = csv.reader(election_data)

    # Read and print the header
    headers = next(file_reader)

    # Print each row in the CSV file. 
    for row in file_reader:

        # Add to the total vote count.
        total_votes += 1
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Initialize the candidate's vote count to 0 (dictionary). 
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate
        candidate_votes[candidate_name] += 1

# Code to calculate vote percentage for each candidate

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100 
# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

            winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
print(winning_candidate_summary)




# Method 1: Create new dictionary for candidate (key) + % of votes (value)
    #candidate_perc = {}

    #for i in range(len(candidate_options)):

    #   name = candidate_options[i]
    #   votes = candidate_votes[name]
    #   candidate_perc[name] = float(votes) / float(total_votes) * 100

    #for key, value in candidate_perc.items():
        #print (f' {key} received {value:.1f} of the votes.')

# Method 2: Iterate through candidate_votes and candidate_optinos
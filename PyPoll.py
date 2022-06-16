# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add the dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save a file to a path
file_to_save = os.path.join("Analysis","election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# List of candidate options and votes
candidate_options = []
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in the csv file
    for row in file_reader:
        #Add to the total vote counter
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate name doesn't match any of the options
        if candidate_name not in candidate_options:
            # Add the candidate to the list
            candidate_options.append(candidate_name)

            # Begin tracking the candidates' vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to the text file
with open(file_to_save,"w") as txt_file:

    # Print the final vote count
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    
    print(election_results, end="")
    
    # Save final vote count to the text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve the votes of the candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, vote count, and percentage
        print(candidate_results)
        # Save the results to the text file
        txt_file.write(candidate_results)

        # Determine winning vote and candidate
        # Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning count to votes and winning percentage to vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning candidate to the candidate name
            winning_candidate = candidate_name

    winning_candidate_summary = (
    f"-------------------------\n"f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
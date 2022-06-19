# PyPoll with Python

## Project Overview
The purpose of the project is to conduct an election audit for a recent congressional election in Colorado, with the goal of identifying the winning candidate and county with the largest election turnout. Additionally, the project looks at how the Python script can be modified to be applicable to any election.

## Resources
Data Source: election_results.csv

Software: Python 3.7.6, Visual Studio Code 1.68.1

## Election Audit Results
The outcomes of the election show that:
- There were 369,711 votes cast in total.
- County results were as follows:
  - Jefferson County had 10.5% of the total votes with 38,855 votes cast. 
  - Denver County had 82.8% of the total votes with 306,055 votes cast. 
  - Arapahoe County had 6.7% of the total votes with 24,801 votes cast.
- Based on the above, Denver county had the largest turnout.
- Candidate results were as follows:
  - Charles Casper Stockham received 23.0% of the votes with a total of 85,213 votes. 
  - Diana DeGette received 73.8% of the votes with a total of 272,892 votes. 
  - Raymon Anthony Doane received 3.1% of the votes with 11,606 votes.
- With a total of 272,892 votes accounting for 73.8% of the total votes cast, the winner of the election is Diana DeGette.
    
## Election Audit Summary
There are several ways in which the script can be modified to be applicable for any other election, such as removing any hard coded numbers. For example, in the data provided for this election, we know that the county name is in the second column and the candidate name is in the third column, which allows us to locate the names with an index number and add them to our empty candidate and county name lists. The code excerpts for these procedures are below, where "row" refers to each row in the election data csv file:

```
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
counties = []
county_votes = {}

(code excerpts skipped)

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
```
It's no guarantee that every single data file will have the election location and candidate names located in the same columns, and so it would be helpful to identify which columns are needed. As any election has registered candidates, the proposed modification is for the election committee to provide a secondary data file listing the candidates. A list would then be made to hold those options titled, for example, "registered_candidates" and the script would loop through the election data csv to identify the index number of the column containing the candidate names. The same procedure would be followed to obtain the index number of the column holding the county (or any other election location) names.

Another consideration is that some elections, such as presidential or gubernatorial races, include multiple candidates running together (i.e., president and vice president). Some elections could then just have a list of individual candidates while others would need a dictionary with the key being the candidate for the primary position and the value being the running mate. In the script for this election, we only had to consider whether the candidate was already on the "candidate_options" list while looping through the rows:

```
# If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
```
Given that an election could have either individual or paired candidates, we would first have to identify whether the script is looking through the candidate list or dictionary, and then set up and if statement before the code above to have it loop through the needed option.

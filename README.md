# Election_Analysis

## Overview of Election Audit

The purpose of this project was to complete the following tasks on behalf of the Colorado Board of Elections:
1) Calculate the total number of votes cast.
2) Get a complete list of candidates who received votes.
3) Calculate the total number of votes each candidate received, along with their percentage breakdown.
4) Calculate the total number of votes within each county, along with their percentage breakdown. 
5) Determine which county had the largest number of votes.
6) Determine the winner of the election based on popular vote.

## Resources

- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election-Audit Results 

The analysis of the election show that:
- There were 369,711 votes cast in the election.

**County Summary**
- The county breakdown of votes was:
  - Jefferson:  10.5% (38,855)
  - Denver:  82.8% (306,055)
  - Arapahoe:  6.7% (24,801)

The county with largest number of votes was Denver with 306,055 votes. 

**Candidate Summary**
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
  
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes. 
  - Raymon Anthony Doane received 3.1% and 11,606.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.

- The winner of the election was:
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
 
## Election-Audit Summary

We encourage the election commission to reuse this Python script for other election tabulations and analysis in the future. In order to work, analysts will need to modify the file paths of the CSV/txt.files that the code is initially reading and writing too. Depending on how the election data is stored, they also may need to change the indexing for the county and candidate variables in the for loop. After these adjustments, the script will save the election board time and money as well. 



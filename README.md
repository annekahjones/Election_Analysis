# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the elections audit of a recent local congressional election

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.73.1

## Election-Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
     - Charles Casper Stockham
     - Diana DeGette
     - Raymon Anthony Doane
- The counties and thier percentage and number of votes:
     - Jefferson - 10.5% (38,855)
     - Denver - 82.8% (306,055)
     -Arapahoe - 6.7% (24,801)
- Denver county had the largest number of votes. 
- The candidate results were:
     - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes
     - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
     - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
 - The winner of the election was:
     - Diana DeGette received 73.8% of the vote and 272,892 number of votes.

## Election-Audit Summary
This coding script can be used for any future elections. It is a simple code that only requires the county name and the candidate name for each person that voted in the election in these areas. It can be modified if there are any additions to the data, such as more counties. When more counties are at play, it simply extends the lengths of our counties list and dictionary. Then, the later loops and decision statements are still able to work to see which county had the biggest turnout. This would be the same instance if there were more candidates added on the ballots. The length of the candidates list and dictionary would simply get longer, which the code will have no problem with dealing with. Since the code is so flexible, it would be a great resource for you to have on hand to be able to use at your convenience. It is easy to use, easy to read, and quick to get results from. 

# Using the open() function with the "w" mode we will write data to the file.
# Create a filename variable to a direct or indirect path to the file.
import os

file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")

# Learning how to use print statements
print("Hello World")



# Praciticing if statements
counties = ["Arapahoe", "Denver", "Jefferson"]

if counties[1] == "Denver":
    print(counties[1])



# Pracitcing if-else statements
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")



# Practicing nested if-else statements
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade
if score >= 90:
    print("Your grade is an A.")
else:
    if score >= 80:
        print("Your grade is a a B.")
    else:
        if score >= 70:
            print("Your grade is a C.")
        else:
            if score >= 60:
                print("Your grade is a D.")
            else:
                print("Your grade is an F.")



# Using Elif statments
## The previous code can be rewritten as such:
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')



# Using membership operators
counties = ["Arapahoe","Denver","Jefferson"]

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")



# Using membership and logical operators
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")



if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")



# Practicing while loops
x = 0
while x <= 5:
    print(x)
    x = x + 1



# Practicing for loops
for county in counties:
    print(county)



# Showing how different functions work
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])



# Getting keys in dictionaries
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)



# Getting values in dictionaries
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))



# Getting key-value pairs
for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")



# Printing each dictionary in a list
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)



# Getting the values from a list of dictionaries
## This is the number of registered voters from each county
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

## If we only want to get the names of the counties from each dictionary, we do this
for county_dict in voting_data:
    print(county_dict['county'])



# Using f-strings
## Old printing version
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

## New printing verison using f-strings
### percentage_votes is no longer needed as a variable because the f-string 
### performs the calculation for us
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")


## Old for loop for printing out the dictionary keys and values
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

## New version for loop for printing out the dictionary keys and values
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")



# Multiline f-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)



# Adding a thousands comma separator to our message
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")



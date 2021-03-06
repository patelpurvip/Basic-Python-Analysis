import os
import csv

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length


# ELECTION RESULTS ANALYSIS (results printed to terminal)
input_path = os.path.join('.',"election_data.csv")
output_file = os.path.join('.', "election_results.txt")
winner = ""

with open(input_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    #print(csv_header)

    voter_roll = list(csvreader)
    vote_count = len(voter_roll)

    print("Election Results:")
    print("-------------------------------------------------------")
    print("Total Votes: " + str(vote_count))
    print("-------------------------------------------------------")

    candidates = []
    names = ""
    for row in voter_roll:
        if row[2] not in candidates:
            candidates.append(row[2])
            names += " " + row[2]
    #print("Candidates receiving votes:", names)
    print("Candidates receiving votes: " + list(candidates)[0] + ", " + list(candidates)[1] + ", " + list(candidates)[2] + ", " +list(candidates)[3])

    Khan = 0
    Correy = 0
    Li = 0
    OTooley = 0

    for row in voter_roll:
        candidate = row[2]
        if candidate == "Khan":
            Khan += 1

        elif candidate == "Correy":
            Correy += 1

        elif candidate == "Li":
            Li += 1

        elif candidate == "O'Tooley":
            OTooley += 1
    
    Khan_percentage = (Khan/vote_count*100).__round__(2)
    Correy_percentage = (Correy/vote_count*100).__round__(2)
    Li_percentage = (Li/vote_count*100).__round__(2)
    OTooley_percentage = (OTooley/vote_count*100).__round__(2)
    
    print("Khan: " + str(Khan_percentage) + "% (" + str(Khan) + " votes)")
    print("Correy: " + str(Correy_percentage) + "% (" + str(Correy) + " votes)")
    print("Li: " + str(Li_percentage) + "% (" + str(Li) + " votes)")
    print("O'Tooley: " + str(OTooley_percentage) + "% (" + str(OTooley) + " votes)")
    print("-------------------------------------------------------")

    if Khan > Correy and Khan > Li and Khan > OTooley:
        print("Winner: Khan")
        winner = "Khan"
    elif Correy > Khan and Correy > Li and Correy > OTooley:
        print("Winner: Correy")
        winner = "Correy"
    elif Li > Correy and Li > Khan and Li > OTooley:
        print("Winner: Li")
        winner = "Li"
    elif OTooley > Correy and OTooley > Li and OTooley > Khan:
        print("Winner: O'Tooley")
        winner = "O'Tooley"


#  WRITE RESULTS TO TXT
with open(output_file, "w", newline="") as output_file:
    output_file.write("Election Results:")
    output_file.write("\n -------------------------------------------------------")
    output_file.write("\n Total Votes: " + str(vote_count))
    output_file.write("\n -------------------------------------------------------")
    output_file.write("\n Candidates receiving votes: " + list(candidates)[0] + ", " + list(candidates)[1] + ", " + list(candidates)[2] + ", " +list(candidates)[3])
    output_file.write("\n")
    output_file.write("\n Khan: " + str(Khan_percentage) + "% (" + str(Khan) + " votes)")
    output_file.write("\n Correy: " + str(Correy_percentage) + "% (" + str(Correy) + " votes)")
    output_file.write("\n Li: " + str(Li_percentage) + "% (" + str(Li) + " votes)")
    output_file.write("\n O'Tooley: " + str(OTooley_percentage) + "% (" + str(OTooley) + " votes)")
    output_file.write("\n -------------------------------------------------------")
    output_file.write("\n Winner: " + str(winner))
    output_file.close()


 

    
    
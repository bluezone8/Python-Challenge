import os # load os module into python
import csv # load CSV module into python

filelocation=os.path.join('Resources', 'election_data.csv') # assigns filepath of data csv file to variable
with open(filelocation, "r") as new_csv: #open csv in read mode and assign to a variable
    vote_data=csv.reader(new_csv) # assign data in the csv file to a variable

    poll_list=[] # create a new empty list to hold candidate names
    next(vote_data) # skip the header row in the data

    for i in vote_data: # iterate through the election data
        if i[2] not in poll_list: # checks to see if the record in the current row in the 2 inex column is in the list yet
            poll_list.append(i[2]) # if the record is not the list yet it gets added to the list

    total_votes=vote_data.line_num-1 # counts the number of votes cast in the election

    # sets up variables for counting the votes for each candidate and assigns initial values of 0
    kc=0
    cc=0
    lc=0
    oc=0

    new_csv.seek(0) # Resets the read point in the csv file to the beginning
    for i in vote_data: # iterates through the election data again
        if i[2] == poll_list[0]: # These conditionals are checking to see which candidate received the vote in that row and adds it the votes for that candidate
            kc=kc+1
        elif i[2] == poll_list[1]:
            cc=cc+1
        elif i[2] == poll_list[2]:
            lc=lc+1
        elif i[2] == poll_list[3]:
            oc=oc+1

    print("Election Results") # Prints the title to the console/terminal
    print(f"The total number of votes cast in the election is: {total_votes}") # prints the total vote count the console/terminal

    # calculates the percentage of votes each candidate received and assigns it to a variable  
    kp=round((kc/total_votes)*100, 2) 
    cp=round((cc/total_votes)*100, 2)
    lp=round((lc/total_votes)*100, 2)
    op=round((oc/total_votes)*100, 2)

    # prints the candiate name, no. of votes, and percnt. of votes to the console/terminal 
    print("Candidate:", poll_list[0],"  ", "Votes Received:", kc,"  ", "Percent of Vote Total:", kp)
    print("Candidate:", poll_list[1],"  ", "Votes Received:", cc,"  ", "Percent of Vote Total:", cp)
    print("Candidate:", poll_list[2],"  ", "Votes Received:", lc,"  ", "Percent of Vote Total:", lp)
    print("Candidate:", poll_list[3],"  ", "Votes Received:", oc,"  ", "Percent of Vote Total:", op)


    wnr="" # establishes and empty string variable for the election winner name

    if kp>cp and kp>lp and kp>op: # These conditionals are checking to see which candidate had the largest percentage of votes and printing their name to the console/terminal
        print("Election Winner: ", poll_list[0])
        wnr=poll_list[0]
    elif cp>kp and cp>lp and cp>op:
        print("Election Winner: ", poll_list[1])
        wnr=poll_list[1]
    if lp>cp and lp>kp and lp>op:
        print("Election Winner: ", poll_list[2])
        wnr=poll_list[2]
    if op>cp and kp>lp and op>kp:
        print("Election Winner: ", poll_list[3])
        wnr=poll_list[3]

    # Block to create a text file in the Analysis folder that records the election results
    txtlocation=os.path.join("Analysis", "PyPoll Election Results Analysis.txt") #assigns a variable to a new txt file in the Analysis folder
    with open(txtlocation, "w") as new_txt: # creates the text file
        new_txt.write("ELECTION RESULTS\n") # subsequent lines write the election result analysis to the new text file
        new_txt.write("\n")
        new_txt.write("\n")
        new_txt.write("\n")
        new_txt.write("The total number of votes cast in the election is:" + str(total_votes))
        new_txt.write("\n")
        new_txt.write("\n")
        new_txt.write("Candidate:" + poll_list[0] + "  "+ "Votes Received:" + str(kc) + "  " + "Percent of Vote Total:" + str(kp))
        new_txt.write("\n")
        new_txt.write("Candidate:" + poll_list[1] + "  "+ "Votes Received:" + str(cc) + "  " + "Percent of Vote Total:" + str(cp))
        new_txt.write("\n")
        new_txt.write("Candidate:" + poll_list[2] + "  "+ "Votes Received:" + str(lc) + "  " + "Percent of Vote Total:" + str(lp))
        new_txt.write("\n")
        new_txt.write("Candidate:" + poll_list[3] + "  "+ "Votes Received:" + str(oc) + "  " + "Percent of Vote Total:" + str(op))
        new_txt.write("\n")
        new_txt.write("\n")
        new_txt.write("Election Winner:" + wnr)
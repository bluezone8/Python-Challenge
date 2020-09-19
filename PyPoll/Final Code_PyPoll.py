import csv

with open("election_data.csv", "r") as new_csv:
    vote_data=csv.reader(new_csv)

    poll_list=[]
    next(vote_data)

    for i in vote_data:
        if i[2] not in poll_list:
            poll_list.append(i[2])

    total_votes=vote_data.line_num-1

    kc=0
    cc=0
    lc=0
    oc=0

    new_csv.seek(0)
    for i in vote_data:
        if i[2] == poll_list[0]:
            kc=kc+1
        elif i[2] == poll_list[1]:
            cc=cc+1
        elif i[2] == poll_list[2]:
            lc=lc+1
        elif i[2] == poll_list[3]:
            oc=oc+1
    print("Election Results")
    print(f"The total number of votes cast in the election is: {total_votes}")

    kp=round((kc/total_votes)*100, 2)
    cp=round((cc/total_votes)*100, 2)
    lp=round((lc/total_votes)*100, 2)
    op=round((oc/total_votes)*100, 2)

    print("Candidate:", poll_list[0],"  ", "Votes Received:", kc,"  ", "Percent of Vote Total:", kp)
    print("Candidate:", poll_list[1],"  ", "Votes Received:", cc,"  ", "Percent of Vote Total:", cp)
    print("Candidate:", poll_list[2],"  ", "Votes Received:", lc,"  ", "Percent of Vote Total:", lp)
    print("Candidate:", poll_list[3],"  ", "Votes Received:", oc,"  ", "Percent of Vote Total:", op)

    wnr=""
    if kp>cp and kp>lp and kp>op:
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

    with open("PyPoll Election Results Analysis.txt", "w") as new_txt:
        new_txt.write("ELECTION RESULTS\n")
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

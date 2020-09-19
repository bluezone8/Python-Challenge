import csv

with open("election_data.csv", "r") as new_csv:
    voter_data=csv.DictReader(new_csv)
    cand_list=[]

    for i in voter_data:
        if i["Candidate"] not in  cand_list:
            cand_list.append(i["Candidate"]) 

    total_votes=voter_data.line_num-1    
    print(f"The total number of votes cast is:  {total_votes}")
    print("Complete list of candidates: ")
    print(*cand_list, sep=", ")

    kcnt=0
    ccnt=0
    lcnt=0
    ocnt=0
    kind=cand_list[0]
    cind=cand_list[1]
    lind=cand_list[2]
    oind=cand_list[3]

    for j in voter_data:
        if j["Candidate"] == kind:
            kcnt=kcnt+1
        if str(j["Candidate"]) == str(cand_list[1]):
            ccnt=ccnt+1
        if str(j["Candidate"]) == str(cand_list[2]):
            lcnt=lcnt+1
        if str(j["Candidate"]) == str(cand_list[3]):
            ocnt=ocnt+1

    print(cand_list[0], kcnt)
    print(cand_list[1], ccnt)
    print(cand_list[2], lcnt)
    print(cand_list[3], ocnt)


    cntr=0
    new_dict={}
    for o in cand_list:
        for p in voter_data:
            if str(p["Candidate"]) == o:
                cntr=cntr+1
        new_dict.update({o:cntr})

    for cand_cntr in new_dict.items():
        print(cand_cntr)
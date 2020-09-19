#PYTHON HOMEWORK EXPERIMENTS 3

import csv
with open ("budget_data.csv", "r") as new_csv:
    fin_data=csv.DictReader(new_csv)
    new_list=[]
    for i in fin_data: #get the ProfitLoss data into the list
        pltran=int(i["Profit/Losses"])
        new_list.append(pltran)
    print(new_list)
    print(len(new_list))
    cntr=0
    sum_diff=0
    while cntr<85:
        curr=new_list[cntr]
        nxt=new_list[cntr+1]
        diff=nxt-curr
        sum_diff=sum_diff+diff
        print(diff, sum_diff)
        cntr=cntr+1
    lst_cnt=(len(new_list)-1)
    print(sum_diff/lst_cnt)
#PYTHON HOMEWORK EXPERIMENTS 4

import csv
with open("budget_data.csv", "r") as new_csv:
    fin_data=csv.DictReader(new_csv)
    diff=0
    big_diff=0
    low_diff=0
    last_pl=0
    curr_pl=0
    for i in fin_data:
        curr_pl=int(i["Profit/Losses"])
        diff=curr_pl-last_pl
        if diff>big_diff:
            big_diff=diff
            big_date=i["Date"]
        if diff<low_diff:
            low_diff=diff
            low_date=i["Date"]
        print(i, curr_pl, last_pl, diff ,big_diff, low_diff)
        last_pl=curr_pl
   
    print(f"The greatest increase in profit over the period is:{big_diff} {big_date}")
    print(f"The greatest decrease in profit over the period is:{low_diff} {low_date}")


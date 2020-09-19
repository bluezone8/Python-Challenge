#PYTHON HOMEWORK EXPERIMENTS 2

import csv
with open("budget_data.csv", "r") as new_csv:
    fin_data=csv.DictReader(new_csv)
    sum_losses=0
    changesum=0
    for i in fin_data:
        prof_loss=int(i["Profit/Losses"])
        sum_losses=sum_losses+prof_loss
        print(i) #Test
    total_months=fin_data.line_num-1
    print(f"The total number of months of data is: {total_months}")
    print(f"The total sum of profit and losses for data is:{sum_losses}")
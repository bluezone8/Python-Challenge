#PYTHON HOMEWORK EXPERIMENTS 1

import csv
with open("budget_data.csv", "r") as new_csv:
    fin_data=csv.DictReader(new_csv)
    sum_losses=0
    changesum=0
    for i in fin_data:
        # iter_num=int(i.)
        # iter_num2=iter_num+1
        # if iternum2!=86:
        #     iterdiff=iternum2-iternum
        #     changesum=changesum+iterdiff
        proloss=int(i["Profit/Losses"])
        sum_losses=sum_losses+proloss
        print(i)
    total_months=fin_data.line_num-1
    ave_pl_change=changesum/total_months
    print(f"The total number of months of data is: {total_months}")
    print(f"The total sum of profit and losses for data is:{sum_losses}")
    print(f"The average change in profit/loss for data is:{ave_pl_change}")
    
#PYTHON HOMEWORK EXPERIMENTS 6


import csv
with open("budget_data.csv", "r") as new_csv:
    fin_data=csv.DictReader(new_csv)
    diff=0
    big_diff=0
    low_diff=0
    last_pl=0
    curr_pl=0
    sum_diff=0
    sum_pl=0
    cntr=1
    for i in fin_data:
        curr_pl=int(i["Profit/Losses"])
        sum_pl=sum_pl+curr_pl
        diff=curr_pl-last_pl
        if cntr>1: #Delays calculation until second iteration
            sum_diff=sum_diff+diff
        if diff>big_diff:
            big_diff=diff
            big_date=i["Date"]
        if diff<low_diff:
            low_diff=diff
            low_date=i["Date"]
        print(i, curr_pl, last_pl, diff ,sum_diff,big_diff, low_diff)
        last_pl=curr_pl
        cntr=cntr+1

    tot_mnths=fin_data.line_num-1 #Subtract 1 from total number of lines of data to exclude header
    sumdf_count=tot_mnths-1 #Subtract 1 from total months because first delta occurs in second month  
    ave_dpl=round(sum_diff/sumdf_count, 2)

    print("Financial Analysis")
    print(f"The total number of months included in the period is:{tot_mnths}")
    print(f"The net total amount of profit/loss over the period is:${sum_pl}")
    print(f"The average change in profit/loss over the period is:${ave_dpl}")
    print(f"The greatest increase in profit over the period is:${big_diff} {big_date}")
    print(f"The greatest decrease in profit over the period is:${low_diff} {low_date}")

    #Convert Integer Variables to Strings to output to text file
    str_tm=str(tot_mnths)
    str_spl=str(sum_pl)
    str_adpl=str(ave_dpl)
    str_bdf=str(big_diff)
    str_bdt=str(big_date)
    str_ldf=str(low_diff)
    str_ldt=str(low_date)

    with open("PyBank Finacial Analysis.txt", "w") as new_txt:
        new_txt.write("Financial Analysis\n")
        new_txt.write("\n")
        new_txt.write("The total number of months in the period is:" + str_tm + "\n")
        new_txt.write("The net total amount of profit/loss over the period is:$" + str_spl + "\n")
        new_txt.write("The average change in profit/loss over the period is:$" + str_adpl + "\n")
        new_txt.write("The greatest increase in profit over the period is:$" + str_bdf + "in" + str_bdt + "\n")
        new_txt.write("The greatest decrease in profit over the period is:$" + str_ldf + "in" + str_ldt + "\n")

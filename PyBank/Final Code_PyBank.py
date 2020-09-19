import csv # Load csv module into python
with open("budget_data.csv", "r") as new_csv: # Open csv file in read mode and assign to variable
    fin_data=csv.DictReader(new_csv) # Create a dictionary from the csv data 
    diff=0 #Variable initial value assignment block
    big_diff=0
    low_diff=0
    last_pl=0
    curr_pl=0
    sum_diff=0
    sum_pl=0
    cntr=1
    for i in fin_data: # Loop to iterate through the rows of the data
        curr_pl=int(i["Profit/Losses"]) # Convert the P/L data on current row to an integer for calculations
        sum_pl=sum_pl+curr_pl # Adds current row P/L value to sum of P/L data
        diff=curr_pl-last_pl # calculates month to month difference in P/L
        if cntr>1: # Delays Month to month calculation until second loop iteration (second month)
            sum_diff=sum_diff+diff # Adds current calculated P/L difference to sum of P/L differences
        if diff>big_diff: # Determines if current difference is greater (increase) than prior differences
            big_diff=diff # Assigns current difference to greatest seen thus far
            big_date=i["Date"] # Records the date of the greatest difference thus far
        if diff<low_diff: # Determines if current difference is greater decrease than prior differences
            low_diff=diff # Assigns current difference to greatest decrease seen thus far
            low_date=i["Date"] # Records the date of the greatest decrease seen thus far
        last_pl=curr_pl # Establishes the current row as the last row for the next loop iteration
        cntr=cntr+1 # Increments the counter to allow the P/L difference calculations to begin

    tot_mnths=fin_data.line_num-1 #Subtract 1 from total number of lines of data to exclude header
    sumdf_count=tot_mnths-1 #Subtract 1 from total months because first delta occurs in second month  
    ave_dpl=round(sum_diff/sumdf_count, 2) # Assigns variable to caluclated average of month to month P/L differences and restricts the value to 2 significant digits

    # Block to output all of the program results to the terminal
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

    # Block to create a new text file and write the program results to the file
    with open("PyBank Finacial Analysis.txt", "w") as new_txt:
        new_txt.write("Financial Analysis\n")
        new_txt.write("\n")
        new_txt.write("The total number of months in the period is:" + str_tm + "\n")
        new_txt.write("The net total amount of profit/loss over the period is:$" + str_spl + "\n")
        new_txt.write("The average change in profit/loss over the period is:$" + str_adpl + "\n")
        new_txt.write("The greatest increase in profit over the period is:$" + str_bdf + "in" + str_bdt + "\n")
        new_txt.write("The greatest decrease in profit over the period is:$" + str_ldf + "in" + str_ldt + "\n")

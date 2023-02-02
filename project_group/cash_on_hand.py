#import the relevant modules
from pathlib import Path
import csv

#define the function used to calculate the cash surplus/deficit
def coh_function():
    """
    this function calculates the cash deficit day on day, if not, the cash surplus day on day

    there are no parameters
    """

    #Read the excel file of overheads from the csv_reports file
    fp_read = Path.cwd() /"project_group"/"csv_reports"/"Cash on Hand.csv"
    #write the output into a new .txt file titled "team_members.txt"
    fp_write = Path.cwd() /"project_group"/"team_members.txt"
    #use command touch to enable the output 
    fp_write.touch()

    #assign the variable for the cash on hand on the previous day, equate it to 0
    prev_coh = 0

    #assign the variable for the cash on hand on the current day, equate it to 0
    curr_coh = 0

    #assign a variable for the output type for the possible outcomes (deficit/surplus)
    output = 1

    #open the excel file and begin the commands needed on the excel file
    with fp_read.open(mode="r", encoding="UTF8", newline="") as file:
        # create csv reader object using csv
        reader = csv.reader(file) 
        # to skip reading header
        next(reader)
        # iterate each row with loop
        for row in reader:
            #assign the value in the second columnn with index to the current cash on hand
            curr_coh = float(row[1])
            #create an event where if the current cash on hand is less than the previous cash on hand
            if curr_coh < prev_coh:
                #assign the output to a different value to indicate a different output type
                output = 2

                # write the result to a text file
                with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
                    #the difference between cash on hand on the previous day and the current day
                    difference = prev_coh - curr_coh
                    file.write(f"[CASH DEFICIT] DAY:{row[0]}, AMOUNT: USD{difference}\n")
            #assign the previous cash on hand to the current cash on hand so the loop can restart
            prev_coh = curr_coh

    #create a condition where ouput = 1, which is when the deficit condition is not fufilled, meaning that the result is a surplus
    if output == 1:
        #write the result to a text file
        with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
            file.write(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")

#end the function
coh_function()
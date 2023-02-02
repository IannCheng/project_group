#import the relevant modules
from pathlib import Path
import csv

#define the function used to calculate the cash surplus/deficit
def profitandloss_function():
    """
    this function calculates the net profit deficit day on day, if not, the net profit surplus day on day

    there are no parameters
    """
    #Read the excel file of overheads from the csv_reports file
    fp_read = Path.cwd() /"project_group"/"csv_reports"/"Profit and Loss.csv"
    #write the output into a new .txt file titled "team_members.txt"
    fp_write = Path.cwd() /"project_group"/"team_members.txt"
    fp_write.touch()

    prev_pl = 0
    curr_pl = 0

    output = 1

    with fp_read.open(mode="r", encoding="UTF8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            curr_pl = float(row[4])
            if curr_pl < prev_pl:
                output = 2
                with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
                    difference = prev_pl - curr_pl
                    file.write(f"[NET PROFIT DEFICIT] DAY:{row[0]}, AMOUNT: USD{difference}\n")
            prev_pl = curr_pl

    if output == 1:
        with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
            file.write(f"[NET PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")

profitandloss_function()
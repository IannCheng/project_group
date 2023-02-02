#import the relevant modules
import csv
from pathlib import Path

#define the function used to calculate highest overheads
def overheads_function():
    """
    this function is used to calculate the highest overheads and 
    write the result into a text file with the variable name and amount

    no parameters required
    
    """

    #Read the excel file of overheads from the csv_reports file
    fp_read = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"
    #write the output into a new .txt file titled "team_members.txt"
    fp_write = Path.cwd()/"project_group"/"team_members.txt"
    #use command touch to enable the output
    fp_write.touch()

    #open the excel file and begin the commands needed on the excel file
    with fp_read.open(mode="r", encoding="UTF8", newline="") as file:

        reader = csv.reader(file) # create csv reader object using csv
        next(reader)              # to skip reading header
        overheads_variable = ""   # create a variable with an empty string to store the overhead variable
        overheads_number = 0      # create a variable and equate it to 0 to store the overhead value 

        for row in reader:        # iterate each row with loop
            # create a condition where if the value in the second column of the excel is more than the current overheads_number variable
            if float(row[1]) > overheads_number:
                    #assign the new value to the variable of overheads_number
                    overheads_number = float(row[1])
                    #assign the new overheads variable to the corresponding overheads value by using index 0
                    overheads_variable = row[0]

    # write the result to a text file
    with fp_write.open(mode="w", encoding="UTF8", newline="") as file:
        file.write(f"[HIGHEST OVERHEADS] {overheads_variable}: {overheads_number}%\n")

#end the function
overheads_function()



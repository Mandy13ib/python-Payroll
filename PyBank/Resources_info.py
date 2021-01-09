import os
import csv

#set up path from Python challenge (make sure you are in python challenge as a start)
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    #definitons
    total_profit_and_loss = 0
    Profit_Loss = []
    profit_Loss_Change = []
    Date_Change = []
    data_max = 0
    data_min = 0


    #setup to remove , that divides info
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    next (csvreader)
    # Read each row of data after the header row
    for row in csvreader:
    # pulls info
        Date_Change.append(row[0])

        # count the number of line in the first row to find the total amounts of months 
        # this only works because each month counts as one line
        total_line_Count = sum(1 for line in open(csvpath))
        # print(f"Total Months: {total_line_Count}")      

        # this is a list of profit and loss over all
        total_profit_and_loss = total_profit_and_loss + int(row[1]) 
        #adding elements to list
        Profit_Loss.append(row[1])

for x in range(1, len(Profit_Loss)):
    #adds the total of profit and losses over all
    profit_Loss_Change.append(int(Profit_Loss[x]) -int(Profit_Loss[x-1]))

#Change in profit and loss over all and the average
average_change = round(sum(profit_Loss_Change)/len(profit_Loss_Change),2)

#Max increase in profit
MxPftLsChange = max(profit_Loss_Change)

#the greatest decrease in profit
MnPftLsChange = min(profit_Loss_Change)

#greatest increase over all - Date and amount
date_max = Date_Change[profit_Loss_Change.index(MxPftLsChange)+1]

#Decrease in losses - date and amount
date_min = Date_Change[profit_Loss_Change.index(MnPftLsChange)+1]

#print results
print(f"Financial Analysis")
print("--------------------------------------------------")
print(f'Total Months:  {total_line_Count-1}')
print(f"Total:  ${total_profit_and_loss}")
print(f"Average Changes: ${average_change}")
print(f"Greatest Increase in Profits: {date_max} (${MxPftLsChange})")
print(f"Greatest Decrease in Profits: {date_min} (${MnPftLsChange})")
#exporting results into text file
textfileoutput = open("Analysis/analysis.text","w")
textfileoutput.write(f"Financial Analysis\n")
textfileoutput.write("-------------------------------------------\n")
textfileoutput.write(f"Total Months:  {total_line_Count-1}\n")
textfileoutput.write(f"Total:  ${total_profit_and_loss}\n")
textfileoutput.write(f"Average Changes:  ${average_change}\n")
textfileoutput.write(f"Greatest Increase InProfits: {data_max} (${MxPftLsChange})\n")
textfileoutput.write(f"Greatest Decrease InProfits: {data_min} (${MnPftLsChange})\n")











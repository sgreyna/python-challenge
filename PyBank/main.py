import os
import csv

# Specify the csv file to read
file_csv = os.path.join( "..", "resources", "budget_data.csv")

#Open and read csv
with open(file_csv, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	#Read the header row
	csv_header = next(csvfile)
	
	#Get the value of firstRow ans assign to varriable
	firstRow=[] 
	firstRow=next(csvreader)
	maxMonth = firstRow[0]
	maxValue = firstRow[1]
	
	#Read through each row	
	cntMonths = 0
	totalNum = 0
	for row in csvreader:
		if len(row[0]) >1 :  #for value in column have more than 1 character
			cntMonths += 1 #cnt each row as month
			totalNum += int(row[1]) #add each month values
			
		if float(row[1]) > float(maxValue):  #if value is more than first value 
			maxValue = float(row[1]) #then replace the value
			maxMonth = row[0] #replace the month
		
		if float(row[1]) < float(maxValue):  #if value is more than less value 
			minValue = float(row[1]) #then replace the value
			minMonth = row[0] #replace the month
	
	avgChange = totalNum/cntMonths	
	
	#Print to console and export to Excel	
	print("")			
	print ("Financial Analysis")
	print("")
	print ("---------------------------------------------------------")
	print(f'Total Months:   {cntMonths}')
	print(f'Total:   ${totalNum}')
	print(f'Average  Change:   ${round(avgChange,2)}')
	print(f'Greatest Increase in Profits:   {maxMonth}  ${maxValue}')
	print(f'Greatest Decrease in Profits:  {minMonth}  ${minValue}')
	
# Specify the file to write to
output_path = os.path.join("..", "resources", "summary.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as newcsvfile:
	# Initialize csv.writer
	newcsvwriter = csv.writer(newcsvfile)
    	#Write the report header
	newcsvwriter.writerow(['Financial Analysis'])		
	# Write the all other row
	newcsvwriter.writerow(['---------------------------------------------------------'])
	newcsvwriter.writerow(['Total Months:', cntMonths])
	newcsvwriter.writerow(['Total:', 'Frost', totalNum])
	newcsvwriter.writerow(['Average Change:', avgChange])
	newcsvwriter.writerow(['Greatest Increase in Profits: ', maxMonth, maxValue])
	newcsvwriter.writerow(['Greatest Increase in Profits: ', minMonth, minValue])
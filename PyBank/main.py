import os
import csv

# Specify the csv file to read
file_csv = os.path.join( "..", "resources", "budget_data.csv")

#Open and read csv
with open(file_csv, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	#Read the header row
	csv_header = next(csvfile)
	
	#Read through each row
	for row in csvreader:
	
	#The total number of months included in the dataset
		maxNum = 0
		minNum = 0
		totalMonths = 0
		totalNum = 0
		
		
		if row[0] !="":
			totalMonths += 1
			totalNum += float(row[1])
					
		#if float(row[1]) > maxNum:
		#	maxNum = float=([row[1])
		#	maxMonth = row[0]
		#	print (MaxNum)
					
		#if float(row[1]) < minNum:
		#	minNum = float(row[1])
		#	minMonth = row[0]

		#AvgNum = TotalNum / TotalMonths	
				
	#Print to console and export to Excel				
	print ("Financial Analysis")
	print("")
	print ("---------------------------------------------------------")
	print(f" totalMonths: " + totalMonths)

		
		
		
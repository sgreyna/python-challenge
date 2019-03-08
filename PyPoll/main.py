import os
import csv

# Specify the csv file to read
file_csv = os.path.join( "..", "resources", "election_data.csv")

#Open and read csv
with open(file_csv, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	#Read the header row
	csv_header = next(csvfile)
	
	#Get the value of firstRow and assign to varriable
	firstRow=[] 
	firstRow=next(csvreader)
	voteVal = firstRow[0]	
	candidate=[] #array to hold each candidate
	candidate.append(firstRow[2]) #assign first candidate to array
	votes =[]
	vote1 = 0
	vote2 = 0
	vote3 = 0
	vote4 = 0

	#do for each row:  find the total count of records and distinct list of candidates
	cntVoter = 0
	for row in csvreader:
		if len(row[0]) >1 :  #for value in column have more than 1 character
			cntVoter += 1 #cnt each voter ID
		
		if row[2] not in candidate:  #if the candidate name is different
			candidate.append(row[2]) #assign next candidate to array
		
		if row[2] == candidate[0]:
			vote1 += 1
		
		if len(candidate) > 1 and row[2] == candidate[1]:
			vote2 +=1
			
		if len(candidate) > 2 and row[2] == candidate[2]:
			vote3 += 1
		
		if len(candidate) > 3 and row[2] == candidate[3]:	
			vote4 += 1
		
		if vote1 > vote2 and vote1 > vote3 and vote1 > vote4:
			winner = candidate[0]
		
		if vote2 > vote3 and vote2 > vote4 and vote2 > vote1:
			winner = candidate[1]
		
		if vote3 > vote2 and vote3 > vote3 and vote3 > vote4:
			winner = candidate[2]
		
		if vote4 > vote2 and vote4 > vote3 and vote4 > vote1:
			winner = candidate[3]

#Print to console and export to Excel	
print("")		
print ("---------------------------------------------------------")	
print ("Election Results")
print ("---------------------------------------------------------")
print(f'Total Votes:   {cntVoter}')
print ("---------------------------------------------------------")
print(f'{candidate[0]} : {(vote1/cntVoter)*100.000}%   ({vote1})')
print(f'{candidate[1]} : {(vote2/cntVoter)*100.000}%   ({vote2})')
print(f'{candidate[2]} : {(vote3/cntVoter)*100.000}%   ({vote3})')
print(f'{candidate[3]} : {(vote4/cntVoter)*100.000}%   ({vote4})')
print ("---------------------------------------------------------")
print (f'Winner: {winner}')
print ("---------------------------------------------------------")

# Specify the file to write to
output_path = os.path.join("..", "resources", "summary_election.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as newcsvfile:
	# Initialize csv.writer
	newcsvwriter = csv.writer(newcsvfile)
    	#Write the report header
	newcsvwriter.writerow(['---------------------------------------------------------'])
	newcsvwriter.writerow(['Election Results'])		
	newcsvwriter.writerow(['---------------------------------------------------------'])
	newcsvwriter.writerow(['Total Votes:', cntVoter])
	newcsvwriter.writerow(['---------------------------------------------------------'])
	newcsvwriter.writerow([candidate[0],':',  vote1/cntVoter, vote1])
	newcsvwriter.writerow([candidate[1],':',  vote2/cntVoter, vote2])
	newcsvwriter.writerow([candidate[2],':',  vote3/cntVoter, vote3])
	newcsvwriter.writerow([candidate[3],':',  vote4/cntVoter, vote4])
	newcsvwriter.writerow(['---------------------------------------------------------'])
	newcsvwriter.writerow(['Winner:', winner])
	newcsvwriter.writerow(['---------------------------------------------------------'])

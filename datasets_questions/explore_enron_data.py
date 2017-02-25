#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#Q1
print len(enron_data)
#Q2
print "enron_data size (people count): " + str(len(enron_data["SKILLING JEFFREY K"]))
#Shows the available features
print "feature count per person: " + str(enron_data["SKILLING JEFFREY K"])

#Q3
count = 0
datasetperson = []
for person in enron_data:
  if(enron_data[person]["poi"] == 1):
    datasetperson.append(person)
    count +=1
    
print "POI count in data set: " + str(count)

#Q4
import sys
infile = "../final_project/poi_names.txt"
poi_names = []
with open(infile) as inf:
  for line in inf:
    if "(y)" in line or "(n)" in line:
      poi_names.append(line)
		
print "Poi count: " + str(len(poi_names))
  
#Q5
for line in enron_data :
  if "Prentice".upper() in line:
    print "James Prentice total stock: " + str(enron_data[line]["total_stock_value"])
	
#Q6
for line in enron_data :
  if "Colwell".upper() in line:
    print "Wesley Colwell poi count: " + str(enron_data[line]["from_this_person_to_poi"])

#Q7
for line in enron_data :
  if "Skilling".upper() in line:
    print "Jeffrey K. Skilling exercised stock options: " + str(enron_data[line]["exercised_stock_options"])
	
#Q8
highestPayment = 0
person =""
for line in enron_data :
  if "Skilling".upper() in line and enron_data[line]["total_payments"] > highestPayment:
    highestPayment = enron_data[line]["total_payments"]
    print line + "with " + str(highestPayment)
  if "Lay".upper() in line and enron_data[line]["total_payments"] > highestPayment:
    highestPayment = enron_data[line]["total_payments"]
    print line + "with " + str(highestPayment)
  if "Fastow".upper() in line and enron_data[line]["total_payments"] > highestPayment:
    highestPayment = enron_data[line]["total_payments"]
    print line + "with " + str(highestPayment)
    
#Q9
salaryavail=0
emailcount=0
for line in enron_data:
  if "NaN" not in str(enron_data[line]["salary"]):
    salaryavail+=1
  if "NaN" not in str(enron_data[line]["email_address"]):
    emailcount+=1
    
print "Salary available: " + str(salaryavail) + " Email available: " + str(emailcount)

#Q10
nancount=0
for line in enron_data:
  if "NaN" in str(enron_data[line]["total_payments"]):
    nancount +=1
    
print "Number of totalpayments which are nan " + str(nancount) + " in percent " + str(float(nancount)/len(enron_data))

#Q11
nanpoi=0
for line in enron_data:
  if "NaN" in str(enron_data[line]["total_payments"]) and enron_data[line]["poi"] :
    nanpoi +=1
    
print "Number of poi with NaN totalpayments " + str(nanpoi) + " in percent " + str(float(nanpoi)/len(enron_data))
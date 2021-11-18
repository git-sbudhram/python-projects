#imports the csv library 
import csv

# takes user input and stores them in the variables 
fName = input("What is your name: ")
lName = input("What is your surname: ")
jobTitle = input("What is your job title: ")
company = input("What is your company name: ")

# here the dictionary is created with in a variable named "userData"
userData = {"Name: ":fName, "Surname: ":lName, "Jobtitle: ":jobTitle, "Company: ":company}

# "w" stands for write and "a" stands for append. "w" overwrites everything where "a" appends something (adds something)
# here the csv file is opened, or if it doesn't exist it's created instead 
a_file = open("personalinfo.csv", "a") 

# delimiter \t removes all commas 
writer = csv.writer(a_file, delimiter="\t") 

# "i" is assigned to a value in userData in each loop, in loop 1 it's "Name", in loop 2 it's "Surname" etc
# userData[i] pulls the values given by the user 
for i, userData[i] in userData.items():
    
    # each value in i is printed in the csv file, as a seperate row, with this command
    writer.writerow([i, userData[i]])

# closes the file 
a_file.close()

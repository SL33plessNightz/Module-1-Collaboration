# Kenne Allen
# CaseStudy if else.py
# My app will take user input until ZZZ is inserted for the last name. The inputs wll handle the student's
# first name, last name, and gpa
#then the program will determine if they are enough for the dean and/or honor role list


while True:
    last_n = input("Enter student's last name or ZZZ to quit: ")
    
    if last_n == "ZZZ":
        break
    first_n = input("Enter Student's first name: ")
    gpa = float(input("Enter student's gpa: "))
    
    if gpa >= 3.5:
        print(first_n, last_n, "has made the Dean's list")
        
    if gpa >= 3.25:
        print(first_n, last_n, "has made the honor role")

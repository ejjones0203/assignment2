# Program Name: assignment2.py
# Course: IT3883 Group 18
# Student Name: Enjie Jones
# Assignment Number: Lab 2
# Due Date: 2/7/2025
# Purpose: What does the program do (in a few sentences)? This program will open a file, read it, split the first space (the name of the student), average the grades in another list, sort them using the sort function and itemgetter.
# List Specific resources used to complete the assignment: https://www.geeksforgeeks.org/python-list-sort-method/ and https://note.nkmk.me/en/python-key-sort-sorted-max-min/


from operator import itemgetter

def sort (file):

    students = [] #initialize an empty list to store students

    inputfile = open(file, "r") #standard file open procedure
    for line in inputfile: #iterates through each line of the input file
        word = line.split() #split each word at space
        names = word[0] #take the first item in list and store it as a name
        grade = [] #initialize an empty list to store grades
        for x in word[1:]: #slice the list from the names
            grade.append(int(x)) #append grades from file
            avg = sum(grade) / len(grade) #average the grades
        students.append((names, avg)) #combine both name and grades

    students.sort(key=itemgetter(1), reverse = True) #itemgetter is pointing to the second item to sort, also appending reverse or the list wont appear in correct order

    for names, avg in students:
        print(f"{names} {avg:.2f}") #iterate and print all names and averages using the elusive f string

file = "assignment2input.txt"

sort(file)


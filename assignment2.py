# Program Name: assignment2.py
# Course: IT3883 Group 18
# Student Name: Enjie Jones
# Assignment Number: Lab 2
# Due Date: 2/7/2025
# Purpose: What does the program do (in a few sentences)? This program will open a file, read it, split the first space (the name of the student), average the grades in another list, sort them using the sort function and itemgetter.
# List Specific resources used to complete the assignment: https://www.geeksforgeeks.org/python-list-sort-method/ and https://note.nkmk.me/en/python-key-sort-sorted-max-min/


from operator import itemgetter

def sort (file):

    students = []

    inputfile = open(file, "r")
    for line in inputfile:
        word = line.split()
        names = word[0]
        grade = []
        for x in word[1:]:
            grade.append(int(x))
        avg = sum(grade) / len(grade)
        students.append((names, avg))

    students.sort(key=itemgetter(1), reverse = True)

    for names, avg in students:
        print(f"{names} {avg:.2f}")

file = "assignment2input.txt"

sort(file)


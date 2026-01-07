#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 18:02:02 2025

@author: darius

Questionnaire: For what purposes did you use Generative AI / LLMs when completing your assignment?
[] Not at all
[] Which ones did you use? (e.g., ChatGPT, Bard, etc.) _____________
[] Explaining programming concepts
[] Practicing coding exercises
[x] Debugging code
[x] Reviewing your Python code
[] Optimizing code
[] Writing or completing code
[] Other (please specify): _____________

"""

student_data = {
    "Andrei": {"age": 20, "country": "Romania"},
    "Ioana": {"age": 22, "country": "Italy"},
    "Mihai": {"age": 21, "country": "Spain"},
    "Elena": {"age": 23, "country": "France"},
    "Cristian": {"age": 20, "country": "Germany"},
    "Ana": {"age": 24, "country": "Portugal"},
    "Radu": {"age": 22, "country": "Romania"},
    "Maria": {"age": 21, "country": "Hungary"},
    "Vlad": {"age": 23, "country": "Belgium"},
    "Gabriela": {"age": 20, "country": "Romania"}
}

i = 0
while i < 2:
    i=i+1
    name= input("enter student name: ")
    if name == "" and i==2:
        #print("stop input")
        break
    
    if name == "" and i==1:
        #print("one name skipped, one more student can be added")
        continue
    
    age = input("enter student age: ")
    country = input("enter student country: ")
    
    student_data[name]={"age": int(age), "country": country}
    
#print(student_data)

ages = [info["age"] for info in student_data.values()] #info is a temporary variable representing each student’s inner dictionary as we loop through student_data.values().
average_age = sum(ages) / len(ages)
#print(ages)
countries = {info["country"] for info in student_data.values()}
print("\nThe agreage age is: ",average_age)


young_students = [name for name, info in student_data.items() if info["age"] < average_age]

print("The list of young students is: ",young_students)
print("The set of unique countries is: ",countries)

total_students = len(student_data)
print("Total number of students:", total_students)


percentage_young = (len(young_students) / total_students) * 100
print("Percentage of students under average age:", round(percentage_young, 2), "%")


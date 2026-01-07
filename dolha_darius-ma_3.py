 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 17:39:16 2025

@author: darius
"""

"""
Questionnaire: For what purposes did you use Generative AI / LLMs when completing your assignment?
[] Not at all
[] Which ones did you use? (e.g., ChatGPT, Bard, etc.) _____________
[] Explaining programming concepts
[] Practicing coding exercises
[] Debugging code
[x] Reviewing your Python code
[] Optimizing code
[] Writing or completing code
[x] Other (please specify): genearting the keys and values of the dictionary

"""  


"""
Assignment 3: Building Information Modeling (BIM) Tool

Think of an inspiring building, pavilion, or structure that you would like to explore more.

Imagine you are developing a Building Information Modeling (BIM) Tool that stores information about different building elements of your chosen building inspiration.
Your task is to create a Python program that interacts with the user to collect and analyze data using dictionaries, loops, built-in functions, user-defined functions (UDFs), and lambda functions.
The program should perform the following tasks:


1. Create a dictionary called building_elements that will store information about various building elements.
Each element should be identified by a unique key (e.g., a string or integer).
The value associated with each key should be another dictionary containing information such as the following:

key: The unique key for the element. (e.g. InW.01.23)
type: The type of the building element (e.g., "wall," "window," "door," etc.).
room: The name of the room assigned to the element (e.g., "living room," "staircase," etc.).
length: The length of the element in meters.
height: The height of the element in meters.
thickness: The width of the element in meters.
or other

2. Create a function called add_element that allows users to add a new building element to the building_elements dictionary.
This function should contained the previous parameters you defined:

3. Use lambda functions for calculate_area and calculate_volume.

4. Create a function called get_elements_by_type to list elements of a chosen type (e.g., "wall," "window," "door").

5. Use built-in functions like sum(), max(), or len() to summarize data.

6. Include a menu loop allowing users to repeatedly perform actions until they choose to exit.
"""



building_elements = {
    "InW.01.01": {
        "key": "InW.01.01",
        "type": "dome frame",
        "room": "living",
        "length": 12.5,
        "height": 22.3,
        "thickness": 0.5
    },
    "InW.01.02": {
        "key": "InW.01.02",
        "type": "bed",
        "room": "bedroom",
        "length": 3.0,
        "height": 2.8,
        "thickness": 0.15
    },
    "InW.02.01": {
        "key": "InW.02.01",
        "type": "glass panel",
        "room": "bedroom",
        "length": 2.5,
        "height": 3.0,
        "thickness": 0.12
    },
    "InW.02.02": {
        "key": "InW.02.02",
        "type": "chair",
        "room": "living",
        "length": 8.2,
        "height": 0.5,
        "thickness": 0.4
    },
    "InW.03.01": {
        "key": "InW.03.01",
        "type": "entrance door",
        "room": "hallway",
        "length": 1.5,
        "height": 2.2,
        "thickness": 0.08
    },
    "InW.03.02": {
        "key": "InW.03.02",
        "type": "chair",
        "room": "hallway",
        "length": 4.0,
        "height": 3.0,
        "thickness": 0.1
    }
}

def add_element():
    key = input("Enter unique element key: ")
    
    if key.isnumeric():
        print("error")
        return
    
    element_type = input("Enter element type (e.g., wall, window, door): ")
    room = input("Enter room or area: ")
    
    length = float(input("Enter element length (m): "))
    height = float(input("Enter element height (m): "))
    thickness = float(input("Enter element thickness (m): "))
    
    element = {
        "key": key,
        "type": element_type,
        "room": room,
        "length": length,
        "height": height,
        "thickness": thickness
    }
    
    building_elements[key] = element
    print("\nElement added successfully!\n")
    

calculate_area = lambda length, height: length * height
calculate_volume = lambda length, height, thickness: length * height * thickness

def display_area_and_volume(dic):
    for key,info in dic.items():
       ar=round(calculate_area(info["length"],info["height"]),2)
       vol=round(calculate_volume(info["length"],info["height"],info["thickness"]),2)
       print("Area of ",key," is ",ar,"\n")
       print("Volume of ",key," is ",vol,"\n")
       
      
def get_elements_by_type(dic,typ):
    for key,info in dic.items():
        if(info["type"] == typ):
           print(key,info,"\n")
           
def summarize_elements(dic):
    print("\nBuilding Summary:")
    print("Total elements:", len(dic))
    total_area = sum(calculate_area(info["length"], info["height"]) for info in dic.values())
    total_volume = sum(calculate_volume(info["length"], info["height"], info["thickness"]) for info in dic.values())
    print("Total area (m²):", round(total_area, 2))
    print("Total volume (m³):", round(total_volume, 2))
    tallest = max(dic.values(), key=lambda info: info["height"])
    print("Tallest element:", tallest)
        
       
"""  
add_element()
#print(building_elements)
display_area_and_volume(building_elements)
get_elements_by_type(building_elements,"chair")
summarize_elements(building_elements)
"""

while True:
    print("\nBIM Tool Menu:")
    print("1. Add a new element")
    print("2. Display area & volume of all elements")
    print("3. List elements by type")
    print("4. Show summary")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        add_element()
    elif choice == "2":
        display_area_and_volume(building_elements)
    elif choice == "3":
        typ = input("Enter type to search (e.g., chair, wall): ")
        get_elements_by_type(building_elements, typ)
    elif choice == "4":
        summarize_elements(building_elements)
    elif choice == "5":
        print("Exiting BIM Tool. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")


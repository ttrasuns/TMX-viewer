# python TMX viewer
import sys
import xml.etree.ElementTree as ET
from termcolor import colored

def get_file_contents(xml_file): #finds only content segments
    tree = ET.parse(xml_file)
    tuv = tree.findall(".//tuv")
    output = []
    for seg in tuv:
        for n in seg:
            output.append(n.text)
    return output

def read_file_contents(contents):
    i = 0
    for line in contents:
        if i == 0:
            print(colored(line, attrs=["bold"]))
            i = 1
            continue
        print(line + "\n")
        i = 0


def find_string(contents, string_to_find):
    string_to_find = string_to_find.lower()
    counter = -1
    for segment in contents:
        counter+=1
        if string_to_find in segment.lower(): #prints source and target lines
            if counter % 2 == 0:
                print(contents[counter])
                print(colored(contents[counter+1], attrs=["bold"]))                
            else:                
                print(colored(contents[counter-1], attrs=["bold"]))
                print(contents[counter])
            print("\n")


try:
    file = sys.argv[1]
except:
    print("No file given, quitting...")
    quit()

contents = get_file_contents(file)


while True:
    print("press 1 to show contents, press 2 — to search, q — to quit: ")
    user_action = input()
    if user_action == "1":
        read_file_contents(contents)
    elif user_action == "2":
        search_keyword = input("Input string to search: ")
        if len(search_keyword) > 0:
            print("\033c", end="") #clears screen
            find_string(contents, search_keyword)
    elif user_action == "q":
        quit()

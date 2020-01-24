# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

#word count
count = 0

#read user input for which word
search_word = input("What word do you want to search for? ")

#read the file text
file = open('song.txt','r')

#parse by line
contents = file.readlines()

#close the file object, we dont need it anymore
file.close()

#search everyline
for line in contents:
    #get rid of commas
    line = line.replace(',','')
    #turn line into a list of words
    list = line.split()
    #check every word in the list
    for word in list:
        #increment the count if we match our word
        if word == search_word:
            count+=1
print(search_word, " appears ", count, " times")


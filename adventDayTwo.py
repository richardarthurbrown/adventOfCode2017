# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:21:00 2017

@author: Richard
"""
#import raw input for puzzle as csv file
import csv

input = []
#change the below filename to your puzzle input
with open('adventInput.csv', newline='') as f:
    reader = csv.reader(f)
    for number in reader:
        input.append(number)
#the above imports the file as an array of strings, which must be converted
#for the purposes of this file I hardcoded the dimensions of the array
#in order to convert each value to an int
for i in range(0, 16):
    for j in range (0, 16):
        input[i][j] = int(input[i][j])
#now we have an array of ints
#time to implement checksum
checksum = 0
for i in range(0, 16):
#find the largest and smallest values on each line
    largest = input[i][0]
    smallest = input[i][0]
    for j in range (0, 16):
        if input[i][j] > largest:
            largest = input[i][j]
        if input[i][j] < smallest:
            smallest = input[i][j]
#calculate the difference
    difference = largest - smallest
#add to the total
    checksum += difference
        
##second half of the puzzle concerns evenly divisible values
checkTwo = 0
result = 0
#loops go through each row in the input file and compare the values
for i in range(0, 16):
    for j in range(0, 16):
        for k in range(0, 16):
            #finds a value that is modulo 0 while ignoring self-division
            if (input[i][j] % input[i][k] == 0 and input[i][j] != input[i][k]):
                #divides the values
                result = input[i][j] / input[i][k]
                #adds to the checksum
                checkTwo += result
print(checkTwo)        
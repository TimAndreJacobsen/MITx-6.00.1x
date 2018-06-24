# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 10:56:43 2018

@author: Desktop
"""


#==============================================================================
# # Problem 1
# # Vowel counter
# # Takes a String s and iterates through every char and checks if its a vowel
# s = "azcbobobegghakl"
# 
# def checkVowel(letter):
#     if letter == "a":
#         return True
#     elif letter == "e":
#         return True
#     elif letter == "i":
#         return True
#     elif letter == "o":
#         return True
#     elif letter == "u":
#         return True
#     else:
#         return False
# 
# numberOfVowels = 0
# for letter in s:
#     if (checkVowel(letter)):
#         numberOfVowels += 1
# print("Number of vowels: " + str(numberOfVowels))
#==============================================================================
 
#==============================================================================    
# # Problem 2
# # bob counter
# # Takes a string and checks how many times the name bob appears
# 
# s = 'obbobobobobbbobbobooghpobobboobboob'
# 
# def checkBob(s):
#     bobs = 0 # initialize a bob counter
#     bob = "bob" # the name we want to find in the param string
#     s += "  "
#     
#     for i in range(len(s)):
#         if s[i] == bob[0]:
#             if s[i+1] == bob[1]:
#                 if s[i+2] == bob[2]:
#                     bobs += 1
#     print("Number of times bob occurs is: " + str(bobs))
#     
# checkBob(s)    
#==============================================================================

#==============================================================================
# # Problem 3
# # Check if sequence of chars are in alphabetical order(not concurrent)
# 
# s = "abcdefghijklmnopqrstuvwxyz"
# 
# def checkNext(char, nextChar):
#     if char <= nextChar:
#         return True
#     else:
#         return False
#     
# 
# def substring(s):
#     subStr = s[0]
#     strList = []
#     i = 0
#     
#     for char in s: # kgjf
#         if len(s) > i+1:
#             if checkNext(char, s[i+1]):
#                 subStr += s[i+1] # "
#                 i += 1
#             else:
#                 strList.append(subStr)
#                 i += 1
#                 subStr = s[i]
#         
#     strList.append(subStr)
#     answer = max(strList, key=len)
#     print(answer)
#         
# print("Longest substring in alphabetical order is: ", end="")
# substring(s)                
#==============================================================================
















# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:17:40 2020

@author: Vineeta
"""

items = [5, 7, 10, 12, 15]
 
print("list of items is", items)
 
x = int(input("enter item to search:"))
 
i = flag = 0
 
while i < len(items):
	if items[i] == x:
		flag = 1
		break
 
	i = i + 1
 
if flag == 1:
	print("item found at position:", i + 1)
else:
	print("item not found")
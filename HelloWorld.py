#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if( i != k ) and (i != j) and (j != k):
                print (i,j,k)

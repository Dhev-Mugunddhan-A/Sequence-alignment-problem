# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def dp(score_mat,i,j,s1,s2,prev_point):
    
    while(i<=16):
        while(j<=16):
            if(s1[i-1]==s2[j-1]):
                score_mat[i][j]=score_mat[i-1][j-1]+5
                return dp(score_mat,i,j+1,s1,s2,prev_point)
            
            else:
                niegh=[score_mat[i-1][j-1]-4,score_mat[i-1][j]-4,score_mat[i][j-1]-4,0]
                score_mat[i][j]=max(niegh)
                return dp(score_mat,i,j+1,s1,s2,prev_point)
    
    
    
    
    
    
        return dp(score_mat,i+1,1,s1,s2,prev_point)
    return score_mat


#main code

s1='AGTCAGTCAGTCAGTC'
s2='GATCAGTCAGTCAGTC'

score_mat=np.zeros((17,17),dtype=int)
prev_point=np.zeros((17,17,2),dtype=int)

    
score_mat=dp(score_mat,1,1,s1,s2,prev_point)
print(score_mat)






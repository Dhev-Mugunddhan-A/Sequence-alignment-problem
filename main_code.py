# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#this is for the local sequence alignment problem with linear gap penalty math_score=5 and mismatch_score=gap_penalty=-4 

import numpy as np

def scoring(score_mat,i,j,s1,s2,prev_pointer):
    
    if(i<len(s1)+1):
        if(j<len(s2)+1):
            if(s1[i-1]==s2[j-1]):
                score_mat[i][j]=score_mat[i-1][j-1]+5
                prev_pointer[i][j][0]=i-1
                prev_pointer[i][j][1]=j-1
                return scoring(score_mat,i,j+1,s1,s2,prev_pointer)
            
            else:
                
                neigh=[score_mat[i-1][j-1]-4,score_mat[i-1][j]-4,score_mat[i][j-1]-4,0]
                a=max(neigh)
                score_mat[i][j]=a
                if(neigh.index(a)==0):
                    prev_pointer[i][j][0]=i-1
                    prev_pointer[i][j][1]=j-1
                elif(neigh.index(a)==1):
                    prev_pointer[i][j][0]=i-1
                    prev_pointer[i][j][1]=j
                elif(neigh.index(a)==2):
                    prev_pointer[i][j][0]=i
                    prev_pointer[i][j][1]=j-1
                elif(neigh.index(a)==3):
                    prev_pointer[i][j][0]=0
                    prev_pointer[i][j][1]=0
                
                return scoring(score_mat,i,j+1,s1,s2,prev_pointer)  
    
        return scoring(score_mat,i+1,1,s1,s2,prev_pointer)
    return score_mat,prev_pointer

def backtrace(prev_pointer,i,j,s1,s2,t1,t2):
    if(i==0 and j==0):
        return t1,t2
    else:
        pp=prev_pointer[i][j]
        if(pp[0]<i and pp[1]==j): #downward gap condition
            t1,t2=backtrace(prev_pointer, pp[0], pp[1], s1, s2, t1, t2)
            t1+=s1[i-1]
            t2+='_'
            print()
            return t1,t2
        
        elif(pp[0]==i and pp[1]<j): #right gap condition
            t1,t2=backtrace(prev_pointer, pp[0], pp[1], s1, s2, t1, t2)
            t1+='_'
            t2+=s2[j-1]
            return t1,t2
        else: #no gap condition
                t1,t2=backtrace(prev_pointer,pp[0], pp[1], s1, s2, t1, t2)
                t1+=s1[i-1]
                t2+=s2[j-1]
                return t1,t2
            
            
    
                    
            
        
#main code
if(__name__=='__main__'):
    s1=input('Enter Sequence 1:')
    s2=input('Enter Sequence 2:')

    score_mat=np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    prev_pointer=np.zeros((len(s1)+1,len(s2)+1,2))    
    score_mat,prev_pointer=scoring(score_mat,1,1,s1,s2,prev_pointer)
    prev_pointer=prev_pointer.astype(int)
    maxind=np.unravel_index(score_mat.argmax(),score_mat.shape)
    print(score_mat)
    print(score_mat.max(),maxind)
    t1=t2=''
    t1,t2=backtrace(prev_pointer,maxind[0],maxind[1],s1,s2,t1,t2)
    print(t1)
    print(t2)






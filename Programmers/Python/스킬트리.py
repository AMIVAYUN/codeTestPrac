# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 12:19:44 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(skill, skill_trees):
    answer = 0
    dit = {};
    
    for i in range( len( skill ) ):
        dit[ skill[ i ] ] = i;

    
    for upgrade in skill_trees:
        start = 0;
        flag = False;
        for ch in upgrade:
            
            if( ch not in dit ):
                continue;
                
            if( dit[ ch ] != start ):
                flag = True;
                break;
            elif( dit[ ch ] == start ):
                start += 1;
            
        if( flag ):
            continue;
        
        answer += 1;

        
    return answer
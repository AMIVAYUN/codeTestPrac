# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 13:05:09 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""



from collections import defaultdict
from collections import deque;

answer = 0

def solution( cacheSize, cities ):
    answer = 0;
    cache = deque();
    for city in cities:
        city = city.lower();
        if( city in cache ):
            cache.remove( city );
            cache.append( city );
            answer += 1;
        else:
            cache.append( city );
            if( len( cache ) > cacheSize ):
                cache.popleft();
            
            answer += 5;
    
    return answer;
            
            
        
    
    
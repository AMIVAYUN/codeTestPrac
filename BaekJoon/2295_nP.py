# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:47:51 2022
@FileName: 2295.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2295
"""

#Wrong
def mainw():
    N = int( input() );
    lst = [];
    
    
    for i in range( N ):
        lst.append( int( input() ) );
    
    lst = sorted( lst );
    
    for i in range( N - 1, -1, -1 ):
        target = lst[ i ];
        
        dit = { j: target - j  for j in lst };
        
        lt = 0; rt = len( lst ) - 1;
        
        while lt<= rt:
            mid = ( lt + rt ) // 2 ;
            temp = lst[ lt ] + lst[ rt ];
            if( ( temp == dit[ lst[ mid ] ] ) ):
                print( dit[ lst[ mid ] ] + lst[ mid ] );
                return
            
            else:
                if( temp > dit[ lst[ mid ] ] ):
                    rt -= 1;
                    
                else:
                    lt += 1;
        
     
def main():
    N = int( input() );
    lst = [];
    
    
    for i in range( N ):
        lst.append( int( input() ) );
    
    lst = sorted( lst );
    
    for i in range( N - 1, -1, -1 ):
        target = lst[ i ];
        
        dit = { target - j: j for j in lst };
        
        lt = 0; rt = len( lst ) - 1;
        
        while lt< rt:
            mid = ( lt + rt ) // 2 ;
            mtemp = target - lst[ mid ];
            temp = lst[ lt ] + lst[ rt ];
            if( temp in dit ):
                print( temp + dit[ temp ] );
                return
            
            else:
                if( temp > mtemp ):
                    rt -= 1;
                    
                else:
                    lt += 1;  
    
    
    
    
    
    
    
    
    
if( __name__ == "__main__" ):
    main();
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 12:00:47 2022
@FileName: 2839.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2839
"""




def main():
    N = int( input() );
    if ( N % 5 == 0 ):
        print( N // 5 );
        return
    else:
        cnt = 0;
        sub = N;
        while sub > 0:
            sub -= 3;
            cnt += 1;
        
            if( sub % 5 == 0 ):
                print ( sub // 5 + cnt );
                
                return
            
        if( N % 3 == 0 ):
            print( N // 3 );
            return;
        
        print( -1 );
        return
        
    
    
if( __name__ == "__main__" ):
    main()
        

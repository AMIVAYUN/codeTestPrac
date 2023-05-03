# -*- coding: utf-8 -*-
"""
Created on Thu May  4 03:02:41 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
def ispseudo( str0, lt, rt ):
    while lt <= rt :
        if( str0[ lt ] != str0[ rt ] ):
            return False;
        lt += 1; rt -= 1;
        
    return True;



def isPalin( str0, lt, rt ):

    '''
    끝에서 부터 가는게 맞음.
    '''
    #print( str0, len( str0 ) );

 
    while lt <= rt and lt >= 0 and rt < len( str0 ):
   
        #print( lt, rt )
        
        if( str0[ lt ] == str0[ rt ] ):
            lt += 1; rt -= 1;
            
        else:
            
            if( ispseudo( str0, lt + 1, rt ) or ispseudo( str0, lt, rt - 1 ) ):
                return 1;
            else:
                return 2;

    
    return 0;
    '''
    SOL1
    leng = len( str0 );
    cnt = 0;
    
    if( leng % 2 ):
        lt = leng //2; rt = leng // 2 ;
        
    else:
        lt = leng // 2 - 1; rt = leng // 2;
        
    
    while lt >= 0 and rt < leng and cnt < 1:

        if( str0[ lt ] == str0[ rt ] ):
            lt -= 1;
            rt += 1;
            
        else:
            
            
            if( rt + 1 < leng and str0[ lt ] == str0[ rt + 1 ] ):
                rt += 1;
                cnt += 1;
                
            elif( str0[ lt - 1 ] == str0[ rt ] ):
                lt -= 1;
                cnt += 1;
            
            else:
                return 2;
                
    '''
    return cnt;
    

T = int( input() );
import sys;
for i in range( T ):
    str0 = input();
    
    print( isPalin( str0, 0, len( str0 ) - 1 ) );
                
    sys.stdout.flush();
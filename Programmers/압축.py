# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:15:25 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution( msg ):
    answer = [];
    dit = { chr( i ) : i % 64 for i in range( 65, 91 ) }
    st = 27;
    s_idx, e_idx = 0, 2;
    
    while s_idx < len( msg ):

        if( msg[ s_idx: e_idx ] in dit ):
                
            while e_idx < len( msg ) and msg[ s_idx: e_idx ] in dit:
                e_idx += 1;
    
            if( msg[ s_idx: e_idx ] not in dit ):
                
                dit[ msg[ s_idx: e_idx ] ] = st;
                st += 1;
                answer.append( dit[ msg[ s_idx: e_idx - 1 ] ] );
                s_idx = e_idx - 1;
                e_idx = s_idx + 2;
            else:
                answer.append( dit[ msg[ s_idx: e_idx ] ] );
                s_idx = e_idx;
                e_idx = s_idx + 2;
            
            
        
        else:
            dit[ msg[ s_idx: e_idx ] ] = st;
            st += 1;
            answer.append( dit[ msg[ s_idx: s_idx + 1 ] ] );
            s_idx += 1;
            e_idx = s_idx + 2;
        

    return answer; 

solution( 'ABABABABABABABAB'	)
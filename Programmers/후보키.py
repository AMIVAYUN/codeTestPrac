# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 14:51:53 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(relation):
    import itertools
    n = len( relation[ 0 ] );
    answer = [];
    numlst = [ i for i in range( n ) ];
    
    
    for i in range( 1, n + 1 ):
        cmb = list( itertools.combinations( numlst, i ) );
        
        for case in cmb:

            dit = {};
            
            flag = True;
            
            for idx in range( len( relation ) ):

                rel = relation[ idx ];
                tmp = [];
                for num in case:
                    tmp.append( rel[ num ] );
                    
                if( tuple( tmp ) in dit ):
                    flag = False;
                    break;
                
                else:
                    dit[ tuple( tmp ) ] = rel;
            
            if( flag ):
                f2 = True;
                c_ =set( case )
                for key in answer:
                    
                    if( key & c_ == key or key & c_ == c_ ):
                        f2 = False;
                        break;
                
                if( f2 ):
                    
                    
                    answer.append( c_ );
                
    return len( answer )

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
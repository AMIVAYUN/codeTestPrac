# -*- coding: utf-8 -*-
"""
Created on Mon May  2 20:16:58 2022
@FileName: 1018.py
@author: YUNJUSEOK
"""
def f1( operand ):
    count = [];
    
    result1 = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBBBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
    resul2 = makeResult1( result1 );
    return resul2
def f2( operand ):
    resul2 = makeResult1( operand );
    
    return resul2;

def makeResult1( operand ):
    
    result = [];
    
    for j in range( 0, len(operand) - 7 ):
        
        for i in range( 0, len( operand[0] ) - 7 ):
            result.append( getMin( [ row[i:i+8] for row in operand[j:j+8]] ) )
        
    
    return min( result );
    
def getMin( result1 ):
    ordW= ord ( 'W' );
    ordB= ord ( 'B' );
    result = [];
    result.append( checkSum( ordW, ordB, result1 ) );
    result.append( checkSum ( ordB, ordW, result1 ) );
    return min( result );
def checkSum( fOrd,sOrd,operand ):
    sum0 = 0;
    for j in range( 8 ):
        for i in range( 8 ):
            
            if( j%2 == 0 ):
                if( i%2 ==0 ):
                    
                    sum0 += int( ord( operand[j][i] ) != fOrd ) 
                else:
                    
                    sum0 += int( ord( operand[j][i] ) != sOrd ) 
            else:
                if( i%2 ==0):
                    
                    sum0 += int( ord( operand[j][i] ) != sOrd ) 
                else:
                    sum0 += int( ord( operand[j][i] ) != fOrd ) 
        
        
    return sum0;
            


def main():
    
    N,M = map( int, input().split() );
    operand = [ ];
    
    for i in range( N ):
        operand.append( input() );
    
    result = f2( operand );
    print( result)
        
    

if( __name__ =="__main__" ):
    main();


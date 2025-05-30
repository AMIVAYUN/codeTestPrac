# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:50:00 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
def solution(line):

    import itertools;
    
    cmb = list( itertools.combinations( line, 2 ) );
    leng = len( cmb );
    '''
    x = BF - ED // AD - BC y = EC - AF // AD - BC
    AX BY E
    CX DY F
    '''
    lst =[]
    
    Mxx = 0;
    Mnx = float( "inf" );
    
    Mxy = 0;
    Mny = float( "inf" );
    for i in range( leng ):
        
        A, B, E = cmb[ i ][ 0 ];
        C, D, F = cmb[ i ][ 1 ];
        DIV = ( A * D ) - ( B * C ) 
        if( DIV == 0 ):
            continue;
        
        x = ( ( B * F ) - ( E * D ) ) / DIV;
        
        y = ( ( E * C ) - ( A * F ) ) / DIV;
        
        
        if( float( x ).is_integer() and float( y ).is_integer() ):
            
            Mxx = max( Mxx, int( x ) );
            Mxy = max( Mny, int( y ) );

            Mnx = min( Mnx, int( x ) );
            Mny = min( Mny, int( y ) );
            lst.append( ( int( x ), int( y ) ) )
    
    
    
    
    
    lenx = Mxx - Mnx + 1;
    
    leny = Mxy - Mny + 1;
    answer = [ list( '.' * lenx ) for _ in range( leny ) ]    
    for i in answer:
        print( i )
    # 각 좌표마다 * 그리기 
    for point in lst:
        x,y = point
        print( x, y , Mxy-y, x - Mnx)
        #Mxy- y 틀림
        answer[Mxy-y] = answer[Mxy-y][:x-Mnx] + ['*'] + answer[Mxy -y][x-Mnx+1:]
     
    return [''.join(ans) for ans in answer]
solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]] )

solution( [[0, 1, -1], [1, 0, -1], [1, 0, 1]] )
solution( [[1, -1, 0], [2, -1, 0]] )

solution( [[1, -1, 0], [2, -1, 0], [4, -1, 0]] )
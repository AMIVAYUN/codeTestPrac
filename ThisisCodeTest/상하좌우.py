# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:28:03 2022
@FileName: 상하좌우.py
@author: YUNJUSEOK
@Link:
"""
def decorator( func ):
    def wrapper( *args, **kwargs ):
        import time;
        start= time.time();
        print( "-" * 10 ,func.__name__, "-" * 10 );
        func( *args, **kwargs )
        
        print( func.__name__, "의 실행시간은 ",time.time() - start, "입니다." );
    return wrapper

#pos( x, y )
def Left( n, pos ):
    nx = pos[ 0 ] - 1;
    ny = pos[ 1 ];
    if( 0<= nx < n and 0<= ny < n):
        return ( nx, ny )
    return pos;

def Right( n, pos ):
    nx = pos[ 0 ] + 1;
    ny = pos[ 1 ];
    if( 0<= nx < n and 0<= ny < n):
        return ( nx, ny )
    return pos;
def Up( n, pos ):
    nx = pos[ 0 ] ;
    ny = pos[ 1 ] - 1;
    if( 0<= nx < n and 0<= ny < n):
        return ( nx, ny )
    return pos;
def Down( n, pos ):
    nx = pos[ 0 ];
    ny = pos[ 1 ] + 1;
    if( 0<= nx < n and 0<= ny < n):
        return ( nx, ny )
    return pos;

#실패
def DelUnder( a ):
    return -( a ^ -1 );
#02
def move( n, pos, str0 ):
    dit = { "L" : ( -1, 0 ), "R": ( 1, 0 ), "U": ( 0, -1 ), "D": ( 0, 1 ) }
    movepos = dit[ str0 ];
    nx, ny = pos[ 0 ] + movepos[ 0 ], pos[ 1 ] + movepos[ 1 ];
    
    return ( nx, ny ) if 0<= nx < n and 0<= ny < n else pos; 
    

def LRUD_01():
    # 범위를 벗어나는 무빙은 무시됨.
    dit = { "L" : Left, "R": Right , "U": Up, "D": Down }
    N = int( input( ) )
    pos = ( 0, 0 )
    lst = [ i for i in input().split() ];
    
    for i in lst:
        pos = dit[ i ]( N, pos );
    
    print( pos[ 1 ] + 1, pos[0] + 1  )
    
def LRUD_02():
    N = 5
    pos = ( 0, 0 )
    lst = [ "R","R","R","U","D","D"]
    
    for i in lst:
        pos = move( N, pos, i );
    
    print( [ pos[ i ] + 1 for i in range( 1, -1, -1 )]);

#02 의 move 함수를 제거하여 본 함수에 합일
def LRUD_03( N, pos, lst ):
    dit = { "L" : ( -1, 0 ), "R": ( 1, 0 ), "U": ( 0, -1 ), "D": ( 0, 1 ) }
    for i in lst:
        mvpos = dit[ i ];
        nx, ny = pos[ 0 ] + mvpos[ 0 ] , pos[ 1 ] + mvpos[ 1 ];
        pos = ( nx, ny ) if 0<= nx < N and 0<= ny < N else pos;  
    
    print( [ pos[ i ] + 1 for i in range( 1, -1, -1 )]);

#02의 OVER 0 <= x 을 없애보자
def LRUD_04( N, pos, lst ):
    dit = { "L" : ( -1, 0 ), "R": ( 1, 0 ), "U": ( 0, -1 ), "D": ( 0, 1 ) }
    for i in lst:
        mvpos = dit[ i ];
        nx, ny = pos[ 0 ] + mvpos[ 0 ] , pos[ 1 ] + mvpos[ 1 ];
        nx *= int( nx >= 0 ); ny *= int( ny >= 0 );
        pos = ( nx, ny ) if nx < N and ny < N else pos;  
    
    print( [ pos[ i ] + 1 for i in range( 1, -1, -1 )]);
    
# Under를 지워보자 x< N 
def LRUD_05( n, pos, lst ):
    dit = { "L" : ( -1, 0 ), "R": ( 1, 0 ), "U": ( 0, -1 ), "D": ( 0, 1 ) }
    for i in lst:
        mvpos = dit[ i ];
        nx, ny = pos[ 0 ] + mvpos[ 0 ] , pos[ 1 ] + mvpos[ 1 ];
        
        nx = ( nx * ( int ( nx < n ) ) ) + ( pos[ 0 ] * ( int( not( nx < n ) ) ) )
        
        nx *= int( nx >= 0 ); 
        
        ny = ( ny * ( int ( ny < n ) ) ) + ( pos[ 0 ] * ( int( not( ny < n ) ) ) )
        
        ny *= int( ny >= 0 );
        
        pos = ( nx, ny )
    
    print( [ pos[ i ] + 1 for i in range( 1, -1, -1 )]);
    
#방향성이 잘못 됨. 05는 IF가 사라진게 아님
def LRUD_06( N, pos, lst ):
    dit = { "L" : ( -1, 0 ), "R": ( 1, 0 ), "U": ( 0, -1 ), "D": ( 0, 1 ) }
    for i in lst:
        mvpos = dit[ i ];
        nx, ny = ( pos[ 0 ] + mvpos[ 0 ] ) if 0<= pos[ 0 ] + mvpos[ 0 ] else pos[ 0 ], ( pos[ 1 ] + mvpos[ 1 ] ) if 0<= pos[ 1 ] + mvpos[ 1 ] else pos[ 1 ];

        pos = ( nx & 3, ny & 3 )
    
    print( [ pos[ i ] + 1 for i in range( 1, -1, -1 )]);

def LRUD_07( N, pos, lst ):
    dit = { "L" : ( -1, 0 ), "R": ( 1, 0 ), "U": ( 0, -1 ), "D": ( 0, 1 ) }
    for i in lst:
        mvpos = dit[ i ];
        nx = ( pos[ 0 ] + mvpos[ 0 ] ) if 0<= pos[ 0 ] + mvpos[ 0 ] else pos[ 0 ];
        ny = ( pos[ 1 ] + mvpos[ 1 ] ) if 0<= pos[ 1 ] + mvpos[ 1 ] else pos[ 1 ];
        pos = ( nx & 3, ny & 3 )
    
    print( [ pos[ i ] + 1 for i in range( 1, -1, -1 )]);

# or 을 이용한 Over 제거
def LRUD_08( N, pos, lst ):
    dit = { "L" : ( -1, 0 ), "R": ( 1, 0 ), "U": ( 0, -1 ), "D": ( 0, 1 ) }
    for i in lst:
        mvpos = dit[ i ];
        nx, ny = pos[ 0 ] + mvpos[ 0 ] or 1 , pos[ 1 ] + mvpos[ 1 ] or 1;
        print( nx, ny )
        pos = ( nx, ny ) if nx < N and ny < N else pos;  
    
    print( [ pos[ i ] for i in range( 1, -1, -1 )]);
# Under 제거 Try -> nx and ( nx % N )
def LRUD_09( N, pos, lst ):
    dit = { "L" : ( -1, 0 ), "R": ( 1, 0 ), "U": ( 0, -1 ), "D": ( 0, 1 ) }
    for i in lst:
        mvpos = dit[ i ];
        nx, ny = pos[ 0 ] + mvpos[ 0 ] or 1 , pos[ 1 ] + mvpos[ 1 ] or 1;
        nx = nx and ( nx % ( N + 1 ) ); ny = ny and ( ny % ( N + 1 ) );
        pos = ( nx, ny )  
    
    print( [ pos[ i ] for i in range( 1, -1, -1 )]);
    
def LRUD_10( N, pos, lst ):
    dit = { "L" : ( -1, 0 ), "R": ( 1, 0 ), "U": ( 0, -1 ), "D": ( 0, 1 ) }
    for i in lst:
        mvpos = dit[ i ];
        nx, ny = pos[ 0 ] + mvpos[ 0 ] or 1 , pos[ 1 ] + mvpos[ 1 ] or 1;
        nx -= not( nx % ( N + 1 ) ); ny -= not( ny % ( N + 1 ) );
        pos = ( nx, ny )  
    print( [ pos[ i ] for i in range( 1, -1, -1 )]);
    
def LRUD_11( N, pos, lst ):
    dit = { "L" : ( -1, 0 ), "R": ( 1, 0 ), "U": ( 0, -1 ), "D": ( 0, 1 ) }
    for i in lst:
        mvpos = dit[ i ];
        nx, ny = pos[ 0 ] + mvpos[ 0 ] or 1 , pos[ 1 ] + mvpos[ 1 ] or 1;
        nx -= ( ( ( nx ^ (N + 1) ) and 1 ) ^ 1 ); ny -= ( ( ( ny ^ (N + 1) ) and 1 ) ^ 1 )
        pos = ( nx, ny )  
    print( [ pos[ i ] for i in range( 1, -1, -1 )]);
    
def LRUD_12( N, pos, lst ):
    dit = { "L" : ( -1, 0 ), "R": ( 1, 0 ), "U": ( 0, -1 ), "D": ( 0, 1 ) }
    for i in lst:
        mvpos = dit[ i ];
        nx, ny = pos[ 0 ] + mvpos[ 0 ] or 1 , pos[ 1 ] + mvpos[ 1 ] or 1;
        nx -= ( ( nx % ( N + 1 ) ) and 1 ) ^ 1; ny -= ( ( ny % ( N + 1 ) ) and 1 ) ^ 1
        pos = ( nx, ny )  
    print( [ pos[ i ] for i in range( 1, -1, -1 )]);                

#배열을 활용
def LRUD_13( N, pos, lst ):
    dit = { "L" : ( -1, 0 ), "R": ( 1, 0 ), "U": ( 0, -1 ), "D": ( 0, 1 ) }
    pl = [ 1 ] + ( [ 0 ] * N ) 
    for i in lst:
        mvpos = dit[ i ];
        nx =  pos[ 0 ] + mvpos[ 0 ] or 1;
        ny = pos[ 1 ] + mvpos[ 1 ] or 1;
        nx -= pl [ nx % ( N + 1 ) ] ; 
        ny -= pl [ ny % ( N + 1 ) ] ;
        pos = ( nx, ny )  
    print( [ pos[ i ] for i in range( 1, -1, -1 )]);                

def LRUD_14( N, pos, lst ):
    x, y = 0, 1;
    
    dit = { "L" : ( -1, 0 ), "R": ( 1, 0 ), "U": ( 0, -1 ), "D": ( 0, 1 ) }
    pl = [ 1 ] + ( [ 0 ] * N ) 
    for i in lst:
        mvpos = dit[ i ];
        nx =  pos[ x ] + mvpos[ x ] or 1;
        ny = pos[ y ] + mvpos[ y ] or 1;
        nx -= pl [ nx % ( N + 1 ) ] ; 
        ny -= pl [ ny % ( N + 1 ) ] ;
        pos = ( nx, ny )  
    print( [ pos[ i ] for i in range( 1, -1, -1 )]);                
    
def LRUD_15( N, pos, lst ):
    xy = ( 0 , 1 );
    
    dit = { "L" : ( -1, 0 ), "R": ( 1, 0 ), "U": ( 0, -1 ), "D": ( 0, 1 ) }
    pl = [ 1 ] + ( [ 0 ] * N ) 
    for i in lst:
        mvpos = dit[ i ];
        nx =  pos[ xy[0] ] + mvpos[ xy[0] ] or 1;
        ny = pos[ xy[1] ] + mvpos[ xy[1] ] or 1;
        nx -= pl [ nx % ( N + 1 ) ] ; 
        ny -= pl [ ny % ( N + 1 ) ] ;
        pos = ( nx, ny )  
    print( [ pos[ i ] for i in range( 1, -1, -1 )]);                
    
def LRUD_B_1( N, lst ):
    x, y = 1, 1;
    
    
    
    
    
def lrud_test():
    N = 5;
    pos = ( 0, 0 )
    lst = [ "R","R","R","U","D","D"]
    pos2 =( 1, 1 )
    print(" -- 02 --")
    LRUD_02();
    dl3 = decorator( LRUD_03 );
    dl3( N, pos, lst )
    
    dl4 = decorator( LRUD_04 );
    dl4( N, pos, lst );
    
    dl5 = decorator( LRUD_05 );
    dl5( N, pos, lst );
    
    dl6 = decorator( LRUD_06 );
    dl6( N, pos, lst );
    
    dl8 = decorator( LRUD_08 );
    dl8( N, pos2, lst );
    
    dl9 = decorator( LRUD_09 );
    dl9( N, pos2, lst );

def lrud_test09_2():
    N = 5;
    lst = [ "D" for i in range( N + 5 ) ]
    pos2 = ( 1, 1 )
    
    dl9 = decorator( LRUD_09 );
    dl9( N, pos2, lst );

    
def lrud_test09():
    
    
    
    N = 1000000
    pos = ( 0, 0 )
    lst = [ "D" for i in range( N - 1 ) ]
    pos2 =( 1, 1 )
    dl4 = decorator( LRUD_04 );
    dl4( N, pos, lst );
    
    
    dl9 = decorator( LRUD_09 );
    dl9( N, pos2, lst );
    
    
def lrud_test10():
    
    
    
    N = 1000000
    pos = ( 0, 0 )
    lst = [ "D" for i in range( N ) ]
    pos2 =( 1, 1 )
    dl4 = decorator( LRUD_04 );
    dl4( N, pos, lst );
    
    
    dl10 = decorator( LRUD_10 );
    dl10( N, pos2, lst );
 
def lrud_test14():
    N = 1000000
    pos = ( 0, 0 )
    lst = [ "D" for i in range( N ) ]
    pos2 =( 1, 1 )
    
    dl4 = decorator( LRUD_04 );
    dl4( N, pos, lst );
    
    
    dl10 = decorator( LRUD_10 );
    dl10( N, pos2, lst );
    
    
    dl11 = decorator( LRUD_11 );
    dl11( N, pos2, lst );
    
    dl12 = decorator( LRUD_12 );
    dl12( N, pos2, lst );
    
    
    dl13 = decorator( LRUD_13 );
    dl13( N, pos2, lst );
    
    dl14 = decorator( LRUD_14 );
    dl14( N, pos2, lst );
    
    dl15 = decorator( LRUD_15 );
    dl15( N, pos2, lst );
    
    
def main():
    lrud_test();   
    lrud_test09();
    lrud_test09_2();
    lrud_test10();
    lrud_test14();
    
if( __name__ == "__main__"):
    main();
    
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 13:46:27 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
def t1():
    

    M, N, L = map( int, input().split() );
    
    hunters = list( map( int, input().split() ) );
    
    monsters = set();
    
    for i in range( N ):
        x, y =  map( int, input().split() )
        
        if( y > L ):
            continue;
        monsters.add( ( x, y ) );
    
    
    s_monsters = set( sorted( monsters, key = lambda x: ( x[ 0 ], x[ 1 ] ) ) );
    
    ans = 0 ;
    
    for hunter in hunters:
        target = set();
        
        
        for monster in s_monsters:
            if( abs( hunter - monster[ 0 ]  ) + abs( monster[ 1 ] ) <= L ):
                target.add( monster );
        
        
        s_monsters = s_monsters.difference( target );
        
        ans += len( target );
        
    print( ans )

#5% out
def t2():
    M, N, L = map( int, input().split() );
    
    hunters =list( sorted(  list( map( int, input().split() ) ) ) );
    ans = 0;
    
    for i in range( N ):
        x, y = map( int, input().split() )
        
        if( y > L ):
            continue;
            
        else:
            
            cond = False;
            lt = 0; rt = M -1;
            
            while lt <= rt:
                
                mid = ( lt + rt ) // 2 ;
                
                if( mid >= M):
                    rt -= 1;
                    continue;
                    
                    
                if( abs( hunters[ mid ] - x ) + y <= L ):
                    lt = mid + 1;
                    cond = True;
                else:
                    rt = mid - 1;
            
            ans += int( cond );
            
                    
    print( ans )
    
def t3():
    M, N, L = map( int, input().split() );
    
    hunters =list( sorted(  list( map( int, input().split() ) ) ) );
    ans = 0;
    
    for i in range( N ):
        x, y = map( int, input().split() )
        
        if( y > L ):
            continue;
            
        else:
            
            lt = 0; rt = M - 1;
            
            while lt < rt:
                
                mid = ( lt + rt ) // 2 ;
                    
                    
                if( hunters[mid] > x ):
                    lt = mid + 1;
                else:
                    rt = mid;
            
            ans += int( ( ( abs( hunters[ rt ] -x ) + y ) <= L ) or ( abs( hunters[ rt - 1 ] - x ) + y ) <= L );
            
                    
    print( ans )

def t4():
    M, N, L = map( int, input().split() );
    
    hunters =list( sorted(  list( map( int, input().split() ) ) ) );
    ans = 0;
    
    for i in range( N ):
        x, y = map( int, input().split() )
        
        if( y > L ):
            continue;
            
        else:
            tg = M - 1
            lt = 0; rt = M - 1;
            
            while lt < rt:
                
                mid = ( lt + rt ) // 2 ;
                
                if( mid >= M ):
                    rt -= 1;
                    
                    continue;
                    
                if( hunters[ mid ] > x ):
                    
                    lt = mid + 1
                else:
                    tg = mid
                    rt = mid - 1;
            
            res = ( abs( hunters[ tg ] -x ) + y ) <= L or ( ( abs( hunters[ tg + 1 ] - x ) + y <=L ) if tg - 1 >= 0 else False )
            ans += int( res );
            
                    
    print( ans )
t4()
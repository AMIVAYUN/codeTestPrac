# -*- coding: utf-8 -*-
"""
Created on Sun May 29 17:32:23 2022
@FileName: 비밀지도.py
@author: YUNJUSEOK
@Link : https://programmers.co.kr/learn/courses/30/lessons/17681

@Input & Output : 매개변수	값
                        n	5
                        arr1	[9, 20, 28, 18, 11]
                        arr2	[30, 1, 21, 17, 28]
                        출력	["#####","# # #", "### #", "# ##", "#####"] 
                        
"""
def solution1( n, arr1, arr2 ):
    answer = [];
    arr1 = [ '0' * ( n - len( bin( i )[ 2: ] ) )+bin( i )[ 2: ] for i in arr1 ];
    arr2 = [ '0' * ( n - len( bin( i )[ 2: ] ) )+bin( i )[ 2: ] for i in arr2 ];
    arr3 = [ [] * n for i in range( n )]
   
    for i in range( n ):
        for j in range( n ):
            if( arr1[ i ][ j ] == arr2[ i ][ j ] == '0'):
                
                arr3[ i ].append( ' ' );
            else:
                
                arr3[ i ].append( '#' );
            
    
    for i in range( n ):
        str0 = ''.join( j for j in arr3[ i ] );
        
        answer.append( str0 );

        
    return answer;

def solution2( n, arr1, arr2 ):
    answer = [];
    arr1 = [ '0' * ( n - len( bin( i )[ 2: ] ) )+bin( i )[ 2: ] for i in arr1 ];
    arr2 = [ '0' * ( n - len( bin( i )[ 2: ] ) )+bin( i )[ 2: ] for i in arr2 ];
    arr3 = [ [] * n for i in range( n )]
   
    for i in range( n ):
        str0 = ''
        for j in range( n ):
            if( arr1[ i ][ j ] == arr2[ i ][ j ] == '0'):
                
                str0 = str0 + "0"
            else:
                
                str0 = str0 + "#"
            
        answer.append( str0 );

        
    return answer;
        



    
def solution3(n, arr1, arr2):
    # bin로 나타내기전에 해당 문제는 결국 비트 연산이므로 각 자리수를 or 연산을 통해 합치고 bin 문자열로 나타낸
    # 다음에 str의 padding method인 rjust를 사용해 0패딩을 해주어 각 자리수를 맞춰주었습니다. 
    lst = [ ( bin( arr1[ i ] | arr2[ i ] )[2:] ).rjust( n, "0" ) for i in range( len( arr1 ) ) ]
    answer = [];
    for i in range( len( lst ) ):
        temp = ''.join( "#" if j == '1' else " " for j in lst[ i ] )
        
        answer.append( temp );
    
   


    return answer;   
    
    
def solution4(n, arr1, arr2):
    # bin로 나타내기전에 해당 문제는 결국 비트 연산이므로 각 자리수를 or 연산을 통해 합치고 bin 문자열로 나타낸
    # 다음에 str의 padding method인 rjust를 사용해 0패딩을 해주어 각 자리수를 맞춰주었습니다. 
    doc = " #"
    lst = [ ( bin( arr1[ i ] | arr2[ i ] )[2:] ).rjust( n, "0" ) for i in range( len( arr1 ) ) ]
    answer = [];
    for i in range( len( lst ) ):
        
        temp = ''.join( doc[ int( j == '1') ] for j in lst[ i ] )
        
        
        answer.append( temp );
    
   


    return answer;   
    
def solution5(n, arr1, arr2):
    # bin로 나타내기전에 해당 문제는 결국 비트 연산이므로 각 자리수를 or 연산을 통해 합치고 bin 문자열로 나타낸
    # 다음에 str의 padding method인 rjust를 사용해 0패딩을 해주어 각 자리수를 맞춰주었습니다. 
    doc = " #"
    lst = [ ( bin( arr1[ i ] | arr2[ i ] )[2:] ).rjust( n, "0" ) for i in range( len( arr1 ) ) ]
    lenx = len( lst )
    answer = [ ''.join( [ doc[ int( lst[i][j] == '1' ) ] for j in range( len( lst[ i ] ) ) ] ) for i in range( lenx )  ];
    
    return answer
def solution5(n, arr1, arr2):
    # bin로 나타내기전에 해당 문제는 결국 비트 연산이므로 각 자리수를 or 연산을 통해 합치고 bin 문자열로 나타낸
    # 다음에 str의 padding method인 rjust를 사용해 0패딩을 해주어 각 자리수를 맞춰주었습니다. 
    doc = " #"
    
    lst = [ "0" * ( n - len( ( bin( arr1[ i ] | arr2[ i ] )[2:] ) ) ) + ( bin( arr1[ i ] | arr2[ i ] )[2:] ) for i in range( len( arr1 ) ) ]
    lenx = len( lst )
    answer = [ ''.join( [ doc[ int( lst[i][j] == '1' ) ] for j in range( len( lst[ i ] ) ) ] ) for i in range( lenx )  ];
    
    return answer
def solution6( n, arr1, arr2 ):
    # bin로 나타내기전에 해당 문제는 결국 비트 연산이므로 각 자리수를 or 연산을 통해 합치고 bin 문자열로 나타낸
    # 다음에 str의 padding method인 rjust를 사용해 0패딩을 해주어 각 자리수를 맞춰주었습니다. 
    doc = " #"
    leny = len( arr1 );
    lst = [ 0 ] * leny ;
    
    for i in range( leny ):
        tmp = ( bin( arr1[ i ] | arr2[ i ] )[2:] );
        k = "0" * ( n - len( tmp ) );
        strtmp = '';
        for j in ( k + tmp ):
            strtmp += doc [ ( j == '1' ) & 1 ]
        
    
        lst[ i ] = strtmp;
    
    return lst

def solution7( n, arr1, arr2 ):
    # bin로 나타내기전에 해당 문제는 결국 비트 연산이므로 각 자리수를 or 연산을 통해 합치고 bin 문자열로 나타낸
    # 다음에 str의 padding method인 rjust를 사용해 0패딩을 해주어 각 자리수를 맞춰주었습니다. 
    doc = " #"
    leny = len( arr1 );
    lst = [ 0 ] * leny ;
    
    for i in range( leny ):
        tmp = ( bin( arr1[ i ] | arr2[ i ] )[2:] );
        k = "0" * ( n - len( tmp ) );
        strtmp = '';
        for j in ( k + tmp ):
            strtmp += doc [ j & 1 ]
        
    
        lst[ i ] = strtmp;
    
    return lst

def solution8(n, arr1, arr2):
    # bin로 나타내기전에 해당 문제는 결국 비트 연산이므로 각 자리수를 or 연산을 통해 합치고 bin 문자열로 나타낸
    # 다음에 str의 padding method인 rjust를 사용해 0패딩을 해주어 각 자리수를 맞춰주었습니다. 
    doc = " #"
    
    lst = [ "0" * ( n - len( ( bin( arr1[ i ] | arr2[ i ] )[2:] ) ) ) + ( bin( arr1[ i ] | arr2[ i ] )[2:] ) for i in range( len( arr1 ) ) ]
    lenx = len( lst )
    answer = [ ''.join( [ doc[ ord ( lst[i][j] ) & 1 ] for j in range( len( lst[ i ] ) ) ] ) for i in range( lenx )  ];
    
    return answer

def solution9( n, arr1, arr2 ):
    import copy;
    doc = " #"
    answer = [];
    lst = [ arr1[i] | arr2[i] for i in range( len( arr1 ) ) ] 
    for i in lst:
        str0 = ""
        n_ = [0] * n ;
        idx = n - 1;
        while( idx > -1 ):
            
            str0 += doc[ i % 2 ];
            idx -= 1;
            i //= 2;
        answer.append( str0 );
    
    print( answer );
    return answer;
        
       
        
def solution10( n , arr1, arr2 ):
    import copy;
    doc = " #"
    answer = [];
    lst = [ arr1[i] | arr2[i] for i in range( len( arr1 ) ) ] 
    for i in lst:
        str0 = ""
        n_ = [0] * n ;
        idx = n - 1;
        while( idx > -1 ):
            
            str0 += doc[ i & 1 ];
            idx -= 1;
            i = i >> 2;
        answer.append( str0 );
    
    print( answer );
    return answer;  
    
def solution10( n , arr1, arr2 ):
    doc = " #"
    answer = [];
    lst = [ arr1[i] | arr2[i] for i in range( len( arr1 ) ) ] 
    for i in lst:
        str0 = ""
        n_ = [0] * n ;
        idx = n - 1;
        for idx in range( n - 1 , -1 , -1 ):
            str0 += doc[ ( i >> idx ) & 1 ];
            idx -= 1;
    
            
            
        answer.append( str0 );
    
  
    return answer;  
        
def solution11( n , arr1, arr2 ):
    #assignment
    doc = " #"
    answer = [ "0" ] * len( arr1 );
    lst = [ arr1[i] | arr2[i] for i in range( len( arr1 ) ) ] 
    #logic
    for i in range( len( lst ) ):
        str0 = ""
        idx = n - 1;
        for idx in range( n - 1 , -1 , -1 ):
            str0 += doc[ ( lst[ i ] >> idx ) & 1 ];
        answer[ i ] = answer[ i ].replace( "0", str0 ); 
    #return
    return answer;  
        
def solution12( n , arr1, arr2 ):
    #assignment
    doc = " #"
    answer = [ "0" ] * len( arr1 );
    lst = [ arr1[i] | arr2[i] for i in range( len( arr1 ) ) ] 
    #logic
    for i in range( len( lst ) ):
        str0 = ""
        idx = n - 1;
        for idx in range( n - 1 , -1 , -1 ):
            str0 += doc[ ( lst[ i ] >> idx ) & 1 ];
        answer[ i ] = str0;
    #return
    return answer;  
        
    
        
    
def main():
    global answer;
    n = 5;
    arr1 =	[9, 20, 28, 18, 11];
    arr2 =	[30, 1, 21, 17, 28];
    answer = solution12( n, arr1, arr2 ) 
    print( answer );
   
answer = [];
    
    
    


if( __name__ == "__main__" ):
    main();

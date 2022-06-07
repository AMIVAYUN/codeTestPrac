# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 15:56:26 2022
@FileName: 1300.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1300
@ REF: https://velog.io/@dlrmsghks7/%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%EC%95%8C%EC%95%84%EB%B4%85%EC%8B%9C%EB%8B%A4
"""
#Heap 활용 메모리 아웃
def main():
    import heapq, sys;
    N = int( sys.stdin.readline() );
    
    lst = [  i * j for j in range( 1, N + 1 )  for i in range( 1, N + 1 ) ] 
    
    heapq.heapify( lst );
    K = int( sys.stdin.readline() );
    print( lst[ K ] )
    
    
    




if( __name__ == "__main__"):
    main()
#선형 탐색 실패
def main():
    N = int( input() );
    K = int( input() );
    Ka = K
    
    while True:
        n = 0;
        for i in range( 1, N + 1 ):
            n += min( N, Ka // i );
        
        if( n > K ):
            Ka -= 1;
        
        if( n < K ):
            print( Ka + 1 )
            break;
    
    




if( __name__ == "__main__"):
    main()
    
def main():
    N = int( input( ) );
    K = int( input( ) );
    lt, rt = 0, K ;
    answer = 0;
    while lt <= rt:
        
        mid = ( lt + rt ) // 2;
        print( lt, rt, mid );
        cnt = 0;
        for i in range( 1, N + 1 ):
            cnt+= min( mid // i , N );
        
        if( cnt >= K ):
            answer = mid;
            rt = mid - 1;
        else:
            lt = mid + 1;
            
    
    
    print( answer )
    
    
if( __name__ == "__main__" ):
    
    main();


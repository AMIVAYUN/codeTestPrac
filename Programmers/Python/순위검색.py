from bisect import bisect_left as bs;
def solution(info, query)
    answer = []
    info_lst = [];
    query_lst = [];
    for i in info
        str0 = i.split();
        info_lst.append( ( str0[ -1], int( str0[-1] ) ) );
    for j in query
        str0 = j.replace( and,   ).split();
        query_lst.append( (''.join( str0[ -1 ] ), int( str0[ -1 ] ) ) )
    
    
    from collections import defaultdict;
    import itertools; 
    dit = defaultdict( list );
    
    for i in info_lst
        dit[ ''.join( i[ 0 ] ) ].append( i[ 1 ] );
        standard = [ 0, 1, 2, 3 ]
        for num in range( 1, 5 )
            cmb = itertools.combinations( standard, num );
            for case in cmb
                tmp = i[ 0 ][]
                for idx in case
                    tmp[ idx ] = -;
                dit[ ''.join(tmp) ].append( i[ 1 ] );
    
    for value in dit.values()
        value.sort();
    
    
                
    for q,qs in query_lst
        lenx = len( dit [ q ] );
        idx = bs( dit[ q ], qs );
        answer.append( lenx - idx );
            
    
    return answer
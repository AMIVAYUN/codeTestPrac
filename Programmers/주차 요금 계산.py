def solution(fees, records):
    answer = [];
    import math
    
    fields = dict();
    
    timestamp = dict();
    for record in records:
        time, number, direct = record.split();
        if( direct == 'IN' ):
            if( number not in fields ):
                fields[ number ] = 0;
            timestamp[ number ] = time;
            
        else:
            inval = timestamp.pop( number );
            
            in_hour,in_minute = inval.split( ":" );
            
            out_hour, out_minute = time.split( ":" );
            
            in_hour, in_minute = int( in_hour ), int( in_minute );
            
            out_hour, out_minute = int( out_hour ), int( out_minute );
            
            if( out_minute < in_minute ):
                out_minute += 60;
                out_hour -= 1;
            
            rs_hour = out_hour - in_hour;
            rs_minute = out_minute - in_minute;
            
            fields[ number ] += ( rs_hour * 60 ) + rs_minute
    
    
    for remain in timestamp:
        s_hour = 23;
        s_min = 59;
        
        re_hour, re_min = map( int, timestamp[ remain ].split(":" ) ) ;
        s_hour -= re_hour;
        s_min -= re_min;
        fields[ remain ] += ( s_hour * 60 ) + s_min;
        
    baseTime, baseFee, unitTime, unitFee = fees;
    
    result = dict();

    for field in fields:
        
        number, time = field, fields[ field ]
        
        if( time < baseTime ):
            base = 0;
        else:
            base = time - baseTime
            
        if( unitTime > base and base != 0):
            rs = 1;
        
        elif( base == 0 ):
            rs = 0;
        
        
        else:
            rs = math.ceil( base / unitTime );
        
        result[ int( number ) ] = baseFee +(  rs * unitFee )
    
    
    answer = [ i[ 1 ] for i in list( sorted( result.items(), key = lambda x: x[ 0 ] ) ) ]
    
        
    return answer

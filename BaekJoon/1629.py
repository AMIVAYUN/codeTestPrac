A, B, C = map( int, input().split() );

result = 1;


if A > C: A %= C;

div = B//2;

mod = B % 2;

def recurs( a, b, c ):

    div, mod = b // 2, b % 2;

    if b == 1:
        return a % c;


    result = recurs( a, div, c );

    return result * result * a % c if mod else result * result % c;

print ( recurs( A, B, C ) );

# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:46:25 2022
@FileName: .py
@author: YUNJUSEOK
"""

#["c","f","j"]
#"j" 에서 에러 발생. 
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters_B = [ i for i in letters if ord( i )  > ord( target ) % 122 ];
        
        return letters_B[0] if( len( letters_B ) > 0 ) else letters[0]
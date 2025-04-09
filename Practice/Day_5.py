""" mirrored right triangle

        * 
      * * 
    * * * 
  * * * * 
* * * * *

solution 1-

def mirrored_right_triangle(n):
    for i in range(1, n + 1):
        spaces = '  ' * (n - i)         # 2 spaces for better alignment
        stars = '* ' * i                # star with space after it
        print(spaces + stars)

# Example usage:
mirrored_right_triangle(5)

solution 2- 
n=5
for x in range(1,n+1):
    print('  '*(n-x)+'* '*x)
"""



"""
Right down mirror star Pattern
Pattern -
*****
 ****
  ***
   **
    *

n=5
for x in range(n):
    print('  '*x+' *'*(n-x))

"""

""" Downward full Pyramid Pattern of star
        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             * 

n=5
for x in range(n):
    print(' '*x+' *'*(n-x))

"""

""" Equilateral triangle pattern of star
             *   
           *  *   
          *  *  *   
         *  *  *  *   
        *  *  *  *  *   
       *  *  *  *  *  *   
      *  *  *  *  *  *  * 

n=5
for x in range(1,n+1):
    print(' '*(n-x)+' *'*x)

"""


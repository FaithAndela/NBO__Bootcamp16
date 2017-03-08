
def find_max_min(A):
    """ function to create Min_Max with an arguement A"""
    result=[]
    for num in A:
        if min (A) != max (A):
            result.append(min (A) )
            result.append(max (A) ) 
            return result
        else:
            """check if in the list the maximum and minimum are equal in the list"""
            result=[]
            result.append(len (A) )
            return result
print(find_max_min( [6,4]) )


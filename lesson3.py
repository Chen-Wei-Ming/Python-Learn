# define new function
def print2Varfunction(var1 , var2):
    # print string and var , use %s , %d
    print('1 : %s , 2 : %s'  %(var1,var2))

def recursivefunction(start , end , count):
    if start > end :
        return count
    else:
        count = count + start
        return recursivefunction(start+1 , end , count)
# call function
print2Varfunction('string1' , 'string2')
# resulte  = 1 : string1 , 2 : string2
print(recursivefunction(1 , 5 , 0))
# result = 15

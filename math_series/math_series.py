
# series=input(" Please enter fibonacci or lucas > ")
# terms=int(input(" number in series>"))



def fibonacci(n):
     """ 
     The function was created to take number that its length of index given and it will start from 0 and 1
     """
     if n <= 1:
       return n
     else:
       return(fibonacci(n-1) + fibonacci(n-2))

def lucas(n):
    """ 
    The function was created to take number that its length of index  given and it will start from 2 and 1
    """

    if n == 0:
        return 2
    if n == 1:
        return 1
 
   
    return lucas(n - 1) +  lucas(n - 2)


def sum_series(n,firstNum=0,secondNum=1): 
    """
    The function was created to take number that its length of index  given and it will start from first and second
    """
    if n<0:
        return "Cant do sum series on negative num"
    if n==0:
        return firstNum  
    if n==1:
        return secondNum       
    return sum_series(n-1, firstNum, secondNum) + sum_series(n-2, firstNum, secondNum)       


print(sum_series(5))
# print(lucas(5))
# print(fibonacci(5))


       



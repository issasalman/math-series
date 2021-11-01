
# series=input(" Please enter fibonacci or lucas > ")
# terms=int(input(" number in series>"))



def fibonacci(n):
     if n <= 1:
       return n
     else:
       return(fibonacci(n-1) + fibonacci(n-2))

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
 
   
    return lucas(n - 1) +  lucas(n - 2)


def sum_series(n,firstNum=0,secondNum=1): 
    if n<0:
        return "Cant do sum series on negative num"
    if n==0:
        return firstNum  
    if n==1:
        return secondNum       
    return sum_series(n-1, firstNum, secondNum) + sum_series(n-2, firstNum, secondNum)       


# print(sum_series(2,5,5))
# print(lucas(5))
# print(fibonacci(5))


       



def calculate(arr):
    if len(arr) == 0:
        return 0 
    total = 0
    for i in arr:
        total+= i
    return total/ len(arr)

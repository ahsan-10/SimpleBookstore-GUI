def SortTuple(tup): 
      
    # Getting the length of list  
    # of tuples 
    n = len(tup) 
      
    for i in range(n): 
        for j in range(n-i-1): 
              
            if tup[j][0] > tup[j + 1][0]: 
                tup[j], tup[j + 1] = tup[j + 1], tup[j] 
                  
    return tup 
      
# Driver's code 
  
tup = [("Gold", 28), ("Gold", 30), ("Silver", 29), 
        ("Gold", 21), ("Silver", "C")] 
          
print(SortTuple(tup)) 
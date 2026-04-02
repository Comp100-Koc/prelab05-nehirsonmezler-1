def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    a = a[2:]
    b = b[2:]
    
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = ""
    
    while i >= 0 or j >= 0 or carry:
        total = carry
        
        if i >= 0:
            if a[i] == '1':
                total += 1
            i -= 1
        
        if j >= 0:
            if b[j] == '1':
                total += 1
            j -= 1
        
        if total == 0:
            result = "0" + result
            carry = 0
        elif total == 1:
            result = "1" + result
            carry = 0
        elif total == 2:
            result = "0" + result
            carry = 1
        else:
            result = "1" + result
            carry = 1
    
   
    result = result.lstrip('0')
    if result == "":
        result = "0"
    
    return "0b" + result
    

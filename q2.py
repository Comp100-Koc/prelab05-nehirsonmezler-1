def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    changed = True
    
    while changed:
        changed = False
        i = 0
        new_s = ""
        
        while i < len(s):
            if i < len(s) - 1 and s[i] == s[i+1]:
                changed = True
                i += 2  
            else:
                new_s += s[i]
                i += 1
        
        s = new_s
    
    return s

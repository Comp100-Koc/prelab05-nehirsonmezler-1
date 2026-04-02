def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    longest = ""
    n = len(s)
    
    for i in range(n):
        for j in range(i + 2, n + 1):  
            sub = s[i:j]
            
            if sub == sub[::-1]:  
                if len(sub) > len(longest):
                    longest = sub
    
    return longest
    

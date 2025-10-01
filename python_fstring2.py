def palindrome_check(s: str) -> bool:
    s = ''.join(ch.lower() for ch in s if ch.isalnum())  
    
    if len(s) <= 1:   # base case
        return True

    if s[0] != s[-1]: # compare first and last
        return False

    return palindrome_check(s[1:-1])  # check insid
print(palindrome_check("racar"))
print(palindrome_check("A man ,A plan ,woww"))
print(palindrome_check("ogogo"))



def sum_nested_list(lst: list) -> int:
    total = 0
    for item in lst:
        if isinstance(item, int):       
            total += item
        elif isinstance(item, list):    
            total += sum_nested_list(item)
    return total
print(sum_nested_list([1, [2, 3], [4, [5, 6]], 7]))  
print(sum_nested_list([10, [20, [30]], 40]))         

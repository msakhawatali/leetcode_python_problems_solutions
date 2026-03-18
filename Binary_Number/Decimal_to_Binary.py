def decimal_to_binary_manual(num):
    if num == 0:
        return "0"
    binary_str = ""
    temp_num = abs(num) 
    while temp_num > 0:
        remainder = temp_num % 2
        binary_str = str(remainder) + binary_str 
        temp_num //= 2    
    if num < 0:
        binary_str = "-" + binary_str    
    return binary_str

print(decimal_to_binary_manual(42))
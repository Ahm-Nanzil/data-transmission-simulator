def calculate_even_parity(data):
    count_ones = data.count('1')
    if count_ones % 2 == 0:
        return '0'  # Even parity
    else:
        return '1'  # Odd parity

def check_for_errors(data, parity_bit):
    count_ones = data.count('1')
    if parity_bit == '0' and count_ones % 2 != 0:
        return True  # Error detected
    elif parity_bit == '1' and count_ones % 2 == 0:
        return True  # Error detected
    else:
        return False  # No error detected

# Example usage:
data_word = '11101'
even_parity_bit = calculate_even_parity(data_word)
error_detected = check_for_errors(data_word, even_parity_bit)
print("Error detected:", error_detected)

# project end
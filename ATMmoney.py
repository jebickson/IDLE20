def atm_withdrawal(input_str):
    # Parse the input string
    amounts = list(map(int, input_str.split(',')))
    
    # First amount is the total amount in the ATM
    K = amounts[0]
    # The rest are the amounts requested by each person
    requests = amounts[1:]
    
    # Initialize the result list
    result = []
    
    for request in requests:
        if request <= K:
            result.append('1')  # Successful withdrawal
            K -= request  # Decrease the available amount in ATM
        else:
            result.append('0')  # Withdrawal failed
    
    # Join the results into a single string and return
    return ''.join(result)

# Example usage
input_data = "5,10,3,5,3,2,1"
output = atm_withdrawal(input_data)
print(output)
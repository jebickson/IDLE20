def calculate_total_amount(N, P):
    # Step 1: Calculate the initial total amount
    initial_total = N * P
    
    # Step 2: Determine the number of items that are not billed
    if N >= 201:
        discounted_items = 30
    elif N >= 101:
        discounted_items = 20
    elif N >= 50:
        discounted_items = 10
    else:
        discounted_items = 0
    
    # Step 3: Calculate the total items billed
    items_billed = max(0, N - discounted_items)
    total_after_discounted_items = items_billed * P
    
    # Step 4: Calculate the additional discount based on the total amount
    if total_after_discounted_items >= 10001:
        discount_percentage = 20
    elif total_after_discounted_items >= 1001:
        discount_percentage = 15
    else:
        discount_percentage = 10
    
    # Step 5: Calculate the final amount after the additional discount
    discount_amount = (total_after_discounted_items * discount_percentage) / 100
    final_amount = total_after_discounted_items - discount_amount
    
    return final_amount

# Input format
input_data = input("Enter N and P separated by a comma (N,P): ")
N, P = map(int, input_data.split(','))

# Calculate and print the final amount
final_amount = calculate_total_amount(N, P)
print(f"Final amount payable by the customer: {final_amount:.2f}")
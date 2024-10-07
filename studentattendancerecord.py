def can_be_rewarded(attendance_record):
    # Check for the number of 'A's
    absent_count = attendance_record.count('A')
    
    # Check for more than two continuous 'L's
    late_streak = 0
    
    for char in attendance_record:
        if char == 'L':
            late_streak += 1
            if late_streak > 2:
                return False  # More than two continuous 'L's
        else:
            late_streak = 0  # Reset the streak for 'P' or 'A'
    
    # If absent count is more than 1, return False
    if absent_count > 1:
        return False
    
    return True  # Student can be rewarded

# Input format
attendance_record = input("Enter the attendance record: ")

# Check if the student can be rewarded and print the result
if can_be_rewarded(attendance_record):
    print("True.")
else:
    print("False.")
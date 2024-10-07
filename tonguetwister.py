def is_tongue_twister(paragraph, anchor_letter):
    words = paragraph.split()
    anchor_words = [word for word in words if word.lower().startswith(anchor_letter.lower())]
    
    # Check conditions
    if len(anchor_words) < 7:
        return "Inappropriate Entry"
    if len(anchor_words) > 20:
        return "Inappropriate Entry"
    for i in range(1, len(anchor_words)):
        if anchor_words[i].lower() == anchor_words[i - 1].lower():
            return "Inappropriate Entry"

    return "Good Tongue Twister"

# Input format
input_data = input("Enter the paragraph and anchor letter separated by '#': ")

# Split the input
paragraph, anchor_letter = input_data.split('#', 1)

# Check for tongue twister and print the result
result = is_tongue_twister(paragraph.strip(), anchor_letter.strip())
print(result)
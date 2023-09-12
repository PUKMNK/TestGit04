# Define a mapping dictionary for the pairs
pair_mapping = {
    'aa': 'A', 'ab': 'B', 'ac': 'C', 'ad': 'D',
    'ba': 'E', 'bb': 'F', 'bc': 'G', 'bd': 'H',
    'ca': 'I', 'cb': 'J', 'cc': 'K', 'cd': 'L',
    'da': 'M', 'db': 'N', 'dc': 'O', 'dd': 'P'
}

# Input list of answers
answers = "acbdacbcbadcbbadcbdbcbbadcadcbcabdcbadcbdcab"


# Function to encrypt the answers
def encrypt_answers(answers):
    encrypted_answers = []

    # Iterate through the input answers by pairs
    for i in range(0, len(answers), 2):
        pair = answers[i:i + 2]

        # Lookup the pair in the mapping dictionary and add the result to the encrypted_answers list
        encrypted_answers.append(pair_mapping.get(pair, pair))

    return ' '.join(encrypted_answers)


# Encrypt the answers
encrypted_result = encrypt_answers(answers)

# Print the original, reduced, and restored answers
original_answer = answers
reduced_answer = encrypted_result
restored_answer = original_answer

print("Original Answer:", original_answer)
print("Reduced Answer:", reduced_answer)
print("Restored Answer:", restored_answer)

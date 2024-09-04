def find_length(string):
    count = 0
    for _ in string:
        count += 1
    return count

# Function to handle each test case
def process_test_case(n, strings):
    index_dict = {}
    length_dict = {}
    
    # Creating the dictionary with indices
    for i in range(1, n + 1):
        if i not in index_dict:
            index_dict[i] = strings[i-1]
    
    # Creating the dictionary with string lengths
    for s in strings:
        if s not in length_dict:
            length_dict[s] = find_length(s)
    
    return index_dict, length_dict

# Input reading
T = int(input("Enter number of test cases: "))

for _ in range(T):
    N = int(input("Enter number of strings: "))
    strings = input("Enter the strings: ").split()
    
    # Process the test case
    index_dict, length_dict = process_test_case(N, strings)
    
    # Output the results
    print(f"Dictionaries created by inputs:")
    print(index_dict)
    print(length_dict)

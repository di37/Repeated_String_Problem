def repeatedString(s, n):
    '''Computes and returns total number of occurances of the character 'a' 
       in the prefix of length n of an infinitely repeating string.

    Parameters:
        s - Input string which is considered to be repeated infinitely.
        n - The first number of letters to be considered for counting number 
        of occurances of the character 'a' in the infinite string.
    
    Returns:
        Total number of occurances of the character 'a'.
    '''
    
    # Length of string.
    len_str = len(s)

    # Number of repeated strings to be considered.
    num_strs = n//len_str

    # Remainder: Lets consider an example - s = 'abc' and n = 11.
    # Therefore, the string to be considered for finding the number
    # of occurances of 'a' will be: 'abcabcabcab'. The string is 
    # repeating 3 times(abcabcabc). Now, remaining letters are only 2(ab). 
    # Therefore, length of remaining letters is calculated as below syntax.
    remainder = n%len_str

    # Counter to count number of a's from given string.
    count1 = 0

    # Counter to count a's from the remaining set of letters. In the end, it 
    # will be used to calculate total number of a's in the string.
    count2 = 0

    for i in range(len_str):
        # Calculating number of occurances of character 'a' from the given string
        if s[i] == 'a':
            count1 += 1
        # Calculating number of occurances from remaining letters
        # if they exist.
        if s[i] == 'a' and i < remainder:
            count2 += 1

    # Calculating total number of a's in the string
    total = count1*num_strs + count2

    return total

# Testing
print(repeatedString('aba', 10))

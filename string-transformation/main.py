#!/bin/python3

#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    # Variable for the final output
    transformed_sentence = ""
    
    # Iterate on each sentence's character
    for i in range(len(sentence)):
        current_char = sentence[i]
        previous_char = sentence[i - 1] if i > 0 else ""
        
        # Determine if the current and previous chars are alphanumeric
        if current_char.isalpha() and previous_char.isalpha():
            if current_char.lower() > previous_char.lower():
                transformed_sentence += current_char.upper()
            elif current_char.lower() < previous_char.lower():
                transformed_sentence += current_char.lower()
            else:
                transformed_sentence += current_char
        else:
            transformed_sentence += current_char
    
    return transformed_sentence
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()

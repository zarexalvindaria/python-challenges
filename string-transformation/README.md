# Python: String Transformation

There is a sentence that consists of space-separated strings of upper and lower case English letters. Transform each string according to the given algorithm and return the new sentence.

Each string should be modified as follows:

1. The first character of the string remains unchanged
2. For each subsequent character, say x, consider a letter preceding it, say y:
   - If y precedes x in the English alphabet, transform x to uppercase
   - If x precedes y in the English alphabet, transform x to lowercase
   - If x and y are equal, the letter remains unchanged
 
## Example

sentence = "coOL dog"

The first letters of both words remain unchanged. Then, for the word "coOL" the first "o" is made uppercase because the letter preceding it, "c", comes earlier in the alphabet. Next, the case of the second "O" is unchanged because the letter preceding is also "o", and finally the "L" is made lowercase because the letter preceding it, "O", comes later in the alphabet. The second word, "dOg", is transformed according to the same rules. Return the resulting sentence 'cOOl dOg'.
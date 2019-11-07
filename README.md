# JalapenoHotties
CS 4500 big project - Listener with Raspberry Pi


*******     prompt_user_for_rules.py     ************

It will ask user to input the words, phrases or patterns they want to look for.
- First program will start prompting user to input words they want to count separated by comma
    Example: sine, cosine, tangent, cotangent
  After accepting words, program will parse it by comma and validate that it does not exceed the maximum number of words
  We also have auto correct which will identify possible misspelled words and ask user if that word was misspelled, so they
  can change the word or keep it the way it is.
  
- Second program will prompt user to input phrases they want to count separated by comma
    Example: cosine and tangent, derivative of sine and so on
  After accepting phrases, program will parse it by comma and validate that it does not exceed the maximum number of words
  We also have auto correct which will identify possible misspelled words and ask user if that word was misspelled, so they
  can change the word or keep it the way it is.
  
- Third program will prompt user to input patterns they want to count separated by comma
    Example: cosine sine 2 15, derivative tangent 5 13
  After accepting patterns, program will parse it by comma and validate that it does not exceed the maximum number of words
  We also have auto correct which will identify possible misspelled words and ask user if that word was misspelled, so they
  can change the word or keep it the way it is.
  For lower bound and upper bound numbers it validates if input is actually a number or not.
  
After gathering all the data program will output to a file called "rules.txt"

****** check_against.py******

It will read rules.txt and check for specific pattterns in voice.txt 

-First part of program will take voice.txt and remove all extraneous symbols such as '/n' and '/'.  After removing these, it adds all the words in the file to the list to word_list. It also makes all words in the list lower case.  An array is also created that appends a zero for as many lines as there are in rules.txt.  The position of the zero on the list corresponds with the line number of rules.txt.

-The second part of the code splits the rules.txt into three cases:

Case 1: The line of rules.txt has only one word.  If this is the case, the program traverses the length of word_list looking for a match with this word.  When it finds a match, one is added to the position location that matches the line number where the single keyword was found.

Case 2: The line of rules.txt has three words, which are our phrases.  This will be two key words separated by one word.  The program searches the length of rules.txt for the first key term, then searches to see if the next word is in the next spot over in the list, then does the same for the second key word.  If this is all true, one is added to the position location that matches the line number where the single keyword was found.  

Case 3:  The line of rules.txt has four words, which are our patterns.  This will be two key words followed by a lower bound of words in between the two terms, and an upperbound of words between the two terms.  One is added to the upperbound and lowerbound so that the position is actually the amount of words the user desires.  If the program finds the first term in words_list, the program then searches for the second term.  If the second term is in a position that is in the range of the given lower bound and upper bound, a one is added to the position location that mactches the line nubmer where the single keyword was found.



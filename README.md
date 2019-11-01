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
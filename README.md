# JalapenoHotties - Raspberry Pi with the Listener
Computer Science 4250 - Software Profession

Implementing a listener onto the Raspberry pi, which detects an individual conversation, then analyze his/her speeches and output the statistics of the "influential" words. The application will provide counts of words, phrases, and patterns from the codebook as the statistics. The ultimate goal of this project is to achieve onboard offline capability.


## Requirement
- Raspberry Pi 3 Model B (or better)
	- CPU: 1.4GHz 64-bit quad-core ARM Cortex-A53 CPU
	- RAM: 1GB LPDDR2 SDRAM
	- WIFI: Dual-band 802.11ac wireless LAN (2.4GHz and 5GHz ) and Bluetooth 4.2
- Audio DAC HAT Sound Card Audio + Speaker + MIC (or better)
- Raspbian (operating system based on Debian optimized for the Raspberry Pi hardware)


## Installation
- Voice Engine
	- Download the file in the voiceEngine folder and follow the README instruction. 
- Make Codebook
	- Download the file in the codeBook folder and follow the README instruction. 
- Word Counter
	- Download the file in the wordCounter folder and follow the README instruction. 


## Make Codebook

It will ask the user to input the words, phrases or patterns they want to look for.

- First, the program will start prompting the user to input words they want to count separated by a comma.
    - Example: sine, cosine, tangent, cotangent
	- After accepting words, the program will parse it by comma and validate that it does not exceed the maximum number of words. We also have autocorrected which will identify possible misspelled words and ask the user if that word was misspelled, so they can change the word or keep it the way it is.
  
- Second, the program will prompt the user to input phrases they want to count separated by a comma
    - Example: cosine and tangent, derivative of sine and so on
	- We also have autocorrected which will identify possible misspelled words and ask the user if that word was misspelled, so they can change the word or keep it the way it is.
  
- Third, the program will prompt the user to input patterns they want to count separated by a comma
    - Example: cosine sine 2 15, derivative tangent 5 13
	- After accepting patterns, the program will parse it by comma and validate that it does not exceed the maximum number of words. We also have autocorrected which will identify possible misspelled words and ask the user if that word was misspelled, so they can change the word or keep it the way it is. For lower bound and upper bound numbers it validates if the input is a number or not.

After gathering all the data, it will output to a file called "rules.txt".


## Word Counter

It will read rules.txt and check for specific patterns in voice.txt 

- The first part of the program will take voice.txt and remove all extraneous symbols such as '/n' and '/'.  After removing these, it adds all the words in the file to the list to word_list. It also makes all words in the list lower case. An array is also created that appends a zero for as many lines as there are in rules.txt. The position of the zero on the list corresponds with the line number of rules.txt.

- The second part of the code splits the rules.txt into three cases:

    - Case 1: The line of rules.txt has only one word. If this is the case, the program traverses the length of word_list looking for a match with this word. When it finds a match, one is added to the position location that matches the line number where the single keyword was found.

    - Case 2: The line of rules.txt has three words, which are our phrases. This will be two keywords separated by one word. The program searches the length of rules.txt for the first key term, then searches to see if the next word is in the next spot over in the list, then does the same for the second keyword. If this is all true, one is added to the position location that matches the line number where the single keyword was found.  

    - Case 3: The line of rules.txt has four words, which are our patterns. This will be two keywords followed by a lower bound of words in between the two terms, and an upper bound of words between the two terms. One is added to the upper bound and lower bound so that the position is the number of words the user desires. If the program finds the first term in words_list, the program then searches for the second term. If the second term is in a position that is in the range of the given lower bound and upper bound, a one is added to the position location that matches the line number where the single keyword was found.


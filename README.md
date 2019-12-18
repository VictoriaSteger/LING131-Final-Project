# LING131-Final-Project
Repository for the LING131 Group Final Project
1. Upload the ebooks as text files to the github account - DONE
	1. Break up the Sherlock Holmes text file into individual stories - DONE
2. Do magic
	1. wordnet - get words to look for
	2. find sentences with those words - take the context?
		1. rule out false positives
		2. theta roles for each sentence - verbnet
		3. spacey - named entity recognition
	3. Review the results
		1. resolve any issues with pronouns - the most recent named entity?
	4. Create a test file
3. Install spacy (pip install spacy) 
    and en_core_web_sm (pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz)

4. Profit

ACTUAL TEXT ONCE WE'RE READY TO DELETE THE ABOVE:

For this project, we attempted to create a murder mystery spoilor generator, wherein you can input a murder mystery in the form of a .txt file and the program would return who the murderer is.

Packages needed for this project:
	1. nltk
	2. Spacey
	3. ?

In order to run this code, simply run "main.py". You will them be prompted to enter a file name - we have provided several text files for that purpose in the repository. The program will then return who it thinks the killer is, as well as how accurate it would be if it were randomly guessing the killer, rather than using our program. You will then be prompted if you want to check a second file. Once you are done checking all of the files you want, the program will then tell you how accurate the program was overall.

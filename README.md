For this project, we attempted to create a murder mystery spoilor generator, wherein you can input a murder mystery in the form of a .txt file and the program would return who the murderer is.

1. Packages needed for this project:
	1. nltk
	2. SpaCy

2. Resources needed for this project:
    1.en_core_web_sm -- installed by running "pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz"

In order to run this code, simply run "trial.py" - NOT "main.py". Main was used during the testing phase of the code (and trial does everything main currently does plus more). The program will then loop through all of the .txt files in the "data" folder, and for each story will tell you the list of suspects, list of potential victims, the most likely killer, and the most likely victim. At the end of the program, it will tell you how accurate our program is overall, and compare it to the accuracy of randomly selecting a killer and victim from the list of characters.

Not all of the files currently on github are used in the final product, but were used during the development of the code to test out ideas.

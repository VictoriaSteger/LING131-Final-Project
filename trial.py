import random

def testing(file, accused):
    
    if file == "The Adventure of Black Peter.txt":
        killer = ""
    elif file == "The Adventure of Black Peter.txt":
        pass
    elif file == "The Adventure of the Abbey Grange.txt":
        pass
    elif file == "The Adventure of the Bruce-Partington Plans.txt":
        pass
    elif file == "The Adventure of the Cardboard Box.txt":
        pass
    elif file == "The Adventure of the Crooked Man.txt":
        pass
    elif file == "The Adventure of the Dancing Men.txt":
        pass
    elif file == "The Adventure of the Devil's Foot.txt":
        pass
    elif file == "The Adventure of the Dying Detective.txt":
        pass
    elif file == "The Adventure of the Empty House.txt":
        pass
    elif file == "The Adventure of the Golden Pince-Nez.txt":
        pass
    elif file == "The Adventure of the Greek Interpreter - Question.txt":
        pass
    elif file == "The Adventure of the Norwood Builder.txt":
        pass
    elif file == "The Adventure of the Reigate Squire.txt":
        pass
    elif file == "The Adventure of the Resident Patient.txt":
        pass
    elif file == "The Adventure of the Silver Blaze.txt":
        pass
    elif file == "The Adventure of the Speckled Band.txt":
        pass
    elif file == "The Adventure of Wisteria Lodge.txt":
        pass
    elif file == "The Boscombe Valley Mystery.txt":
        pass
    elif file == "The Five Orange Pips.txt":
        pass
    elif file == "The Murder on the Links - Agatha Christie.txt":
        pass
    elif file == "The Musgrave Ritual - Question.txt":
        pass
    elif file == "The Mysterious Affair at Styles - Agatha Christie.txt":
        pass
    elif file == "The Secret Adversary - Agatha Christie.txt":
        pass
    elif file == "The Sign of the Four.txt":
        pass
    elif file == "The Valley of Fear.txt":
        pass
    else:
        print("File is not valid - you are the killer :)")
    
    if killer == accused:
        truth = 1
    else:
        truth = 0
    return truth
    
def bad_detective(people):
    rand = random.randint(0,(len(people)))
    definitely_the_killer = people[rand]
    return definitely_the_killer

def red_herring_sucess_rate(killer, people):
    truth = 0
    for i in range(100):
        definitely_the_killer = bad_detective(people)
        if definitely_the_killer == killer:
            truth += 1
    result = truth/100
    return result

def actual_success_rate(outcomes, num_tested):
    return outcomes/num_tested
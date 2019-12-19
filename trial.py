import random

def testing(file, accused):
    
    if file == "./The Adventure of Black Peter.txt":
        killer = ""
    elif file == "./The Adventure of Black Peter.txt":
        killer = ""
    elif file == "./The Adventure of the Abbey Grange.txt":
        killer = ""
    elif file == "./The Adventure of the Bruce-Partington Plans.txt":
        killer = ""
    elif file == "./The Adventure of the Cardboard Box.txt":
        killer = ""
    elif file == "./The Adventure of the Crooked Man.txt":
        killer = ""
    elif file == "./The Adventure of the Dancing Men.txt":
        killer = ""
    elif file == "./The Adventure of the Dying Detective.txt":
        killer = "Culverton Smith"
    elif file == "./The Adventure of the Empty House.txt":
        killer = ""
    elif file == "./The Adventure of the Golden Pince-Nez.txt":
        killer = ""
    elif file == "./The Adventure of the Norwood Builder.txt":
        killer = ""
    elif file == "./The Adventure of the Reigate Squire.txt":
        killer = ""
    elif file == "./The Adventure of the Resident Patient.txt":
        killer = ""
    elif file == "./The Adventure of the Silver Blaze.txt":
        killer = ""
    elif file == "./The Adventure of the Speckled Band.txt":
        killer = ""
    elif file == "./The Adventure of Wisteria Lodge.txt":
        killer = ""
    elif file == "./The Boscombe Valley Mystery.txt":
        killer = ""
    elif file == "./The Five Orange Pips.txt":
        killer = ""
    elif file == "./The Murder on the Links - Agatha Christie.txt":
        killer = ""
    elif file == "./The Musgrave Ritual - Question.txt":
        killer = ""
    elif file == "./The Mysterious Affair at Styles - Agatha Christie.txt":
        killer = ""
    elif file == "./The Secret Adversary - Agatha Christie.txt":
        killer = ""
    elif file == "./The Sign of the Four.txt":
        killer = ""
    elif file == "./The Valley of Fear.txt":
        killer = ""
    else:
        print("File is not valid - you are the killer :)")
    
    murderer = accused.split()
    if killer == accused or killer == murderer[0] or killer == murderer[1]:
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

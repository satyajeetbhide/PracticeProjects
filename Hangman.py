import sys
import random
import string

print ("Welcome to Steve's Hangman! ... Try not to die.");

_Dictionary = ['Welcome', 'human', 'hang'];
failedStr = "uRaDeadMan";

def create_dictionary():
    #read file and store all words in a list
    print("Creating dictionary from file \(placeholder\)");

def display_dictionary():
    for i in range(len(_Dictionary)):
        print(_Dictionary[i]);

def select_word():
    dictIndex = random.randrange(len(_Dictionary));
    return _Dictionary[dictIndex].lower();

def find_all_guessedLetter_indices(question, guessedLetter):
    hit = question.find(guessedLetter);
    locations = [];
    while (hit != -1):
        locations.append(hit);
        hit = question.find(guessedLetter,hit+1);

    return locations;

def play_Hangman():
    question = select_word();
    print("Alright let's go...\n"+len(question)*' _ ');
    #print("Hint: "+question);

    tries = 0;
    guessedLetters = 0;
    incompleteAnswer = len(question)*"*";

    while(guessedLetters < len(question) and tries < 10) :
        guessedLetter = input("Guess a letter:\t");
        guessedLetter = guessedLetter.strip();
        tries += 1;

        if(len(guessedLetter)!=1):
            print("One letter at a time please .. take another shot");
            print(incompleteAnswer.replace('*',' _ '));
            continue;

        if(incompleteAnswer.find(guessedLetter)!=-1):
            continue; #user has already successfully guessed this letter, so all occurences of it are already filled into the incompleteAnswer

        if(question.find(guessedLetter) != -1):
            hits = find_all_guessedLetter_indices(question,guessedLetter);
            for i in hits:
                incompleteAnswer = incompleteAnswer[:i]+guessedLetter+incompleteAnswer[i+1:];
            guessedLetters = guessedLetters+len(hits);
        else:
            print("Wrong guess ... "+ failedStr[:tries]);
        print (incompleteAnswer.replace('*',' _ '));

    if (guessedLetters == len(question)):
        print("\nNicely done!");
    else:
        print("You Sir, are Dead! What a pity :(");

def main():
    #create_dictionary();
    #display_dictionary();
    gameOn = 'y';

    while (gameOn == 'y'):
        gameOn = input("\nUp for a new game? <y/n>: ");

        if (gameOn == 'y'):
            play_Hangman();
        else:
            print("\n\n\nHave a Good Day :)");

if __name__ == "__main__" :
    main();

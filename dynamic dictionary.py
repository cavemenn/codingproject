'''
Write a program that will allow the user to:
1) Add new definitions
2) Search existing definitions
3) Delete the definition that he has chosen

Since need to add and delete definition, list in dict tor dict in dict can be used
I think dict in dict is the way to go but lets see (i was correct haha)
'''
dictionary = {}
import time
#meni
while (True):
    print('Hello! This is a dictionary that allows you to add new definitions, search existing definitions and delete definitions')
    print('/')
    print('What would you like to do? ')
    print('Add (+), Search(=), Delete (-) & Press 4 to end program')
    askuser = input('Enter your desired function: ')

    if (askuser == '+'):
        word = input('Whats the word you would like to define? ')
        definition = input('Enter definition: ')
        dictionary[word] = definition
        print('Definition has been added!')
        print(dictionary)
        time.sleep(3)
    elif (askuser == '='):
        word = input('Whats the word you would like to know the definition to? ')
        if word in dictionary:
            print(word,':',dictionary[word])
        else:
            print('Definition has not been found :(')
        time.sleep(3)
    elif (askuser=='-'):
        word = input('What word would you like to delete? ')
        if word in dictionary:
            dictionary.pop(word)
            print(word,'has been deleted!')
        else:
            print( word, 'does not exist!')
        time.sleep(3)
    elif (askuser == "4"):
        print('Bye!')
        break
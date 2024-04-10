#Working with Lists
def prompt_user() -> bool:
    while True:
        keepLoop = input('Continue(Y/N)? ')
        if keepLoop == 'y' or keepLoop == 'Y':
            return True
        elif keepLoop == 'n' or keepLoop == 'N':
            return False 
        else:
            continue
    
def main():
    strings = []

    while True:
        word = input('Enter word: ')
        strings.append(word)
    
        if prompt_user() == False:
            break
        else:
            continue

    print(strings)

main()
        
    

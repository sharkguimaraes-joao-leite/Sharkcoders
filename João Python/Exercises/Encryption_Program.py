import string

#Variables
chara = string.punctuation + string.digits + string.ascii_letters + " "
chara = list(chara)
asking = True
incrypting = True

key = ['W', 'O', 'b', 'R', 'E', ' ', 'N', '-', ')', '7', '`', 'D', 'T', '.', ':', '6', 'f', 'Y', '\\',
       'X', '_', '[', 'v', 'o', 'H', '&', 'P', ']', '8', '~', 'Z', "'", 'e', '3', '!', 'V', 'x', '"',
       'c', 'u', '$', 'C', '^', 'K', 'I', 'd', 'j', '?', '4', '/', 'p', 'Q', '=', 'q', ';', '|', '(',
       'G', 'a', 'F', '<', '>', 'y', 'M', '5', 'z', 'k', 'B', '{', 'L', '%', '}', 'l', 'A', '1', '@',
       'i', 't', '+', 'U', 'h', 'r', 'g', 's', '2', '9', 'm', ',', '#', 'S', '0', 'w', '*', 'n', 'J']

word = ""
cipher_word = ""

#Main Code
while incrypting:
    asking = True
    print("************")
    print("1. Incrypt")
    print("2. Unincrypt")
    print("************")
    act = input("What would you like to do?: ")
    print("--------------------------------------")
    if act == "1":
        word = input("What message would you like to incrypt?: ")
        print("--------------------------------------")
        for letter in word:
            index = chara.index(letter)
            cipher_word += key[index]
        print(f"Incrypted word: {cipher_word}")
        print("--------------------------------------")
        word = ""
        cipher_word = ""
    elif act == "2":
        cipher_word = input("What message would you like to unincrypt?: ")
        print("--------------------------------------")
        for letter in cipher_word:
            index = key.index(letter)
            word += chara[index]
        print(f"Unincrypted word: {word}")
        print("--------------------------------------")
        word = ""
        cipher_word = ""
    else:
        print("Not an option!")
        print("--------------------------------------")
    while asking:
            incrypt = input("Do you need anything un/incrypted again (y/n)?: ").lower()
            print("--------------------------------------")
            if incrypt == "y":
                print("Hell yeah!")
                asking = False
                print("--------------------------------------")
            elif incrypt == "n":
                print("Ok...")
                print("--------------------------------------")
                asking = False
                incrypting = False
                break
            else:
                print("Type y or n, asshole!")
                print("--------------------------------------")
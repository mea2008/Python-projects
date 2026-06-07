# This program will encrypt your message and decrypt your message.
import string
import random
import pyperclip


def generate_key():
    # This consists of all the ASCII characters from the string module
    initial = string.printable

    # Here we typecast the string into a list so the items can be randomized
    initial = list(initial)

    # Then we remove some problematic items from the list 
    initial.remove("\x0b")
    initial.remove("\x0c")
    initial.remove(" ")
    initial.remove("\r")

    # Next we make a copy of the list
    key = initial.copy()


    # Now we use the random.shuffle function to shuffle all the entries of the copy
    random.shuffle(key)

    return initial, key


def encrypt_message():
    current = input("Enter the text to be encrypted: ")
    current_list = list(current)

    # Creating a copy of the original message
    current_working = current_list.copy()

    # This loop will replace all the items' indexes in the given list with the indexes
    # of the corresponding items from the initial list
    for i in range(len(current_working)):
        if current_working[i] in initial:
            current_working[i] = initial.index(current_working[i])

    # This loop will replace all the items in the given list with the items
    # of matcing indexes from the key list
    for i in range(len(current_working)):
        for j in range(len(key)):
            if current_working[i] == key.index(key[j]):
                current_working[i] = key[j]

    # Convert it back to a string
    current_encrypted = "".join(current_working)
    return current_list, current_working, current, current_encrypted


def decrypt_message():
    # Decrypting the message
    current_decrypting = input("Enter the message to decrypt: ")
    current_decrypting_list = list(current_decrypting)

    # This loop will replace all the items' indexes in the given list with the indexes
    # of the corresponding items' indexes from the "key" list
    for i in range(len(current_decrypting_list)):
        if current_decrypting_list[i] in key:
            current_decrypting_list[i] = key.index(current_decrypting_list[i])

    # This loop will replace all the items in the given list with the items
    # of matcing indexes from the "initial" list
    for i in range(len(current_decrypting_list)):
        for j in range(len(initial)):
            if current_decrypting_list[i] == initial.index(initial[j]):
                current_decrypting_list[i] = initial[j]

    current_decrypted = "".join(current_decrypting_list)
    return current_decrypting_list, current_decrypted


print("Welcome to the Encryption/Decryption program."), input()
initial, key = generate_key()
print("A random key has been generated."), input()
i = 1
while i == 1:
    ("\nSelect one of the following options:\n")
    print(
        "Select one of the options.\n1. Encrypt a message\n2. Decrypt a message\n3. Look at the current key\n4. Copy the current key\n5. Generate a new key\n6. Enter a custom key\n7. Stop the program"
    )
    choice = input("\nYour choice (1/2/3/4/5): ")

    if choice == "1":
        (current_list, current_working, current, current_encrypted) = encrypt_message()
        print(f"Your encrypted message is : {current_encrypted}")
        input()
    elif choice == "2":
        current_decrypting_list, current_decrypted = decrypt_message()
        print(f"The decrypted message is : {current_decrypted}")
        input()
    elif choice == "3":
        print(f"Your current key is : \n{key}\n"), input()
    elif choice == "4":
        key_copy = str(key)
        pyperclip.copy(key_copy)
        print("The key has been copied to the clipboard!")
        input()
    elif choice == "5":
        initial, key = generate_key()
        print("A new key has been generated!"), input()
    elif choice == "6":
        print(
            "Paste your custom key (to use the same key, cop\nMAKE SURE IT IS IN THE RIGHT FORMAT : ['a','b','c','d'] OR ELSE ERRORS MAY OCCUR"
        )
        custom_input = input()
        key = eval(custom_input)
        print("\nCustom key entered!"), input()
    elif choice == "7":
        print("\nGoodbye :)")
        i = 0, input()
    else:
        print(f"your choice was wrong."), input()

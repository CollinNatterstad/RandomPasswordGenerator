def main():
    #importing necessary libraries.
    
    import random, string
    
    #getting user criteria for password length
    
    password_length = int(input("How many characters would you like your password to have? "))
    
    #creating an empty list to store the password inside. 

    password = []
    
    #establishing what characters are allowed to be chosen.
    password_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits 

    #for loop to iterate over the password_length choosing a character at random from the pool of choices in password_characters.
    for x in range (password_length):
        password.append(random.choice(password_characters))

    #printing the password to the terminal. 
    print("".join(password))



if __name__ == "__main__":
    main()
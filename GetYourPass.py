#This is a Password generator
#It will provide the user a randomly generated alphanumerical password of desired size

#we import "string" function/file
import string 
#we import "random" functon/file
import random 

#contents for generating the password
alphabet = string.ascii_letters 
digit = string.digits
symbols= "!@#$%^&*()_"
contents = list(alphabet + digit + symbols) 

 # variable for storing the password
password=[]

print('Welcome to Password Generator developed by Fardin Inc.')
#Gather the name of the user
user = str(input('Enter your name:')) 
#Extra information (not mandatory)
student_ID=str(input('Enter your Student ID: ')) 

#A normal greeting
print('Hello ' + user +'('+student_ID +')' + ', Welcome to Password Generator!') 

#Gather the desired size of password
length = int(input('Enter the length of password:')) 


 
#Providing the range of the length of password
if length>7 and length<65:
        #Gathers the number of alphabets the user desires
        alph_count=int(input('How many alphabets would you like? :')) 
        #Gathers the number of digits the user desires
        digit_count=int(input('How many digits would you like? :')) 
        #Gathers the symbols of digits the user desires
        sym_count=int(input('How many symbols would you like? :')) 
    
        total_count= alph_count + digit_count + sym_count
        
        #The Character count has to be less than the desired length of the user
        if total_count > length: 
                print('Character count cannot be greater than Length of password')
        
                    
        else:
                
                #randomly arranging the combinations
            for i in range(alph_count):
                    password.append(random.choice(alphabet))
                    
            for i in range(digit_count):
                    password.append(random.choice(digit))
                    
            for i in range(sym_count):
                    password.append(random.choice(symbols))
                    
        #Shuffling the remaining combination due to extra slots            
        if total_count< length:
                random.shuffle(contents)
            
                for i in range(length - total_count):
                    password.append(random.choice(contents))
                
                
        #Randomly Shuffles the elements for password
        random.shuffle(password) 
        
        #Extra Addition
                        
        print('Your password is generating...') 
        
        #Converting the list into string and then printing the list
        print('Here is your password: ' + "".join(password))  #The password is printed
        
        #Social Awareness message
        print('**Do not share your password with anyone due to security reasons.**') 
        
        #Ratings 
        review= input('Please leave a rating on a scale of 1-5: ')
        print('Your review has been saved in our database for improvising. Thank you.')
elif length <8 : 
        print('Password has to be of at minimum 8 characters')
elif length > 64: ##Providing the range of the length of password
        print('Password can be of maximum 64 characters')
else:
    print("None")

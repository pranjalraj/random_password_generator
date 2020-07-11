import string
import random
if __name__ == "__main__":
    print("Welcome to password generator. Help us build your password by answering the following questions with a y or n (lowercase)")
    a=input("Do you want lowercase letters in your password?")
    b=input("Do you want uppercase letters in your password?")
    c=input("Do you want numerical digits in your password?")
    d=input("Do you want punctuation marks in your password?")
    if a=="y":
        s1=string.ascii_lowercase
    else:
        s1=""
    if b=="y":
        s2=string.ascii_uppercase
    else:
        s2=""
    if c=="y":
        s3=string.digits
    else:
        s3=""
    if d=="y":
        s4=string.punctuation
    else:
        s4=""
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    plen=int(input("Enter the length of your password: "))
    print("".join(s[0:plen]))

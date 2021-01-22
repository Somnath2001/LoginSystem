import os
import time
print("Welcome To login Program Created by Somnath12")
time.sleep(1)
print('')
print("Verifying That You're Not A Robot ....")
time.sleep(1)
print("Checking For Manual Verification...")
time.sleep(2)
print("Robot Detected !!!!")
time.sleep(3)
print("Manual Verification Nedded !!!")
time.sleep(1)
print("Type 1 To Solve Verification")
Choice = int(input("Enter Here : "))
Author = 'PROGRAMME by 12'
a = []
if Choice == 1:
  name = input("Enter Your Fullname Name :\n")
  email = input("Enter Gmail Without @gmail.com : \n")
  while(1):
    password = input("Enter Your Password : ")
    if len(password) < 8:
      print("Password Must Be More Than 8 Character")
      continue
    elif len(password)> 8:
      pass1 = input("Enter your password again : ")
      if password==pass1:
        print("Account Created Successfully ")
        a.append(email + '@gmail.com')
        a.append(password)
        print("Type 1 To Login")
        Log = int(input(""))
        if Log == 1 :
          print("Enter Your Gmail Without @gmail.com")
          Gm = str(input(""))
          ps = input("Enter Your Password : ")
          if Gm and ps in a:
            print("Login Successful")
            time.sleep(1)
            print("Coded By", Author)
            time.sleep(1)
            while(1):
              print('Do You Want To Hack Your Own Password???')
              print('If Yes Type Y Else Type Any Other Alphabet')
              passwd = str(input('Enter Here >>> '))
              if passwd == 'Y' or 'y':
                print('Wait !!!!')
                time.sleep(1)
                print('Checking DataBase ...')
                time.sleep(2)
                print('Database Fetched !!!')
                time.sleep(1)
                print('Decompiling DataBase .....')
                time.sleep(3)
                print('Decompile Successful |_|')
                time.sleep(1)
                print('Getting Names ')
                print('Searching For Your Gmail')
                time.sleep(2)
                print('Gmail Found !')
                time.sleep(2)
                print('Getting Password !')
                time.sleep(2)
                print('Password Found !')
                time.sleep(1)
                print('Your Gmail And Password Is {}'.format(a))
                break
              else:
                  exit
            
          else :
            print("Gmail Or Password Incorrect")
            print("Create Password Again")
      else:
        print("Password Not Matched")
        print("Enter Your Password Again")
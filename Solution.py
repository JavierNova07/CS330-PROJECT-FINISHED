def main():
    number=0
    unlock='232361'
    lock='232364'
    exitOut='000000'
    print("The system is locked")
    sw=True
    while sw:
        try:
            number=input("Enter the code to unlock or lock the system, to exit press 000000 ")
            validatedInput=checkInput(number)
            if validatedInput:
                if unlock in str(number):
                    print("System unlocked")
                elif lock in str(number):
                    print("System locked")
                elif exitOut in (str(number)):
                    sw=False
        except ValueError:
            print("Must be an integer and between 0-9, to exit enter 70")
def checkInput(digits):
    counter=0
    if digits.isnumeric():
        for digit in digits:
            counter+=1
        if counter==6:
            return True
        else:
            return False
    else:
        return False
    
      
  
main()
#913520451033444232364
#print(i)
#913520334412451033444123970001112334451334410101
'''The keypad has ten keys, labeled from '0' to '9'.
The security engine will unlock the lock when it finds the correct
un-locking access code in the input string. Likewise, the security engine will
lock the lock when it finds the correct locking access code in the input string.

For example, let's assume that the un-locking code is 33441. If the user
enters the string 91352033441245, then the lock will be unlocked as soon as
the engine finds the last correct letter of the access code in the input string.
The engine will lock the lock again when the user enters the locking code.
Assuming that the locking code is 33444 then the lock will be locked and unlocked as described below:'''


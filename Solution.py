def main():
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




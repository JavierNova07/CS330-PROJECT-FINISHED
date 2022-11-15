import random
def main():
    number=23236
    unlock=232361
    lock=232364
    exitOut=000000
    count=0
    sw=True
    while sw:
        try:
            option=input(" Press enter 1 to generate random code or 000000 to exit ")
            if exitOut == int(option):
                sw=False
            elif option == '1':
                option = str(number)+str(random.randint(0, 9))
            
                if unlock == int(option):
                    print("System unlocked after " + str(count) + " digits." )
                else:
                    count += 6
              #elif lock == int(option):
               #     print("System locked")
                #    count+=1
        except ValueError:
            print("Wrong entry")


'''def checkInput(digits: str):
    counter = 0
    if digits.isnumeric():
        for digit in digits:
            counter += 1
        
        if counter == 6:
            return True
        else:
            return False
            
    else:
        return False'''

  
main()

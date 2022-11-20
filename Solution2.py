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
            elif int(option)<=0:
                print("Wrong entry")
            elif option == '1':
                option = str(number)+str(random.randint(0, 9))
            
                if unlock == int(option):
                    print("System unlocked after " + str(count) + " digits." )
                    print("Avererage is: ",count/int(option))
                    print("Minimum number of tries is 1: ")
                else:
                    count += 6
        except ValueError:
            print("Wrong entry")


  
main()

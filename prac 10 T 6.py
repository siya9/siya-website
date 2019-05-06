#import tester                                    #import tester module, remove comment hash-tag to test

def sayIt(inp):                                 #create function converting numbers into words
    n = ""                                 #initialize value to be output as words
    if(inp == "0"):                                 #check if the number is zero 
        n = " zero"
        inp = ""                                 #change number to empty quotes to prevent entering the loop
    while(inp != ""):
        if(inp[0] == "-"):                                 #checking if the number is negetive
            n=n+" minus"                                 #if negative change n to minus
            inp = inp[1:]                                 #read input number from next digit
            continue                                 #repeat loop without finishing
        elif(inp[0] == "1" and len(inp)!=2):
            n=n+" one"            
        elif(inp[0] == "2" and len(inp)!=2):
            n=n+" two"            
        elif(inp[0] == "3" and len(inp)!=2):
            n=n+" three"            
        elif(inp[0] == "4" and len(inp)!=2):                                 #....write first index
            n=n+" four"                                                     #of input number in words....
        elif(inp[0] == "5" and len(inp)!=2):
            n=n+" five"            
        elif(inp[0] == "6" and len(inp)!=2):
            n=n+" six"            
        elif(inp[0] == "7" and len(inp)!=2):
            n=n+" seven"            
        elif(inp[0] == "8" and len(inp)!=2):
            n=n+" eight" 
        elif(inp[0] == "9" and len(inp)!=2):
            n=n+" nine"
            
        if(len(inp)==4):
            n = n +" thousand"            
        elif(len(inp)==3 and inp != "000"):                              #check if hundred value is not zero 
            if(inp[1] == "0" and inp[2] == "0"):
                n = n +" hundred"                                       
            else:
                n = n +" hundred and"            
        elif(len(inp)==2 and inp[0]=="1"):                                 #....for last 2 digits starting with 1
            if(inp == "10"):                                              #assign values and assign empty quotes to input to exit loop
                n=n+" ten"
                inp = ""
            elif(inp == "11"):
                n=n+" eleven"
                inp = ""
            elif(inp == "12"):
                n=n+" twelve"
                inp = ""
            elif(inp == "13"):
                n=n+" thirteen"
                inp = ""
            elif(inp == "14"):
                n=n+" forteen"
                inp = ""
            elif(inp == "15"):
                n=n+" fifteen"
                inp = ""
            elif(inp == "16"):
                n=n+" sixteen"
                inp = ""
            elif(n == "17"):
                n=n+" seventeen"
                inp = ""
            elif(inp == "18"):
                n=n+" eighteen"
                inp = ""
            elif(inp == "19"):
                n=n+" nineteen"
                inp = ""
        elif(len(inp)==2):
            if(inp[0] == "2"):
                n=n+" twenty"
            elif(inp[0] == "3"):
                n=n+" thirty"
            elif(inp[0] == "4"):
                n=n+" forty"
            elif(inp[0] == "5"):
                n=n+" fifty"
            elif(inp[0] == "6"):
                n=n+" and sixty"
            elif(inp[0] == "7"):
                n=n+" seventy"
            elif(inp[0] == "8"):
                n=n+" eighty"
            elif(inp[0] == "9"):
                n=n+" ninety"
            
        inp = inp[1:]
    print(n[1:])
    #return n[1:]                                 #remove comment hash-tag tags to test
    
def main():
    number = input("Please enter a number: ")
    sayIt(number)
    
#    tester.TestEq (sayIt, ["0"], "zero")
#    tester.TestEq (sayIt, ["1"], "one")
#    tester.TestEq (sayIt, ["-1"], "minus one")
#    tester.TestEq (sayIt, ["9"], "nine")
#    tester.TestEq (sayIt, ["-8"], "minus eight")
#    tester.TestEq (sayIt, ["10"], "ten")
#    tester.TestEq (sayIt, ["-11"], "minus eleven")
#    tester.TestEq (sayIt, ["100"], "one hundred")
#    tester.TestEq (sayIt, ["-101"], "minus one hundred and one")
#    tester.TestEq (sayIt, ["999"], "nine hundred and ninety nine")
    
    
if(__name__=="__main__"):
    main()

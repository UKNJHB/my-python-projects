import time
import os
def clean():  
    os.system("cls" if os.name=="nt"else os.system("clear"))
def Currency():  
    print("""

                       Welcome to currency converter
   ||====================================================================||
   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
   ||(100)==================|    Badr Ben Rabbar   |================(100)||
   ||\\$//        ~         '------========--------'                \\$//||
   ||<< /        /$\              // ____ \\                         \ >>||
   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
   ||<<|        \\ //           || <||  >\  ||                        |>>||
   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================|    Badr Ben Rabbar   |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||
___________________________________________________________________________
          

""")
    time.sleep(1)
    creency_convert={
        'USA':1.0,   
        'EUR':0.85,
        'EGP':30.9,
        'RMB':6.5,
        'DH' :10, 
}
    for key in creency_convert:
        print(f"{key}: {creency_convert[key]}")
    return creency_convert
def convert(currency,choose_crrency,creency_convert):     
     return creency_convert[choose_crrency]/creency_convert[currency]

while True:
        clean()
        creency_convert = Currency()
         
        currency=input('Choose a currency to convert from: ').upper()
        while True: 
            amount=float(input('Enter the amount: '))
            if input(f'You entered {amount} {currency}. confirm? y/n: ').lower()=='y':
                 break
        clean()
        print("\n".join(f"{key}: {creency_convert[key]}" for key in creency_convert))

        choose_crrency=input('Choose a currency to convert to: ').upper()
        print('\nAnalyzing your request... Please wait.\n')
        
        time.sleep(3)
        print(f"Checking for {choose_crrency}'s best rates available... Please wait. \n")
        time.sleep(2)
        print(f"Getting a discount price for {currency}.... Please wait.\n")
        time.sleep(3)
        if currency not in creency_convert or choose_crrency not in creency_convert:  
            print(f"Invalid currency. Conversion canceled. ")
            time.sleep(2)
            clean()
            continue
        clean()
        print(f"\nPreparing the deal from {currency} to {choose_crrency}.... Please wait.")
        time.sleep(3)

        rate=convert(currency,choose_crrency,creency_convert)
        
        print(f"Exchange Rate: 1 {currency}= {rate} {choose_crrency} \n")
        print(f"{amount} {currency} is equal to {round(amount* rate,2)} {choose_crrency} ")

        if input("Do yo accept this transaction? (y/n): ").lower()=='y':
            time.sleep(1)
            print("Transaction completed successfully.\nThank you for using our service.")
            break
        else:
            print("Transaction canceled.\n")
            if input("Do you want to perform another conversion? y/n: ").lower()!='y':
                print("Thank you for using our service.")
                break



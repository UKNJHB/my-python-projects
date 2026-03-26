import time
def greet():
    print("hello")
    time.sleep(2)
    if(input('do you want to do it again; y/n: '))=='y':
        greet()#code here repet 
    else:
        print('exiting...')
greet()
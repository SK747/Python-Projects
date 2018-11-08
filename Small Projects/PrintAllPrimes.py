# Simple print prime number script I wrote when first learning Python

pip3 install keyboard

import time
import keyboard

def PrintPrimes():
    """Prints Prime Numbers until told key 'n' is pressed"""
    print ('Press n to stop printing Prime numbers!')
    primes = []
    i = 2
    f = 0
    keep_printing = True
    
    while keep_printing:
        
        if i == 2:
            i = i + 1
            print('2', end=" ")
            primes.append(2)
            
        else:
            for j in primes:
                if i % j == 0:
                    f = f + 1
                    
            if f == 0:
                print(i, end=" ")
                primes.append(i)
                
        i = i + 2
        f = 0
        time.sleep(0.1)
        
        if keyboard.is_pressed('n'):
            keep_printing = False
            print ('Program has stopped')
            

PrintPrimes()

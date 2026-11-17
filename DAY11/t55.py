#wap to simulate to simulate a digital lock system.
#thelock should ask the user to engter 4c digit pins.if entered pin doesnt conataon exacatly 4 digotls. the program shpuld display an error msg and ask again .if the pin enterred is correcr, the lock should open. otherwise the proram sgould ask the user to try again .   

c_p = "0603"

while True:
    pin = input("Enter ur 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("Error!")
        continue

    if pin == c_p:
        print("Correct PIN! LOCK OPENED!")
        break
    else:
        print("Try again.")
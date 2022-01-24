import socket #socket
import signal
import sys
import datetime

ct = datetime.datetime.now()


totalAns = "0"
price = 0

socket = socket.socket() # socket declaration
host = '192.168.178.6' # server ip address
port = 8888 # port number 
unicode = "utf-8" #Unicode Transformation Format
bufferSize = 2048 #buffersize

print('[*] Waiting for connection from kitchen.....')

try:
        socket.connect((host, port))

except socket.error as e:
        print(str(e))

try:
        file = open(r'sales.txt', 'r')

except :
        file = open(r'sales.txt', 'w')
        file.write('Sales Record \n')
        file.close()
        file = open(r'sales.txt', 'r')

file = open(r'sales.txt', 'a') # append file sales.txt
file1 = open('menu.txt')# open menu.txt file
listM = file1.read() #listM will read from menu.txt

Response = socket.recv(bufferSize)  # get data from server
print(Response.decode(unicode)) # print response if get data

while True:
    
    print(listM)#print text from menu.txt file 
    
    opt = input('\nEnter your choice : \n> ') # client will enter choice
    if opt == "A" or opt == "B" or opt == "C" or opt == "D" or opt == "E" or opt == "F" or opt == "G": 
        qty = input("\nQuantity per Order: ") # client input quantity
        prc = '0.00' #str
        price = 0.00 #int
 
        ServerData = opt + ":" + qty + ":" + prc #serverdata will contain option, quantity and price data
        socket.send(str.encode(ServerData)) # send serverData data to server
        
        price = socket.recv(bufferSize) #get data from derver
        price = price.decode(unicode) #encoding data to original data
        price = str(price) #set price as str
        food = socket.recv(bufferSize) #get data from sever
        food = food.decode(unicode) #encoding data to original data
        quantity = int(qty) #set quantity as int

        #free gift choice 
        add = input('\nFree Gift For Opening  (Y/N): ')
        if add == "Y":
         sideAdd = input('We have [A]Tissue | [B]Thermos | [C]T-shirt\nInput your choice (A/B/C): ')

         if sideAdd == "A":
          add = "Tissue \n"
          

         elif sideAdd == "B":
          add = "Thermos \n"
          

         elif sideAdd == "C":
          add = "T-shirt \n"
          
         else:
          print( "Wrong Free Gift!!!")
          break

        else:
         add = "No Free Gift\n"

       
        
        #type selection
        dine = input('\nPlease select: - [A]Take away  [B]Dine in: ')
        if dine == "A":
           type= "Take Away\n"
           name = input('\nEnter your name: ')
           number = input('\nEnter your phone number: ')
           print("Total to Pay: RM " + str(price))

        elif dine == "B":
           type= "Dine in \n"
           name = input('\nEnter your name: ')
           number = input('\nEnter your meja: ')
           print("Total to Pay: RM " + str(price))
          
           
        else:
           print( "Wrong Input!!!")
           break

        ServerData1 = dine  #serverdata will contain option, quantity and price data
        socket.send(str.encode(ServerData1)) # send serverData data to server
        
        socket.send(str.encode(number)) # send serverData data to server
        seluruh = socket.recv(bufferSize) #get data from derver
        seluruh = seluruh.decode(unicode) #encoding data to original data
        
        print("\nSTRAW HAT CAFE\n")
        print("\n\t\t\t*********RECEIPT*********\n")
        print("\t\t\tNAME: " + name)
        print("\t\t\tNUMBER: " + number)
        print("\n\t\t\tFOOD: " + food)
        print("\t\t\tQUANTITY: " + str(quantity))
        print("\t\t\tFREE GIFT: " + add)
        print("\t\t\tTYPE: " + type)
        print("\t\t\tTotal to Pay: RM " + str(price) + "\n")
        print("\n\t\t\t*********THANK YOU*********\n")

    elif opt == 'Q':
        totalAns = str(totalAns) + str(price)
        print ("Total Sales For", ct, end = "\tRM:")
        print (seluruh)
        print(r"""
               ----------------------------------
               -           THANK YOU            -
               ----------------------------------
               """)
        break

    else:
        print("[*]Sorry you enter the wrong input... please try again")
        break

write = '\n' + name + '| ' + str(food) + '| ' + str(quantity) + '|  ' + str(add) + '| ' + str(type) + '| ' + str(number) + '| ' + str(price) + '\n'
file.write(write)
file.close#close file

socket.close()#close socket

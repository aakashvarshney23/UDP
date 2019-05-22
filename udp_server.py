def calculate_in(number):
    updated = [i for i in number.split(",")]
    flag = True
    for items in updated:
        if not items.isdigit():
            if items.startswith("-"):
                if not items[1:].isdigit():
                    flag = False
            else:
                flag = False

    if flag == False:
        return "Invalid"

    updated = [int(i) for i in updated]
    new_list = updated[1:]
    if updated[0] != len(new_list):
        return "Invalid Length"
    result = (
    "Max: ", max(new_list), "Min: ", min(new_list), "Mean: ", float(sum(new_list) / len(new_list)),
    "Total: ",
    sum(new_list))
    result = str(result)
    return result
    
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

while True:
    numbers, clientAddress = serverSocket.recvfrom(2048)
    result = str(calculate_in(numbers.decode()))
    serverSocket.sendto(result.encode(), clientAddress)












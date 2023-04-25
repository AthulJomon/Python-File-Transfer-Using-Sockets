import socket
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(),4571))
    
    with open('./recv_image.jpg','wb') as image_file:
        while True:
            data=s.recv(40960)
            if not data:
                print('No messages from the server. Closing the connection..')
                break
            image_file.write(data)
            print('Batch of data is written to the file succesfully')
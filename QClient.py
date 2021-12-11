#Client code
import socket

#IP = socket.gethostbyname(socket.gethostname())
IP="192.168.0.108"
PORT =4456
SIZE=1024

ADDR =(IP,PORT)
types = { "vedio":".mp4","audio":".mp3","image":".jpg","text":".txt","Ccode":".c","PythonCode":".py"}
pathtxt="C:\\Users\\p vijay\\Desktop\\Client\\clt.txt"
pathc="C:\\Users\\p vijay\\Desktop\\Client\\clt.c"
pathpy="C:\\Users\\p vijay\\Desktop\\Client\\clt.py"
pathimg="C:\\Users\\p vijay\\Desktop\\Client\\clt.jpg"

pathvedio="C:\\Users\\p vijay\\Desktop\\Client\\clt.mp4"
pathaudio="C:\\Users\\p vijay\\Desktop\\Client\\clt.mp3"
path="C:\\Users\\p vijay\\Desktop\\Client\\"

paths={"text":pathtxt , "Ccode":pathc , "PythonCode":pathpy , "image":pathimg , "video":pathvedio}

def main():
    
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)
   

    client.send("Receive Data".encode("utf-8"))
    
    function=input("Enter input to send or receive : ")
 
    client.send(function.encode("utf-8"))
    if function=="send":
        print("Files that can be sent are .txt , .c , .py")
        print("Enter text (For text file) , Ccode (For C program file) , PythonCode (For python program file)")
        type=input("Enter what type of file required to send : ")
        if type=="text" or type=="Ccode" or type=="PythonCode":
            
            client.send(type.encode("utf-8"))
            pathnow=paths[type]
            file=open(pathnow,"r")
            data=file.read();
            name1="clt"+types[type]
            client.send(name1.encode("utf-8"))
            msg4=client.recv(SIZE).decode("utf-8")
            print(f"[SERVER] {msg4}")
            client.send(data.encode("utf-8"))
            
            print("File Name ",file," Sent")
            
    if function=="receive":
        
        print("Enter text( For Text file) ,cCode(For C program) , PythonCode(For Python program) ,\n video(For Video file) , audio(For Audio file) , image(For Image file)")
        type=input("Enter what type of input file required : ")
        if type=="image":
            client.send(type.encode("utf-8"))
            print("Image")
            
            k=client.recv(SIZE).decode("utf-8")
            print(f"[SERVER] {k} ")
            select=input("Enter a file : ")
            client.send(select.encode("utf-8"))
            npath=path+select+".jpg"
            file=open(npath,'wb')
            data_in=client.recv(1024)
            while data_in:
                file.write(data_in)
                data_in=client.recv(1024)
            print("Recevd")
            file.close()
                
        if type=="video":
            client.send(type.encode("utf-8"))
            print("video")
            
            k=client.recv(SIZE).decode("utf-8")
            print(f"[SERVER] {k} ")
            select=input("Enter a file : ")
            client.send(select.encode("utf-8"))
            npath=path+select+".mp4"
            file=open(npath,'wb')
            data_in=client.recv(1024)
            while data_in:
                file.write(data_in)
                data_in=client.recv(1024)
            if data_in==0:
                print("file recieved")
            print("Recevd")
            file.close()
            print("Recevd")
            
        if type=="audio":
            client.send(type.encode("utf-8"))
            print("audio")
            
            k=client.recv(SIZE).decode("utf-8")
            print(f"[SERVER] {k} ")
            select=input("Enter a file : ")
            client.send(select.encode("utf-8"))
            npath=path+select+".mpeg"
            file=open(npath,'wb')
            data_in=client.recv(1024)
            while data_in:
                file.write(data_in)
                data_in=client.recv(1024)
            print("Recevd")
            file.close()

        if type=="text":
            #openfile
            client.send(type.encode("utf-8"))
            print("text")
            msg2=client.recv(SIZE).decode("utf-8")
            print(f"[SERVER] {msg2}")
            select=input("Enter a file : ")
            client.send(select.encode("utf-8"))
            
            npath=path+select+".txt"
            file=open(npath,'w')
            data=client.recv(1024).decode("utf-8")

            file.write(data)
            file.close()
            
        if type=="cCode":
            #openfile
            client.send(type.encode("utf-8"))
            print("C Code")
            msg2=client.recv(SIZE).decode("utf-8")
            print(f"[SERVER] {msg2}")
            select=input("Enter a file : ")
            client.send(select.encode("utf-8"))
            
            npath=path+select+".c"
            file=open(npath,'w')
            data=client.recv(1024).decode("utf-8")

            file.write(data)
            file.close()
            
        if type=="PythonCode":
            #openfile
            client.send(type.encode("utf-8"))
            print("Python Code")
            msg2=client.recv(SIZE).decode("utf-8")
            print(f"[SERVER] {msg2}")
            select=input("Enter a file : ")
            client.send(select.encode("utf-8"))
            
            npath=path+select+".py"
            file=open(npath,'w')
            data=client.recv(1024).decode("utf-8")

            file.write(data)
            file.close()
            

    print("exit")
       
        
            

    
         

    
    


if __name__== "__main__":
    main()

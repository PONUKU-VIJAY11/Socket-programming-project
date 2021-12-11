#Server code
import socket

IP="192.168.0.108"   #IP addresses of the Server
PORT= 4456           # PORT Number
SIZE=1024                 

ADDR=(IP,PORT)       #Address

pathtxt="C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\ser.txt"
pathc="C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\ser.c"
pathpy="C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\ser.py"
pathimg="C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\ser.jpg"
pathvid="C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\ser.mp4"
pathaid="C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\ser.mp3"
path="C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\"

paths={"text":pathtxt , "Ccode":pathc , "PythonCode":pathpy , "image":pathimg , "video":pathvid, "audio":pathaid}
types={"text":".txt" , "Ccode":".c" , "PythonCode":".py" , "image":".jpg" ,"video":".mp4","audio":"mp3"}

img={"ser1":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\ser1.jpg",
     "ser2":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\ser2.jpg",
     "ser3":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\ser3.jpg",
     "ser4":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\ser4.jpg"}

vid={"vdser1":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\vdser1.mp4",
     "vdser2":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\vdser2.mp4"}

aud={"audser1":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\audser1.mpeg",
     "audser2":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\audser2.mpeg"}

txt={"sertext1":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\sertext1.txt",
     "sertext2":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\sertext2.txt",
     "sertext3":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\sertext3.txt"}

cCd={"serc1":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\serc1.c",
     "serc2":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\serc2.c",
     "serc3":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\serc3.c"}

pyn={"serp1":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\serp1.py",
     "serp2":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\serp2.py",
     "serp3":"C:\\Users\\91807\\Desktop\\Courses\\CN\\A2\\serp3.py"}

imgN="ser1  ser2  ser3  ser4 "
     
def main():
    print("SErver is starting")
    try:
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("Socket created")
    except socket.error as er:
        print("Socke creation failed with error %s "%(er))

    server.bind(ADDR)   #binding
    server.listen()     
    print("Server is listening")
    print("Waiting for client to connect")

    while True:
        connection, address = server.accept()
        print(f" NEW CONNECTION {address} connected")
        print("Connection Established between Server and Client")

        msg=connection.recv(SIZE).decode("utf-8")
        print(f"[CLIENT] Received Data")

        msg=connection.recv(SIZE).decode("utf-8")
        if msg=="send":
            print("send is selected")
            msg2=connection.recv(SIZE).decode("utf-8")
            if msg2=="text" or msg2=="Ccode" or msg2=="PythonCode":
             #   msg3=connection.recv(SIZE).decode("utf-8")
                name1=connection.recv(SIZE).decode("utf-8")
                connection.send("Filename given".encode("utf-8"))
                file=open(name1,"w")
                data=connection.recv(SIZE).decode("utf-8")
                file.write(data)
                print("File send to Server by Client")

        if msg=="receive":
            msg2=connection.recv(SIZE).decode("utf-8")
            if msg2=="image":
                connection.send("ser1  ser2  ser3  ser4 ".encode("utf-8"))
                msg3=connection.recv(SIZE).decode("utf-8")
                print(f"[CLIENT] {msg3}")
                i=msg3
                path=img[i]
                print("path for image ",path)

                f=open(path,'rb')
                data_in=f.read(1024)
                while data_in:
                    connection.send(data_in)
                    data_in=f.read(1024)
                    print("sending")
                print("Sending Completd")
                f.close()
            if msg2=="audio":
                connection.send("audser1  audser2 ".encode("utf-8"))
                msg3=connection.recv(SIZE).decode("utf-8")
                print(f"[CLIENT] {msg3}")
                i=msg3
                path=aud[i]
                print("path for audio ",path)

                f=open(path,'rb')
                data_in=f.read(1024)
                while data_in:
                    connection.send(data_in)
                    data_in=f.read(1024)
                    print("sending")
                print("Sending Completd")
                f.close()
            if msg2=="text":
                connection.send("sertext1  sertext2 sertext3".encode("utf-8"))
                msg3=connection.recv(SIZE).decode("utf-8")
                print(f"[CLIENT] {msg3}")
                i=msg3
                path=txt[i]
                print("path for text ",path)

                f=open(path,'r')
                data=f.read(1024)
                connection.send(data.encode("utf-8"))
                print("Sending Completd")
                f.close()
            if msg2=="cCode":
                connection.send("serc1  serc2 serc3".encode("utf-8"))
                msg3=connection.recv(SIZE).decode("utf-8")
                print(f"[CLIENT] {msg3}")
                i=msg3
                path=cCd[i]
                print("path for cCode ",path)

                f=open(path,'r')
                data=f.read(1024)
                connection.send(data.encode("utf-8"))
                print("Sending Completd")
                f.close()
            if msg2=="PythonCode":
                connection.send("serp1  serp2 serp3".encode("utf-8"))
                msg3=connection.recv(SIZE).decode("utf-8")
                print(f"[CLIENT] {msg3}")
                i=msg3
                path=pyn[i]
                print("path for python code ",path)

                f=open(path,'r')
                data=f.read(1024)
                connection.send(data.encode("utf-8"))
                print("Sending Completd")
                f.close()
            if msg2=="video":
                connection.send("vdser1  vdser2 ".encode("utf-8"))
                msg3=connection.recv(SIZE).decode("utf-8")
                print(f"[CLIENT] {msg3}")
                i=msg3
                path=vid[i]
                print("path for video ",path)

                f=open(path,'rb')
                data_in=f.read(1024)
                while data_in:
                    connection.send(data_in)
                    data_in=f.read(1024)
                    print("sending")
                print("Sending Completd")
                f.close()

                

                
                
                
                                             
         

if __name__=="__main__":
    main()

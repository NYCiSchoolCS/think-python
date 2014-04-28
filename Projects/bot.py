import sys
import socket
import string

HOST = "54.84.9.196"
PORT = 6667
NICK = "erica_bot"
IDENT = "guest"
REALNAME = "erica greene bot"
CHANNEL = "#CS101"

def run_bot():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("NICK %s\r\n" % NICK)
    s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
    s.send("JOIN %s\r\n" % CHANNEL)
    readbuffer = ""

    while 1:
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()

        for line in temp:
            print line
            line = string.rstrip(line)
            line = string.split(line)

            # If a private message was sent, check if it was for you. If message is
            # for you, then parse it and respond. Otherwise, do nothing.
            if line[1] == "PRIVMSG":
                if line[3] == ":" + NICK:
                    message = ' '.join(line[4:])
                    response = parse_message(message)

                    s.send("PRIVMSG #CS101 %s\r\n" % response)

            # If server PING's us, we need to PONG back
            if line[0]=="PING":
                s.send("PONG %s\r\n" % line[1])


def parse_message(message):
    """
    Parses IRC message and returns a response.
    Remember: all multi-word responses need to start with colon (:)
    """
    return ":hi"

######################## MAIN PROGRAM ###############################

run_bot()

import sys
import socket, binascii, datetime

def main():
    item = "685951b0aa4acf24aa4acf248101053030303631373536343834322d3030310091100c004d0000000f00000000001900000000093a000000001389024e00000000000d04ec0032000008980000000000000000be35040100650000004500000000000000009a16"
    sSock = socket(AF_INET, SOCK_STREAM)
    sSock.connect((serverHost, serverPort))
    sSock.send(item)

if __name__ == '__main__':main()
    
import re
import os

words =[]
sentences = []
ltrcount = 0
filename = input("Please provide the file name:")
txtpath = os.path.join(filename+".txt")

with open(txtpath,'r') as txtfile:
    data=txtfile.readline()
    print("1")
    print(data)
    words = data.split(" ")
    print(words)
    print(len(words))
    sentences = data.split(".")
    print(sentences)
    print(len(sentences))
    sentences.remove("")
    print(len(sentences))
    for x in words:
        ltrcount = ltrcount + len(x)
    avgltrcount = ltrcount/len(words)
    print("ltrcount:"+str(ltrcount))
    print("avgltrcount:"+ str(avgltrcount))
    print("avgstnclength:"+str((len(words)/len(sentences))))
    print(len(words[0]))
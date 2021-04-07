from gtts import gTTS
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
import f_opt

tpx = ThreadPoolExecutor(100)

WordLst = []
readFile = False #if data is comming from file
counter = 0   # Thread counters
current = -1  # Thread lock

def writer(inp, idn):
    global current
    tfo = BytesIO()
    gTTS(" "+inp+".").write_to_fp(tfo)
    tfo = tfo.getvalue()
    while idn != current:
        pass
    WordLst.append(tfo)
    current = -1

def readFrom(file):
    global readFile
    global counter
    global current
    readFile = True
    data = None
    with open(file,"r") as fio:
        data = fio.readlines()
    for i,v in enumerate(data):
        tpx.submit(writer,v,i)
    counter = len(data)

f_opt.f_opt({
    "-r":([str],readFrom)
    })


if readFile == False:
    while True:
        inp = input("Word:")
        if inp == "":
            break
        tpx.submit(writer, inp, counter)
        counter += 1
    print("Converting text to speech . . .")

for i in range(0, counter):
    current = i
    while current != -1:
        pass
    print("Thread",i,"has completed")
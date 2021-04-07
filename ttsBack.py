from gtts import gTTS
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor

tpx = ThreadPoolExecutor(100)

WordLst = []


def writer(i, idn):
    global current
    tfo = BytesIO()
    gTTS(" "+inp+".").write_to_fp(tfo)
    while True:
        if idn == current:
            WordLst.append(tfo.getvalue())
            current = -1
            break


counter = 0
current = -1
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
    print("thread", i, "completed")

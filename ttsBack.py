from gtts import gTTS
from io import BytesIO

WordLst = []
while True:
    inp = input("Word:")
    if inp == "":
        break
    WordLst.append(" "+inp+".")

for i,v in enumerate(WordLst):
    tfo = BytesIO()
    gTTS(v,slow=True).write_to_fp(tfo)
    WordLst[i]=tfo.getvalue()
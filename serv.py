from flask import Flask
import ttsBack

server = Flask(__name__)

@server.route("/")
def indexHtml():
    return open("index.html", "r").read()


@server.route("/index.js")
def indexJS():
    return open("index.js", "r").read()

@server.route("/audio<id>.mp3")
def retAudio(id):
    try:
        return ttsBack.WordLst[int(id)]
    except:
        return "NO MORE AUDIO"

@server.route("/amt",methods=['POST'])
def getAmt():
    return str(len(ttsBack.WordLst))

if __name__ == "__main__":
    server.run(host="localhost", port=8080, debug=False)

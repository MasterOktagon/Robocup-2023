from meinePins import *

class InvalidFileException(BaseException):
    def __init__(self,desc):
        self.desc = desc
    def __repr__(self):
        return self.desc

def SchreibeWerte(sensoren):
    f = open(DATEI,"w")
    f.write("")
    f.close()
    f = open(DATEI,"a")
    STR = ""
    for s in sensoren:
        STR += s.name + "\t Left (min/max)\n"
        STR += str(s.miniL) + "\n"
        STR += str(s.maxiL) + "\n"
        STR += "\t Right (min/max)\n"
        STR += str(s.miniR) + "\n"
        STR += str(s.maxiR) + "\n"
    #print(STR)
    f.write(STR)
    
    f.close()

def LadeWerte(sensoren,fpath=DATEI):
    f = open(fpath,"r")
    print("Lade...")
    lines = f.readlines()
    if len(lines)%6 != 0:
        raise InvalidFileException(".wrt data must be stored in a valid format")
    for i in range (len(sensoren)):
        sensoren[i].miniL = int(lines[i * 6 +1])
        sensoren[i].maxiL = int(lines[i * 6 +2])
        sensoren[i].miniR = int(lines[i * 6 +4])
        sensoren[i].maxiR = int(lines[i * 6 +5])
    print("Laden erfolgreich!")
    
        
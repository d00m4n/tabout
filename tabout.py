# ------------------------------| Classes
class color:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def setcolor(text, color="white"):    
   colors= {"purple":'\033[95m',"blue" : '\033[94m',"green" : '\033[92m' ,"yellow" : '\033[93m',"red" : '\033[91m',"white" : '\033[0m',"cyan" : '\033[96m'}#,BOLD = '\033[1m',UNDERLINE = '\033[4m'}
   return (colors[color.lower()]+text+colors["white"])

def tabout(
    text,value,separator=":",
    textcolor="white",
    valuecolor="cyan",
    head="",
    headcolor="white",
    textsize=8,
    skin=""    
    ):
    spaces=(textsize - len(text))
    if spaces < 0:
        text=text[0:textsize-2]+".."
    if skin.lower()=="error":
        textcolor="red"
        valuecolor="red"

    print(setcolor(head,headcolor)+setcolor(text,textcolor)+" "*spaces,separator,setcolor(value,valuecolor)+color.ENDC)

# tabout("Profile loaded","red",valuecolor="cyan",textsize=10)

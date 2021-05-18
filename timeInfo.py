from datetime import *

def getDateAndTime():
    date = datetime.today().strftime("%B %d, %Y")
    time = datetime.now().strftime('%I:%M %p')

    return [str(date), str(time)]

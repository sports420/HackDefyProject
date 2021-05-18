from pyjokes import *

def getJoke(categ):
    if categ == "neutral":
        return get_joke(category="neutral")
    elif "tongue" in categ.split("-") or "twister" in categ.split("-"):
        return get_joke(category="twister")
    elif "any" in categ.split():
        return get_joke(category="all")
    else:
        return "I am sorry. That is not a valid category."

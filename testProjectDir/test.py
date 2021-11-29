import sys
sys.path.append("NLGWebsite")
from server import run, runNoClass

def getOutput(text):
    return "Hi this is some output for input:"+text

runNoClass(getOutput)

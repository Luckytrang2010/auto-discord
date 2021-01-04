import requests
import time

#put request to https://discord.com/api/v8/channels/{channelid}/recipients/{userid}
allahu_akbar = False
channel = int(input("Channel ID: "))
recipient = input("Recipients to auto-add: ")
victims = recipient.split(",")

def spam_add(t,recipients):
    allahu_akbar = True
    while allahu_akbar == True:
        time.sleep(2)
        for i in recipients:
            h = {"authorization":t}
            kewl = requests.put("https://discord.com/api/v8/channels/{}/recipients/{}".format(channel,i),headers=h)
            print("{} {}\n{}".format(kewl.status_code,kewl.reason,kewl.text))

token = open("./token.txt","r").read()
if len(token.split("\n")) > 1:
    op = input("It appears that your input in token.txt has multiple tokens, are you sure? [Y/N]: ")
    if op.lower() == "y":
        tokens = token.split("\n")
        for i in tokens:
            spam_add(token,victims)
    elif op.lower() == "n":
        spam_add(token,victims)
else:
    spam_add(token,victims)

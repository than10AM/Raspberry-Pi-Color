
currentcolor="0 0 0"
israinbowrunning=False
import discord, sys, subprocess,os

from subprocess import Popen, PIPE

import time



def cmdcolor(nextcolor):
    
    with open('cmd.sh','r+') as myfile:
        data = myfile.read()
        myfile.seek(0)
        global currentcolor
        myfile.write('sudo python3 ledcontroller.py '+ currentcolor + " " +  nextcolor)
        myfile.truncate()
    os.system("./cmd.sh")
    currentcolor=nextcolor

    
cmdcolor("0 0 0")



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return


        #if message.content == 'ping':
         #   await message.channel.send('yes')
        if message.content.lower() == 'red':
            cmdcolor("255 0 0")
        
            
            await message.channel.send('okay set color from '+currentcolor+' to ' + "255 0 0")       
        if message.content.lower()  == 'blue':
            cmdcolor("0 0 255")
            
            await message.channel.send('okay set color from '+currentcolor+' to ' + "0 0 255")       

        if message.content.lower()  == 'green':
            cmdcolor("0 255 0")
            await message.channel.send('okay set color from '+currentcolor+' to ' + "0 255 0")
            
        if message.content.lower()  == 'purple':
            cmdcolor("159 43 120")
            await message.channel.send('okay set color from '+currentcolor+' to ' + "230 230 250")      
        
        if message.content.lower()  == 'rainbow':
            process = Popen(['sh', 'rainbowcmd.sh', '-d'])
            await message.channel.send('okay set color from '+currentcolor+' to ' + "rainbow")
            
        if message.content.lower()  == 'hot pink':
            cmdcolor("248 24 148")
            await message.channel.send('okay set color from '+currentcolor+' to ' + "230 230 250")      
          
    


client = MyClient()
client.run('OTI1NDY3ODI3NjEwMTkzOTgx.YctjFA.n75DyyZIgOA315nWqc1bmm8q_1c')
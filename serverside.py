
currentcolor="0 0 0"
israinbowrunning=False
import discord, sys, subprocess,os, signal

from subprocess import Popen, PIPE

import time



def cmdcolor(nextcolor):
    global currentcolor
    
    result = subprocess.Popen(' exec sudo python3 ledcontroller.py ' + currentcolor + ' '+ nextcolor, stdout=subprocess.PIPE, shell=True)
    time.sleep(1)
    os.kill(result.pid, signal.SIGKILL)   # should always kill a process  
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

        if message.content.lower()  == 'grey':
            cmdcolor("200 200 200")
            await message.channel.send('okay set color from '+currentcolor+' to ' + "255 255 255")           
        
        if message.content.lower()  == 'white':
            cmdcolor("255 255 255")
            await message.channel.send('okay set color from '+currentcolor+' to ' + "255 255 255")           
        
        if message.content.lower()  == 'rainbow':
            process = Popen(['sh', 'rainbowcmd.sh', '-d'])
            await message.channel.send('okay set color from '+currentcolor+' to ' + "rainbow")
            
        if message.content.lower()  == 'hot pink':
            cmdcolor("248 24 148")
            await message.channel.send('okay set color from '+currentcolor+' to ' + "230 230 250")      
          
        if message.content.lower()  == 'black':
            cmdcolor("0 0 0")
            await message.channel.send('okay set color from '+currentcolor+' to ' + "0 0 0")          

        if message.content.lower()  == 'yellow':
            cmdcolor("255 255 0")
            await message.channel.send('okay set color from '+currentcolor+' to ' + "0 0 0")
            
client = MyClient()
client.run('OTc2NDU0Mjk0Nzc5ODU4OTU0.Gd4F23.wE_w_Et1QcwGzv7Q29lXOZFjyBd9bdSLnGEjjA')
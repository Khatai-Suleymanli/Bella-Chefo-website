import pyttsx3
import datetime
import webbrowser
import os
from gtts import gTTS
from PIL import Image

import subprocess
import sys


print("enter your name")

#root = tkinter.Tk()
#inname ="tenor.gif"
#root.mainloop()
 
def userstart():
    print("please enter your name")

          


    
user = input()
def wishMe():
    print("hello")
    hour = int(datetime.datetime.now().hour)
    print(hour)
   
    if hour>=6 and hour<12:
        print("Good Morning! " + user)
        print ("I'm your gaming assistant probot")

    elif hour>=12 and hour<18:
        print("Good Afternoon! " + user)
        print ("I'm your gaming assistant probot")

    elif hour>=18 and hour<24:
        print("Good Evening ! " + user)
        print ("I'm your gaming assistant probot")

    else:
        print("Good Night! " + user)
        print ("I'm your gaming assistant probot")
        


  

            


if __name__ == "__main__":
    wishMe()
    while True:
        print("How can i help you?")
        query = input("type your questions: \n")
            
            
        if "who made you"  in query: 
            print("I have been created by bellaChefo team")
           
            
            
        elif  "Who are you" in query: 
            print("I'm your cooking assistant Bella bot. I am always happy to help you to cook :)")
            
         
            
        elif  "What's Bella Chefo" in query: 
            print("Bella Chefo is an app, which helps everybody to solve the problem- What to eat for the dinner. \n That also helps users to eat healthy.")
       
            
        elif  "Onion, pepper, tomato" in query: 
            print(" Mesolla slad is the  best to cook with usng these ingidents")
            

        elif "How to add my own cooking recipe" in query:
            print("Go to the - Add my own recipe section - Fill the page about your recipe - Add your details \n Note: For confirming your recipe that has to be checked by our team.")


        elif "What is the nearest market for me " in query:
            print("The nearest market to you is: NNNN market. \n The cheapest maket is YYYYY market for you..")



        elif "Thanks " in query:
            print("This my pleasure Gamer!")



        elif "Is this app free " in query:
            print("This sis free for all the Chefs. Premium members have to pay a little amount of money.")


        


        
              

        
        elif 'close' in query:
            print("see you soon Gamer")
            exit()
        
        else :
            webbrowser.open(query)

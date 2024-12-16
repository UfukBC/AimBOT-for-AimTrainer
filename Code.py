
import pyautogui
import time
import os
import keyboard


print("Current working directory:", os.getcwd())
   
Control=True

time.sleep(2)  # Wait before checking for the image

while Control:

    if keyboard.is_pressed('k'):
        Control = False

    try:
            
        pic=pyautogui.screenshot(region=(253,72,1395,840))
        width, height = pic.size
            
            

        for x in range (0,width,50):
          for y in range (0,height,50): 

            if(keyboard.is_pressed('k')):
                  Control=False
                  break

            r,g,b=pic.getpixel((x,y))

            if(r==255 and g == 87 and b == 34):
              pyautogui.leftClick(x+253,y+72)         

            ######################################################################
            #                       To be developed...
            # if(pyautogui.locateCenterOnScreen('Target.png',confidence=0.8)!=None):
            #      print("I can see it")

            # center = pyautogui.locateCenterOnScreen('Target.png',confidence=0.8)
            # pyautogui.click(center)
            ########################################################################
            
    except :
        print(Exception)
        print('I cant see')
        time.sleep(1)  

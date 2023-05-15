import time
import model as m
import requests
import io
import base64
from PIL import Image
import urllib.request
import base64
from io import BytesIO


class start():
  def __init__(self,img=None,link=None) :
    self.model = m.Model()
    self.img=img
    if link!=None:
      self.link=self.input_link(link)
    else:
      self.link=None
    self.pos=None
    self.neg=None
    
  def run(self):
    if self.img!=None:
      self.pos,self.neg = self.model.predict(self.img)
      self.img=None
    elif self.link!=None:
      
      self.pos,self.neg = self.model.predict(self.link)
      self.link=None
  def print_caption(self):
    print(self.pos, self.neg)
  
  def input_img(self,img):
    self.img=img
  
  def input_link(self,link):
    req = urllib.request.Request(link, headers = {"User-Agent" : "Mozilla/5.0"})
    res = urllib.request.urlopen(req).read()
    self.link = Image.open(BytesIO(res))
  
  def send2ui(self):
      
    url = "http://127.0.0.1:7860"
    
    payload = {
      "prompt": "{}".format(self.pos),
      "neg_prompt":"{}".format(self.neg),
      "steps": 10  
    }
    
    
    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
    r = response.json()
    image = Image.open(io.BytesIO(base64.b64decode(str(r['images']).split(",",1)[0])))
    image.save('output.png')
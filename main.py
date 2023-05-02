import time
import model as m
import requests
import io
import base64
from PIL import Image

num_of_image=100

if __name__ == "__main__":
  model = m.Model()
  
  image_list=["image{}".format(i) for i in range(num_of_image+1)]

  
  for i in range(2):
    result,neg = model.predict("./image{}.jpg".format(i))
    input=result.split(' ')
    
    
    url = "http://127.0.0.1:7860"
    print(result)
    print("==========================",neg)
    payload = {
      "prompt": "{}".format(result),
      "neg_prompt":"{}".format(neg),
      "steps": 10  
    }
    
    
    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
    r = response.json()
    image = Image.open(io.BytesIO(base64.b64decode(str(r['images']).split(",",1)[0])))
    image.save('output{}.png'.format(i))
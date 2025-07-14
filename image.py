from transformers import BlipProcessor, BlipForConditionalGeneration
#PIL => pillow
from PIL import Image
import requests
import random
import torch #fro pre-defined models
processor=BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model=BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
url="https://images.unsplash.com/photo-1747561246680-a34121708d80"
image=Image.open(requests.get(url,stream=True).raw).convert("RGB")
#create and initialize model and fetch text
inputs=processor(image,return_tensors="pt")
output=model.generate(**inputs)
caption=processor.decode(output[0])
#create hashtags for captions
hashtags=["#flowers","#sky","#hubs","#mountains"]
print(caption)
print(random.choice(hashtags))

chart_caption="{caption}.{random.choice(hashtags)}"
import matplotlib.pyplot as plt
plt.imshow(image)
plt.axis("off")
plt.title(chart_caption,fontsize=10)
plt.show()
#video extraction
import cv2
from transformers import BlipProcessor,BlipForConditionalGeneration
from PIL import Image
processor=BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model=BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
video_path="Sample.mp4"
cap=cv2.VideoCapture(video_path)
success,frame=cap.read()
if success:
    image=Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
    inputs=processor(images=image,return_tensors="pt")
    output=model.generate(**inputs)
    caption=processor.decode(output[0], skip_special_tokens=True)
    print(caption)
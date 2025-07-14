#image to text than translate to regional language
from transformers import BlipProcessor,BlipForConditionalGeneration
from PIL import Image
import requests
from transformers import MBartForConditionalGeneration,MBart50TokenizerFast
processor=BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model=BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
url="https://images.unsplash.com/photo-1747561246680-a34121708d80"
image=Image.open(requests.get(url,stream=True).raw).convert("RGB")
#create and initialize model and fetch text
inputs=processor(image,return_tensors="pt")
output=model.generate(**inputs)
caption=processor.decode(output[0])
#load
model_name="facebook/mbart-large-50-many-to-many-mmt"
tokenizer=MBart50TokenizerFast.from_pretrained(model_name)
model1=MBartForConditionalGeneration.from_pretrained(model_name)
tokenizer.src_lang="en_XX"
target_lang="te_IN"
inp_ing=tokenizer(caption,return_tensors="pt")
out_tok=model1.generate(**inp_ing,forced_box_token_id=tokenizer.lang_code_to_id[target_lang])
caption_te=tokenizer.decode(out_tok[0], skip_special_tokens=True)
print(caption_te)
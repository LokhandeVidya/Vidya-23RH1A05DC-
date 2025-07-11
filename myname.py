from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
name="Mumma"
text=(name+' ')*100
mask=np.array(Image.open("heart_img.webp"))
wordcloud=WordCloud(background_color='white',mask=mask,contour_color='purple',contour_width=0.5,colormap='Purples').generate(text)
plt.figure(figsize=(8,8))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()

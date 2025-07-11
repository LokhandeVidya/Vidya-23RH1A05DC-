from wordcloud import WordCloud
import matplotlib.pyplot as plt

text="""Jammu, Kashmir, Srinagar, Dal Lake, Gulmarg, Pahalgam, Sonamarg, 
Amarnath,Vaishno Devi, snow, mountains, valleys, culture, Wazwan, 
kahwa, saffron, shikara, houseboats, shawls, trekking, 
skiing, beauty, peace, heritage, temples, mosques, Leh, Ladakh, Kargil."""
wordcloud=WordCloud(width=800,height=400,background_color='white').generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud)
plt.show()
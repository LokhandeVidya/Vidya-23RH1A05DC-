from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Family members' names
hashtags = """FAMILY , Ajji, Bapu, Mothi Mau, Mothe Kaka, Vanitha Mau, Chote Kaka,
Mumma, Daddy, Choti Mau, Motha Mama, Chota Mama, Sajan Bhaiya,
Vinu Bhaiya, Payal Didi, Tanu, Didi, Kali, Pavan, Chintu"""

my_name = "FAMILY"

# Repeating the names to give weight in the word cloud
text = (my_name + ' ') * 100 + (' ' + hashtags) * 5

# Create the word cloud
wordcloud = WordCloud(width=1000, height=500, background_color='white', colormap='viridis').generate(text)

# Display the word cloud
plt.figure(figsize=(14, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()

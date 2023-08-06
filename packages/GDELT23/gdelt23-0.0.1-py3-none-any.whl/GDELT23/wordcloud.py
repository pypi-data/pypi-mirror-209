def add_one(number):
    return number + 1


def vcounts22():
    
    dataw = ''.join(data3)
    wordcloud = WordCloud(width= 1000, height = 600, max_words=1000,
                          random_state=1, background_color='gray', colormap='viridis_r',
                          collocations=False, stopwords = STOPWORDS).generate(sum)
    plt.figure(figsize=(30, 20))
    plt.imshow(wordcloud) 
    plt.axis("off")
    plt.show()

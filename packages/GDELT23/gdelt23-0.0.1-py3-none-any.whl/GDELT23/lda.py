def add_one(number):
    return number + 1

def vcount23():
    data4 = pd.DataFrame(data3)
    data5=data4[0].apply(clean_text)
    vect =TfidfVectorizer(stop_words=stop_words,max_features=1000)
    vect_text=vect.fit_transform(data5)
    lda_model=LatentDirichletAllocation(n_components=20,
    learning_method='online',random_state=42,max_iter=1) 
    lda_top=lda_model.fit_transform(vect_text)
    vocab = vect.get_feature_names()
    for i, comp in enumerate(lda_model.components_):
        vocab_comp = zip(vocab, comp)
        sorted_words = sorted(vocab_comp, key= lambda x:x[1], reverse=True)[:20]
        print("Topic "+str(i+1)+": ")
        for t in sorted_words:
            print(t[0], end=" ")
        print("\n")

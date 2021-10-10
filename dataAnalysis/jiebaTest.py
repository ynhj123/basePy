import jieba
from gensim import corpora, models

stop_word = ["，", "不但", "还让", "为"]

if __name__ == '__main__':
    text = "唐喵喵不但喜欢江江江，还让江江江做数据分析"
    # 分词
    list_text = jieba.cut(text)
    print(list(list_text))
    # 添加新词
    jieba.add_word("唐喵喵")
    jieba.add_word("还让")
    list_text = jieba.cut(text)
    print(list(list_text))
    # 词组拆分
    jieba.suggest_freq(("数据", "分析"), True)
    jieba.suggest_freq(("好好", "学习"), True)
    jieba.suggest_freq(("努力", "学习"), True)
    list_text = jieba.cut(text)
    word_list = list(list_text)
    print(word_list)
    # 过滤
    print(list(filter(lambda word: word not in stop_word, word_list)))
    # 去重
    print(set(filter(lambda word: word not in stop_word, word_list)))

    word_list = list(set(filter(lambda word: word not in stop_word, word_list)))

    texts = ["唐喵喵不但喜欢江江江，还喜欢学习",
             "唐喵喵要好好学习，天天向上",
             "江江江为人民服务，努力学习"]
    text_list = []
    for txt in texts:
        words = list(set(filter(lambda word: word not in stop_word, jieba.lcut(txt))))
        text_list.append(words)

    dictionary = corpora.Dictionary(text_list)
    corpus = [dictionary.doc2bow(words) for words in text_list]
    lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=2)
    topics = lda.print_topics(num_words=4)
    for topic in topics:
        print(topic)
    print(lda.inference(corpus))
    new_text = "唐喵喵除了好好学习，还要多锻炼身体"
    words = list(set(filter(lambda word: word not in stop_word, jieba.lcut(new_text))))

    nd_array = lda.inference([dictionary.doc2bow(words)])[0]
    for e, value in enumerate(nd_array[0]):
        print("%d : %.2f" % (e, value))
    for word, word_id in dictionary.token2id.items():
        print(word, lda.get_term_topics(word_id, minimum_probability=1e-8))

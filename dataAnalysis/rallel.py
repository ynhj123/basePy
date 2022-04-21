import json
import os

import jieba
import pandas as pd
import csv


from basePy.dataAnalysis.allDate import stopwordslist, add_word

Happy = []
Good = []
Surprise = []
Anger = []
Sad = []
Fear = []
Disgust = []

stopword = stopwordslist()
add_word = add_word


def emotion_caculate(text):
    positive = 0
    negative = 0
    anger = 0
    disgust = 0
    fear = 0
    sad = 0
    surprise = 0
    good = 0
    happy = 0
    # wordlist = jieba.lcut(text)
    wordlist = list(set(filter(lambda word: word not in stopword, jieba.lcut(text))))
    wordset = set(wordlist)
    wordfreq = []
    for word in wordset:
        freq = wordlist.count(word)
        if word in Positive:
            positive += freq
        if word in Negative:
            negative += freq
        if word in Anger:
            anger += freq
        if word in Disgust:
            disgust += freq
        if word in Fear:
            fear += freq
        if word in Sad:
            sad += freq
        if word in Surprise:
            surprise += freq
        if word in Good:
            good += freq
        if word in Happy:
            happy += freq
    emotion_info = {
        'length': len(wordlist),
        'positive': positive,
        'negative': negative,
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'good': good,
        'sadness': sad,
        'surprise': surprise,
        'happy': happy,
    }
    indexs = ['length', 'positive', 'negative', 'anger', 'disgust', 'fear', 'sadness', 'surprise', 'good', 'happy']
    return pd.Series(emotion_info, index=indexs)


if __name__ == '__main__':
    print(add_word)
    print(stopword)
    for word in add_word:
        jieba.add_word(word)
    df = pd.read_excel('情感词汇本体.xlsx')

    df = df[['词语', '词性种类', '词义数', '词义序号', '情感分类', '强度', '极性']]
    df.head()
    for idx, row in df.iterrows():
        if row['情感分类'] in ['PA', 'PE']:
            Happy.append(row['词语'])
        if row['情感分类'] in ['PD', 'PH', 'PG', 'PB', 'PK']:
            Good.append(row['词语'])
        if row['情感分类'] in ['PC']:
            Surprise.append(row['词语'])
        if row['情感分类'] in ['NA']:
            Anger.append(row['词语'])
        if row['情感分类'] in ['NB', 'NJ', 'NH', 'PF']:
            Sad.append(row['词语'])
        if row['情感分类'] in ['NI', 'NC', 'NG']:
            Fear.append(row['词语'])
        if row['情感分类'] in ['NE', 'ND', 'NN', 'NK', 'NL']:
            Disgust.append(row['词语'])
    Positive = Happy + Good + Surprise
    Negative = Anger + Sad + Fear + Disgust
    print('情绪词语列表整理完成')
    text_pd = pd.read_csv('tmp.csv')
    emotion_df = text_pd['title'].apply(emotion_caculate)
    output_df = pd.concat([text_pd, emotion_df], axis=1)
    output_df.to_csv('output.csv', index=False)
    output_df.head()

import os

import jieba
from gensim import corpora, models
from gensim.models import CoherenceModel, LdaModel
import matplotlib.pyplot as plt
import pyLDAvis.gensim_models

num_topic = 50


# https://mlln.cn/2018/10/11/%E4%B8%AD%E6%96%87%E6%83%85%E6%84%9F%E5%88%86%E6%9E%90%E8%AF%AD%E6%96%99%E5%BA%93%E5%A4%A7%E5%85%A8-%E5%B8%A6%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80/

def coherence(num_topics, corpus, dictionary, texts):
    idamodel = LdaModel(corpus=corpus, num_topics=num_topics, id2word=dictionary)
    ldacm = CoherenceModel(model=idamodel, texts=texts, dictionary=dictionary)
    return ldacm.get_coherence()


stop_word = ["，", "？", "吗", "呢", "。", "的", "呀", "如何", "哪些", "多少", "是否", "有",
             "是", "很", "什么", "怎么", "咋", "-", "怎么回事", "该", "哪里", "多久", "比较",
             "怎么办", "准备", "注意", "啊", "了", "突然", "做", "经常", "也", "有时", "会",
             "不会", " ", "a", "！", "不要", "b", "是不是", "不", "可以", "想要", "不能",
             "一些", "啥", "确诊", "么", "需要", "为什么", "对", "适合", "合适", "和", '容易', '多大',
             '好处', '给', '一次', '一个', '宝宝', '月', '那该', '一定', '回事', '孩子', '推荐', '用量',
             '东西', "去", "没有", "\n", "但是", "还", "这", "一直", "但", "没空", "我",
             "影响", "期间", "显示", "现在", "没有", "来", "使用", "去", "有没有", "小时", "宁愿", "晚上", "来回",
             "知道", "以后", "到", "真的", "爷爷", "之前",
             "就要", "这么", "知道", "可能", "最近", "婆婆", "吵醒", "他",
             "她", "它", "再", "不是", "姐妹", "你们", "现在", "就", "要", "公司", "还是",
             "就是", "朋友", "用", "从", "都", "今天", "真是", "看见", "没", "开始", "确实", "非要",
             "岁", ",", "谢谢", "时", "后来", "女孩", "哪家", "说", "这样", "刚刚", "帮", "拍", "看", "快", "被", "个", "都", "能",
             "特别", "那种", "上", "、", "然后", "哪", "句", "总是", "不想", "所以", "不好", "着", "又", "前", "可是",
             "才", "一般", "终于", "只", "点", "按", "昨晚", "结果", "已经", "好像", "感觉", "😂", "怎样", "好", "啦", "属于", "引起", "深圳",
             "问题", "轻轻", "必须", "上次", "正常", "或", "长得", "更", "意思", "查", "练", "周", "吃", "紧张", "才能", "最新", "具体", "那",
             "笑", "好大", "还要", "里", "很想", "除了", "得", "情况", "多长时间", "原因", "时候", "类型", "与", "里", "加", "在", "每天", "不同",
             "才能", "可行", "起到", "作用", "还有", "沈阳", "大概", "几家", "更好", "究竟", "\t", "多", "其", "要开", "想", "不住", "握", "像",
             "?", "看其", "少", "完", "其", "带来", "让", "一样", "有点", "老是", "闻", "自家", "长小红", "应该", "造成", "管", "偶尔", "几个", "如果",
             "的话", "可不可以", "回事儿", "特", "主要", "没事", "把", "吧", "哪种", "出现", "表现", "要求", "几天", "吃会", "一起", "接近", "所有", "全都",
             "名字", "自己", "几粒", "进行", "要求", "方面", "一起", "以前", "意义", "总", "38", "每次", "下", "各位", "我家", "这是", "九个", "起",
             "身上", "头", "一个月", "六个月", "要生", "八个", "频繁", "37", "厉害", "血", "6", "2", "1", "不吃", "8", "添加", "不用", "+",
             "一天", "0", "3", "4", "5", "7", "9", "有时候", "一", "算是", "之后", "选择", "觉得", "早上", "出生", "听", "没什么", "有关", "一周",
             "或者", "平时", "老", "11", "10", "36", "39", "40", "16", "往", "里面", "一下", "比", "不怎么", "怎么样", "哪个", "很大", "多月",
             "吃点", "有人", "夏天", "生完", "早期", "五个", "三个", "喜欢", "出来", "级别", "（", "）", "：", "出", "便", "两个", "一岁", "超", "太",
             "低", "人", "20", "两个", "出", "冬天", "买", "冬天", "明显", "爱", "红", "补", "学", "这种", "高", "见", "喝", "拉", "生", "一点",
             "擦", "听说", "半月", "满月", "好不好", "怕", "下面", "我们", "肉", "大家", "两岁", "哦", "这个", "算", "们", "家里人", "叫", "男", "穿",
             "选", "了解", "带", "😮", "💨", "…", "/", "哈", "喽", "😞", "\u200d", "52", "😭", "“", "”", "12", "155", "为",
             "妈妈", "变化", "排名", "排名", "好用", "右边", "动", "动", "爸妈", "儿童", "完全", "半夜", "中", "种",
             "大人", "继续", "对于", "大小", "最好", "第一次", "天", "方式", "左边", "其他", "大", "不敢", "跟", "长", "同时", "样子", "打", "换", "型",
             "提供",
             "陪", "些", "有用吗", "开", "不爱", "娃", "所", "四个", "补充", "办法", "产生", "那么", "至", "提升", "抱", "起来", "小儿", "衣服", "质量",
             "十岁", "三四天", "下午",
             "请问", "过", "安排", "遇到", "关系", "因为", "贴", "建议", "喝点", "发生", "地方", "后", "后", "度", "关系", "遇到", "放", "天天", "14",
             "涂抹", "量",
             "越来越", "24", "未", "做法", "以及", "办", "亲", "来说", "23", "不错", "正确", "半", "很多", "夜里", "发", "哪款", "周岁", "不肯",
             "小学", "事情", "生产", "种", "50", "包", "事", "17", "单", "女生", "我要", "不到", "北京", "上学",
             "区别", "腿", "几次", "白色", "几岁", "挺", "15", "13", "什么样", "掉", "最", "老公", "小", "偏", "小心", "纯", "可", "30", "别的",
             "宝贝", "事情", "不让", "100", "27", "必要", "十个", "26", "帮助", "好些", "十一个月", "一边", "超级", "找", "促进", "周多", "声音",
             "通过", "好多", "办", "导致", "长期", "过程", "现象", "确定", "家里", "左右", "范围", "斤", "快点", "请问", "女", "七个", "三岁", "引导",
             "泡泡", "看到", "连续", "五岁", "轻微", "时间", "产后", "证明", "小孩", "控制", "找", "等", "精神", "不长", "女宝", "之间", "户口", "慢慢",
             "管用", "科", "视频", "家", "刚出生", "新生儿", "37.5", "报告", "下来", "女儿", "水平", "很快", "菜", "半个", "D", "爸爸妈妈", "哪些项目",
             "高是", "期", "变得", "咋办", "等到", "号", "在家", "你", "药好"
                                                          "后期", "不够", "功能", "男宝", "身体", "足", "参考", "沟通", "哪些方面", "有些",
             "过去", "第二次", "有利于", "不了", "正", "差", "好转",
             "儿子", "及", "含", "能够", "美",
             "右", "妈咪", "有效", "提高", "反应", "男孩", "反复", "持续", "两天", "一点点", "避免", "这些", "大声", "而且", "好好", "防止", "两天", "处理",
             "厘米",
             "受到", "小朋友", "简单", "严重", "之类", "干", "后能", "不准", "嘛", "还会", "理会", "干什么", "周围", "19", "气", "缺什么", "国家", "只有",
             "中间", "送", "还会", "性", "点点", "完奶", "发出声音", "你", "四岁", "二个月", "下去", "脚", "并且", "每个", "照", "走", "刚", "随时",
             "三天", "三次", "连", "每日", "分别", "连", "改", "年", ":",
             "四周", "几分钟", "只要", "含有", "半岁", "29", "打算", "有个", "含量", "好了吗", "七岁", "中午", "拿", "直接", "左", "右", "给", "代表",
             "不管", "—", "一年", "保证", "》", "只是", "60", "42", "一只",
             "到底", "整个"]
add_word = ["大便", "乳酸菌素片", "验孕棒", "弄东弄西", "健康食物", "果维康", "月子餐", "暖宫贴", "玻尿酸", "月子中心", "流口水", "花粉", "腌萝卜", "准确", "月子会所",
            "补钙", "打人", "打胎", "高跟鞋", "量完", "宝妈", "一岁半", "拉肚子", "拉屎", "后怕", "足型", "拉肚子", "洗衣服", "怀孕", "喂奶", "进口奶粉",
            "肚子疼", "上火", "黄色", "喝完奶", "哭闹", "喝完奶", "挂号", "今年", "三周岁", "请",
            "打疫苗", "喂奶", "黄色", "汤水", "妊娠纹", "盖被子", "照顾", "照看", "黄色", "怀孕", "吃饭", "转醒", "上班", "年龄", "传染", "稀饭"]


def stopwordslist():
    stopwords = [line.strip() for line in open('stopwords.txt', encoding='GBK')]
    stopwords = stopwords + stop_word
    return stopwords


def get_file_list(dir):
    all_count = 1
    text_list = []
    stopword = stopwordslist()
    for word in add_word:
        jieba.add_word(word)

    for home, dirs, files in os.walk(dir):
        for filename in files:
            fullname = os.path.join(home, filename)
            file = open(fullname, "r", encoding='UTF-8')
            for line in file.readlines():
                split_arr = line.split("|")
                txt = split_arr[0]
                # print(txt)
                words = list(set(filter(lambda word: word not in stopword, jieba.lcut(txt))))
                text_list.append(words)
                all_count = all_count + 1
    # print(all_count)
    # print(text_list)
    dictionary = corpora.Dictionary(text_list)
    corpus = [dictionary.doc2bow(words) for words in text_list]
    # 计算困惑度
    # x = range(1, num_topic)
    # y = [coherence(i, corpus, dictionary, text_list) for i in x]
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    # plt.rcParams['axes.unicode_minus'] = False
    # plt.plot(x, y)
    # plt.xlabel('主题数')
    # plt.ylabel('coh大小')
    # plt.title('主题-coh大小变化')
    # plt.show()
    lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=31)
    topics = lda.print_topics(num_topics=31, num_words=10)
    # for i in lda.get_document_topics(corpus)[:]:
    #     listj = [];
    #     for j in i:
    #         listj.append(j[1])
    #     bz = listj.index(max(listj))
    #     print(i[bz][0])
    data = pyLDAvis.gensim_models.prepare(topic_model=lda, corpus=corpus, dictionary=dictionary)
    pyLDAvis.save_html(data, 'D:\\test\\5.html')
    for topic in topics:
        print(topic)

    # print(lda.inference(corpus))
    # for word, word_id in dictionary.token2id.items():
    #     print(word, lda.get_term_topics(word_id, minimum_probability=1e-8))


#  2021年4月8 - 2022 2-28
#  总计 118113条
#  2021年4月8 - 2022 4-9
#  总计 118201

if __name__ == "__main__":
    get_file_list('D:\\mamaData')

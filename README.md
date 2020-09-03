## 近义词训练
任务1:找语义相似的词
INPUT：语料，目标词汇
 - 将语料进行分词
 - 从语料与目标词汇进行训练，找出其中每个词的近义词（目标词汇有一个优先级）排名靠前的词优先

使用包：Gensim，jieba



```python
from gensim.models import word2vec

w2v_model = word2vec.Word2Vec(sentences, 
                              min_count = MIN_COUNT, 
                              workers = CPU_NUM, 
                              size = VEC_SIZE,
                              window = CONTEXT_WINDOW)
```

- min_count: 对于词频 < min_count 的单词，将舍弃（其实最合适的方法是用 UNK 符号代替，即所谓的『未登录词』，这里我们简化起见，认为此类低频词不重要，直接抛弃）
- workers: 可以并行执行的核心数，需要安装 Cython 才能起作用（安装 Cython 的方法很简单，直接 pip install cython）
- size: 词向量的维度，即参考资料[3.]所提到的神经网络隐层节点数
- window: 目标词汇的上下文单词距目标词的最长距离，很好理解，比如 CBOW 模型是用一个词的上下文预测这个词，那这个上下文总得有个限制，如果取得太多，距离目标词太远，有些词就没啥意义了，而如果取得太少，又信息不足，所以 window 就是上下文的一个最长距离



## *中文分词工具*

下面排名根据 GitHub 上的 star 数排名：

1. [Hanlp](https://link.zhihu.com/?target=https%3A//github.com/hankcs/HanLP)
2. [Stanford 分词](https://link.zhihu.com/?target=https%3A//github.com/stanfordnlp/CoreNLP)
3. [ansj 分词器](https://link.zhihu.com/?target=https%3A//github.com/NLPchina/ansj_seg)
4. [哈工大 LTP](https://link.zhihu.com/?target=https%3A//github.com/HIT-SCIR/ltp)
5. [KCWS分词器](https://link.zhihu.com/?target=https%3A//github.com/koth/kcws)
6. [jieba](https://link.zhihu.com/?target=https%3A//github.com/yanyiwu/cppjieba)
7. [IK](https://link.zhihu.com/?target=https%3A//github.com/wks/ik-analyzer)
8. [清华大学THULAC](https://link.zhihu.com/?target=https%3A//github.com/thunlp/THULAC)
9. [ICTCLAS](https://link.zhihu.com/?target=https%3A//github.com/thunlp/THULAC)

## *英文分词工具*

1. [Keras](https://link.zhihu.com/?target=https%3A//github.com/keras-team/keras)
2. [Spacy](https://link.zhihu.com/?target=https%3A//github.com/explosion/spaCy)
3. [Gensim](https://link.zhihu.com/?target=https%3A//github.com/RaRe-Technologies/gensim)
4. [NLTK](https://link.zhihu.com/?target=https%3A//github.com/nltk/nltk)

# PYWE

**Codes for our(Yao Chen, Zhengming Zhang) paper: PYWE(PINYIN-Enhanced Word Embeddings), good luck**

## Brief Abstract
Chen et al.(2015) propose multiple-prototype character embeddings which obtain multiple vectors including position-based, cluster-based and nonparametric method for a character and an effective word selection method.

Yin et al.(2016) propose multi-granularity embedding (MGE) for Chinese words, which makes full use of such word-character-radical composition, and enrich word embeddings by further incorporating fifiner-grained semantics from characters and radicals.

Yu et al.(2017) use three likelihoods to evaluat whether the context words, characters, and components can predict the current target word(JWE).

Sun et al.(2019) introduced a model to learn Chinese word embeddings via three-level composition(VCWE), which extracts the intra-character compositionality from the visual shape of a character and uses the Skip-Gram framework to capture non-compositionality by word embeddings composed by a recurrent neural network with self-attention.

According to the papers above, we'll introduce a new method with pre-train word embedding with the combination of pinyin encodings in this paper...

## Task
1. building pinyin embeddings by pinyin package in python
2. training a pre-train model with the combination of VCWE while improving its network

## prepare the data
We download Chinese Wikipedia dump latest,and normalize all characters as simplified Chinese,then remove nonChinese characters,finally i use PKUSEG for word segmentation.
the data is in:
链接: https://pan.baidu.com/s/1Yv-1X6lxOwf0tzJujBAwug 提取码: 7ny7

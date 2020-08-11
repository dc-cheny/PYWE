import pkuseg
from collections import Counter
import pprint

content = []
lexicon = ['欧几里得'] 
def seg(source_txt, target_txt):
	with open(source_txt, encoding="utf-8") as f:
	    content = f.read()
	print(content)
	seg = pkuseg.pkuseg(model_name="web", user_dict=lexicon)
	text = seg.cut(content)
	print(text)
	stopwords = []
	with open("cn_stopwords.txt", encoding="utf-8") as f:
		stopwords = f.read()
	new_text = []
	for w in text:
		if w not in stopwords:
			new_text.append(w)
	with open(target_txt,"w") as f:
	    f.write(' '.join(new_text))
	counter = Counter(text)
	pprint.pprint(counter.most_common(20))
source_txt = "fenci_"
target_txt = "seg_"
for i in range(368):
    if i<10:
        i = '000'+str(i)
    elif 10<=i and i<100:
        i ='00'+str(i)
    else:
        i='0'+str(i)
    source_txt += i
    target_txt += i
    seg(source_txt, target_txt)
    source_txt = "fenci_"
    target_txt = "seg_"
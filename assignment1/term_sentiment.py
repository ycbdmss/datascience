import sys
import json
import re

def term_score(dic,dic2,s):
    dic1=dic2.copy()
    score=0
    #words=re.findall(r'[^\s!,.?#@":;0-9]+', s)
    words=re.findall(r'\w+',s)
    for i in words:
        if i in dic:
            score+=dic[i]
            
    if score>0:
        for i in words:
            if i in dic1:
                dic1[i]+=1
            elif i not in dic:
                dic1[i]=1
    elif score<0:
        for i in words:
            if i in dic1:
                dic1[i]-=1
            elif i not in dic:
                dic1[i]=-1
    
    return dic1
    
def main():
    scores={}
    terms={}
    with open(sys.argv[1]) as f1:
        for line in f1:
            term,score=line.split("\t")
            scores[term]=int(score)
            
    with open(sys.argv[2]) as fp:
        for line in fp:
            s=json.loads(line)
            if 'text' in s:
                terms=term_score(scores,terms,s['text'])
    for i in terms:
        try:
            print i, terms[i]
        except UnicodeEncodeError:
            pass
if __name__ == '__main__':
    main()

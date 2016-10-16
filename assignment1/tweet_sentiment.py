import json
import sys
import re


def twit_score(dic,s):
    score=0
    words=re.findall(r'\w+',s)
    for i in words:
        if i in dic:
            score+=dic[i]
    return score

def main():
    scores={}
    with open(sys.argv[1]) as f1:
        for line in f1:
            term,score=line.split("\t")
            scores[term]=int(score)
            
    with open(sys.argv[2]) as fp:
        for line in fp:
            s=json.loads(line)
            if 'text' in s:
                print twit_score(scores,s['text'])
            else:
                print 0
                
if __name__ == '__main__':
    main()

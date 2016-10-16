import sys
import json
import re

def term_freq(dic,s):
    dic1=dic.copy()
    score=0
    #words=re.findall(r'[^\s!,.?#@":;0-9]+', s)
    words=re.findall(r'\w+',s)
    for i in words:
        if i in dic:
            dic1[i]+=1.0
        else:
            dic1[i]=1.0
            
    return dic1
    
def main():

    terms={}
    
            
    with open(sys.argv[1]) as fp:
        for line in fp:
            s=json.loads(line)
            if 'text' in s:
                terms=term_freq(terms,s['text'])
    t=sum(terms.values())          
    for i in terms:
        try:
            print i, terms[i]/t
        except UnicodeEncodeError:
            pass
if __name__ == '__main__':
    main()

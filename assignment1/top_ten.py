import sys
import json
import re

def term_freq(dic,s):
    dic1=dic.copy()
    score=0
    #words=re.findall(r'[^\s!,.?#@":;0-9]+', s)
    for i in s:
        if 'text' in i:
            if i['text'] in dic:
                dic1[i['text']]+=1.0
            else:
                dic1[i['text']]=1.0
            
    return dic1
    
def main():

    terms={}
    
            
    with open(sys.argv[1]) as fp:
        for line in fp:
            s=json.loads(line)
            if 'text' in s and len(s['entities']['hashtags'])>0:
                
                terms=term_freq(terms,s['entities']['hashtags'])
            
    for i in sorted(terms,key=terms.get,reverse=True)[:10]:

        print i.encode('utf-8'), terms[i]
        
if __name__ == '__main__':
    main()

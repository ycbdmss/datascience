import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    if record[0]=='a':
        for i in range(5):
            key =(record[1],i)
            mr.emit_intermediate(key, record)
    else:
        for i in range(5):
            key =(i,record[2])
            mr.emit_intermediate(key, record)
            

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    
    total=0
    for i in list_of_values:
        if i[0]=='a':                    
            for j in list_of_values:
                if j[0]=='b' and i[2]==j[1]:
                    total+=i[3]*j[3]
        
                    
    mr.emit((key[0],key[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
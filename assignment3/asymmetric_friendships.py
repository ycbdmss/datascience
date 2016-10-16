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
    key1 = str(record[0])+' '+str(record[1])   
    key2 = str(record[1])+' '+str(record[0])
    mr.emit_intermediate(key1, 1)
    mr.emit_intermediate(key2, 1)
    
    
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    value=key.split(' ')
    if sum(list_of_values)==1:
        mr.emit((value[0],value[1]))
        
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
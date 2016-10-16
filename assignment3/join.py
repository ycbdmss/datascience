import sys
import MapReduce

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    value = record
         
    mr.emit_intermediate(key,value)
          

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    for i in list_of_values:
        if i[0]=='order':
            for j in list_of_values:
                if j[0]!='order':
                    mr.emit((i+j)) 
                    
    
# Part 4

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)                        

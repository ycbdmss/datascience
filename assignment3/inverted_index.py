import sys
import MapReduce

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    s=set()
    for w in words:
        if w not in s:  
            mr.emit_intermediate(w, key)
            s.add(w)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit((key, list_of_values))

# Part 4

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)                        

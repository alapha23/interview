# 2018.6.13 Gao Zhiyuan
#
import array
import random
import os

# 64kb data block, an ordered array of 8000 int64 
num_block_in_segment = 1024 # unknown
num_segment = 256           
max_distance_in_block = 8000 * 10

#try:
for seg_id in range(0, num_segment):
    segment_name = "segment_"+str(seg_id)
    os.mkdir("./data/"+segment_name)
    for x in range(0, num_block_in_segment):
        numbers = random.sample(range(x*max_distance_in_block, (x+1)*max_distance_in_block), 8000)
        numbers.sort()
        block_name = "/block_"+str(x)
        file = open("./data/"+segment_name+block_name, "w+")
        for item in numbers:
            file.write("%d, " % item)
        file.close()

#except IOError:
#        print("IO Error")
print("Sythetic data under data/")

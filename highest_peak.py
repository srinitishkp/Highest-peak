import matplotlib.pyplot as plt
def slice_array(left,right,array):
    temp=[]
    for i in range(left,right+1):
        temp.append(array[i])
    return temp
graph_indices=[]
for x in input("Enter indices separated by commas:").split(","):
    graph_indices.append(int(x)) 
peak= max(graph_indices)
peak_index=graph_indices.index(peak)
left_lower,right_lower=-1,-1
for i in range(peak_index,0,-1):
    if(graph_indices[i]>graph_indices[i-1]):
        continue
    else:
        left_lower=i
        break
for i in range(peak_index,len(graph_indices)):
    if(graph_indices[i]>graph_indices[i+1]):
        continue
    else:
        right_lower=i
        break
highest_mountain=slice_array(left_lower,right_lower,graph_indices)
plt.plot(highest_mountain)
print(f"The no. of nodes is {len(highest_mountain)}")
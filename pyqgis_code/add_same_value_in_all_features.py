#import time
#layer=iface.activeLayer()
visited_index=layer.fields().indexFromName("neighbors_")
attr_map={}
new_value = 0

#tic = time.perf_counter()
for line in layer.getFeatures():
    attr_map[line.id()] = {visited_index: new_value}
    
layer.dataProvider().changeAttributeValues(attr_map)
#toc=time.perf_counter()


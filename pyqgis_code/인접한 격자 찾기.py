layer = iface.activeLayer()
index= QgsSpatialIndex(layer.getFeatures())
featids = []
init_count=0
for feat in layer.getFeatures():
    #print("target : %s" %f.attributes()[0])
    init_count += 1
    for fid in index.intersects(feat.geometry().boundingBox()): # iterate over the index-matches. The index returns the IDs of the features where the boundingbox intersects
        if fid == feat.id(): # ignore self-intersections
            continue
        f = layer.getFeature(fid) # get the feature by the id from the index
        #print(f.attributes()[0])
        if f.geometry().intersects(feat.geometry()): # now check if not only the bounding box intersects, but if the actual features geometries intersect
            featids.append(feat.id()) # if so append the id to a list for selection afterwards
            #print("geometry : %s" %f.attributes()[0])
        
    #print("  ")    
print(init_count)
print(layer.featureCount())

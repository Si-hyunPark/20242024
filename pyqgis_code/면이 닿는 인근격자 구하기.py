# Copyright 2014 Ujaval Gandhi_GNU Genral Public License

from qgis.utils import iface
from PyQt5.QtCore import QVariant

# Names of the fields 
_NAME_FIELD = 'GRID_1K_CD'
_MIN_ID_FIELD = 'min_id'
_NEIGHBORS_FIELD = 'neighbors_'
_ID_FIELD = 'id'

# location of field 
_WHERE_GRID_N_1=17
_WHERE_GRID_N_2=18


layer = iface.activeLayer()

layer.startEditing()

# create new fields
layer_provider = layer.dataProvider()
layer_provider.addAttributes([QgsField(_MIN_ID_FIELD,QVariant.Int),QgsField(_NEIGHBORS_FIELD,QVariant.String),QgsField(_ID_FIELD,QVariant.Int)])
layer.updateFields()

# Create a dictionary of all features
feature_dict = {f.id(): f for f in layer.getFeatures()}

# Build a spatial index
index = QgsSpatialIndex()
for f in feature_dict.values():
    index.insertFeature(f)

# initialize value
min_id=0

# Loop through all features and find features that touch each feature
for f in feature_dict.values():
    ##print ('Working on %s' % f[_NAME_FIELD])
    geom = f.geometry()
    # Find all features that intersect the bounding box of the current feature.
    intersecting_ids = index.intersects(geom.boundingBox())
    ##print("intersecting_ids: %s" %intersecting_ids)
    
    # Initalize neighbors list and sum
    neighbors = []
    for intersecting_id in intersecting_ids:
        ##print(intersecting_id)
        # Look up the feature from the dictionary
        intersecting_f = feature_dict[intersecting_id]
        ##print(intersecting_id)
        # For our purpose we consider a feature as 'neighbor' if it touches or
        # intersects a feature. We use the 'disjoint' predicate to satisfy
        # these conditions. So if a feature is not disjoint, it is a neighbor.
        if (f == intersecting_f):
            f[_ID_FIELD]=intersecting_id
            
        if (not intersecting_f.geometry().disjoint(geom)):
            # add intersecting grid only touched sides including itself 면이 인접한 격자만 이웃으로 추가 자신 포함
            if (f.attributes()[_WHERE_GRID_N_1]==intersecting_f.attributes()[_WHERE_GRID_N_1] or f.attributes()[_WHERE_GRID_N_2]==intersecting_f.attributes()[_WHERE_GRID_N_2]):
                neighbors.append(intersecting_id)
                ##print("field_name %s "%field_name)
                ##print("인접 필드:")
                ##print(intersecting_f[_NAME_FIELD])
                ##print("intersecting_id : %d" %intersecting_id)
    # Find min value in neighbors_ 
    min_id=min(neighbors)
    ##print(neighbors)
    f[_MIN_ID_FIELD]=min_id
    ##print("min id : %d "%min_id)
    f[_NEIGHBORS_FIELD] = ','.join(map(str,neighbors))

####    print("SUM= %d" %neighbors_sum)
    ##print(" ")
##    f[_NEW_NEIGHBORS_FIELD] = ','.join(map(str,neighbors))
####    f[_NEW_SUM_FIELD] = neighbors_sum
#Update the layer with new attribute values.
    layer.updateFeature(f)


layer.commitChanges()
print ('Processing complete.')
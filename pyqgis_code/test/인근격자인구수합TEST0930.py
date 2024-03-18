from qgis.utils import iface
from PyQt5.QtCore import QVariant

# Replace the values below with values from your layer.
# For example, if your identifier field is called 'XYZ', then change the line
# below to _NAME_FIELD = 'XYZ'
_NAME_FIELD = 'GRID_1K_CD'
# Replace the value below with the field name that you want to sum up.
# For example, if the # field that you want to sum up is called 'VALUES', then
# change the line below to _SUM_FIELD = 'VALUES'
_SUM_FIELD = 'TOT'

# Names of the new fields to be added to the layer
_NEW_NEIGHBORS_FIELD = 'NEIGHBORS'
_NEW_SUM_FIELD = 'TOT_SUM'

layer = iface.activeLayer()

# Create 2 new fields in the layer that will hold the list of neighbors and sum
# of the chosen field.
##layer.startEditing()
##layer.dataProvider().addAttributes(
##        [QgsField(_NEW_NEIGHBORS_FIELD, QVariant.String),
##         QgsField(_NEW_SUM_FIELD, QVariant.Int)])
##layer.updateFields()
# Create a dictionary of all features
feature_dict = {f.id(): f for f in layer.getFeatures()}

#getFeatures()
features=layer.getFeatures()
 
# Build a spatial index
index = QgsSpatialIndex()
for f in feature_dict.values():
    index.insertFeature(f)
count =0
n_neighborsum=0
# Loop through all features and find features that touch each feature
for f in feature_dict.values():
    print ('Working on %s' % f[_NAME_FIELD])
    count +=1
    print("count = %d" %count)
    
    geom = f.geometry()
    # Find all features that intersect the bounding box of the current feature.
    # We use spatial index to find the features intersecting the bounding box
    # of the current feature. This will narrow down the features that we need
    # to check neighboring features.
    intersecting_ids = index.intersects(geom.boundingBox())
    # Initalize neighbors list and sum
    neighbors = []
    neighbors_sum = 0
    for intersecting_id in intersecting_ids:
        # Look up the feature from the dictionary
        intersecting_f = feature_dict[intersecting_id]
        ###print(intersecting_f[_NAME_FIELD])
        ##print(intersecting_id)
        # For our purpose we consider a feature as 'neighbor' if it touches or
        # intersects a feature. We use the 'disjoint' predicate to satisfy
        # these conditions. So if a feature is not disjoint, it is a neighbor.
        if (f != intersecting_f and
            not intersecting_f.geometry().disjoint(geom)):
            neighbors.append(intersecting_f[_NAME_FIELD])
            #for get Feature from layer which I want to choose from above repeating sentence
            _tot = intersecting_f.attributes()[5]
            print(intersecting_f[_NAME_FIELD] ,"의 TOT : %d" %_tot)
            ##print("field_name %s "%field_name)
            ##print(type(field_name))
            ##for f in features:
            ##    grid_name = f.attributes()[0]
            ##    _tot = f.attributes()[5]
                ##print("_tot type:%s " %type(_tot))
            ##    if grid_name == field_name:
            ##        n_neighbors_sum=_tot
            ##print("_tot type:%s neighbor_sum type :% s" %_tot %neighbor_sum )
            neighbors_sum = neighbors_sum + _tot
            ##print(intersecting_f[_SUM_FIELD])
            
    print(neighbors)
    print("SUM= %d" %neighbors_sum)
    print(" ")
    ##f[_NEW_NEIGHBORS_FIELD] = ','.join(neighbors)
    ##f[_NEW_SUM_FIELD] = neighbors_sum
    # Update the layer with new attribute values.
    ##layer.updateFeature(f)

##layer.commitChanges()
print ('Processing complete.')
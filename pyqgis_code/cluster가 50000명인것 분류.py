from qgis.utils import iface
from PyQt5.QtCore import QVariant

#Create new field and initialization
##layer_provider=layer.dataProvider()
##layer_provider.addAttributes([QgsField('is_cluster',QVariant.Int)])
##layer.updateFields()

# Names of the new fields to be added to the layer
_NEW_SUM_FIELD = 'TOT_SUM'
_FLAG_FIELD = 'flag'
_NAME_FIELD = 'GRID_1K_CD'
_ID_FIELD = 'id'
_LAND_FIELD = 'land'
_IS_CLUSTER_FIELD = 'is_cluster'
# location of field 
_WHERE_FLAG_FIELD=22
_WHERE_NEIGHBORS_FIELD=20
_WHERE_ID_FIELD = 21
_WHERE_TOT_FIELD = 5
_WHERE_NAME_FIELD = 0
_WHERE_TOT_SUM_FIELD = 23
_WHERE_LAND_FIELD=24
_WHERE_IS_CLUSTER_FIELD = 25


layer = iface.activeLayer()

layer.startEditing()

# Create a dictionary of all features
feature_dict = {f.id(): f for f in layer.getFeatures()}

land_list =[]
for a in feature_dict.values():
    my_list_a = str(a.attributes()[_WHERE_NEIGHBORS_FIELD]) 
    my_list_a = my_list_a.split(',')
    if (a.attributes()[_WHERE_TOT_SUM_FIELD] >= 50000 ):  
        land_list.append(a.attributes()[_WHERE_LAND_FIELD])
        print(land_list)   
for a in feature_dict.values():
    my_list_a = str(a.attributes()[_WHERE_NEIGHBORS_FIELD]) 
    my_list_a = my_list_a.split(',')
    for b in range(len(land_list)):
        if(land_list[b]==a.attributes()[_WHERE_LAND_FIELD]):
            a[_IS_CLUSTER_FIELD] = 1
            ##print("name:%d land:%d cluster_field가 업데이트 되었다" %(a[_WHERE_ID_FIELD],a[_WHERE_LAND_FIELD]))
            layer.updateFeature(a)
            
       
##print(land_list)
##layer.commitChanges()
print ('Processing complete.')
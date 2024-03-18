from qgis.utils import iface
from PyQt5.QtCore import QVariant

#Create new field and initialization
layer_provider=layer.dataProvider()
layer_provider.addAttributes([QgsField('TOT_SUM',QVariant.Int)])
layer.updateFields()


# Names of the new fields to be added to the layer
_NEW_SUM_FIELD = 'TOT_SUM'
_FLAG_FIELD = 'flag'
_NAME_FIELD = 'GRID_1K_CD'

# location of field 
_WHERE_FLAG_FIELD=22
_WHERE_NEIGHBORS_FIELD=20
_WHERE_ID_FIELD = 21
_WHERE_TOT_FIELD = 5

layer = iface.activeLayer()

layer.startEditing()

# Create a dictionary of all features
feature_dict = {f.id(): f for f in layer.getFeatures()}

for a in feature_dict.values():
    n_neighborsum=0
    my_list_a = str(a.attributes()[_WHERE_NEIGHBORS_FIELD]) 
    my_list_a = my_list_a.split(',')
    if (a.attributes()[_WHERE_FLAG_FIELD] == 0 and len(my_list_a)>1):  ##flag==0
        ##print(my_list_a)
        ##print(len(my_list_a))
        ##print("%s 의 리스트 : %s" %(a[_NAME_FIELD], my_list_a))
        for i in range(len(my_list_a)):  ##a의 neighbors_를 돌면서 
            number=my_list_a[i]  ##a의 i번째 이웃
            ##print("number : %s" %number)
            number=int(number)
            for b in feature_dict.values():
                
                if (b.attributes()[_WHERE_ID_FIELD]==number):
                    ##print("%s의 id : %s" %(b[_NAME_FIELD],b.attributes()[_WHERE_ID_FIELD]))

                    n_neighborsum= n_neighborsum + b.attributes()[_WHERE_TOT_FIELD]
                    ##print("tot은 : %d" %b.attributes()[_WHERE_TOT_FIELD])
                a[_NEW_SUM_FIELD]=n_neighborsum
                
        ##print("%s 의 합 : %d" %(a[_NAME_FIELD],n_neighborsum))
        ##print(" ")
        layer.updateFeature(a)
    a[_NEW_SUM_FIELD] = n_neighborsum 
        
    
##layer.commitChanges()
print ('Processing complete.')
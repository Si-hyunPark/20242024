from qgis.utils import iface
from PyQt5.QtCore import QVariant


#Create new field and initialization
layer_provider=layer.dataProvider()
layer_provider.addAttributes([QgsField('TOT_SUM',QVariant.Int),QgsField('land',QVariant.Int)])
layer.updateFields()

# Names of the new fields to be added to the layer
_NEW_SUM_FIELD = 'TOT_SUM'
_FLAG_FIELD = 'flag'
_NAME_FIELD = 'GRID_1K_CD'
_ID_FIELD = 'id'
_LAND_FIELD = 'land'
# location of field 
_WHERE_FLAG_FIELD=22
_WHERE_NEIGHBORS_FIELD=20
_WHERE_ID_FIELD = 21
_WHERE_TOT_FIELD = 5
_WHERE_NAME_FIELD = 0


layer = iface.activeLayer()

layer.startEditing()

# Create a dictionary of all features
feature_dict = {f.id(): f for f in layer.getFeatures()}

land =0 

for a in feature_dict.values():
    sum=0
    my_list_a = str(a.attributes()[_WHERE_NEIGHBORS_FIELD]) 
    my_list_a = my_list_a.split(',')
    if (a.attributes()[_WHERE_FLAG_FIELD] == 0 and len(my_list_a)>1):  ##flag==0
        number=a.attributes()[_WHERE_ID_FIELD]
        for i in range(len(my_list2)):
            number2=my_list2[i][0]
            number2=int(number2)
            if (number2==number):
                for j in range(1,len(my_list2[i])):
                    for b in feature_dict.values():
                        id=int(my_list2[i][j])
                        if(id==b.attributes()[_WHERE_ID_FIELD]):
                            TOT=b.attributes()[_WHERE_TOT_FIELD]
                            sum += TOT
                            ##print("%d의 TOT은 %d" %(b[_ID_FIELD],b[_WHERE_TOT_FIELD]))
                            ##print("%d의 sum은 %d" %(b[_ID_FIELD], sum))
                            b[_LAND_FIELD]=land
                            layer.updateFeature(b)
                            
        if (sum>=50000):
            a[_NEW_SUM_FIELD] = sum
            layer.updateFeature(a)
        land +=1
            
        ##print("id: %d name:%s 의  Sum_tot은 %d" %(a.attributes()[_WHERE_ID_FIELD],a.attributes()[_WHERE_NAME_FIELD],sum))
        ##print(" ")

##layer.commitChanges()
print ('Processing complete.')
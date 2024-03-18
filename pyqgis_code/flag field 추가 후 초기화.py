#Create new field and initialization
layer_provider=layer.dataProvider()
layer_provider.addAttributes([QgsField('flag',QVariant.Int)])
layer.updateFields()

visited_index=layer.fields().indexFromName("flag")
attr_map={}
new_value = 0

for line in layer.getFeatures():
    attr_map[line.id()] = {visited_index: new_value}
layer.dataProvider().changeAttributeValues(attr_map)
print ('Processing complete.')
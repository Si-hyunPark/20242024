pv = layer.dataProvider()
pv.addAttributes([QgsField('grid_num_1',QVariant.Int),QgsField('grid_num_2',QVariant.Int)])
layer.updateFields()

expression1=QgsExpression('substr("GRID_1K_CD",3,2)')
expression2=QgsExpression('substr("GRID_1K_CD",5,2)')

context = QgsExpressionContext()
context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(layer))

with edit(layer):
    for f in layer.getFeatures():
        context.setFeature(f)
        f['grid_num_1']=expression1.evaluate(context)
        f['grid_num_2']=expression2.evaluate(context)
        layer.updateFeature(f)
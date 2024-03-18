from PyQt5.QtCore import QVariant
layer_provider=layer.dataProvider()
layer_provider.addAttributes([QgsField("min_id",QVariant.Int)])
layer.updateFields()
from PyQt5 import QtCore, QtGui, QtWidgets

targetField = 'lbl_int'
rangeList = []
opacity = 1

# define value ranges
minVal = 1500
maxVal = 99999999999999

# range label
lab = 'Group 1'

# color (yellow)
rangeColor = QtGui.QColor('#ffee00')

# create symbol and set properties
symbol1 = QgsSymbol.defaultSymbol(layer.geometryType())
symbol1.setColor(rangeColor)
symbol1.setOpacity(opacity)

#create range and append to rangeList
range1 = QgsRendererRange(minVal, maxVal, symbol1, lab)
rangeList.append(range1)



# define value ranges
minVal = 300
maxVal = 1499

# range label
lab = 'Group 2'

# color (yellow)
rangeColor = QtGui.QColor('#00eeff')

# create symbol and set properties
symbol2 = QgsSymbol.defaultSymbol(layer.geometryType())
symbol2.setColor(rangeColor)
symbol2.setOpacity(opacity)

#create range and append to rangeList
range2 = QgsRendererRange(minVal, maxVal, symbol2, lab)
rangeList.append(range2)



#groupRenderer = QgsGraduatedSymbolRenderer('',rangeList)
#groupRenderer.setMode(QgsGraduatedSymbolRenderer.EqualInterval)
#groupRenderer(groupRenderer)

#layer.setRenderer(groupRenderer)

QgsProject.instance().addMapLayer(layer)
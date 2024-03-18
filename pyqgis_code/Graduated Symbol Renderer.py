from PyQt5 import QtGui

myVectorLayer = QgsVectorLayer("C:/Users/User/Desktop/지역분류체계/urban_emd_20/인구격자읍면동_20_부산/orginal","", "ogr")
myTargetField = 'TOT'
myRangeList = []
myOpacity = 0.6
# Make our first symbol and range...
myMin = 0.0
myMax = 299.0
myLabel = 'Group 1'
myColour = QtGui.QColor('yellow')
mySymbol1 = QgsSymbol.defaultSymbol(myVectorLayer.geometryType())
mySymbol1.setColor(myColour)
mySymbol1.setOpacity(myOpacity)
myRange1 = QgsRendererRange(myMin, myMax, mySymbol1, myLabel)
myRangeList.append(myRange1)
#now make another symbol and range...
myMin = 300.0
myMax = 1499.0
myLabel = 'Group 2'
myColour = QtGui.QColor('blue')
mySymbol2 = QgsSymbol.defaultSymbol(myVectorLayer.geometryType())
mySymbol2.setColor(myColour)
mySymbol2.setOpacity(myOpacity)
myRange2 = QgsRendererRange(myMin, myMax, mySymbol2, myLabel)
myRangeList.append(myRange2)

myMin = 1500.0
myMax = 9999999999
myLabel = 'Group 3'
myColour = QtGui.QColor('red')
mySymbol3 = QgsSymbol.defaultSymbol(myVectorLayer.geometryType())
mySymbol3.setColor(myColour)
mySymbol3.setOpacity(myOpacity)
myRange3 = QgsRendererRange(myMin, myMax, mySymbol3, myLabel)
myRangeList.append(myRange3)


myRenderer = QgsGraduatedSymbolRenderer('', myRangeList)
myRenderer.setMode(QgsGraduatedSymbolRenderer.EqualInterval)
myRenderer.setClassAttribute(myTargetField)

myVectorLayer.setRenderer(myRenderer)
QgsProject.instance().addMapLayer(myVectorLayer)

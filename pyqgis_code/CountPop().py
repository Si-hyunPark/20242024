import sys


def CountPop(a,b):
    layer=iface.activeLayer()
    layer.startEditing()
    fc=layer.featureCount()
    for f in layer.getFeatures():
        if f["gid_num_1"]==a and f["gid_num_2"]==b:
            #global k 
            #k = f
            #print(f.attributes()[3])
            city=f.attributes()[9]
            print(f.attributes()[3])
            
            if city == 1:
                sys.setrecursionlimit(9999999)
                print("it's city")
                print(f.attributes()[3])
                layer.changeAttributeValue(f.id(),9,'4')
                print(f.attributes()[9])
                layer.updateFeature(f)
                print("after update")
                print(f.attributes()[9])

                x=f.attributes()[10]
                y=f.attributes()[11]
                print(x,y)
                print("return:")
                return f.attributes()[3]+ CountPop(x,y+1) + CountPop(x-1,y)+ CountPop(x+1,y)+ CountPop(x,y-1)
    
CountPop(21,84)
    
    

#layer=iface.activeLayer()
#fc = layer.featureCount()


#for i in range(0,fc):
#    if '"TOT">=1500' 
#    feat = layer.getFeature(i)
    
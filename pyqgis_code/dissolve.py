##dissolve
layer=iface.activeLayer()

_LAND_FIELD = 24
import processing

infn = "C:/Users/User/Desktop/지역분류체계/urban_emd_20/인구격자읍면동_20_부산/1007test/is_cluster_1.shp"
outfn2="C:/Users/User/Desktop/지역분류체계/urban_emd_20/인구격자읍면동_20_부산/1007test/dissolve1007.shp"

processing.run("native:dissolve",{'INPUT':infn, 'FIELD':[_IS_CLUSTER_FIELD],'OUTPUT':outfn2})
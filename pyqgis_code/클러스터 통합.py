from qgis.utils import iface
from PyQt5.QtCore import QVariant

# Names of the fields
_NAME_FIELD = 'GRID_1K_CD'
_MIN_ID_FIELD = 'min_id'
_NEW_NEIGHBORS_FIELD = 'neighbors_'
_ID_FIELD = 'id'
_FLAG_FIELD = 'flag'

# location of field 
_WHERE_FLAG_FIELD=22
_WHERE_NEIGHBORS_FIELD=20
_WHERE_ID_FIELD=21
_WHERE_TOT_FIELD = 5

layer = iface.activeLayer()

layer.startEditing()

# Create a dictionary of all features
feature_dict = {f.id(): f for f in layer.getFeatures()}

my_list_a=[]
my_list_b=[]
my_list=[]
my_list2=[]


# Make two pointers 
for a in feature_dict.values():
    for b in feature_dict.values():
        ##print ('Working on %s and %s' % (a[_NAME_FIELD], b[_NAME_FIELD]))
    
    # Initalize neighbors list
        neighbors = []
        ## not the one to compare itself and unmodified grid
        if (a[_ID_FIELD] != b[_ID_FIELD]):  ##비교 대상이 자신이 아니고
            if (a.attributes()[_WHERE_FLAG_FIELD] == 0 and b.attributes()[_WHERE_FLAG_FIELD] == 0 ):  ##통합 되지 않은 격자 중 
                my_list_a = str(a.attributes()[_WHERE_NEIGHBORS_FIELD]) 
                my_list_a = my_list_a.split(',')
                ##print("My list : %s" %my_list_a)
                # Check the a_neighbor one by one
                for i in range(len(my_list_a)):  ##a의 neighbors_를 돌면서 
                    number=my_list_a[i]  ##a의 i번째 이웃
                    my_list_b = str(b.attributes()[_WHERE_NEIGHBORS_FIELD])
                    my_list_b = my_list_b.split(',')
                    
                    # Check elements of a_neighbor is in b_neighbors and both of them are unmodified
                    if((number in my_list_b) and (a[_FLAG_FIELD] == 0 )and (b[_FLAG_FIELD] == 0)): ##만약 b의 neighbors_ 중에 a의 원소가 있고, flag==0 이라면 
                        ##print("common number is %s" %number)
                        ##print("My list b : %s " %b.attributes()[_WHERE_NEIGHBORS_FIELD])
                        ###my_list_b = b.attributes()[_WHERE_NEIGHBORS_FIELD].split(',')
                        ###my_list_a = a.attributes()[_WHERE_NEIGHBORS_FIELD].split(',')
                        ##print(my_list_a)
                        ##print(my_list_b)
                        
                        # Combine a_neighbors and b_neighbors
                        my_list= my_list_a + my_list_b
                        ##print(my_list)
                        
                        # Remove duplicate elements
                        new_list=[]
                        new_list.append(b.attributes()[_WHERE_ID_FIELD])
                        for v in my_list:
                            if v not in new_list:
                                new_list.append(v)
                        print("id: %d grid: %s 의 new list : %s" %(b[_ID_FIELD],b[_NAME_FIELD], new_list))
                        my_list2.append(new_list)
                        
                        a[_FLAG_FIELD] = 1
                        ##b[_NEW_NEIGHBORS_FIELD] = new_list
                        b[_NEW_NEIGHBORS_FIELD]=','.join(map(str,new_list))
                        layer.updateFeature(a)
                        layer.updateFeature(b)

    print(" ")
    
layer.commitChanges()
print ('Processing complete.')
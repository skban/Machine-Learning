#################################################################################################################################################################################################################################################################################################
#4.1 ConceptLearning
D = pd.DataFrame({"Length":[3,4,3,5,5,5,4,5,4,4],"Gills":['no','no','no','no','no','yes','yes','yes','yes','no'],"Beak":['yes','yes','yes','yes','yes','yes','yes','no','no','yes'],"Teeth":['many','many','few','many','few','many','many','many','many','few'],"target":[1,1,1,1,1,0,0,0,0,0]})
#################################################################################################################################################################################################################################################################################################
a=0
possible_instances=[]
for i, Length in enumerate(sorted(D.Length.unique().tolist(),reverse=False)):
    for j, Gills in enumerate(sorted(D.Gills.unique().tolist(),reverse=True)):
        for k, Beak in enumerate(sorted(D.Beak.unique().tolist(),reverse=True)):
            for l, Teeth in enumerate(sorted(D.Teeth.unique().tolist(),reverse=True)):
                a=a+1
                print(a,"Length="+str(Length),"&","Gills="+str(Gills),"&","Beak="+str(Beak),"&","Teeth="+str(Teeth))
                possible_instances.append(set(sorted(["Length="+str(Length),"Gills="+str(Gills),"Beak="+str(Beak),"Teeth="+str(Teeth)],reverse=False)))
len(possible_instances), possible_instances

#################################################################################################################################################################################################################################################################################################
#Algorithm 4.2: LGG-Conj(x, y) – find least general conjunctive generalisation of two conjunctions.
#################################################################################################################################################################################################################################################################################################
def LGGConj(x, y):
    z= x & y
    return z
#print('x',possible_instances[4])
#print('y',possible_instances[12])
##Test
#print("LGGConj(x, y):",LGGConj(possible_instances[4], possible_instances[12]))

#################################################################################################################################
#Input  : data D  possible_instances
#Output : logical expressions H.
#################################################################################################################################################################################################################################################################################################
def LGGSet(d):
    j=0
    instances = d
    instances_len = len(instances)
    x= instances[j]
    print("############################################################################################################")
    h=x
    print(j, "x", x,"(Conjunction)","h", h)
    print("############################################################################################################")
    instances_left = instances_len -1
    while j<instances_left:
        j = j+1
        #print(j)
        x = instances[j]
        if len(LGGConj(h,x)) > 0:
            print("######################################################################################################")
            print(j, "Conjunction of x and h")
            #print("x", x)
            print("h", h)
            h = LGGConj(h,x)
            print("------------------------------------------------------------------------------------------------------")
            print("LGGConj(h,x)-->")
            print("------------------------------------------------------------------------------------------------------")
            print(h)
            print("######################################################################################################")
            #instances_left = instances_left-1
    return h
#################################################################################################################################################################################################################################################################################################

#Input  : data D  possible_instances
#Output : logical expressions H.
def LGGSet(d):
    j=0
    instances = d
    instances_len = len(instances)
    x= instances[j]
    h=x
    instances_left = instances_len -1
    while j<instances_left:
        j = j+1
        x = instances[j]
        h = LGGConj(h,x)
    return h

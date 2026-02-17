a = int(input("Enter the number of weighted values "))
x = []
for i in range(a):
    y = int(input("Enter the weighted value "))
    x.append(y)
normal_load  = []
heavy_load = []
overload = []
invalid_entries =[]
very_light =[]
for i in x:
    if i < 0:
        invalid_entries.append(i)
    elif i >= 0 and i <= 5:
        very_light.append(i)
    elif i >= 6 and i <= 25:
        normal_load.append(i)
    elif i >= 26 and i <= 60:
       heavy_load.append(i)
    else:
        overload.append(i)
total_valid=len(very_light)+len(normal_load)+len(heavy_load)+len(overload)
total_affected=0
L = 14
PLI = L%3
if PLI == 0:
    print("Rule A is applied ")
    invalid_entries = overload + invalid_entries
    total_affected = len(overload)
elif PLI == 1:
    print("Rule B is applied ")
    total_affected=len(very_light)
    del very_light
elif PLI == 2:
    print("Rule C is applied ")
    total_affected=len(overload)+len(invalid_entries)+len(very_light)
    del overload
    del invalid_entries, very_light
print("Total valid weights are ",total_valid)
print("Affected items due to PLI are",total_affected)
print("L and PLI are", L,PLI)
print("normal load ",normal_load)
print("heavy load ",heavy_load)




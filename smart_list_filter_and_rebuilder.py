
n=int(input("Enter number of inputs : "))
data = []
for i in range(n):
    k=input("Enter data:")
    if k.isdigit():
        data.append(int(k))
    else:
        data.append(k)
Number_list = []
String_list = []
count_numbers = 0
count_strings =0
for x in data:
    if type(x) == int:
        Number_list.append(x)
        count_numbers+=1
    elif x=="":
        continue
    else:
        String_list.append(x)
        count_strings+=1
section=input("Enter section : ")
if section=="A":
    print("Section A : Number list :",Number_list)
elif section=="B":
    print("Section B : String list :",String_list)
elif section=="C":
    print("String list :", String_list)
    print("Number list :", Number_list)
print("Total numbers :",count_numbers)
print("Total strings :",count_strings)





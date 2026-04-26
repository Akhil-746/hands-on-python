import copy

def create():
    return [
        {"id":1,"data":{"files":["x.txt","y.txt"],"usage":200}},
        {"id":2,"data":{"files":["z.txt"],"usage":150}}
    ]

def make_copies(d):
    a = d
    b = list(d)
    c = copy.deepcopy(d)
    return a,b,c

def change(d):
    for i in d:
        if i["data"]["files"]:
            i["data"]["files"].pop()
        i["data"]["usage"] += 20

def check(o,s,d):
    leak = 0
    safe = 0
    overlap = 0
    for i in range(len(o)):
        if o[i]["data"]["files"] == s[i]["data"]["files"]:
            leak += 1
        if o[i]["data"]["files"] != d[i]["data"]["files"]:
            safe += 1
        overlap += len(set(o[i]["data"]["files"]) & set(s[i]["data"]["files"]))
    return (leak,safe,overlap)

def show(n,d):
    print("\n",n)
    for i in d:
        print(i)

data = create()
a,b,c = make_copies(data)

print("Before")
show("Original",data)
show("Shallow",b)
show("Deep",c)

change(a)
change(b)
change(c)

print("\nAfter")
show("Original",data)
show("Shallow",b)
show("Deep",c)

print("\nResult:",check(data,b,c))
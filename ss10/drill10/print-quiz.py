i = {
    "q" : "mot ngay co bao nhieu gio :",
    "a" : [12,23,24,15],
}
print(i["q"])
for n,m in enumerate(i["a"]):
    print(n+1,m,sep=". ")
j = int(input("cau tra loi: "))
if j == 3:
    print("dung")
else:
    print("sai")

a = {
    "n1": 100, "n2" : 20, "n3" : 7
}
# Akses Dictionary
print(a['n2'])
print(a.keys())
print(a.values())
print(a.items())

# Mengubah elment
a["n2"] = 10
# Menambah element Dictionary
a['n4'] = 50

# Sesudah di tambahkan 
print(a['n2'])
print(a.keys())
print(a.values())
print(a.items(),"\n")

# Loop Dictionary 
for item in a.items():
    print(item)
    print(item[0])
#HashTable O(1) insertion, O(1) amortized lookup

#Hash tables in python are implememented with the dictionary data structure
hash_table = {}

#to insert a kv pair, address as an array
hash_table["hello"] = "world"
hash_table["foo"] = "bar"

#to access values, access them using the key
print(hash_table["hello"])

#to check if a key exists, use the in keyword
if "hello" in hash_table:
    print("hello is in hash_table")

#to remove, use del
del hash_table["foo"]
print("hash table after deletion", hash_table)

#use a for loop to iterate over kv pairs combined with the items() method
for key, value in hash_table.items():
    print(f"{key}: {value}")


#dictionaries (and hashtables) can also be compared to eachother
#useful for anagram problem on LC for example

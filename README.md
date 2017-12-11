# data-structures

### Hash Table

```
Using a naive hash and Horner's Rule, HashTable() will store based on the supplied key, which must be a string. By default, HashTable() uses the naive hash method, but can be changed on initialization. 

To create an instance if the hash table, HashTable(), from python:

new = HashTable() *you may initiate the table with any size, must be integer, as the first arguement in the function. You may also pass in an alternative hashing method. A naive hash will be used my defaul, but you may also choose `horner_hash` as the second arguement on initialization, or any hashing function you choose to import. For example: HashTable(100000, horner_hash).*

HashTable() contains the following methods:
* _set(key, val) (O(n))_ - sets a value at a given key (must me string) in the table, if key already has value it will be set to new value.
* _get(key) (0(n))_ - retrieve the value of the item with the given key.
* _ _hash(key) (O(n))_ - hashes key and returns an integer between 0 and the size of the table.

To access any contained methods:
new.set(key, val)
new.get(key)
```
### Trie

```
In order to efficiently store words, Trie() will provide a class by which nodes are only inserted if unshared by anthor word. All words share previous characters when possible.

To create an instance if the trie, Trie(), from python:

new = Trie() *you may not initiate the trie with any values.*

Trie() contains the following methods:
* _insert(string) (O log(n))_ - inserts a new node for every letter in string (input must be word) if not able to share with another word.
* _contains(string) (0 log(n))_ - returns True if word is in trie and False if not.
* _size() (O(1))_ - retruns the number of words in the trie.
* _remove(string) (O log(n))_ - removes word from trie and raises error if word not in trie.

To access any contained methods:
new.insert(string)
new.contains(string)
new.size()
new.remove(string)
```
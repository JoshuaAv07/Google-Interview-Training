from trie import Trie

t = Trie()
t.insert("hello")
t.insert("helium")
t.insert("hero")

print(t.search("hello"))
print(t.search("helium"))
print(t.search("her"))    
print(t.starts_with("he"))
print(t.starts_with("ha"))

t.delete("hello")
print(t.search("hello")) 
print(t.search("helium"))
# ----------------------------
# Collections
# ----------------------------

# len(): length of a list/string/dict/etc.
print(len([1, 2, 3]))         # 3
print(len("hello"))           # 5

# set(): remove duplicates
print(set([1, 1, 2, 3, 3]))   # {1, 2, 3}

# list(), dict(), tuple()
print(list("abc"))            # ['a', 'b', 'c']
print(tuple([1, 2, 3]))       # (1, 2, 3)
print(dict([(1, 'a'), (2, 'b')]))  # {1: 'a', 2: 'b'}

# sum(): add values
print(sum([1, 2, 3, 4]))      # 10

# max() and min()
print(max([3, 7, 2, 5]))      # 7
print(min([3, 7, 2, 5]))      # 2

# sorted(): returns sorted list
print(sorted([3, 1, 4, 2]))   # [1, 2, 3, 4]
print(sorted(["banana", "apple", "cherry"])) # ['apple', 'banana', 'cherry']

# any() and all()
print(any([0, 1, 0]))         # True (because at least one True)
print(all([1, 1, 1]))         # True (because all are True)
print(all([1, 0, 1]))         # False

# ----------------------------
# Numbers & math
# ----------------------------

# abs(): absolute value
print(abs(-7))                # 7

# round(): round to nearest integer (or decimals if given)
print(round(3.14159, 2))      # 3.14

# pow(): exponentiation
print(pow(2, 3))              # 8 (same as 2**3)

# divmod(): quotient and remainder
print(divmod(10, 3))          # (3, 1) → 10 // 3 = 3, 10 % 3 = 1

# ----------------------------
# Iteration helpers
# ----------------------------

# range(): sequence of numbers
for i in range(3):
    print(i)                  # 0, 1, 2

# enumerate(): index + value
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)             # (0, 'a'), (1, 'b'), (2, 'c')

# zip(): combine iterables
for a, b in zip([1, 2, 3], ['x', 'y', 'z']):
    print(a, b)               # (1, 'x'), (2, 'y'), (3, 'z')

# map(): apply function
nums = [1, 2, 3, 4]
print(list(map(lambda x: x*2, nums)))   # [2, 4, 6, 8]

# filter(): keep only items that satisfy condition
print(list(filter(lambda x: x % 2 == 0, nums))) # [2, 4]

# ----------------------------
# Strings (methods, not functions)
# ----------------------------

s = "  Hello World  "
print(s.lower())              # "  hello world  "
print(s.upper())              # "  HELLO WORLD  "
print(s.strip())              # "Hello World" (remove spaces)
print("apple,banana,cherry".split(","))  # ['apple', 'banana', 'cherry']
print("-".join(["a", "b", "c"]))         # "a-b-c"

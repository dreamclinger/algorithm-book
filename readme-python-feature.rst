Address of variable, different after +=
====
>>> x = "abc"
>>> id(x)
11173824
>>> x += "def"
>>> id(x)
32831648
>>> x
'abcdef'

Address of list, the same after opera.append
====
>>> y = [1, 2]
>>> id(y)
32413376
>>> y += [2, 3]
>>> id(y)
32413376
>>> y
[1, 2, 2, 3]

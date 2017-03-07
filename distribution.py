"""
distribution.py
Author: Emma Supattapone
Credit: Abby Feyrer

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string
txt = input("Please enter a string of text (the bigger the better): ").lower()
print('The distribution of characters in "' + txt + '" is:')
al = txt.count('a')
a = ("a" * al)

bl = txt.count('b')
b = ("b" * bl)

cl = txt.count('c')
c = ("c" * cl)

dl = txt.count('d')
d = ("d" * dl)

el = txt.count('e')
e = ("e" * el)

fl = txt.count('f')
f = ("f" * fl)

gl = txt.count('g')
g = ("g" * gl)

hl = txt.count('h')
h = ("h" * hl)

il = txt.count('i')
i = ("i" * il)

jl = txt.count('j')
j = ("j" * jl)

kl = txt.count('k')
k = ("k" * kl)

ll = txt.count('l')
l = ("l" * ll)

ml = txt.count('m')
m = ("m" * ml)

nl = txt.count('n')
n = ("n" * nl)

ol = txt.count('o')
o = ("o" * ol)

pl = txt.count('p')
p = ("p" * pl)

ql = txt.count('q')
q = ("q" * ql)

rl = txt.count('r')
r = ("r" * rl)

sl = txt.count('s')
s = ("s" * sl)

tl = txt.count('t')
t = ("t" * tl)

ul = txt.count('u')
u = ("u" * ul)

vl = txt.count('v')
v = ("v" * vl)

wl = txt.count('w')
w = ("w" * wl)

xl = txt.count('x')
x = ("x" * xl)

yl = txt.count('y')
y = ("y" * yl)

zl = txt.count('z')
z = ("z" * zl)



#t = [a, b, c]

e = [al, bl, cl, dl, el, fl, gl, hl, il, jl, kl, ll, ml, nl, ol, pl, ql, rl, sl, tl, ul, vl, wl, xl, yl, zl]
e.sort()
e.reverse()

listo = zip([-al,-bl,-cl],[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z])

listoo = (sorted(list(listo)))
print(listoo)

for x in e:
    print(x)







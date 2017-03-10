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
txt = input("Please enter a string of text (the bigger the better): ")
print('The distribution of characters in "' + txt + '" is: ')
txt.lower()

al = txt.count('a')
bl = txt.count('b')
cl = txt.count('c')
dl = txt.count('d')
el = txt.count('e')
fl = txt.count('f')
gl = txt.count('g')
hl = txt.count('h')
il = txt.count('i')
jlb = txt.count('j')
kl = txt.count('k')
ll = txt.count('l')
ml = txt.count('m')
nl = txt.count('n')
ol = txt.count('o')
pl = txt.count('p')
ql = txt.count('q')
rl = txt.count('r')
sl = txt.count('s')
tl = txt.count('t')
ul = txt.count('u')
vl = txt.count('v')
wl = txt.count('w')
xl = txt.count('x')
yl = txt.count('y')
zl = txt.count('z')





em = [al, bl, cl, dl, el, fl, gl, hl, il, jlb, kl, ll, ml, nl, ol, pl, ql, rl, sl, tl, ul, vl, wl, xl, yl, zl]

a = ("a" * al)
b = ("b" * bl)
c = ("c" * cl)
db = ("d" * dl)
e = ("e" * el)
f = ("f" * fl)
g = ("g" * gl)
hb = ("h" * hl)
i = ("i" * il)
j = ("j" * jlb)
k = ("k" * kl)
l = ("l" * ll)
m = ("m" * ml)
n = ("n" * nl)
o = ("o" * ol)
p = ("p" * pl)
q = ("q" * ql)
r = ("r" * rl)
s = ("s" * sl)
t = ("t" * tl)
u = ("u" * ul)
v = ("v" * vl)
w = ("w" * wl)
x = ("x" * xl)
y = ("y" * yl)
z = ("z" * zl)

am = [a, b, c, db, e, f, g, hb, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
emm = [0 - x for x in em]


listo = list(zip(emm, am))
listo.sort()

for (x, y) in listo:
    print(y)







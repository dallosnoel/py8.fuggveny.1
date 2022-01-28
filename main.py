'''
1. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat) összeadja és az összegükkel tér vissza! 
A program tartalmazza a függvény hívását is!
'''

def osszegzo(*args):
  return sum(args)

print(osszegzo(1, 7, 9))




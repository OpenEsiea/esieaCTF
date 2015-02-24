# Titre
Blaise like banana

# Description
Un certain Blaise aurait chiffré un text d'une valeur inestimable aidez la NSA a retrouvé son texte en trouvant la clé

# How to 

on ouvrant le fichier cyphertext, on découvre plusieurs charabias, 
mais on sait que notre flag sera sous la forme de Esiea{xx} après une petite recherche dans le fichier, 
on trouve cqgcy{yjjwmspzyqcypczcjmlermsq}, on remarque que c'est un cesar . 

Voilà donc un petit code en python qui testera 10 cle de cesar afin de trouver le message clair..

```python
#!/usr/bin/python

import os
import time

message = "cqgcy{yjjwmspzyqcypczcjmlermsq}"
nbtime = 0
mymsg = ""

def decrypt(n):
	newc = 0
	todd = 0
	decrypted = ""
	for i in range(0,len(message)):
		if message[i] != '{' and message[i] != '}':
			if ord(message[i]) + n > 122:
				toadd = (ord(message[i]) + n) - 122
				newc = 96 + toadd
			else:	
				newc = ord(message[i]) + n
			decrypted = decrypted + chr(newc)
			i= i + 1

	return decrypted

while(1):
	for i in range(1, 10):
		print decrypt(i)
		if i == 9:
			exit(1)
		i = i + 1
	time.sleep(2)
```
on obtient un résultat sous forme de :

drhdzzkkxntqazrdzqdadknmfsntr
esieaallyourbasearebelongtous
ftjfbbmmzpvscbtfbsfcfmpohupvt
gukgccnnaqwtdcugctgdgnqpivqwu
hvlhddoobrxuedvhduhehorqjwrxv
iwmieeppcsyvfewievifipsrkxsyw
jxnjffqqdtzwgfxjfwjgjqtslytzx
kyokggrreuaxhgykgxkhkrutmzuay
lzplhhssfvbyihzlhylilsvunavbz

d'ou notre flag esieaallyourbasearebelongtous , il suffit juste de l'écrire sous forme de esiea{xxx}


# Flag
esiea{allyourbasearebelongtous}

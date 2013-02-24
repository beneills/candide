#!/usr/bin/env python
# coding: utf-8

# Analyze the Frnehc text of Candide
# Uncopyright, Ben Eills, 2013

import re, sys

# read text from file specified by first arg
with open(sys.argv[1], 'r') as f: text = f.read()

word_tags = {'optimisme' :  ['optimisme', 'espoir', 'euphorie', 'insouciance',
                             'rêve bleu', 'bonheur', 'joie', 'félicité',
                             'plaisir', 'bien-être', 'béatitude', 'bien',
                             'prospérité', 'chance', 'satisfaction', 'succès'],

             'pessimisme' : ['pessimisme', 'mélancolie', 'bile', 'crainte',
                             'défaitisme', 'inquiétude', 'dépression',
                             'nervosité', 'neurasthénie', 'noirceur', 'sombreur',
                             'malheur', 'tribulation', 'calamité', 'affliction',
                             'catastrophe', 'épreuve', 'accident', 'chagrin',
                             'malchance', 'ennui', 'infortune', 'craindre',
                             'redouter', 'appréhender', 'pressentir',
                             'avoir peur', 'plaindre', 'regretter']}


def indexes(needle):
    return [m.start() for m in re.finditer(needle, text)]


occurrences = {k : sum(map(indexes, v), []) for k, v in word_tags.items()}

oo = occurrences['optimisme']
op = occurrences['pessimisme']

print occurrences


import matplotlib.pyplot as plt

plt.plot(oo, [1]*len(oo), 'bo', label='optimisme') # optimisme
plt.plot(op, [1]*len(op), 'ro', label='pessimisme') # pessimisme

plt.annotate("XX: WHAT HAPPENED AT SEA\nTO CANDIDE AND MARTIN", xy=(105323, 0.999), xytext=(90000, 0.97),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.annotate("Pangloss describes being hanged", xy=(168459, 1.001), xytext=(130000, 1.02),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )


plt.legend()
plt.xlabel(u'Index de Caractère dans le texte francais de Candide')
plt.ylabel(u'?')
plt.show()

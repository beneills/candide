#!/usr/bin/env python
# coding: utf-8

# Analyze the French text of Candide
# Uncopyright, Ben Eills, 2013

import re, sys
from collections import OrderedDict
import matplotlib.pyplot as plt

# Read text from file specified by first arg
if len(sys.argv) < 2:
    exit("Error: please supply input text file.")
with open(sys.argv[1], 'r') as f:
    text = f.read()
    length = len(text)

# Synonym dictionary
word_tags = OrderedDict([('optimisme',  ['optimisme', 'espoir', 'euphorie', 'insouciance',
                                        'rêve bleu', 'bonheur', 'joie', 'félicité',
                                        'plaisir', 'bien-être', 'béatitude', 'bien',
                                        'prospérité', 'chance', 'satisfaction', 'succès']),

                         ('pessimisme', ['pessimisme', 'mélancolie', 'bile', 'crainte',
                                         'défaitisme', 'inquiétude', 'dépression',
                                         'nervosité', 'neurasthénie', 'noirceur', 'sombreur',
                                         'malheur', 'tribulation', 'calamité', 'affliction',
                                         'catastrophe', 'épreuve', 'accident', 'chagrin',
                                         'malchance', 'ennui', 'infortune', 'craindre',
                                         'redouter', 'appréhender', 'pressentir',
                                         'avoir peur', 'plaindre', 'regretter']),
                         ('mer',        ['mer', 'quantité', 'déluge', 'océan', 'flots', 'fourmilière', 'grande tasse']),
                         ('violence',   ['violence', 'battr', 'ardeur',
                                         'emportement', 'véhémence', 'fureur', 'frénésie',
                                         'force', 'vivacité', 'brutalité', 'impétuosité',
                                         'bouillonnement', 'frapp', 'ross', 'remu', 'écras',
                                         'maltrait', 'éreint', 'bless', 'vaincre', 'triomph',
                                         'corrig', 'discut', 'bataill', 'lutt', 'chican',
                                         'sermonn', 'réprimand', 'contest', 'ferraill', 'admonest']),
                         ('religion',   ['religion', 'dévotion', 'foi',
                                         'croyance', 'culte', 'credo', 'principe', 'doctrine',
                                         'dogme', 'opinion', 'adoration', 'prêtre', 'abbé',
                                         'religieux', 'ecclésiastique', 'pontife', 'pasteur',
                                         'druide', 'prédicant', 'aumônier', 'vicaire',
                                         'chapelain', 'péché', 'faute', 'vice', 'crime',
                                         'tache', 'défaut', 'attentat', 'manquement', 'stupre', 'impureté', 'imperfection']),
                         ('amour',      ['amour', 'passion', 'attachement',
                                         'affection', 'flirt', 'caprice', 'amourette',
                                         'tendresse', 'coeur', 'fanatisme', 'adoration',
                                         'amante', 'épouse', 'dame', 'légitime', 'maîtresse',
                                         'nénette', 'concubine', 'bise', 'bisou', 'bécot',
                                         'baise', 'baiser', 'bisette', 'blizzard', 'accolade',
                                         'poutou'])])



def indexes(needle):
    return [m.start() for m in re.finditer(needle, text)]

def percentage_indexes(needle):
    return map(lambda x: 100*float(x)/length, indexes(needle))

def visual_tag(tag, visual_tags):
    try:
        return visual_tags[tag]
    except KeyError:
        return visual_tags['default']

def band_tag(tag, band_tags):
    try:
        return band_tags[tag]
    except KeyError:
        return band_tags['default']

def percent(n):
    return 100*n/float(length)



chapters = [0.0, 2.14551152425, 4.42389336495, 6.70227520566, 9.87845806909, 12.695732269, 13.8942119361, 15.809672536, 18.9798100643, 20.5324341207, 22.4873746731, 25.9435909923, 29.6496670302, 31.9703979757, 35.4308492054, 37.4996029771, 41.2909065885, 45.0065111749, 50.6267667517, 55.8055329105, 58.3242459213, 60.012916477, 70.3847416175, 71.6896234106, 76.4846008068, 81.916402867, 85.090997639, 88.8950059818, 91.5825860481, 92.6831334103, 100]

chapter_colours = ['#F03030', '#303030', '#300000', '#606060', '#600000', '#909090', '#900000', '#C0C0C0', '#C00000', '#F0F0F0', '#F00000', '#C0C090', '#903030', '#C0C060', '#603030', '#303000', '#000000', '#606000', '#000000', '#909000', '#000000', '#C0C000', '#000000', '#F0F000', '#000000', '#F0F030', '#306060', '#F0F000', '#F00000', '#C0C0F0']

def draw_chart(words, visuals, bands):
    occurrences = OrderedDict((k, sum(map(percentage_indexes, v), [])) for k, v in word_tags.items())
    for tag, data in occurrences.iteritems():
        plt.plot(data, [band_tag(tag, band_tags)]*len(data), visual_tag(tag, visual_tags), label=tag.capitalize())


    plt.annotate("XX: WHAT HAPPENED AT SEA\nTO CANDIDE AND MARTIN", xy=(percent(105323), 0.999), xytext=(percent(90000), 0.97),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 )
    
    plt.annotate("Pangloss describes being hanged", xy=(percent(168459), 1.001), xytext=(percent(130000),1.02),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 )


    for i in range(len(chapters[:-1])):
        col = chapter_colours[i]
        plt.axvspan(chapters[i], chapters[i+1], facecolor=col, alpha=0.3)
    plt.legend()
    plt.xlabel(u'% index de Caractère dans le texte francais de Candide')
    plt.yticks([])
    plt.ylim(0.95, 1.05)
    plt.figure(1).patch.set_facecolor('white')
    plt.show()


# Main
visual_tags = {'default'      : 'bo',
               'optimisme'    : 'bo',
               'pessimisme'   : 'ro',
               'violence'     : 'm^',
               'mer'          : 'yD',
               'religion'     : 'kh',
               'amour'        : 'g*'}

band_tags   = {'default'      : 1.0,
               'mer'          : 1.01,
               'violence'     : 0.99,
               'violence'     : 1.02,
               'mer'          : 1.03,
               'religion'     : 0.98,
               'amour'        : 0.97}


draw_chart(word_tags, visual_tags, band_tags)





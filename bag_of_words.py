#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import json
import regex
import sys
from collections import Counter, OrderedDict

#STOPWORDS = ["ad", "al", "allo", "ai", "agli", "all", "agl", "alla", "alle", "con", "col", "coi", "d", "da", "dal", "dallo", "dai", "dagli", "dall", "dagl", "dalla", "dalle", "di", "del", "dello", "dei", "degli", "dell", "degl", "della", "delle", "in", "nel", "nello", "nei", "negli", "nell", "negl", "nella", "nelle", "su", "sul", "sullo", "sui", "sugli", "sull", "sugl", "sulla", "sulle", "per", "tra", "contro", "io", "tu", "lui", "lei", "noi", "voi", "loro", "mio", "mia", "miei", "mie", "tuo", "tua", "tuoi", "tue", "suo", "sua", "suoi", "sue", "nostro", "nostra", "nostri", "nostre", "vostro", "vostra", "vostri", "vostre", "mi", "ti", "ci", "vi", "lo", "la", "li", "le", "gli", "ne", "il", "un", "uno", "una", "ma", "ed", "se", "perché", "anche", "come", "dov", "dove", "che", "chi", "cui", "non", u"più", "quale", "quanto", "quanti", "quanta", "quante", "quello", "quelli", "quella", "quelle", "questo", "questi", "questa", "queste", "si", "tutto", "tutti", "a", "c", "e", "i", "l", "o", "ho", "hai", "ha", "abbiamo", "avete", "hanno", "abbia", "abbiate", "abbiano", u"avrò", "avrai", u"avrà", "avremo", "avrete", "avranno", "avrei", "avresti", "avrebbe", "avremmo", "avreste", "avrebbero", "avevo", "avevi", "aveva", "avevamo", "avevate", "avevano", "ebbi", "avesti", "ebbe", "avemmo", "aveste", "ebbero", "avessi", "avesse", "avessimo", "avessero", "avendo", "avuto", "avuta", "avuti", "avute", "sono", "sei", u"è", "siamo", "siete", "sia", "siate", "siano", u"sarò", "sarai", u"sarà", "saremo", "sarete", "saranno", "sarei", "saresti", "sarebbe", "saremmo", "sareste", "sarebbero", "ero", "eri", "era", "eravamo", "eravate", "erano", "fui", "fosti", "fu", "fummo", "foste", "furono", "fossi", "fosse", "fossimo", "fossero", "essendo", "faccio", "fai", "facciamo", "fanno", "faccia", "facciate", "facciano", u"farò", "farai", u"farà", "faremo", "farete", "faranno", "farei", "faresti", "farebbe", "faremmo", "fareste", "farebbero", "facevo", "facevi", "faceva", "facevamo", "facevate", "facevano", "feci", "facesti", "fece", "facemmo", "faceste", "fecero", "facessi", "facesse", "facessimo", "facessero", "facendo", "s", "sto", "stai", "sta", "stiamo", "stanno", "stia", "stiate", "stiano", u"starò", "starai", u"starà", "staremo", "starete", "staranno", "starei", "staresti", "starebbe", "staremmo", "stareste", "starebbero", "stavo", "stavi", "stava", "stavamo", "stavate", "stavano", "stetti", "stesti", "stette", "stemmo", "steste", "stettero", "stessi", "stesse", "stessimo", "stessero", "stando"]
STOPWORDS = open(sys.argv[2], 'rb').read().strip().split('\n')

tokens = []

with codecs.open(sys.argv[1], 'rb', 'utf-8') as i:
    lines = i.readlines()
    for l in lines:
        # Skip <doc> tags
        if not regex.match(ur'</?doc', l):
            l_tokens = regex.split(ur'[^\p{L}]+', l.lower())
            tokens += [token for token in l_tokens if token and token not in STOPWORDS]

freq = Counter(tokens)
voc = OrderedDict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

json.dump(voc, codecs.open('vocabolario.json', 'wb', 'utf-8'), ensure_ascii=False, indent=2)

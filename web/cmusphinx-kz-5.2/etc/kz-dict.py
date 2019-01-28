#!/usr/bin/python
# -- coding: utf-8 --
 
import sys
import copy

softletters=set(u"әяёюиьеіөү")
startsyl=set(u"#ъьаяоёуюэеиы-")
others = set(["#", "+", "-", u"ь", u"ъ"])

softhard_cons = {                                                                
    u"б" : u"b",
    u"в" : u"v",
    u"г" : u"g",
    u"д" : u"d",
    u"з" : u"z",
    u"к" : u"k",
    u"л" : u"l",
    u"м" : u"m",
    u"н" : u"n",
    u"п" : u"p",
    u"р" : u"r",
    u"с" : u"s",
    u"т" : u"t",
    u"ф" : u"f",
    u"х" : u"h",
    u"һ" : u"h"
}

other_cons = {
    u"ж" : u"zh",
    u"ц" : u"c",
    u"ч" : u"ch",
    u"ш" : u"sh",
    u"щ" : u"sch",
    u"й" : u"j",
    u"ғ" : u"gh",
    u"қ" : u"kh",
    u"ң" : u"ng"
}
                                
vowels = {
    u"а" : u"a",
    u"ә" : u"a",
    u"я" : u"a",
    u"у" : u"u",
    u"ү" : u"u",
    u"ұ" : u"u",
    u"ю" : u"u",
    u"о" : u"o",
    u"ө" : u"o",
    u"ё" : u"o",
    u"э" : u"e",
    u"е" : u"e",
    u"и" : u"i",
    u"і" : u"i",
    u"ы" : u"y",
}


def pallatize(phones):
    for i, phone in enumerate(phones[:-1]):
        if phone in softhard_cons:
            if phones[i+1] in softletters:
                phones[i] = softhard_cons[phone] + "j"
            else:
                phones[i] = softhard_cons[phone]
        if phone in other_cons:
            phones[i] = other_cons[phone]

def convert_vowels(phones):
    new_phones = []
    prev = ""
    for phone in phones:
        if prev in startsyl:
            if phone in set(u"яюеё"):
                new_phones.append("j")
        if phone in vowels:
            new_phones.append(vowels[phone])
        else:
            new_phones.append(phone)
        prev = phone
    return new_phones

def convert(stressword):
    #phones = unicode("#" + stressword + "#", "utf-8")
    # Assign stress marks
    phones = stressword
    stress_phones = []
    #stress = 0
    for phone in phones:
        stress_phones.append(phone)
    
    # Pallatize
    pallatize(stress_phones)
    
    # Assign stress
    phones = convert_vowels(stress_phones)

    # Filter
    phones = [x for x in phones if x not in others]

    return " ".join(phones).encode("utf-8")

src=open("C:\\Nurtas\\Kaz_freq_words\\kz_dict\\kz_dict.txt",encoding="utf-8").read().lower()
words=src.split()

for word in words:
    converted_word=convert(' ' +word+' ')
    print (word,converted_word)
    

'''
for line in open(sys.argv[1]):
    word, stressword = line.split()
    print (word), convert(stressword)
'''


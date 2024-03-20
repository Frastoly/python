from collections import Counter

def harf_var_mi(metin, harf):
    
    return harf in metin

def buyuk_harf_kucult(metin):
    
    return metin.lower()

def harf_adeti(metin):
    
    frekanslar = Counter(metin)
    return {harf: frekans for harf, frekans in frekanslar.items() if harf.isalpha()}
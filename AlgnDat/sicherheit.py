import numpy as np
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def nurAlphabet(text):
    return "".join(char for char in text.upper() if char in alphabet)


def caesarBuchstabe(buchstabe, schlüssel=3):
    if buchstabe in alphabet:
        # index des Buchstaben herausfinden
        index = alphabet.index(buchstabe)
        # index um schlüssel verschieben und modulo 26 nehmen
        index = (index + schlüssel) % 26
        buchstabeVersch = alphabet[index]
        return buchstabeVersch
    else:
        return buchstabe


def caesarText(text, schlüssel=3):
    textVersch = ""
    for buchstabe in text:
        buchstabeVersch = caesarBuchstabe(buchstabe, schlüssel)
        textVersch = textVersch + buchstabeVersch
    return textVersch


def breakCaesar(text):
    zaehler = [0] * 26
    for buchstabe in nurAlphabet(text):
        index = alphabet.index(buchstabe)
        zaehler[index] += 1
    maxHäufigkeit = max(zaehler)
    maxPos = zaehler.index(maxHäufigkeit)
    schlüssel = (maxPos - alphabet.index("E")) % 26
    return schlüssel


'''
textVersch = "QRE ANZR QRE PNRFNE-IREFPUYÜFFRYHAT YRVGRG FVPU IBZ EÖZVFPURA SRYQUREEA TNVHF WHYVHF PNRFNE NO, QRE ANPU QRE ÜOREYVRSREHAT QRF EÖZVFPURA FPUEVSGFGRYYREF FHRGBA QVRFR NEG QRE TRURVZRA XBZZHAVXNGVBA SÜE FRVAR ZVYVGÄEVFPUR XBEERFCBAQRAM IREJRAQRG UNG. QNORV ORAHGMGR PNRFNE RVAR IREFPUVROHAT QRF NYCUNORGF HZ QERV OHPUFGNORA."
key = breakCaesar(textVersch)
print('Geknackter Schlüssel ist:', key)
print('Geknackter Text:')
print(caesarText(textVersch, 26 - key))
'''


def monoAlph(text, permutation):
    ergebnis = ""
    for buchstabe in text.upper():
        if buchstabe in alphabet:
            ergebnis += permutation[buchstabe]
        else:
            ergebnis += buchstabe
    return ergebnis


def makePermDict(key):
    dct = {}
    for klarBuchstabe, chiffBuchstabe in zip(alphabet, key):
        dct[klarBuchstabe] = chiffBuchstabe
    return dct
    # Kurzform:
    # return {klar: chiff for klar, chiff in zip(alphabet, key)}


'''
# Schlüsselpermutation aus Aufgabe 1.2a)
key = "YUOHJDBLZVXCFSPMGTERAINKQZ"
text2a = """Klassische Beispiele für monoalphabetische Substitutionen sind die Caesar-Verschlüsselung und das Playfair-Verfahren. Im Gegensatz zur monoalphabetischen Substitutionen stehen die polyalphabetischen Substitutionen, bei denen zur Verschlüsselung mehrere (viele) verschiedene Alphabete verwendet werden."""
textVersch = monoAlph(text2a, makePermDict(key))
print('Verschlüsselter Text Aufgabe 2a:')
print(textVersch)
'''


def breakMono(text):
    text = nurAlphabet(text)  # für die Analyse brauchen wir nur die Buchstaben
    # Häufigkeiten laut Wikipedia
    mostFrequent = "ENISRATDHULCGMOBWFKZPVJYXQ"
    counter = {}  # diesmal zählen wir mit einem Dictionary (Buchstabe -> Häufigkeit)
    for buchstabe in alphabet:
        counter[buchstabe] = 0
    for buchstabe in text:
        counter[buchstabe] += 1

    countListe = [(count, buchst) for buchst, count in counter.items()]

    # diese Liste *absteigend* sortieren (häufigste zuerst!)
    # Python sortiert Tupel anhand des ersten Eintrags, in diesem Fall also
    # gerade die Häufigkeit; der Buchstabe (zweiter Eintrag des Tupels) wird
    # einfach mitsortiert
    countListe.sort(reverse=True)
    # jetzt die vermutete Schlüsselpermutation erstellen: In Reihenfolge der
    # Wikipedia-Häufigkeiten die Buchstaben aus countListe einfügen
    permutation = {}
    for i in range(26):
        permutation[mostFrequent[i]] = countListe[i][1]
        # Achtung: countListe[i] ist das 2-Tupel (count, buchstabe), also ist
        # countListe[i][1] der buchstabe (countListe[i][0] wäre der Zähler)
    return permutation


def invertPerm(perm):
    """Invertiert eine Permutation; wird zum entschlüsseln monoalphabetisch
    verschlüsselter Texte benötigt (entschlüsseln = verschlüsseln mit inv.
    Perm.)
    """
    antwort = {}
    for klar, chiff in perm.items():
        antwort[chiff] = klar
    return antwort
    # Kurzform:
    # return {chiff: klar for klar, chiff in perm.tems()}


'''
text2b = """XCYEEZEOLJ UJZEMZJCJ DÜT FPSPYCMLYUJRZEOLJ EAUERZRARZPSJS EZSH HZJ OYJEYT-IJTEOLCÜEEJCASB ASH HYE MCYQDYZT-IJTDYLTJS. ZF BJBJSEYRZ ZAT FPSPYCMLYUJRZEOLJS EAUERZRARZPSJS ERJLJS HZJ MPCQYCMLYUJRZEOLJS EAUERZRARZPSJS, UJZ HJSJS ZAT IJTEOLCÜEEJCASB FJLTJTJ (IZJCJ) IJTEOLZJHJSJ YCMLYUJRJ IJTNJSHJR NJTHJS."""
geratenePermutation = breakMono(text2b)
print('Geratene Permutation:')
for b in alphabet:
    print(b, '->', geratenePermutation[b])
print('Entschlüsselter Text:')
print(monoAlph(text2b, invertPerm(geratenePermutation)))
'''


def wortZuZahlen(schlüsselWort):
    schlüssel = []
    for buchstabe in schlüsselWort:
        schlüssel.append(alphabet.index(buchstabe))
    return schlüssel


def zahlenZuWort(schlüssel):
    return "".join(alphabet[index] for index in schlüssel)


def vigenere(text, schlüsselWort):
    schPos = 0  # speichert aktuell gültige Position im Schlüssel
    schlüssel = wortZuZahlen(schlüsselWort)
    ergebnis = ""
    for buchstabe in text.upper():
        if buchstabe in alphabet:
            ergebnis += caesarBuchstabe(buchstabe, schlüssel[schPos])
            # schlüsselpositions erhöhen
            schPos = (schPos + 1) % len(schlüssel)
        else:
            ergebnis += buchstabe
    return ergebnis


'''
text3a = """Dem britischen Mathematiker Charles Babbage gelang um das Jahr achtzehnhundertvierundfuenfzig erstmals die Entzifferung einer Vigenere-Chiffre."""
crypt3a = vigenere(text3a, 'KRYPTOGRAPHIE')
print('Verschlüsselter Text mit Schlüssel "KRYPTOGRAPHIE":')
print(crypt3a)
'''


def breakVigenere(text, keylen):
    text = nurAlphabet(text)
    key = []
    for schPos in range(keylen):
        subtext = text[schPos::keylen]
        subkey = breakCaesar(subtext)
        key.append(subkey)
    return key


'''
text3b = """VCT DAATVWLT-DWLHKZFJMKMTTMHV OWBI IMZ SMF ZGIFTDMKCHKZYG LAJAWEUIMF OCL CLNXLIVZSZ QTSCHM VY KQYYCMJY OCJOTKC. MXM TYGCZN PCX XTU HLXVRCE LWL EWDSPTHBPJWNXAUBT AMVHBANJBAIC. LSVTQ OYGLWH XU YYVMFMPBR TJZ EICWSFEPSVTBAMRPWH HCTMIQLOIQGH CQUBI MAH VMZYXULYMBSFEPSVTB NYGEWHSML, MDVVYGV EYWZWLT. EAY KQWFT CFX LMDWWM SFEPSVTBW ATVMNOB OYGLWH LQJX SCJWW MAH HKZFJMKMTTOIGB TYHBAGBB. WHIALUCLWH XAL XXM NCVMFYGM-NYGAUBACWMHMDOCO AG HMUBOMZHIMF DPPJBJVVYGB MHS OSFI TSHVM SFH AAWWMJ. YGAL CB RSBG IUBIHWBCPMHSMJNKQWLJVVZJMFZOQY ATTSHV MK WWIJFTA TUQJSAT MJMIUSFH LAY TVLTXNXYGCFA TQFYG DAATVWLT-KZCUNJY. SI VCTA SVTZ FCRPL ITNXYCBDCRP YYBIUBI EMLSM, YCCO VYG XJYJAKCHKZY DNXCOQWL UZAYSZAWW SSMXACC BQL MTQFYG TGYHCFA XU BUWZ SWWBRYWVZOCLWLILJYXCFXHMUBOQY CC LAY VMKWWQUBIM WCC."""
key3b = breakVigenere(text3b, 4)
print('Gefundener Schlüssel 3b (in Zahlen):', key3b)
keyword3b = zahlenZuWort(key3b)
print('Gefundener Schlüssel 3b (als Wort):', keyword3b)
# Entschlüsselungs-Schlüssel bauen
decryptKey3b = [alphabet[26 - s] for s in key3b]
print('Enschlüsselter Text:')
print(vigenere(text3b, decryptKey3b))
'''


def ggT(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def _findKeylenVigenere(text, pivot):
    """Rät die Schlüssellänge eines Vigènere-verschlüsselten Textes."""
    text = nurAlphabet(text)
    # suche wiederkehrende Teilstrings der Länge 5 (die 5 ist geraten; falls
    # das nicht klappt, mit anderen Werten probieren
    testLen = pivot
    # wir suchen nach wiederkehrenden Teilstrings der Länge 5. Dies muss nicht
    # funktionieren: ist die Zahl zu klein, kann es sein dass Teilstrings
    # zufälligerweise häufiger vorkommen, ohne dass dies auf gleichen Klartext
    # zurückgeht. Ist die Zahl zu groß, gibt es womöglich gar keine wiederkehrenden
    # Teilstrings dieser Länge mehr, oder aber nur so wenige dass ein Vielfaches
    # der gesuchten Schlüssellänge herauskommt. Hier muss man also experimentieren.
    vorkommen = {}
    # das vorkommen-Dictionary bildet Teilstrings auf die Indizes im Text ab,
    # an denen sie vorkommen
    for i in range(len(text) - testLen):
        substring = text[i:i + testLen]
        if substring not in vorkommen:
            # neue Vorkommen-Liste für diesen Teilstring erstellen
            vorkommen[substring] = [i]
        else:
            # Vorkommen-Liste um Index i erweitern
            vorkommen[substring].append(i)
    # suche den gesamten GGT aller auftretenden Zwischenräume!
    gesamtGGT = -1  # Initialwert
    for subst, vork in vorkommen.items():
        if len(vork) > 1:
            # uns interessieren nur Teilstrings, die mindestens 2x vorkommmen
            for i in range(len(vork) - 1):
                zwischenraum = vork[i + 1] - vork[i]
                if gesamtGGT == -1:
                    # noch auf Initialwert -> setze auf ersten Zwischenraum
                    gesamtGGT = zwischenraum
                else:
                    gesamtGGT = ggT(gesamtGGT, zwischenraum)
    return gesamtGGT

def findKeylenVigenere(text):
    l=0   # todo funktioniert oft aber nicht immer
    while l<=1 or l ==len(text):
        l = np.random.randint(1,101)
        l = _findKeylenVigenere(text,l)
    return l
'''
text3c = "JCX BCZKHXXY-OKLLIBEAYLYYEAHZ MYAZ UNL XXT ZKGHSUYLOMVNYK JCIRIFGNXT OGJ EKEJMUAKGZ URUBYY WK PBMYGKLX FOKAYVQ. MBK VXXOAZ UNL XXS JKOHSOJ WKL IUFRGFINUUKNBYWAK MNHMMONNZCHT. XTHYB CYKJYG OG ZKAXTMTZT SAL FUHHGFINUUKNBYWAKH LAVLZCMANBUH GOWAZ YBT AXNYBSNXDNTRJAGVXZ PXXQXTXXZ, MHTXXXH FKBKKLX. CCX BCXRY NTX PKFVNY TRJAGVXZY ZKHNZTM CYKJYG CCKJ XNXWA KCG YWAROXYMXRQHXN UKMMOGFZ. YGZMMGHWKH BYN WOY OOAXTYKK-PXXMVNFNKMLKFNTA BS MXIBSKBGZYG PUAXBNTXXXN NTX ZGFM RUGMY TRM LOWAKL. XXMM OG CGBK GWAZTXNHAAHWKLMBCXXOGJZNKHYFCZ MYEGHZ KM VNUKRYL HUUHUZK YKYNFGFL JCX KHMFCYLYKAHZ KCGKL OOAXTYKK-WAOZYXY. WG XBKM THYK TCVNN HKZYKHMRCVN AXSUVNN PALWK, ABTA WKL IXYNYMBYWAK IYLCSOYK LLBKXKOWA QULOMDO GBZ MXOHXX FHKMNTA BS DTNL TIBMFYATBNTXXXNWXYBAHWYYVNTBM CG JCX MYLIBBIBMK YBT."
keylen3c = findKeylenVigenere(text3c)
print('Gefundene Schlüssellänge 3c:', keylen3c)
# jetzt wie in der 3b
key3c = breakVigenere(text3c, keylen3c)
print('Gefundener Schlüssel 3c (Zahl):', key3c)
keyword3c = zahlenZuWort(key3c)
print('Gefundener Schlüssel 3c (Wort):', keyword3c)
decryptKey3c = [alphabet[26 - s] for s in key3c]
print('Enschlüsselter Text 3c:')
print(vigenere(text3c, decryptKey3c))
'''
text4 = "HYKAQHHOHASRTNWTNGXALBRHGDDTHWCEVOQPIAAINHAWWXRNJNCHEQSXLTPHCGDJIVXYKTNKTEWSEHAWHCCHSAVHYKAQHHOHAOOPAVHPVXYKWAUPQVUEQSAQXJGTIGTNWTTWBEWHEFWOHAXVIQPCOWTHOTJYTNVRDRQAQZKUGAOXAUIQQSZDHJPXPGTIJGKHHOWTJNDNUTHDIERCOZTNWTNPXPWTHWLEUSEVIORBEWSEHHYKAQHHOHAHDTJJTLHGERSAQQANPJQINHSQCXAUIOLRDGXANGUSIKDCWONOHSAUKEJTJUTRHGOFWHXTOVTHXCCDJBGXAGTNFPAVPNYTNVRDOJAVHAOJJJPHOTAUHPHCVZTEWTJQIAQQQFWOWPXHCALCAUEAUXKGTCHWKHGAQYAZTEOHVXGOHAXHCYDTODGRHGOFWHXTOVTHXCCXCZHXJHWWHJBLVGHXPVPJDAUVTRHGNDTPGXAEJYKHPDQAQOQRGZQJJJQALTEQTIWTTWSAUCQUPQVSAULEHSAUWKOJJJTEQTOCTEFWAQHXHHPHWPCTEJIOLRDGXASTNLDZHJJPXPWTHEPNLBCHWALBPHMPHXJQDNPPHHGPHMPZTEVIWXHNHXYKTJGGAGJJGPJCTJDJBVDZDHODQALCAUVAZXOVTJOPAQVAGTOWTTWTOLBRHGCOTEFWVXBOFWHXTOVTHDJYKWEHGZLTLHGERSADQCHAALIAWLAUSAQZWQCGDHEVZEWTOWUNLTZPPJWTOWPQISEHHAZTEVTXHZKPBPPPJUTYKIOFWJHAHGXAVRDOJAVHAOAWHCCHSAVKAUHYKAQHHOHAPHCPHMPHHDHGWXHFHIVWBQVHJXGJRRDGTNJTDHXIWTTWHLDAPHCSHXOHOAUAAJISHGZHCZLTOSPHWTJZTHFWAPXPGTIVTHETJEJYKHPDQAQKAUHYKAQHHOHAPZJNGTJZTNGTJCJODBIHCCHUWVHPGXAHCPVENHRDHCZHPHSWWETPYTNVRDLTXXCCGTNHXJCTHQTJWTEOIAAIAODAVIIDCJXCILIPHAOKPAXUEJZALIODCWONOHLALHPGTNWTTWZALCARSAUCQULAQXCHGAGJJGPJCTJDJBETEVEEHAOZTEVTSHXHHGGXGVLHPOPAVHPVXYKSEHHYKAQHHOHAHDTJJTJLRDWBEWSAPZWVXONXPHHPKTNDJOIXJGTJXCPHGZHGRRGWXHOHIVXCCGPOVTOVXYKQALSAPHYKAQHHOHAQPTEQLKUIWXHALCAPLKHGPHGXXRDKPJGTHWJJGPQFWZHGPHMPPXPHXJHBSRGPETCLCJWAWHHOWHEFWFHSKFWZXGYKVAVRDLRGWTODJOVDNWXAUTJXCSDWNVRDHXJOXYKTNQVNDBISPWUTEQKEHAAQUWHAHHCZHGOFWHXTOVTHIXJGTJGPVXLAUSAQOQHGOWIAAIOFWHXTOVTHNDIEXJDIERCAQQAZTNWTPRWJHSWVHAVTEQTNRAHHHLLTHWLWVSWYDJNAWUIAAIXCLOFWHXTOVTHLHPGXADCVDWHGTNPDAJAEFWGHXPHCSLGZVDXHGALIOLBAUHPHCOFWNLIPYDJOEWXUGPWWOQEHGPDAHHSWQCJRRDYTNEAALQAQSAQCCUPIPEWDGAZTNGTJQJJJTIDTOVXDUTNZPDUHYKTEQAEFWGHXPDBWQUWQVALCAVLKUIAVOQVIAKTJJTSLRDWTPLHPPXJGTOWTJVTEQTOGTNQVNDBIHPAXHOHGOWJJZPDUHYKTEQAEFWWQTEQTIZDNWPJIPJJLEUSZDHCDCVHEWDGRHGSRGBHCIHXOWOALVPVXYKQAUTEWHWEIAWGWJGWPBAQSWVHZLTWQOWKAZHGQHQNLVCHQHLTXHCAQEWDGAVDOWPNNGAGJVLTNWLQUSAGPOVTEQTQHQAUENXTBXCCDAHHGNHHPOXYKTJPDAJAEFWGHXPHCIDRDEPNLHPHHXOTEETJVIWWIAWLWHXJHGDDAXHCILAHLDJPTEVIJXGYDTEQWQQSAUIOLCJYDHOTIRTCOXYKZALIAQJAEGEJPJKPJGTEQTOZDAUIAUQQFWAVZKHCJHCJXCWOAAZDAUIAUSEHBEWSEHHAQIAWGWJGWPBAQQAJXJQTJDAOVRDOJAVHAOPQVENRQEHGPZTNGTJEXOVXYKTEQHYKAQHHOLVAUZHDGPHMPHGCLQPHXJHPQVUQHWNOXYKTXHHYKGALQQQVSXGZHOSHXPDJOHCZDRDWKAUDAIUAQIHLRDWJJGXOWXJFGUSIKRAEPEHHBAQIEHGPHXJCXCHXJNAWUIAAIWXHOWPPLHPLHYKVHHXYKKAUIALAPHCQQHEQCEJTJEJYKHPDQAQUKOVAQLWHGAHXJHBYLEDHGPHMPRCHBPJJGEIUJLRDWDDQTSHXPHGAVOQJPAQVHLRD"
l = findKeylenVigenere(text4)
print(l)
key4 = breakVigenere(text4,l)
print('Schluessel: ' +zahlenZuWort(key4))
decryptKey4 = [alphabet[26 - s] for s in key4]
print('Enschlüsselter Text:')
print(vigenere(text4, decryptKey4))
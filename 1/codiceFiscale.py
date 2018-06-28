#Moduli
import sys
import string

#Strutture dati Globali
vocali = ('a','e','i','o','u')
mesi = ('a','b','c','d','e','h','l','m','p','r','s','t')
comuni = {'udine':'l483', 'verona':'l781', 'legnago': 'e512'}

#CODICI DI CONTROLLO
regole_pari = {}
alfabeto = string.ascii_lowercase
for i in xrange (0,10):
    regole_pari[str(i)] = i
for i in xrange (0,26):
    regole_pari[alfabeto[i]] = i

regole_dispari = {}
temp_tuple = (1,0,5,7,9,13,15,17,19,21)
for i in xrange(0,10):
    regole_dispari[str(i)] = temp_tuple[i]
    regole_dispari[alfabeto[i]] = temp_tuple[i]

temp_tuple2 = (2,4,18,20,11,3,6,8,12,14,16,10,22,25,24,23)
index = 0
for i in xrange(10,26):
    regole_dispari[alfabeto[i]] = temp_tuple2[index]
    index += 1

regole_resto = [alfabeto[i] for i in xrange(0,26)]

#------------------------------

def estrai_nome(aString):
	temp_string = ''
	for aChar in aString:
		if not aChar in vocali:
			temp_string += aChar

		if len(temp_string) >= 4:
			temp_string = temp_string[0] + temp_string[2] + temp_string[3]
			break

	index = 0
	while len(temp_string) < 3 and index < len(aString):
		if (not aString[index] in temp_string) or (aString[index] in vocali) :
			temp_string += aString[index]
		index += 1
		
	for i in range(0, 3-len(temp_string)):
		temp_string = temp_string + 'x'

	return temp_string
    
    
def estrai_cognome(aString):
	temp_string = ''
	for aChar in aString:
		if not aChar in vocali:
			temp_string += aChar

		if len(temp_string) >= 3:
			break

	index = 0
	while len(temp_string) < 3 and index < len(aString):
		if (not aString[index] in temp_string) or (aString[index] in vocali) :
			temp_string += aString[index]
		index += 1
		
	for i in range(0, 3-len(temp_string)):
		temp_string = temp_string + 'x'

	return temp_string


def genera_mese(unMese):
    return mesi[int(unMese)-1]


def codice_comune(comune):
    return comuni[comune]


def genera_giorno(unGiorno, unSesso):
	if unSesso == 'm':
		return unGiorno
	else:
		return str(int(unGiorno)+40)


def genera_codice_controllo(aCodiceFiscale):
    parita = 1
    temp_dispari = 0
    temp_pari = 0

    for aChar in aCodiceFiscale:
        if parita:
            temp_dispari += int(regole_dispari.get(aChar))
            parita = 0
        else:
            temp_pari += int(regole_pari.get(aChar))
            parita = 1

    return regole_resto[(temp_dispari+temp_pari) % 26]

def main(nome, cognome, data_nascita, comune, sesso): #pragma: no cover
    nomeCF = estrai_nome(nome)
    cognomeCF = estrai_cognome(cognome)

    data_nascitaCF = data_nascita.split("/")
    anno_nascitaCF = data_nascitaCF[2][2:]

    mese_nascitaCF = genera_mese(data_nascitaCF[1])
    giorno_nascitaCF = genera_giorno(data_nascitaCF[0], sesso)

    codice_fiscale = cognomeCF + nomeCF + anno_nascitaCF + mese_nascitaCF + giorno_nascitaCF + codice_comune(comune.lower())

    codiceCF = genera_codice_controllo(codice_fiscale)

    codice_fiscale += codiceCF

    print codice_fiscale

if __name__ == '__main__': #pragma: no cover
	if len(sys.argv) > 5:
		main(string.lower(sys.argv[1]).replace(' ', ''), string.lower(sys.argv[2]).replace(' ', ''), string.lower(sys.argv[3]), string.lower(sys.argv[4]).replace(' ', ''), string.lower(sys.argv[5]))
	else:
		print("Missing argument")

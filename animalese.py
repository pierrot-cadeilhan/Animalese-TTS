import wave

index = [c for c in 'abcdefghijklmnopqrstuvwxyz123456789']
#gérer caractère de plusieurs caractères (easter eggs: tuturu, $$$=welcome to san andreas)

#Introduire des paramètres comme vitesse (frequence), hauteur (frequence), timbre ?

def load(text):
    text = text.lower()
    data = []
    for c in text:
        if c in index:
            w = wave.open(f'audio/{c}.wav', 'rb')
            data.append([w.getparams(), w.readframes(w.getnframes())])
            w.close()
        elif c == '~' and len(data) > 0:
            data.append(data[-1])
        else:
            w = wave.open(f'audio/void.wav', 'rb')
            data.append([w.getparams(), w.readframes(w.getnframes())])
            w.close()
    return data

def generate(data, outfile='output.wav'):
    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()
    return outfile

if __name__=='__main__':
    data = load("c est un mur porteur")
    file = generate(data)
    print(file)
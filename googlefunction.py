from googletrans import Translator
tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)
matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"
tarjima = tarjimon.translate(matn_uz)
print(tarjima.text)

def eng(matn):
        tarjimon = Translator()
        tarjima = tarjimon.translate(matn, dest='uz')
        return tarjima

sss = eng(input(''))
print(sss)
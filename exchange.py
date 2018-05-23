import requests
import sys
url = "http://api.fixer.io/latest?base="

print("Kurlar Hesaplanıyor.....")
print("*******Hoşgeldiniz*******")
birinci_doviz = input("Elinizdeki Paranın Cinsi:")
birinci_doviz.isupper()
ikinci_döviz = input("Döviz Cinsi:")
ikinci_döviz.isupper()
try:
    miktar = float(input("Elinizdeki Paranın Miktarı:"))
except:
    sys.stderr.write("Doğru bir miktar giriniz")



response = requests.get(url + birinci_doviz)

json_verisi = response.json()
try:
    print(json_verisi["rates"][ikinci_döviz] * miktar)
except KeyError:
    sys.stderr.write("Lütfen para birimlerini doğru girin")
    sys.stderr.flush()

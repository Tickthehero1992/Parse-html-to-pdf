from bs4 import BeautifulSoup
import pdfkit
from googletrans import Translator
import os

path_to_save = "PDF_FILES/"
try:
    os.mkdir(path_to_save)
except:
    pass

translator = Translator()
def converter(pathik):
    #print(pathik)
    with open(pathik, mode='r', encoding='utf8') as istok:
     istok_text=istok.read()
     istok=BeautifulSoup(istok_text,'lxml')
     for tag in istok.find_all('p', {"class":"header-info-full_name"}):
        name_file=tag.text
        print(name_file)
        #file_output=path_to_save+translator.translate(name_file,src='ru', dest='en').text+".pdf"
        file_output=path_to_save+name_file+".pdf"
        #print(file_output)
        pdfkit.from_file(pathik,file_output)

for root,dirs, files in os.walk(os.getcwd()):
    for file in files:
     if file.endswith(".html"):
       print(file)
       try: converter(file)
       except: pass
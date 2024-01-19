wd = r"/home/yair/GHub/Codigos-em-financas/data/"

import os
for filename in os.listdir(wd):
    if 'Cart_' in filename:
        os.remove(wd+filename)

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("prefs", {
  "download.default_directory": wd,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


url=[
    'https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-brasil-100-ibrx-100-composicao-da-carteira.htm',   #IBR100
    'https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-brasil-50-ibrx-50-composicao-da-carteira.htm',     #IBR50
    'https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-ibovespa-ibovespa-composicao-da-carteira.htm',     #IBOV
    'https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-de-segmentos-e-setoriais/indice-dividendos-idiv-composicao-da-carteira.htm', #IDIV
    'https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-de-segmentos-e-setoriais/indice-small-cap-smll-composicao-da-carteira.htm'
    ]

for sitio in  url :
    driver.get(sitio)
    sleep(3)
    if sitio == url[0] :
        driver.find_element(By.ID,'onetrust-accept-btn-handler').click()
        driver.implicitly_wait(3) # seconds
    driver.switch_to.frame("bvmf_iframe")
    driver.find_element(By.CLASS_NAME , 'primary-text').find_element(By.TAG_NAME,"a").click()
    sleep(3)

driver.close()    

'''
    remanejo dos nomes dos arquivos
'''

files_dict = {'IBOVDia':'Cart_Ibov',
'SMLLDia':'Cart_Small',
'IBXXDia':'Cart_IBr100',
'IBXLDia':'Cart_IBr50',
'IDIVDia':'Cart_Idiv'}

for chave in files_dict.keys(): 
    for filename in os.listdir(wd):
        if chave in filename:
            os.rename(wd+filename,wd+files_dict[chave]+'.csv')


# driver.get(url[0])
# sleep(3)
# driver.find_element(By.ID,'onetrust-accept-btn-handler').click()
# driver.implicitly_wait(3) # seconds
# driver.switch_to.frame("bvmf_iframe")
# driver.find_element(By.CLASS_NAME , 'primary-text').find_element(By.TAG_NAME,"a").click()


# river.get(url[1])
# sleep(3)
# driver.find_element(By.ID,'onetrust-accept-btn-handler').click()
# driver.implicitly_wait(3) # seconds
# driver.switch_to.frame("bvmf_iframe")
# driver.find_element(By.CLASS_NAME , 'primary-text').find_element(By.TAG_NAME,"a").click()
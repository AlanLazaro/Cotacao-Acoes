from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def driverConfig():
    PATH = "chromedriver.exe"
    invisibilidade = Options()
    invisibilidade.headless = True
    driver = webdriver.Chrome(PATH, options=invisibilidade)
    return driver

def abrindoGoogle():
    driver = driverConfig()
    driver.get("https://www.google.com/")
    return driver


def fazendoBusca(driver):
    loop = True

    pesquisa = driver.find_element_by_class_name("gLFyf.gsfi")
    pesquisa.clear()
    acao = input("Ação: ").strip()

    if acao == "":
        loop = False

    else:
        pesquisa.send_keys('cotação ' + acao)
        pesquisa.send_keys(Keys.RETURN)

        try:
            valorAcao = driver.find_element_by_class_name("IsqQVc.NprOob.XcVN5d")
            valorAcaoTexto = valorAcao.text

            print('O Ultimo valor de ', acao, 'encontado é de RS:' + valorAcaoTexto)

        except:
            print(f"Erro, Papel: {acao} não encontrado")

        return loop

loop = True

driver = abrindoGoogle()

while loop == True:
    loop = fazendoBusca(driver)

print('fim')

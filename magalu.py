from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

import pyautogui as waitTime
import pyautogui as keyboardFunctions

import pandas as pd

navegador = opcoesSelenium.Chrome()

# Preparando o site
navegador.get("https://www.magazineluiza.com.br/")

# Procura pelo campo ID e digita o nome do produto
navegador.find_element(By.ID, "input-search").send_keys("geladeira")

# Tempo para o computador processas as informações
waitTime.sleep(2)

# Apertando a tecla do teclado enter para pesquisar o produto
keyboardFunctions.press("enter")

# Tempo para o computador processas as informações
waitTime.sleep(10)

# Criando o DataFrame que vai receber os dados
listaDataFrame = []

listaProdutos = navegador.find_elements(By.CLASS_NAME, "BCSuy")

# for = para
for item in listaProdutos:

    nomeProduto = ""
    precoProduto = ""
    urlProduto = ""

    if nomeProduto == "":

        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "enKhKW").text
        except Exception:
            pass

    elif nomeProduto == "":

        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "sc-kOjCZu").text
        except Exception:
            pass

    # --------------------------------------
    #
    if precoProduto == "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "kPMBBS").text
        except Exception:
            pass

    elif precoProduto == "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "sc-ehkVkK").text
        except Exception:
            pass

    elif precoProduto == "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "jDmBNY").text
        except Exception:
            pass

    elif precoProduto == "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "sc-kDvujY").text
        except Exception:
            pass

    else:

        precoProduto = "0"

    # -----------------------------------------

    if urlProduto == "":

        try:
            urlProduto = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        except Exception:
            pass

    else:

        urlProduto = "-"

    print(nomeProduto, "-", precoProduto)
    print(urlProduto)

    dadosLinha = nomeProduto + ";" + precoProduto + ";" + urlProduto

    # Populando o DataFrame com as informações
    listaDataFrame.append(dadosLinha)

arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')
arquivoExcel.save()

dataFrame = pd.DataFrame(listaDataFrame, columns=['Descrição;Preço;Url'])

# Prepara o arquivo do Excel usando xlsxwriter como mecanismo
arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)

# Salva as informações no arquivo de Excel
arquivoExcel.save()
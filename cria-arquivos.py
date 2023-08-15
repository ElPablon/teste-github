import os
import glob 
import datetime as dt

arquivos = [
    {'dir': f'C://Users//{os.getlogin()}//Desktop//Diretórios//Dir_1//', 'file_name': "Sim Varejo"},
    {'dir': f'C://Users//{os.getlogin()}//Desktop//Diretórios//Dir_2//', 'file_name': 'Sim Atacado'},
    {'dir': f'C://Users//{os.getlogin()}//Desktop//Diretórios//Dir_3//', 'file_name': 'Sim GG'},
    {'dir': f'C://Users//{os.getlogin()}//Desktop//Diretórios//Dir_4//', 'file_name': 'AA'},
    {'dir': f'C://Users//{os.getlogin()}//Desktop//Teste1//Teste2//Teste3//', 'file_name': 'AA'},
]

#Dicionário/Lista de nomes e diretórios das pastas
'''
arquivos = [
{'dir' : "P://Pricing//1. Varejo//", 'file_name': "Sim Varejo"},
{'dir' : "P://Pricing//2. Atacado//", 'file_name': "Sim Atacado"},
{'dir' : "P://Pricing//3. Condutor e GG//", 'file_name': "Sim GG"},
{'dir' : "P://Pricing//4. AutoAvaliar//", 'file_name': "AA"},
{'dir' : "P://Pricing//6. Premium//", 'file_name': "Premium"},
{'dir' : "P://Pricing//7. Ações Localiza//Promoções Localiza//", 'file_name': "Promoções Localiza"},
{'dir' : "P://Pricing//7. Ações Localiza//Alterações de Preço Localiza//2023//", 'file_name': "Alt Localiza"},
{'dir' : "P://Pricing//8. Créditos de Alçada//", 'file_name': "Créditos"},
{'dir' : "P://Pricing//9. Política Tableau//", 'file_name': "Pol Tableau"},
{'dir' : "P://Pricing//12. Concorrência//Extração Concorrência//2023//", 'file_name': "Ext Conc"},
{'dir' : "P://Pricing//14. Precificação//Valores//", 'file_name': "Valores"},
{'dir' : "P://Pricing//15. Analise de Preços//2023//", 'file_name': "Análise"},
{'dir' : "P://Pricing//15. Analise de Preços//Atacado//", 'file_name': "Análise Atac"},
{'dir' : "P://Pricing//16. Laudos e O.S//Precificação Avarias//", 'file_name': "Prec Avarias"},
{'dir' : "P://Pricing//18. Dash//", 'file_name': "Dash"},
{'dir' : "P://Pricing//20. Lotes//Reportes//", 'file_name': ""},
{'dir' : "P://Pricing//21. Cartas de Preço//", 'file_name': "Cartas"},
{'dir' : "P://Pricing//24. Templates Pricing//Precificação e regras//", 'file_name': "Regras"},
{'dir' : "P://Pricing//24. Templates Pricing//Propriedades OPC avarias//", 'file_name': "Propriedades"},    
{'dir' : "P://Pricing//24. Templates Pricing//Resultados baixados//", 'file_name': "Resultados"}
]
'''

#Define o Próximo Mês

proximo_mes = dt.date.today().month + 1

#Pega o nome do mês no padrão "Mmm"
hashmap = {
    1: 'Jan',
    2: 'Fev',
    3: "Mar",
    4: "Abr",
    5: "Mai",
    6: "Jun",
    7: "Jul",
    8: "Ago",
    9: "Set",
    10: "Out",
    11: "Nov",
    12: "Dez"
}

mes_00 = str(proximo_mes).zfill(2)

# 'dix' é o número índice da lista e o 'i' é o conteúdo da lista
for dix, i in enumerate(arquivos):
    if len(glob.glob(f"{i['dir']}*")) == 0:
        print('diretorio nao existe')
    nome = mes_00 + ". " + hashmap[proximo_mes] + " "
    print(nome)
    print(f"criando a pasta {nome + i['file_name']} no caminho {i['dir']}")
    try:
        os.makedirs(i['dir'] + nome + i['file_name'])
    except FileExistsError:
        print('o arquivo ja existe')


'''for i in dataframe:
    print(i['dir'] + '08 ' + i['file_name'])'''


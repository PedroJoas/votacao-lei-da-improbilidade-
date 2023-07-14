# Importações da biblibotecas
from bs4 import BeautifulSoup
from requests import get
import pandas as pd

# Url e requisições
url = 'https://radames.manosso.nom.br/palavras/politica/qual-e-a-ideologia-de-cada-partido-brasileiro/'

page = get(url)

soup = BeautifulSoup(page.text, 'html.parser')

# As informações que queremos está dentro de uma table, 
# então vamos usar o método .find do BeautifulSoup e 
# passamos o elemento que queremos, que no caso é uma table.
table = soup.find('table')

# o método .read_html lê uma string, então convertemos a table em string e 
# vai voltar um array, por isso colocamos o [0], para pegar somente o primeiro valor do array, 
# que no caso, é o código da table.

df_partidos = pd.read_html(str(table), header=0)[0]
# Por fim, salvamos o Dataframe pandas em um arquivo csv
df_partidos.to_csv('./Dados/df_partidos.csv', index=False)

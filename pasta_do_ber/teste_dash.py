import pandas as pd

# Cria um dataframe de exemplo
data = {'nome': ['João', 'Maria', 'José'], 'idade': [25, 30, 40]}
df = pd.DataFrame(data)

# Escreve o dataframe em um arquivo HTML
with open('arquivo.html', 'w', encoding='utf-8') as f:
    f.write(df.to_html())

    
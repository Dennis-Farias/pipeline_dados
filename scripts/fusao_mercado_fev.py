from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Extract

dados_empresaA = Dados(path_json, 'json')
print(f"\nNomes das colunas da empresa A: {dados_empresaA.nome_colunas}\n")
print(f"Quantidade de linhas da empresa A: {dados_empresaA.qtd_linhas}\n")

dados_empresaB = Dados(path_csv, 'csv')
print(f"Nomes das colunas da empresa B: {dados_empresaB.nome_colunas}\n")
print(f"Quantidade de linhas da empresa B: {dados_empresaB.qtd_linhas}\n")

# Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(f"Novos nomes de colunas: {dados_empresaB.nome_colunas}\n")

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f"Nomes das colunas da fusão das empresas: {dados_fusao.nome_colunas}\n")
print(f"Quantidade de linhas da fusão das empresas: {dados_fusao.qtd_linhas}\n")

# Load

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f"Caminho para os dados combinados: {path_dados_combinados}\n")

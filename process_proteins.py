import pandas as pd

info = pd.read_table('data/raw/9606.protein.info.v11.5.txt')
info.columns = ['id','name','size','annotation']
info['id'].replace('9606\.','',regex=True, inplace=True)
#pathways = info['annotation'].str.split(';',expand=True)
info.drop(columns=['annotation'],inplace=True)
print(info.head())
info.to_csv('data/clean/nodes_Protein.csv', index=False)
del info

links = pd.read_table('data/raw/9606.protein.links.v11.5.txt', delimiter=' ')
links.columns = ['source','target','score']
links['source'] = links['source'].replace('9606\.','',regex=True)
links['target'] = links['target'].replace('9606\.','',regex=True)

print(links.head())
links.to_csv('data/clean/edges_Protein.csv', index=False)

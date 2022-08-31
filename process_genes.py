#from gtfparse import read_gtf
import pandas as pd

#df = read_gtf('data/raw/Homo_sapiens.GRCh38.107.gtf')
#df.to_csv('data/clean/GRCh38.csv', index=False)
df = pd.read_csv('data/clean/GRCh38.csv')
print(df.head())


# select chromosomes 1-22, X & Y
chrs = [*[str(i) for i in range(1,22)],*['X','Y']]
df = df[df['seqname'].isin(chrs)]

# select gene from feature
df = df[df['feature'] == 'gene']

# remove pseudogenes
# df = df.loc[~df['gene_biotype'].str.contains('pseudogene'),:]

# select gene biotype
df = df.loc[df['gene_biotype'].isin(['protein_coding','lncRNA','miRNA'])]

df.rename(columns={'seqname':'chr'}, inplace=True)

cols_rm=['source','gene_source','feature','start','end','exon_version','protein_version', 'score', 'strand', 'frame','gene_version','tag','transcript_version','ccds_id','exon_number','transcript_support_level','transcript_source','transcript_biotype','exon_id','transcript_name','transcript_id']
df.drop(columns=cols_rm, inplace=True)
#import altair as alt
#alt.renderers.enable('altair_viewer')
#df[['feature','gene_biotype']].drop_duplicates()

df['chr'] = 'Crh'+df['chr']

lncrna = df[df['gene_biotype'] == 'lncRNA']
lncrna = lncrna.drop(columns=['gene_biotype','protein_id'])
lncrna.to_csv('data/clean/lncRNAs.csv',index=False)

mirna = df[df['gene_biotype'] == 'miRNA']
mirna = mirna.drop(columns=['gene_biotype','protein_id'])
mirna.to_csv('data/clean/miRNAs.csv', index=False)

df = df.loc[df['gene_biotype'] == 'protein_coding']
df = df.drop(columns=['gene_biotype'])
df.to_csv('data/clean/proteinCoding.csv', index=False)
print(df.head())

# columns:
# 'seqname', 'source', 'feature', 'start', 'end', 'score', 'strand',
# 'frame', 'gene_id', 'gene_version', 'gene_name', 'gene_source',
#'gene_biotype', 'transcript_id', 'transcript_version',
#'transcript_name', 'transcript_source', 'transcript_biotype', 'tag',
#'ccds_id', 'exon_number', 'exon_id', 'exon_version', 'protein_id',
# 'protein_version', 'transcript_support_level'

# seqname:
# ['1' '2' '3' '4' '5' '6' '7' 'X' '8' '9' '11' '10' '12' '13' '14' '15'
# '16' '17' '18' '20' '19' 'Y' '22' '21' 'MT' 'KI270728.1' 'KI270727.1'
# 'KI270442.1' 'GL000225.1' 'GL000009.2' 'GL000194.1' 'GL000205.2'
# 'GL000195.1' 'KI270733.1' 'GL000219.1' 'GL000216.2' 'KI270744.1'
# 'KI270734.1' 'GL000213.1' 'GL000220.1' 'GL000218.1' 'KI270731.1'
# 'KI270750.1' 'KI270721.1' 'KI270726.1' 'KI270711.1' 'KI270713.1']

# source:
# 'ensembl_havana' 'havana' 'ensembl' 'havana_tagene'
# 'ensembl_havana_tagene' 'mirbase' 'ensembl_tagene' 'insdc'

# feature:
# 'gene' 'transcript' 'exon' 'CDS' 'start_codon' 'stop_codon'
# 'five_prime_utr' 'three_prime_utr' 'Selenocysteine'

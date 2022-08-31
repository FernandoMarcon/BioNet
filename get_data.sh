#!/bin/bash

OUTDIR=data/raw
mkdir -p $OUTDIR
cd $OUTDIR

GENEURL=http://ftp.ensembl.org/pub/release-107/gtf/homo_sapiens/Homo_sapiens.GRCh38.107.gtf.gz

echo " [GENES] Downloading GTF"
wget $GENEURL

FNAME="$(basename $GENEURL)"
echo " [ GENES ] extracting $FNAME "
gzip -d $FNAME

echo " [ GENES ] Done! "


PROTEINLINK="https://stringdb-static.org/download/protein.links.v11.5/9606.protein.links.v11.5.txt.gz"
PROTEININFO="https://stringdb-static.org/download/protein.info.v11.5/9606.protein.info.v11.5.txt.gz"
echo
echo " [ PROTEINS ] Downloading Protein Links "
wget $PROTEINLINK

FNAME="$(basename $PROTEINLINK)"
echo " [ PROTEINS ] Extracting $FNAME "
gzip -d $FNAME

echo " [ PROTEINS ] Downloading Protein Info "
wget $PROTEININFO

FNAME="$(basename $PROTEININFO)"
echo " [ PROTEINS ] Extracting $FNAME "
gzip -d $FNAME

echo " [ PROTEINS ] Done! "

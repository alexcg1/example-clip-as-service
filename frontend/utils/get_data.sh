# You'll need Kaggle installed for this
mkdir data
kaggle datasets download -f quotes.csv manann/quotes-500k
unzip quotes.csv.zip
rm -f quotes.csv.zip
mv quotes.csv data

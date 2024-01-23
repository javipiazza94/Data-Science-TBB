import pandas as pd

# Nombre del archivo TSV de entrada
input_file_tsv = "C://Users//Javi P. Piazza//Downloads//en.openfoodfacts.org.products.tsv"

# Nombre del archivo CSV de salida
output_file_csv = "C://Users//Javi P. Piazza//Downloads//en.openfoodfacts.org.products.csv"

# Leer el archivo TSV y guardarlo como CSV
df = pd.read_csv(input_file_tsv, sep='\t')
df.to_csv(output_file_csv, index=False)



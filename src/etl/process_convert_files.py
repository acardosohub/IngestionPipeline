import pandas as pd
def process_file(file_path):
    """Processa um arquivo de acordo com a lógica desejada."""
    print(f"Processando arquivo: {file_path}")
    # Adicione aqui a lógica de processamento do arquivo
    df = pd.read_csv(file_path)
    df.to_parquet('/datalake/1.raw/data.parquet', engine='pyarrow')
    # Adicione aqui a lógica de processamento do arquivo

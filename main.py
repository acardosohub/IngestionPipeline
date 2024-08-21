import src.filesystem.module_files as fs
import src.logging.all_function as log

# Diretório inicial a ser processado
#landing_path = '/dataLake/0.landing/'
print("Definindo as variáveis")
initial_directory = '/dataLake/0.landing/'
processed_directory = '/dataLake/5.Processed/'
processed_files = set()
log.writelog(f"Iniciando a função para checar os arquivos no diretorio {initial_directory} .")
processed_files = fs.process_directory(initial_directory, processed_directory, processed_files )
print(processed_files)
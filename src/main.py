import src.filesystem.modulefiles as fs



# Diretório inicial a ser processado
#landing_path = '/dataLake/0.landing/'
initial_directory = '/dataLake/0.landing/'
processed_directory = '/dataLake/5.Processed/'
processed_files = set()
processed_files = fs.process_directory(initial_directory, processed_directory, processed_files )
print(processed_files)

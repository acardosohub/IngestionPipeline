import os
from src.filesystem.modulecompress import is_compressed, extract_file
import shutil
def count_files_in_directory(directory):
    """Conta todos os arquivos em um diretório, incluindo subdiretórios."""
    count = 0
    for root, dirs, files in os.walk(directory):
        count += len(files)
    return count

def process_directory(directory, processed_dir , processed_files):
    """Processa todos os arquivos em um diretório, descompactando conforme necessário."""

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path in processed_files:
                continue

            if is_compressed(file_path):
                initial_files = count_files_in_directory(root)
                # Descompacta no mesmo diretório
                expected_count = extract_file(file_path, root)
                final_files = count_files_in_directory(root)
                extracted_count = final_files - initial_files
                print(f"Arquivo Descompactado {file_path} - Quantidade de arquivos descompactados {extracted_count}")
                print(f"Arquivo Descompactado {file_path} - Quantidade de arquivos esperados {expected_count}")
                if extracted_count == expected_count:
                    # Adiciona o arquivo à lista de processados
                    processed_files.add(file_path)
                    # Move o arquivo compactado para a pasta processed
                    os.makedirs(processed_dir, exist_ok=True)
                    print(f'Caminho {file_path} Movido {os.path.join(processed_dir, file)} ')
                    shutil.move(file_path, os.path.join(processed_dir, file))
                    # Recursivamente processa os novos arquivos extraídos
                    process_directory(root, processed_dir , processed_files )
                else:
                    print(
                        f"Falha ao descompactar {file_path} ou número de arquivos descompactados não corresponde ao esperado.")
            else:
                # process_file(file_path)
                # Adiciona o arquivo à lista de processados
                processed_files.add(file_path)
    return  processed_files
import zipfile
import tarfile

def extract_file(file_path, extract_to):
    """Extrai um arquivo compactado para um diretório especificado e retorna os novos arquivos extraídos."""
    if zipfile.is_zipfile(file_path):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
            expected_count = len([f for f in zip_ref.namelist() if not f.endswith('/')])
    elif tarfile.is_tarfile(file_path):
        with tarfile.open(file_path, 'r') as tar_ref:
            tar_ref.extractall(extract_to)
            expected_count = len([m for m in tar_ref.getmembers() if m.isfile()])
    else:
        return 0 # Retorna zero se não for um arquivo compactado válido
    return expected_count

def is_compressed(file_path):
    """Verifica se um arquivo é um arquivo compactado."""
    return zipfile.is_zipfile(file_path) or tarfile.is_tarfile(file_path)
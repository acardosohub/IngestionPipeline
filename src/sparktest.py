from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

def test_spark_connection():
    try:
        # Criar uma SparkSession
        spark = (
            SparkSession.builder \
            .appName("PyCharmJob") \
            .master("spark://spark-master:7077") \
            .config("spark.executor.memory", "2g") \
            .config("spark.executor.cores", "2") \
            .config("spark.executor.instances", "6") \
            .getOrCreate()
        )

        # Tente a leitura de dados de uma tabela MySQL para um DataFrame
        try:
            # Caminho para o arquivo Parquet
            parquet_file_path = '/dataLake/1.raw/data.parquet/'

            # Lê o arquivo Parquet
            df = spark.read.parquet(parquet_file_path)

            # Mostra o schema do DataFrame
            df.printSchema()

            # Mostra as primeiras 20 linhas do DataFrame
            df.show()

            # Calcula a média de uma coluna específica
            column_name = "Amount Paid"
            average_df = df.select(avg(column_name).alias('average_value'))

            # Exibe o resultado
            average_df.show()
            
        except Exception as e:
            print("Erro ao ler dados do MySQL:", e)

        # Finalizar a SparkSession
        spark.stop()
    except Exception as e:
        print(f"Failed to connect to Spark: {e}")

if __name__ == "__main__":
    test_spark_connection()

from pyspark.sql import SparkSession

# Cria uma sessão Spark spark://spark-master:7077
spark = SparkSession.builder \
    .appName("Teste do Ambiente Spark") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

# Cria um DataFrame simples com alguns dados
data = [("Alice", 29), ("Bob", 31), ("Catherine", 25)]
columns = ["Nome", "Idade"]

df = spark.createDataFrame(data, columns)

# Mostra o DataFrame
df.show()

# Conta o número de linhas no DataFrame
count = df.count()

print(f"O DataFrame contém {count} linhas.")

# Para a sessão Spark
spark.stop()
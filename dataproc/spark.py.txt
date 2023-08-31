from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import col, lag, avg

# Inicializa a sessão Spark
spark = SparkSession.builder.appName("GCS_to_BQ").getOrCreate()

# Define as configurações do Google Cloud Storage
gcs_bucket = "seu-bucket"
gcs_path = "caminho/para/seu/arquivo.csv"

# Lê o CSV do Google Cloud Storage
df = spark.read.csv(f"gs://{gcs_bucket}/{gcs_path}", header=True)

# Calcula a volatilidade do dia (High - Low)
df = df.withColumn("Volatility", col("High") - col("Low"))

# Calcula a variação do Close de hoje com o do dia de ontem
window_spec = Window.orderBy("Date")
df = df.withColumn("Close_Prev_Day", lag(col("Close/Last")).over(window_spec))
df = df.withColumn("Close_Variation", col("Close/Last") - col("Close_Prev_Day"))

# Calcula a média da variação de fechamento dos últimos 5 dias
window_spec_5days = Window.orderBy("Date").rowsBetween(-4, 0)
df = df.withColumn("Close_Variation_Avg_5days", avg(col("Close_Variation")).over(window_spec_5days))

# Escreve o resultado na tabela do BigQuery
table_name = "seu_projeto.seu_dataset.sua_tabela"
df.write.format("bigquery").option("table", table_name).mode("overwrite").save()

# Encerra a sessão Spark
spark.stop()


O *Google Dataproc* é um serviço gerenciado que permite executar clusters do Apache Spark e Apache Hadoop de maneira eficiente na infraestrutura do Google Cloud. 

## Comando gcloud que aloca um cluster no serviço Google Dataproc

```bash
  gcloud dataproc clusters create cluster-dataproc-phcj \
    --enable-component-gateway \
    --region us-east1 \
    --zone us-east1-c \
    --master-machine-type n1-standard-2 \
    --master-boot-disk-size 500 --num-workers 2 \
    --worker-machine-type n1-standard-2 \
    --worker-boot-disk-size 500 \
    --image-version 2.0-debian10 \
    --scopes 'https://www.googleapis.com/auth/cloud-platform' \
    --project project_name
```

### Detalhes do comando

1. `gcloud dataproc clusters create`: Isso indica que você está usando o Google Cloud SDK para criar um novo cluster no Google Dataproc.

2. `cluster-dataproc-phcj`: Este é o nome que você está dando ao cluster que será criado. Você pode substituir "cluster-dataproc-phcj" pelo nome desejado para o seu cluster.

3. `--enable-component-gateway`: Essa opção indica que você deseja habilitar o componente de gateway para o cluster. Isso permite que você acesse interfaces da web de componentes individuais do cluster, como o Spark UI, através de um proxy seguro.

4. `--region us-east1`: Especifica a região onde o cluster será criado. Neste caso, o cluster será criado na região us-east1 (leste dos EUA).

5. `--zone us-east1-c`: Especifica a zona dentro da região escolhida onde o cluster será criado. Neste caso, o cluster será criado na zona us-east1-c.

6. `--master-machine-type n1-standard-2`: Define o tipo de máquina para o nó mestre do cluster. Neste caso, está definido como "n1-standard-2", que é uma máquina virtual com recursos de CPU e memória específicos.

7. `--master-boot-disk-size 500`: Especifica o tamanho do disco de inicialização para o nó mestre do cluster. O valor é definido como 500 GB.

8. `--num-workers 2`: Define o número de nós de trabalho (workers) no cluster. Neste caso, o cluster terá 2 nós de trabalho.

9. `--worker-machine-type n1-standard-2`: Define o tipo de máquina para os nós de trabalho do cluster. Novamente, está definido como "n1-standard-2".

10. `--worker-boot-disk-size 500`: Especifica o tamanho do disco de inicialização para os nós de trabalho do cluster. O valor é definido como 500 GB.

11. `--image-version 2.0-debian10`: Indica a versão da imagem do Dataproc que será usada para criar o cluster. Neste caso, a versão 2.0 com base no sistema Debian 10 será usada.

12. `--scopes 'https://www.googleapis.com/auth/cloud-platform'`: Define os escopos de acesso para o cluster. Neste caso, o escopo 'https://www.googleapis.com/auth/cloud-platform' é configurado, o que permitirá ao cluster acessar recursos na Google Cloud Platform.

13. `--project project_name`: Especifica o projeto do Google Cloud onde o cluster será criado. Substitua "project_name" pelo ID do projeto correto.


Após alocado o cluster podemos submeter o codigo pyspark ao cluster com seguinte comando:

```bash
  gcloud dataproc jobs submit pyspark --cluster=cluster-dataproc-phcj dataproc.py
```

Ao executar o comando é gerado um id para o job. Para acompanhar o log de execução do job podemos usar o seguinte comando:

```bash
gcloud dataproc jobs wait <job_id> --project silver-charmer-243611 --region us-east1
```

Ao final da execução do job, podemos desalocar o cluster.

```bash
gcloud dataproc clusters delete cluster-dataproc-phcj --region=us-east1
```

<br>
<br>

## Comando gcloud que aloca um cluster SERVELESS no serviço Google Dataproc

Uma opção incrivel é alocar o cluster sem se preocupar com os requisitos técnicos, e o GCP provem essa possibilidade. O comando seguinte permite isso.

```bash

gcloud dataproc batches submit pyspark dataproc.py \
    --batch=batch-dataproc \
    --deps-bucket=gs://phcj-code-repository \
    --region=us-east1 \
    --py-files='dataproc.py'

```

### Detalhes do comando

- `gcloud dataproc batches submit pyspark`: Isso indica que você está usando o Google Cloud SDK (`gcloud`) para submeter um trabalho do tipo pyspark (Python com Apache Spark) para o serviço Google Dataproc Batch.

- `dataproc.py`: Este é o nome do arquivo Python que contém o código do ETL para as análises de avaliações do Yelp. Certifique-se de que esse arquivo exista no diretório atual ou forneça o caminho correto.

- `--batch=batch-dataproc`: Define o nome do lote (batch) do trabalho. Nesse caso, o nome é "batch-dataproc". Esse nome é usado para identificar o lote no Dataproc.

- `--deps-bucket=gs://phcj-code-repository`: Especifica o bucket do Google Cloud Storage onde as dependências do trabalho estão localizadas. Nesse caso, o caminho do bucket é "gs://phcj-code-repository".

- `--region=us-east1`: Especifica a região onde o trabalho será executado. Nesse caso, o trabalho será executado na região us-east1 (leste dos EUA).

- `--py-files='dataproc.py'`: Lista os arquivos Python que devem ser distribuídos e disponibilizados para o ambiente de execução do Spark. Isso garante que o arquivo de script principal e suas dependências sejam acessíveis durante a execução.

Para acompanhar o log de execução do job podemos usar o seguinte comando:

```bash
gcloud dataproc batches wait batch-dataproc --project project_name --region us-east1
```

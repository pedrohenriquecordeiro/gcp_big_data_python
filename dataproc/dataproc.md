
O *Google Dataproc* é um serviço gerenciado que permite executar clusters do Apache Spark e Apache Hadoop de maneira eficiente na infraestrutura do Google Cloud. 

## Comando gcloud que aloca um cluster no serviço Google Dataproc

```bash
  gcloud dataproc clusters create owshq-apache-spark --enable-component-gateway --region us-east1 --zone us-east1-c --master-machine-type n1-standard-2 --master-boot-disk-size 500 --num-workers 2 --worker-machine-type n1-standard-2 --worker-boot-disk-size 500 --image-version 2.0-debian10 --scopes 'https://www.googleapis.com/auth/cloud-platform' --project silver-charmer-243611

```

### Detalhes do comando gcloud

1. `gcloud dataproc clusters create`: Isso indica que você está usando o Google Cloud SDK para criar um novo cluster no Google Dataproc.

2. `owshq-apache-spark`: Este é o nome que você está dando ao cluster que será criado. Você pode substituir "owshq-apache-spark" pelo nome desejado para o seu cluster.

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

13. `--project silver-charmer-243611`: Especifica o projeto do Google Cloud onde o cluster será criado. Substitua "silver-charmer-243611" pelo ID do projeto correto.





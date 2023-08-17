
## Publicador - PubSub 

O **Google Cloud Pub/Sub** é um serviço de mensagens assíncrono no Google Cloud Platform. Ele permite que aplicativos se comuniquem através de tópicos e assinantes. Os publicadores enviam mensagens para tópicos, e os assinantes se inscrevem nesses tópicos para receber as mensagens. O serviço garante a entrega confiável e escalável das mensagens, permitindo o processamento assíncrono por parte dos assinantes. O Pub/Sub simplifica a comunicação em sistemas distribuídos e lida automaticamente com a entrega de mensagens.

#### Começando com o Google Cloud Pub/Sub:

1.  **Crie um novo projeto no Google Cloud:** O Projeto é um ambiente no Google Cloud Platform que contém recursos e serviços. Cada projeto é identificado por um `project_id`, que é um identificador único para rastrear e gerenciar os recursos dentro do projeto.
    
2.  **Ative o Serviço:** Dentro do projeto, ative o serviço Google Cloud Pub/Sub e crie um tópico.
    
3.  **Configuração de Identificação:**  Crie uma conta de serviço para o projeto. Após criar a conta de serviço, exporte a key em um arquivo JSON. Após a exportação da key, vá na interface do PubSub e adicione a conta de serviço do projeto criado anteriormente nas permissões do tópico PubSub.

#### Código Publicador:

Vejamos um código que ilustra o processo de publicar uma mensagem simples em um tópico no Google Cloud Pub/Sub.
```py
# Importa o módulo pubsub_v1 da biblioteca google.cloud
from google.cloud import pubsub_v1

# Importa o módulo service_account da biblioteca google.oauth2
from google.oauth2 import service_account

# Cria as credenciais a partir das informações da conta de serviço
credentials = (
    service_account
    .Credentials
    .from_service_account_file("docs/key_json_service_account.json")
)

# Obtém o ID do projeto a partir das credenciais
project_id = credentials.project_id

# Define o nome do tópico
topic_name = 'topic-name'

# Cria um cliente de publicador (publisher) usando as credenciais
publisher = pubsub_v1.PublisherClient(credentials=credentials)

# Cria o caminho completo do tópico a ser usado
topic_path = publisher.topic_path(project_id, topic_name)

# Define os dados da mensagem a ser publicada
message_data = b'Hello from the outher side'

# Publica a mensagem no tópico
future = publisher.publish(topic_path, data=message_data)

# Aguarda a conclusão da publicação da mensagem
future.result()

# Imprime uma mensagem indicando que a mensagem foi publicada
print(f"Mensagem publicada no tópico '{topic_path}': {message_data.decode('utf-8')}")

```
Após a publicação, a mensagem é entregue a todos os assinantes do tópico, sem importar a quantidade de assinantes ou suas localizações geográficas. Essa funcionalidade se mostra especialmente valiosa em situações onde a disseminação ágil e confiável de informações é essencial para diversas partes interessadas.

Além disso, o Google Cloud Pub/Sub oferece uma integração com outros serviços dentro do ecossistema do Google Cloud, incluindo o BigQuery. Essa integração possibilita a configuração do fluxo de mensagens do Pub/Sub para que elas sejam automaticamente direcionadas a tabelas do BigQuery. 



## Publicador - PubSub 

O **Google Cloud Pub/Sub** é um serviço de mensagens assíncrono no Google Cloud Platform. Ele permite que aplicativos se comuniquem através de tópicos e assinantes. Os publicadores enviam mensagens para tópicos, e os assinantes se inscrevem nesses tópicos para receber as mensagens. O serviço garante a entrega confiável e escalável das mensagens, permitindo o processamento assíncrono por parte dos assinantes. O Pub/Sub simplifica a comunicação em sistemas distribuídos e lida automaticamente com a entrega de mensagens.

#### Começando com o Google Cloud Pub/Sub:

1.  **Crie um novo projeto no Google Cloud:** O Projeto é um ambiente no Google Cloud Platform que contém recursos e serviços. Cada projeto é identificado por um `project_id`, que é um identificador único para rastrear e gerenciar os recursos dentro do projeto.
    
2.  **Ative o Serviço:** Dentro do projeto, ative o serviço Google Cloud Pub/Sub. 
    
3.  **Configuração de Identificação:** Configure a autenticação usando informações da conta de serviço. Isso geralmente envolve um arquivo JSON que contém as credenciais necessárias.

#### Código Publicador:

Vejamos um código que ilustra o processo de publicar uma mensagem simples em um tópico no Google Cloud Pub/Sub.
```py
# Importa os módulos necessários
import os
import json

# Importa as classes do Google Cloud Pub/Sub e de autenticação JWT
from google.cloud import pubsub_v1
from google.auth import jwt

# Carrega as informações da conta de serviço a partir de um arquivo JSON
service_account_info = json.load(open("service-account-info.json"))

# Cria as credenciais JWT a partir das informações da conta de serviço
credentials = jwt.Credentials.from_service_account_info(service_account_info)

# Cria um cliente do Pub/Sub para publicadores usando as credenciais 
publisher = pubsub_v1.PublisherClient(credentials=credentials)

# Define o ID do projeto e o nome do tópico
project_id = 'GOOGLE_CLOUD_PROJECT_ID'
topic = 'TOPIC_NAME'

# Cria o nome completo do tópico a ser criado usando f-strings
topic_name = f'projects/{project_id}/topics/{topic}'

# Cria um novo tópico no Google Cloud Pub/Sub
publisher.create_topic(name=topic_name)

# Publica uma mensagem no tópico especificado
future = publisher.publish(topic_name, b'My first message!', spam='eggs')

# Aguarda a conclusão da publicação da mensagem
future.result()
```
Após a publicação, a mensagem é entregue a todos os assinantes do tópico, sem importar a quantidade de assinantes ou suas localizações geográficas. Essa funcionalidade se mostra especialmente valiosa em situações onde a disseminação ágil e confiável de informações é essencial para diversas partes interessadas.

Além disso, o Google Cloud Pub/Sub oferece uma integração com outros serviços dentro do ecossistema do Google Cloud, incluindo o BigQuery. Essa integração possibilita a configuração do fluxo de mensagens do Pub/Sub para que elas sejam automaticamente direcionadas a tabelas do BigQuery. 


## Assinante - PubSub 

O **Google Cloud Pub/Sub** é um serviço de mensagens assíncrono no Google Cloud Platform. Ele permite que aplicativos se comuniquem através de tópicos e assinantes. Os publicadores enviam mensagens para tópicos, e os assinantes se inscrevem nesses tópicos para receber as mensagens. O serviço garante a entrega confiável e escalável das mensagens, permitindo o processamento assíncrono por parte dos assinantes. O Pub/Sub simplifica a comunicação em sistemas distribuídos e lida automaticamente com a entrega de mensagens.

#### Começando com o Google Cloud Pub/Sub:

1.  **Crie um novo projeto no Google Cloud:** O Projeto é um ambiente no Google Cloud Platform que contém recursos e serviços. Cada projeto é identificado por um `project_id`, que é um identificador único para rastrear e gerenciar os recursos dentro do projeto.
    
2.  **Ative o Serviço:** Dentro do projeto, ative o serviço Google Cloud Pub/Sub. 
    
3.  **Configuração de Identificação:** Configure a autenticação usando informações da conta de serviço. Isso geralmente envolve um arquivo JSON que contém as credenciais necessárias.

#### Código Assinante:

Vejamos um código que ilustra o processo de assinatura de um tópico no Google Cloud Pub/Sub.
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

# Define o ID do projeto e o nome do tópico
project_id = 'GOOGLE_CLOUD_PROJECT_ID'  # Substitua pelo ID do seu projeto no Google Cloud
topic = 'TOPIC_NAME'  # Substitua pelo nome do tópico que você deseja criar/publicar
subscription = 'SUBSCRIPTION_NAME'  # Substitua pelo nome da assinatura que você deseja criar

# Cria o nome completo do tópico e da assinatura a serem criados usando f-strings
topic_name = f'projects/{project_id}/topics/{topic}'
subscription_name = f'projects/{project_id}/subscriptions/{subscription}'

# Define uma função de callback para processar as mensagens recebidas
def callback(message):
    print(message.data)  # Imprime os dados da mensagem recebida
    message.ack()        # Confirma o recebimento da mensagem

# Cria um cliente de assinante (subscriber)
with pubsub_v1.SubscriberClient() as subscriber:
    # Cria uma nova assinatura para o tópico especificado
    subscriber.create_subscription(
        name=subscription_name, 
        topic=topic_name)
    
    # Inicia a subscrição à assinatura criada, passando a função de callback
    future = subscriber.subscribe(subscription_name, callback)

try:
    future.result()  # Aguarda até que o resultado esteja disponível
except KeyboardInterrupt:
    future.cancel()  # Cancela a subscrição se houver uma interrupção de teclado

```

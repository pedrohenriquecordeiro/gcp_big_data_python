
## Assinante - PubSub 

O **Google Cloud Pub/Sub** é um serviço de mensagens assíncrono no Google Cloud Platform. Ele permite que aplicativos se comuniquem através de tópicos e assinantes. Os publicadores enviam mensagens para tópicos, e os assinantes se inscrevem nesses tópicos para receber as mensagens. O serviço garante a entrega confiável e escalável das mensagens, permitindo o processamento assíncrono por parte dos assinantes. O Pub/Sub simplifica a comunicação em sistemas distribuídos e lida automaticamente com a entrega de mensagens.

#### Começando com o Google Cloud Pub/Sub:

1.  **Crie um novo projeto no Google Cloud:** O Projeto é um ambiente no Google Cloud Platform que contém recursos e serviços. Cada projeto é identificado por um `project_id`, que é um identificador único para rastrear e gerenciar os recursos dentro do projeto.
    
2.  **Ative o Serviço:** Dentro do projeto, ative o serviço Google Cloud Pub/Sub. 
    
3.  **Configuração de Autenticação:** Crie uma conta de serviço para o projeto. Após criar a conta de serviço, exporte a key em um arquivo JSON. Após a exportação da key, vá na interface do PubSub e adicione a conta de serviço do projeto criado anteriormente nas permissões da assinatura PubSub.

#### Código Assinante:

Vejamos um código que ilustra o processo de assinatura de um tópico no Google Cloud Pub/Sub.
```py
# Importa as classes do Google Cloud Pub/Sub e de autenticação JWT
from google.cloud import pubsub_v1
from google.oauth2 import service_account

# Cria as credenciais a partir das informações da conta de serviço
credentials = (
    service_account
    .Credentials
    .from_service_account_file("docs/key_json_service_account.json")
)

# Obtém o ID do projeto a partir das credenciais
project_id = credentials.project_id

# Define o nome da assinatura
subscription_name = 'topic-name'

# Cria um cliente de assinante (subscriber) usando as credenciais
subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

# Cria o caminho completo da assinatura a ser usada
subscription_path = subscriber.subscription_path(project_id, subscription_name)

# Define uma função de callback para processar as mensagens recebidas
def callback(message):
    print(f"Received message: {message.data.decode('utf-8')}")
    message.ack()  # Confirma o recebimento da mensagem

# Inicia a subscrição à assinatura criada, passando a função de callback
future = subscriber.subscribe(subscription_path, callback)

# Imprime uma mensagem indicando que o script está aguardando mensagens
print(f"Aguardando mensagens do tópico '{subscription_path}'...")

try:
    future.result()  # Aguarda até que o resultado do futuro (future) esteja disponível
except KeyboardInterrupt:
    future.cancel()  # Cancela a subscrição se houver uma interrupção de teclado

```

Note que é fundamental que a conta de serviço criada para o projeto tenha permissão adequada na assinatura PubSub, caso contrário irá ser gerado um erro por falta de permissão.

import random
import string
import time

from google.cloud import pubsub_v1
from google.oauth2 import service_account

# Cria as credenciais a partir das informações da conta de serviço
credentials = (
    service_account
    .Credentials
    .from_service_account_file("docs/project-tester-2023-a40860db8b45.json")
)

project_id = credentials.project_id
topic_name = 'topic-tester'


# Cria um cliente de publicador (publisher) usando as credenciais
publisher = pubsub_v1.PublisherClient(credentials=credentials)

# Cria o nome completo do tópico a ser usado
topic_path = publisher.topic_path(project_id, topic_name)

# Função para gerar mensagens aleatórias
def generate_random_message():
    message_length = random.randint(10, 50)  # Tamanho aleatório da mensagem
    message = ''.join(random.choices(string.ascii_letters + string.digits, k=message_length))
    return message.encode('utf-8')

while True:
    message_data = generate_random_message()
    future = publisher.publish(topic_path, data=message_data)
    future.result()  # Aguarda a conclusão da publicação da mensagem
    print(f"Mensagem publicada no tópico: {message_data.decode('utf-8')}")
    time.sleep(random.uniform(1, 5))  # Aguarda um tempo aleatório entre 1 e 5 segundos

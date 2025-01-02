
# Projeto de Notificação via WhatsApp e Gmail

Este projeto é uma aplicação Django que permite enviar notificações tanto por e-mail usando o Gmail quanto por WhatsApp utilizando a API do CallMeBot.

## Funcionalidades

- Envio de e-mails de notificação para um ou mais destinatários.
- Envio de mensagens via WhatsApp utilizando a API do CallMeBot.

## Pré-requisitos

- Python 3.x
- Django
- Dependências do projeto (listadas em `requirements.txt`)

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/nythan5/Notify.git
   cd Notify
   ```

2. Crie um ambiente virtual para o projeto:

   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   
   - No Linux/macOS:

     ```bash
     source venv/bin/activate
     ```

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

4. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

## Configuração

Antes de executar o projeto, é necessário configurar algumas variáveis de ambiente para o envio de notificações:

1. Configure as credenciais do Gmail no arquivo `.env` ou diretamente no seu ambiente de desenvolvimento:

   ```
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=seu_email@gmail.com
   EMAIL_HOST_PASSWORD=sua_senha
   EMAIL_ADMIN_RECEIVER=destinatario@gmail.com
   ```

2. Configure as credenciais da API do CallMeBot para enviar mensagens via WhatsApp:

   ```
   CALLMEBOT_API_URL=https://api.callmebot.com/whatsapp.php
   CALLMEBOT_PHONE_NUMBER=seu_numero_de_whatsapp
   CALLMEBOT_API_KEY=sua_chave_api
   ```

**Importante**: Para utilizar a API do CallMeBot, você precisa de uma chave de API, que pode ser obtida no [CallMeBot](https://www.callmebot.com/).

## Uso

Após a instalação e configuração, você pode usar o projeto para enviar notificações por e-mail e WhatsApp. O envio de mensagens pode ser feito via chamadas de funções ou pela interface de administração do Django (se configurada).

## Contribuições

Se você deseja contribuir com este projeto, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Licença

Este projeto está licenciado sob a licença MIT.

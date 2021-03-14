# A simple dialogflow template for running a custom chatbot on your website

## Getting Started

1. Clone this repo
```bash
git clone https://github.com/machaao/dialogflow-chatapp-template.git

cd dialogflow-chatapp-template
```

2. Installing Dependencies
```bash
pip install -r requirements.txt
```

3. Getting Required Tokens
- [Get Google Auth Token](https://cloud.google.com/dialogflow/es/docs/quick/setup)
- [Get MessengerX.io Auth Token](https://blog.messengerx.io/tutorials/get-api-token-for-messengerx-io-chat-app-marketplace/)

3. Environment Variable  
Create file with name ```.env```
```bash
GOOGLE_APPLICATION_CREDENTIALS=<YOUR_AUTH_KEY_PATH>
MESSENGERX_API_TOKEN=<YOU-MESSENGERX-API-KEY> (Get a FREE DEV token from -> portal.messengerx.io)
MESSENGERX_BASE_URL=https://ganglia-dev.machaao.com
```

4. Running Server
```bash
machaao run -p 5000 -t <YOU-MESSENGERX-API-KEY>
```

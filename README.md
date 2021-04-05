# A basic dialogflow template for running a custom chatbot on your website

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
- [Get Google Private Key](https://cloud.google.com/dialogflow/es/docs/quick/setup)
- [Get MessengerX.io Auth Token](https://blog.messengerx.io/tutorials/get-api-token-for-messengerx-io-chat-app-marketplace/)

4. Training Dialogflow Bot
- [Create and Customize the chatapp](https://cloud.google.com/dialogflow/es/docs/tutorials/build-an-agent/create-customize-agent)

5. Environment Variable  
Create file with name ```.env```
```bash
GOOGLE_APPLICATION_CREDENTIALS=<YOUR_AUTH_KEY_PATH>
MESSENGERX_API_TOKEN= <YOU-MESSENGERX-API-KEY> (Get a FREE DEV token from -> portal.messengerx.io)
MESSENGERX_BASE_URL= https://ganglia-dev.machaao.com
PROJECT_ID= <YOUR-DIALOGFLOW-PROJECT-ID>
```

6. Running locally 
```bash
machaao run -p 5000 -t <YOU-MESSENGERX-API-KEY>
```

7. To run for production, please contact us via support@messengerx.io

## Related Articles
- https://blog.messengerx.io/tutorials/get-api-token-for-messengerx-io-chat-app-marketplace/
- https://blog.messengerx.io/tutorials/build-deeply-personalized-chatbots-at-production-scale/
- https://blog.messengerx.io/tutorials/build-an-ai-based-chatbot-for-your-website-app-using-wit-ai/

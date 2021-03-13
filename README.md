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

3. Environment Variable  
Create file with name ```.env```
```bash
DIALOGFLOW_AUTH_TOKEN=<YOUR_DIALOGFLOW_AUTH_TOKEN>
MESSENGERX_API_TOKEN=<YOU-MESSENGERX-API-KEY>
MESSENGERX_BASE_URL=https://ganglia-dev.machaao.com
```

4. Running Server
```bash
machaao run -p 5000 -t <YOU-MESSENGERX-API-KEY>
```

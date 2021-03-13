# Machaao Dialogflow Template

## Getting Started

1. Clone this repo
```bash
git clone https://github.com/machaao/dialogflow-chatapp-template.git

cd machaao-dialogflow-template
```

2. Installing Dependencies
```bash
pip install -r requirements.txt
```

3. Environment Variable  
Create file with name ```.env```
```bash
DIALOGFLOW_AUTH_TOKEN=<YOU-WIT-ACCESS-TOKEN>
MESSENGERX_API_TOKEN=<YOU-MESSENGERX-API-KEY>
MESSENGERX_BASE_URL=https://ganglia-dev.machaao.com
```

4. Running Server
```bash
machaao run -p 5000 -t <YOU-MESSENGERX-API-KEY>
```

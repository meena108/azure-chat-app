🚀 Quick Start

```bash
# 1 Clone & enter the repo
git clone https://github.com/meena108/azure-chat-app.git
cd azure-chat-app

# 2 Install dependencies (use venv if you like)
pip install -r requirements.txt

# 3 Create your .env
cp .env.example .env
# then edit .env and add:
# PROJECT_ENDPOINT=...
# API_KEY=...
# MODEL_DEPLOYMENT=gpt-4o

# 4 Run!
python chat-app.py

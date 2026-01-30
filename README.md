# 🤖 JARVIS V2 - Assistente Empresarial

Sistema empresarial completo com IA, agentes especializados e arquitetura modular.

## 🏗️ Arquitetura

```
jarvis-v2/
├── backend/          # FastAPI + Python
│   ├── main.py       # Servidor principal
│   ├── auth.py       # Autenticação JWT
│   └── requirements.txt
├── frontend/         # React + Vite
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── App.jsx
│   └── package.json
└── README.md
```

## 🚀 Como Rodar

### 1️⃣ Backend (Python)

```bash
cd backend

# Criar ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente (opcional)
copy .env.example .env
# Edite o .env com suas chaves da OpenAI

# Iniciar servidor
uvicorn main:app --reload
```

**API rodará em:** http://localhost:8000
**Documentação:** http://localhost:8000/docs

### 2️⃣ Frontend (React)

```bash
cd frontend

# Instalar dependências
npm install

# Iniciar desenvolvimento
npm run dev
```

**App rodará em:** http://localhost:3000

### 3️⃣ Configuração OpenAI ChatKit (Opcional)

Para ativar a integração completa com ChatKit:

1. **Obtenha sua API Key da OpenAI**
2. **Configure no backend (.env):**
   ```env
   OPENAI_API_KEY=sk-your-key-here
   CHATKIT_WORKFLOW_ID=wf_your-workflow-id
   ```
3. **Instale a biblioteca ChatKit no frontend:**
   ```bash
   cd frontend
   npm install @openai/chatkit-react
   ```

## 🔐 Usuários de Teste

| Usuário   | Senha | Papel     | Agentes Disponíveis |
|-----------|-------|-----------|-------------------|
| admin     | 1234  | admin     | Todos os agentes  |
| ti        | 1234  | ti        | Sistema, TI       |
| operador  | 1234  | operador  | Vendas apenas     |

## 🤖 Sistema de Agentes

### Agentes Disponíveis:
- **🖥️ Sistema**: Operações do sistema
- **🔧 TI**: Diagnósticos técnicos
- **💼 Vendas**: Estratégias comerciais
- **💰 Financeiro**: Análises financeiras
- **📈 Marketing**: Campanhas e divulgação

### Classificação Automática:
O orquestrador analisa sua mensagem e direciona automaticamente para o agente mais adequado:

- "Erro no sistema" → Agente TI
- "Vender produto" → Agente Vendas
- "Custo do projeto" → Agente Financeiro
- "Campanha marketing" → Agente Marketing

## 🛠️ Tecnologias

### Backend:
- **FastAPI** - API moderna e rápida
- **JWT** - Autenticação segura
- **PostgreSQL** - Banco principal (opcional)
- **Redis** - Cache e sessões (opcional)
- **RBAC** - Controle de acesso baseado em papéis

### Frontend:
- **React 18** - Interface moderna
- **Vite** - Build tool rápido
- **Axios** - Cliente HTTP
- **Lucide React** - Ícones

## 🔧 Configuração Avançada

### Variáveis de Ambiente:

**Backend (.env):**
```env
JARVIS_MODE=hybrid          # offline | online | hybrid
POSTGRES_DSN=dbname=jarvis user=jarvis password=jarvis host=localhost
REDIS_URL=redis://localhost:6379/0
OPENAI_API_KEY=your_key_here
```

**Frontend (.env):**
```env
VITE_API_URL=http://localhost:8000
```

### Modos de Operação:
- **offline**: Usa LLM local
- **online**: Usa APIs externas (OpenAI)
- **hybrid**: Tenta online, fallback para local

## 📊 Recursos

### ✅ Implementado:
- Sistema de login com JWT
- Chat em tempo real
- Sistema de agentes especializados
- RBAC (controle de acesso)
- Memória de conversas
- Interface responsiva
- Fallback para serviços indisponíveis
- **🆕 Integração OpenAI ChatKit**
- **🆕 LLM real com OpenAI GPT-4**
- **🆕 Sistema de Plugins Modular**
- **🆕 Gerenciador de Plugins Visual**
- **🆕 Plugins de Exemplo (Weather, Calculator)**

### 🔄 Próximas Funcionalidades:
- WhatsApp Bot
- Dashboard administrativo
- Marketplace de plugins
- Deploy automatizado
- App desktop (Electron)

## 🐳 Docker (Opcional)

```yaml
# docker-compose.yml
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - JARVIS_MODE=hybrid
  
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
  
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
  
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: jarvis
      POSTGRES_USER: jarvis
      POSTGRES_PASSWORD: jarvis
    ports:
      - "5432:5432"
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🆘 Suporte

- **Issues**: Reporte bugs ou solicite funcionalidades
- **Discussões**: Tire dúvidas e compartilhe ideias
- **Wiki**: Documentação detalhada

---

**Desenvolvido com ❤️ para empresas que querem automatizar processos com IA**
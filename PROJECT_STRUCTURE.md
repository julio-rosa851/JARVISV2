# 📁 JARVIS V2 - Estrutura Completa do Projeto

## 🎯 Visão Geral
Sistema JARVIS V2 completo com interface gráfica, monitoramento avançado, integração Datadog e Firebase, sistema de plugins e distribuição executável.

## 📂 Estrutura de Arquivos

```
jarvis-v2/
├── 📁 assets/                          # Recursos visuais
│   ├── jarvis-icon.ico                 # Ícone do aplicativo (Windows)
│   └── jarvis-icon.png                 # Ícone PNG
│
├── 📁 backend/                         # Backend Python/FastAPI
│   ├── 📁 __pycache__/                 # Cache Python
│   ├── 📁 plugins/                     # Sistema de plugins
│   │   ├── base.py                     # Classe base para plugins
│   │   ├── manager.py                  # Gerenciador de plugins
│   │   ├── __init__.py                 # Inicialização
│   │   └── 📁 examples/                # Exemplos de plugins
│   │       ├── 📁 calculator_tool/     # Plugin calculadora
│   │       └── 📁 weather_agent/       # Plugin clima
│   ├── 📁 venv/                        # Ambiente virtual Python
│   ├── .env.example                    # Exemplo de variáveis de ambiente
│   ├── auth.py                         # Sistema de autenticação
│   ├── datadog_metrics.py              # Métricas Datadog customizadas
│   ├── firebase_config.py              # Configuração Firebase
│   ├── main.py                         # Backend principal (completo)
│   ├── requirements.txt                # Dependências Python
│   ├── simple_main.py                  # Backend simplificado (ativo)
│   └── telemetry.py                    # OpenTelemetry configuration
│
├── 📁 docs/                            # Documentação
│   └── PLUGIN_DEVELOPMENT.md           # Guia de desenvolvimento de plugins
│
├── 📁 frontend/                        # Frontend React/Vite
│   ├── 📁 node_modules/                # Dependências Node.js
│   ├── 📁 src/                         # Código fonte
│   │   ├── 📁 components/              # Componentes React
│   │   │   ├── Chat.jsx                # Componente de chat
│   │   │   ├── ChatKitWidget.jsx       # Widget ChatKit
│   │   │   ├── Login.jsx               # Componente de login
│   │   │   └── PluginManager.jsx       # Gerenciador de plugins
│   │   ├── 📁 services/                # Serviços
│   │   │   ├── api.js                  # Cliente API
│   │   │   └── chatkit.js              # Integração ChatKit
│   │   ├── App.jsx                     # Componente principal
│   │   ├── index.css                   # Estilos globais
│   │   └── main.jsx                    # Ponto de entrada
│   ├── .env                            # Variáveis de ambiente
│   ├── index.html                      # HTML principal
│   ├── package-lock.json               # Lock de dependências
│   ├── package.json                    # Configuração do projeto
│   └── vite.config.js                  # Configuração Vite
│
├── 📄 auto-update.py                   # Sistema de auto-atualização
├── 📄 build-all.bat                    # Script de build completo
├── 📄 build-executable.bat             # Criador de executáveis
├── 📄 create-icon.py                   # Gerador de ícones
├── 📄 create-installer.bat             # Criador de instalador Windows
├── 📄 datadog-config.yaml              # Configuração Datadog Agent
├── 📄 EXECUTABLE.md                    # Guia do executável
├── 📄 jarvis-launcher.py               # Launcher gráfico principal
├── 📄 monitoring-dashboard.html        # Dashboard de monitoramento
├── 📄 MONITORING.md                    # Guia de monitoramento
├── 📄 otel-config.yaml                 # Configuração OpenTelemetry
├── 📄 package.json                     # Configuração raiz do projeto
├── 📄 README.md                        # Documentação principal
├── 📄 setup-datadog-monitoring.bat     # Setup Datadog
├── 📄 start-with-monitoring.bat        # Inicialização com monitoramento
└── 📄 start.bat                        # Script de inicialização principal
```

## 🚀 Scripts de Execução

### Desenvolvimento
- **`start.bat`** - Inicia sistema básico (backend + frontend)
- **`start-with-monitoring.bat`** - Inicia com monitoramento completo
- **`setup-datadog-monitoring.bat`** - Configura Datadog pela primeira vez

### Build e Distribuição
- **`build-all.bat`** - Build completo (recomendado)
- **`build-executable.bat`** - Cria executáveis PyInstaller
- **`create-installer.bat`** - Gera instalador Windows (NSIS)
- **`create-icon.py`** - Cria ícones do aplicativo

## 🎯 Componentes Principais

### 🖥️ Interface
- **`jarvis-launcher.py`** - Launcher gráfico com Tkinter
- **`monitoring-dashboard.html`** - Dashboard web de monitoramento
- **Frontend React** - Interface de usuário moderna

### 🔧 Backend
- **`simple_main.py`** - API FastAPI simplificada (ativa)
- **`main.py`** - API FastAPI completa com todos os recursos
- **`auth.py`** - Sistema de autenticação JWT
- **Sistema de plugins** - Arquitetura extensível

### 📊 Observabilidade
- **`telemetry.py`** - OpenTelemetry configuration
- **`datadog_metrics.py`** - Métricas customizadas Datadog
- **`otel-config.yaml`** - Configuração do collector
- **`datadog-config.yaml`** - Configuração Datadog Agent

### 🔥 Integrações
- **`firebase_config.py`** - Firebase Admin SDK
- **ChatKit integration** - OpenAI ChatKit
- **Plugin system** - Arquitetura modular

### 🔄 Manutenção
- **`auto-update.py`** - Sistema de atualizações automáticas
- **Backup e restore** - Preservação de configurações

## 🌐 Portas e Serviços

| Serviço | Porta | Arquivo | Status |
|---------|-------|---------|--------|
| Frontend | 3000 | `frontend/` | ✅ Configurado |
| Backend API | 8001 | `simple_main.py` | ✅ Rodando |
| Prometheus (Backend) | 8002 | `telemetry.py` | ✅ Configurado |
| OTEL Collector | 8888 | `otel-config.yaml` | ✅ Configurado |
| Prometheus Export | 8889 | `otel-config.yaml` | ✅ Configurado |
| OTLP gRPC | 4317 | `otel-config.yaml` | ✅ Configurado |
| OTLP HTTP | 4318 | `otel-config.yaml` | ✅ Configurado |

## 🔐 Configurações

### Variáveis de Ambiente
- **Backend**: `.env.example` → `.env`
- **Frontend**: `.env` (já configurado)
- **Datadog**: `DATADOG_API_KEY`, `DATADOG_SITE`
- **Firebase**: Service account path/JSON

### Arquivos de Config
- **`otel-config.yaml`** - OpenTelemetry Collector
- **`datadog-config.yaml`** - Datadog Agent
- **`config/jarvis-config.json`** - Configurações do launcher

## 📚 Documentação

- **`README.md`** - Documentação principal do projeto
- **`MONITORING.md`** - Guia completo de monitoramento
- **`EXECUTABLE.md`** - Guia do executável e distribuição
- **`docs/PLUGIN_DEVELOPMENT.md`** - Desenvolvimento de plugins
- **`PROJECT_STRUCTURE.md`** - Este arquivo (estrutura do projeto)

## 🎯 Status do Projeto

### ✅ Implementado
- [x] Backend FastAPI com autenticação
- [x] Frontend React com Vite
- [x] Sistema de plugins extensível
- [x] Integração Firebase completa
- [x] Monitoramento OpenTelemetry
- [x] Métricas Datadog customizadas
- [x] Dashboard de monitoramento
- [x] Launcher gráfico completo
- [x] Sistema de auto-update
- [x] Build de executáveis
- [x] Instalador Windows
- [x] Documentação completa

### 🔄 Em Desenvolvimento
- [ ] Testes automatizados
- [ ] CI/CD pipeline
- [ ] Docker containers
- [ ] Plugins adicionais
- [ ] Mobile app

### 🎯 Próximos Passos
1. **Executar build**: `build-all.bat`
2. **Testar executável**: `JARVIS-V2-Launcher.exe`
3. **Configurar Datadog**: API Key e site
4. **Configurar Firebase**: Service account
5. **Distribuir**: Instalador ou versão portátil

## 🆘 Suporte

### Logs e Debug
- **Backend logs**: Console do Python
- **Frontend logs**: Browser DevTools
- **Launcher logs**: Interface gráfica
- **OTEL logs**: Collector console

### Troubleshooting
- **Portas ocupadas**: Verificar netstat
- **Dependências**: requirements.txt e package.json
- **Permissões**: Executar como administrador se necessário
- **Firewall**: Permitir portas necessárias

---

**🤖 JARVIS V2 - Sistema Completo de Assistente Empresarial com IA**
*Versão 2.0.0 - Janeiro 2026*
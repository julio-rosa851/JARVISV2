# 🚀 JARVIS V2 - Guia do Executável

## 📦 Versões Disponíveis

### 🖥️ Instalador Windows (`JARVIS-V2-Setup.exe`)
- **Instalação completa** no sistema
- **Atalhos automáticos** (Menu Iniciar + Área de Trabalho)
- **Desinstalador integrado**
- **Registro no Windows** (Adicionar/Remover Programas)
- **Requer privilégios de administrador**

### 💼 Versão Portátil (`JARVIS-V2-Portable.zip`)
- **Não requer instalação**
- **Executa de qualquer pasta**
- **Ideal para USB/rede**
- **Não modifica o sistema**
- **Não requer privilégios especiais**

## 🚀 Como Usar

### Instalador
1. Execute `JARVIS-V2-Setup.exe`
2. Siga o assistente de instalação
3. Use o atalho "JARVIS V2" na área de trabalho

### Portátil
1. Descompacte `JARVIS-V2-Portable.zip`
2. Execute `install.bat` (opcional - cria atalho)
3. Execute `JARVIS-V2-Launcher.exe`

## 🎯 Interface do Launcher

### 🎮 Controles Principais
- **🚀 Iniciar JARVIS**: Inicia todos os serviços
- **⏹️ Parar Sistema**: Para todos os serviços
- **📊 Dashboard**: Abre dashboard de monitoramento
- **⚙️ Configurações**: Abre painel de configurações
- **🔄 Verificar Atualizações**: Busca novas versões

### 📊 Status dos Serviços
- **🟢 Verde**: Serviço rodando
- **🔴 Vermelho**: Serviço parado
- **⚠️ Amarelo**: Serviço com problemas

### 🔗 Links Rápidos
- **🌐 Frontend**: Interface do usuário (porta 3000)
- **🔧 API**: Backend REST API (porta 8001)
- **📚 Docs**: Documentação Swagger
- **📊 Métricas**: Prometheus metrics
- **🐕 Datadog**: Dashboard de observabilidade

### 📝 Logs do Sistema
- **Tempo real**: Logs aparecem conforme sistema executa
- **Scroll automático**: Sempre mostra logs mais recentes
- **Cores**: Diferentes tipos de mensagem

## ⚙️ Configurações

### 🐕 Datadog
- **API Key**: Chave de acesso ao Datadog
- **Site**: ddog-gov.com (Government Cloud)
- **Tags**: Aplicadas automaticamente

### 🔥 Firebase
- **Service Account**: Caminho para arquivo de credenciais
- **Auto-configuração**: Detecta credenciais padrão

### 📁 Arquivos de Configuração
- `config/jarvis-config.json`: Configurações principais
- `config/otel-config.yaml`: OpenTelemetry
- `config/datadog-config.yaml`: Datadog Agent

## 🔄 Sistema de Atualizações

### Verificação Automática
- **Startup**: Verifica ao iniciar (opcional)
- **Manual**: Botão "Verificar Atualizações"
- **GitHub**: Busca releases no repositório

### Processo de Atualização
1. **Download**: Baixa nova versão
2. **Backup**: Salva configurações atuais
3. **Aplicação**: Substitui arquivos
4. **Restauração**: Mantém configurações
5. **Limpeza**: Remove arquivos temporários

## 🛠️ Troubleshooting

### ❌ Launcher não abre
```bash
# Verificar dependências
# Windows 10/11 com .NET Framework 4.7+
# Visual C++ Redistributable

# Executar via linha de comando para ver erros
JARVIS-V2-Launcher.exe
```

### ❌ Backend não inicia
- **Porta ocupada**: Mude porta no código
- **Dependências**: Verifique Python/bibliotecas
- **Firewall**: Permita acesso às portas

### ❌ Frontend não carrega
- **Porta 3000**: Verifique se está livre
- **Arquivos**: Confirme se pasta `frontend` existe
- **Servidor HTTP**: Python deve estar no PATH

### ❌ Monitoramento não funciona
- **OpenTelemetry**: Baixe `otelcol-contrib.exe`
- **Configuração**: Verifique `otel-config.yaml`
- **Datadog**: Confirme API Key válida

## 📊 Portas Utilizadas

| Serviço | Porta | Descrição |
|---------|-------|-----------|
| Frontend | 3000 | Interface do usuário |
| Backend | 8001 | API REST |
| Prometheus (Backend) | 8002 | Métricas internas |
| OTEL Collector | 8888 | Métricas do collector |
| Prometheus Export | 8889 | Métricas exportadas |
| OTLP gRPC | 4317 | Telemetria gRPC |
| OTLP HTTP | 4318 | Telemetria HTTP |

## 🔐 Segurança

### Dados Locais
- **Configurações**: Armazenadas localmente
- **Logs**: Não contêm informações sensíveis
- **Credenciais**: Apenas em arquivos de config

### Comunicação Externa
- **Datadog**: HTTPS para ddog-gov.com
- **GitHub**: HTTPS para verificar atualizações
- **Firebase**: HTTPS para APIs Google

### Firewall
```bash
# Portas de entrada necessárias
3000/tcp  # Frontend
8001/tcp  # Backend API
8002/tcp  # Prometheus (opcional)
8888/tcp  # OTEL Metrics (opcional)
8889/tcp  # Prometheus Export (opcional)
```

## 📚 Estrutura de Arquivos

```
JARVIS-V2-Portable/
├── JARVIS-V2-Launcher.exe     # Launcher principal
├── backend/
│   └── JARVIS-V2-Backend.exe  # Backend executável
├── frontend/                  # Arquivos do frontend
├── config/                    # Configurações
├── monitoring/                # OpenTelemetry
├── monitoring-dashboard.html  # Dashboard local
├── README.txt                 # Instruções básicas
└── install.bat               # Criador de atalho
```

## 🆘 Suporte

### Logs de Debug
1. Execute launcher via linha de comando
2. Verifique logs na interface
3. Consulte arquivos em `logs/` (se existir)

### Informações do Sistema
- **OS**: Windows 10/11
- **Python**: 3.8+ (embutido no executável)
- **Node.js**: Não necessário (servidor HTTP Python)
- **.NET**: Framework 4.7+ (para interface)

### Contato
- **GitHub**: Issues no repositório
- **Email**: Suporte técnico
- **Documentação**: MONITORING.md

## 🎯 Próximos Passos

Após executar o JARVIS V2:

1. **Acesse**: http://localhost:3000
2. **Login**: admin / 1234 (padrão)
3. **Configure**: Datadog e Firebase
4. **Monitore**: Dashboard de observabilidade
5. **Explore**: Agentes e funcionalidades

Aproveite o JARVIS V2! 🤖✨
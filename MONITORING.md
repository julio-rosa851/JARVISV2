# 📊 JARVIS V2 - Guia de Monitoramento e Observabilidade

## 🎯 Visão Geral

O JARVIS V2 implementa uma stack completa de observabilidade com:

- **OpenTelemetry**: Coleta de traces, métricas e logs
- **Prometheus**: Métricas e alertas
- **Datadog**: Observabilidade avançada (Gov Cloud)
- **Firebase Analytics**: Dados de usuário e conversas

## 🚀 Início Rápido

### 1. Setup Básico
```bash
# Iniciar apenas com Prometheus
start.bat

# Iniciar com monitoramento completo
start-with-monitoring.bat

# Setup Datadog (primeira vez)
setup-datadog-monitoring.bat
```

### 2. Acessar Dashboards
- **Dashboard Local**: `monitoring-dashboard.html`
- **Prometheus**: http://localhost:8889/metrics
- **Datadog**: https://app.ddog-gov.com
- **API Health**: http://localhost:8001/health

## 📈 Métricas Disponíveis

### Sistema
- `jarvis.system.memory.usage` - Uso de memória
- `jarvis.system.cpu.percent` - Uso de CPU
- `jarvis.system.firebase.available` - Status Firebase
- `jarvis.system.sessions.active` - Sessões ativas

### API
- `jarvis.api.requests.total` - Total de requisições
- `jarvis.api.request.duration` - Duração das requisições
- `jarvis.errors.total` - Total de erros

### Agentes
- `jarvis.agent.executions.total` - Execuções de agentes
- `jarvis.agent.execution.duration` - Tempo de processamento
- `jarvis.chat.messages.total` - Mensagens de chat
- `jarvis.chat.message.length` - Tamanho das mensagens

### Firebase
- `jarvis.firebase.operations.total` - Operações Firebase
- `jarvis.firebase.operation.duration` - Duração das operações

### Autenticação
- `jarvis.auth.login.attempts` - Tentativas de login

## 🔧 Configuração

### Variáveis de Ambiente
```bash
# Datadog
DATADOG_API_KEY=401c3160ae0a60569c3070239ee296c4
DATADOG_SITE=ddog-gov.com

# OpenTelemetry
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
OTEL_SERVICE_NAME=jarvis-v2
OTEL_SERVICE_VERSION=2.0.0
OTEL_RESOURCE_ATTRIBUTES=service.name=jarvis-v2,service.version=2.0.0,deployment.environment=development
```

### Portas Utilizadas
- **8001**: Backend API
- **3000**: Frontend
- **8002**: Prometheus (backend)
- **8888**: OpenTelemetry Collector metrics
- **8889**: Prometheus exporter
- **4317**: OTLP gRPC receiver
- **4318**: OTLP HTTP receiver

## 🐕 Datadog Integration

### Configuração
1. **API Key**: `401c3160ae0a60569c3070239ee296c4`
2. **Site**: `ddog-gov.com` (Government Cloud)
3. **Dashboard**: https://app.ddog-gov.com

### Tags Padrão
- `service:jarvis-v2`
- `version:2.0.0`
- `env:development`
- `project:jarvis-v2`
- `component:ai-assistant`
- `team:development`

### Dashboards Recomendados
1. **APM**: Traces de requisições e performance
2. **Infrastructure**: Métricas de sistema
3. **Logs**: Logs centralizados
4. **Custom Metrics**: Métricas específicas do JARVIS

## 📊 OpenTelemetry

### Receivers
- **OTLP**: Recebe telemetria das aplicações
- **Host Metrics**: Métricas do sistema operacional
- **Prometheus**: Scraping de métricas

### Processors
- **Batch**: Agrupa dados para eficiência
- **Resource**: Adiciona metadados

### Exporters
- **Datadog**: Envia para Datadog Gov Cloud
- **Prometheus**: Métricas locais
- **Logging**: Debug local
- **File**: Backup em arquivo

## 🔍 Troubleshooting

### Problemas Comuns

#### OpenTelemetry Collector não inicia
```bash
# Verificar se as portas estão livres
netstat -ano | findstr :4317
netstat -ano | findstr :4318

# Verificar logs
monitoring\otelcol-contrib.exe --config=otel-config.yaml
```

#### Datadog não recebe dados
1. Verificar API Key
2. Verificar conectividade com ddog-gov.com
3. Verificar logs do collector

#### Prometheus métricas não aparecem
```bash
# Testar endpoint
curl http://localhost:8002/metrics
curl http://localhost:8889/metrics
```

### Logs Importantes
- **Backend**: Console do Python
- **OTEL Collector**: Janela "OTEL Collector"
- **Datadog**: https://app.ddog-gov.com/logs

## 📚 Recursos Adicionais

### Documentação
- [OpenTelemetry](https://opentelemetry.io/docs/)
- [Datadog Gov Cloud](https://docs.datadoghq.com/getting_started/site/)
- [Prometheus](https://prometheus.io/docs/)

### Exemplos de Queries

#### Prometheus
```promql
# Taxa de requisições por minuto
rate(jarvis_api_requests_total[1m])

# Latência P95
histogram_quantile(0.95, jarvis_api_request_duration_seconds_bucket)

# Erros por agente
sum by (agent) (jarvis_errors_total)
```

#### Datadog
```
# Requisições por endpoint
sum:jarvis.api.requests.total{*} by {endpoint}

# Tempo médio de resposta
avg:jarvis.api.request.duration{*}

# Agentes mais utilizados
sum:jarvis.agent.executions.total{*} by {agent}
```

## 🚨 Alertas Sugeridos

### Datadog Monitors
1. **High Error Rate**: `jarvis.errors.total > 10/min`
2. **High Latency**: `jarvis.api.request.duration > 2s`
3. **Firebase Down**: `jarvis.system.firebase.available == 0`
4. **High Memory**: `jarvis.system.memory.usage > 80%`

### Configuração de Alertas
```yaml
# Exemplo de monitor Datadog
name: "JARVIS V2 - High Error Rate"
type: "metric alert"
query: "avg(last_5m):sum:jarvis.errors.total{*}.as_rate() > 0.1"
message: "JARVIS V2 está com alta taxa de erros"
tags:
  - "service:jarvis-v2"
  - "team:development"
```

## 🔐 Segurança

### Dados Sensíveis
- API Keys são configuradas via variáveis de ambiente
- Logs não contêm informações sensíveis
- Métricas são agregadas (sem PII)

### Compliance
- Datadog Gov Cloud (FedRAMP)
- Dados permanecem nos EUA
- Criptografia em trânsito e repouso
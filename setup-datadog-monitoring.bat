@echo off
echo ========================================
echo  JARVIS V2 - Setup Datadog Monitoring
echo ========================================

echo 🔍 Verificando dependências...

REM Verificar se curl está disponível
where curl >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ curl não encontrado! Necessário para download.
    echo 💡 Instale curl ou use PowerShell para downloads.
    pause
    exit /b 1
)

echo 📦 Criando diretório de monitoramento...
if not exist "monitoring" mkdir monitoring
cd monitoring

echo 🔽 Baixando OpenTelemetry Collector Contrib (com suporte Datadog)...
if not exist "otelcol-contrib.exe" (
    echo Baixando OpenTelemetry Collector Contrib...
    curl -L -o otelcol-contrib.exe https://github.com/open-telemetry/opentelemetry-collector-releases/releases/latest/download/otelcol-contrib_windows_amd64.exe
    
    if %errorlevel% neq 0 (
        echo ❌ Erro ao baixar OpenTelemetry Collector
        pause
        exit /b 1
    )
    
    echo ✅ OpenTelemetry Collector baixado com sucesso!
) else (
    echo ✅ OpenTelemetry Collector já existe
)

cd ..

echo 📝 Configurando variáveis de ambiente...
echo.
echo IMPORTANTE: Configure as seguintes variáveis de ambiente:
echo.
echo SET DATADOG_API_KEY=401c3160ae0a60569c3070239ee296c4
echo SET DATADOG_SITE=ddog-gov.com
echo SET OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
echo SET OTEL_SERVICE_NAME=jarvis-v2
echo SET OTEL_SERVICE_VERSION=2.0.0
echo.

REM Criar arquivo de variáveis de ambiente
echo @echo off > set-env.bat
echo SET DATADOG_API_KEY=401c3160ae0a60569c3070239ee296c4 >> set-env.bat
echo SET DATADOG_SITE=ddog-gov.com >> set-env.bat
echo SET OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318 >> set-env.bat
echo SET OTEL_SERVICE_NAME=jarvis-v2 >> set-env.bat
echo SET OTEL_SERVICE_VERSION=2.0.0 >> set-env.bat
echo SET OTEL_RESOURCE_ATTRIBUTES=service.name=jarvis-v2,service.version=2.0.0,deployment.environment=development >> set-env.bat

echo ✅ Arquivo set-env.bat criado!

echo 🧪 Testando configuração...
call set-env.bat

echo 📊 Iniciando OpenTelemetry Collector com Datadog...
start "OTEL Collector" cmd /k "monitoring\otelcol-contrib.exe --config=otel-config.yaml"

echo ⏳ Aguardando collector iniciar...
timeout /t 5 /nobreak >nul

echo 🔍 Testando endpoints...
echo Testando OTLP HTTP endpoint...
curl -s -o nul -w "HTTP: %%{http_code}\n" http://localhost:4318/v1/traces

echo Testando OTLP gRPC endpoint...
curl -s -o nul -w "gRPC Health: %%{http_code}\n" http://localhost:4317

echo Testando Prometheus metrics...
curl -s -o nul -w "Prometheus: %%{http_code}\n" http://localhost:8889/metrics

echo.
echo ========================================
echo  🎯 Setup Completo!
echo ========================================
echo.
echo 📊 Serviços de Monitoramento:
echo   • OpenTelemetry Collector: Rodando
echo   • Datadog Integration: Configurado
echo   • Prometheus Metrics: http://localhost:8889/metrics
echo   • OTLP HTTP: http://localhost:4318
echo   • OTLP gRPC: http://localhost:4317
echo.
echo 🐕 Datadog:
echo   • Site: ddog-gov.com
echo   • Dashboard: https://app.ddog-gov.com
echo   • API Key: 401c3160ae0a60569c3070239ee296c4
echo.
echo 🚀 Próximos passos:
echo   1. Execute: start.bat (para iniciar JARVIS V2)
echo   2. Acesse: https://app.ddog-gov.com
echo   3. Verifique métricas em: APM ^& Infrastructure
echo.
echo 💡 Para parar o collector: Feche a janela "OTEL Collector"
echo.
pause
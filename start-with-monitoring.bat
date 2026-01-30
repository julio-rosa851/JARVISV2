@echo off
echo ========================================
echo  JARVIS V2 - Iniciando com Monitoramento
echo ========================================

REM Verificar se o OpenTelemetry Collector está instalado
where otelcol >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ OpenTelemetry Collector não encontrado!
    echo 📥 Baixando OpenTelemetry Collector...
    
    REM Criar diretório para o collector
    if not exist "otel" mkdir otel
    cd otel
    
    REM Baixar o collector (Windows)
    curl -L -o otelcol.exe https://github.com/open-telemetry/opentelemetry-collector-releases/releases/latest/download/otelcol_windows_amd64.exe
    
    if %errorlevel% neq 0 (
        echo ❌ Erro ao baixar OpenTelemetry Collector
        pause
        exit /b 1
    )
    
    cd ..
    echo ✅ OpenTelemetry Collector baixado com sucesso!
)

echo 🚀 Iniciando OpenTelemetry Collector...
start "OTEL Collector" cmd /k "otel\otelcol.exe --config=otel-config.yaml"

REM Aguardar o collector iniciar
timeout /t 3 /nobreak >nul

echo 🔥 Iniciando Backend JARVIS V2...
cd backend
start "JARVIS Backend" cmd /k "venv\Scripts\activate && python simple_main.py"

REM Aguardar o backend iniciar
timeout /t 5 /nobreak >nul

echo 🌐 Iniciando Frontend JARVIS V2...
cd ..\frontend
start "JARVIS Frontend" cmd /k "npm run dev"

echo ========================================
echo  🎯 JARVIS V2 Iniciado com Monitoramento!
echo ========================================
echo.
echo 📊 Serviços Disponíveis:
echo   • Backend API: http://localhost:8001
echo   • Frontend: http://localhost:3000
echo   • Métricas Prometheus: http://localhost:8889/metrics
echo   • OTEL Collector Metrics: http://localhost:8888/metrics
echo   • OTEL HTTP Receiver: http://localhost:4318
echo   • OTEL gRPC Receiver: http://localhost:4317
echo.
echo 🔍 Monitoramento:
echo   • Métricas de sistema coletadas a cada 10s
echo   • Traces e logs centralizados
echo   • Dados salvos em: telemetry-data.json
echo.
echo Pressione qualquer tecla para continuar...
pause >nul
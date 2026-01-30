@echo off
echo 🤖 JARVIS V2 - Iniciando Sistema com Monitoramento...
echo.

echo 📦 Verificando Node.js...
node -v
if %errorlevel% neq 0 (
    echo ❌ Node.js não encontrado! Instale em: https://nodejs.org
    pause
    exit /b 1
)

echo 🐍 Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado! Instale em: https://python.org
    pause
    exit /b 1
)

echo.
echo 🚀 Iniciando Backend com Telemetria...
cd backend
if not exist venv (
    echo 📦 Criando ambiente virtual...
    python -m venv venv
)

call venv\Scripts\activate
pip install -r requirements.txt
start "JARVIS Backend" cmd /k "python simple_main.py"

echo.
echo 🌐 Iniciando Frontend...
cd ..\frontend
if not exist node_modules (
    echo 📦 Instalando dependências...
    npm install
)

start "JARVIS Frontend" cmd /k "npm run dev"

echo.
echo 📊 Abrindo Dashboard de Monitoramento...
start "" "monitoring-dashboard.html"

echo.
echo ✅ JARVIS V2 iniciado com sucesso!
echo.
echo 🔗 Links Principais:
echo    Frontend:     http://localhost:3000
echo    Backend:      http://localhost:8001
echo    API Docs:     http://localhost:8001/docs
echo    Dashboard:    monitoring-dashboard.html
echo.
echo 📊 Monitoramento:
echo    Prometheus:   http://localhost:8002/metrics
echo    Health Check: http://localhost:8001/health
echo.
echo 🔐 Login de teste:
echo    Usuário: admin
echo    Senha:   1234
echo.
echo 💡 Para monitoramento completo, execute:
echo    start-with-monitoring.bat
echo.
pause
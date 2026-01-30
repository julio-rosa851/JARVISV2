@echo off
echo ========================================
echo  JARVIS V2 - Build Completo
echo ========================================
echo.
echo 🤖 Este script irá:
echo   1. Criar ícone do aplicativo
echo   2. Instalar dependências
echo   3. Criar executáveis
echo   4. Gerar versão portátil
echo   5. Criar instalador Windows
echo.
echo ⏱️ Tempo estimado: 5-10 minutos
echo.
pause

echo 🎨 Criando ícone...
python create-icon.py
if %errorlevel% neq 0 (
    echo ❌ Erro ao criar ícone
    pause
    exit /b 1
)

echo 📦 Instalando dependências do build...
pip install pyinstaller requests pillow
if %errorlevel% neq 0 (
    echo ❌ Erro ao instalar dependências
    pause
    exit /b 1
)

echo 🏗️ Executando build dos executáveis...
call build-executable.bat
if %errorlevel% neq 0 (
    echo ❌ Erro no build dos executáveis
    pause
    exit /b 1
)

echo 📦 Criando instalador Windows...
call create-installer.bat
if %errorlevel% neq 0 (
    echo ⚠️ Erro ao criar instalador (NSIS pode não estar instalado)
    echo 💡 Você ainda pode usar a versão portátil: JARVIS-V2-Portable.zip
)

echo.
echo ========================================
echo  🎉 Build Completo Finalizado!
echo ========================================
echo.
echo 📁 Arquivos criados:
if exist "JARVIS-V2-Setup.exe" (
    echo   ✅ JARVIS-V2-Setup.exe (instalador)
) else (
    echo   ❌ JARVIS-V2-Setup.exe (não criado - NSIS necessário)
)
echo   ✅ JARVIS-V2-Portable.zip (versão portátil)
echo   ✅ JARVIS-V2-Portable\ (pasta de desenvolvimento)
echo.
echo 🚀 Para testar:
echo   • Descompacte JARVIS-V2-Portable.zip
echo   • Execute JARVIS-V2-Launcher.exe
echo   • Ou instale usando JARVIS-V2-Setup.exe
echo.
echo 📊 Recursos incluídos:
echo   • Interface gráfica completa
echo   • Sistema de monitoramento
echo   • Integração Datadog
echo   • Auto-update
echo   • Configurações visuais
echo.
echo 🔗 Links importantes:
echo   • Frontend: http://localhost:3000
echo   • Backend: http://localhost:8001
echo   • Dashboard: monitoring-dashboard.html
echo   • Datadog: https://app.ddog-gov.com
echo.
pause
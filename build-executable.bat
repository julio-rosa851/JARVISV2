@echo off
echo ========================================
echo  JARVIS V2 - Build Executável
echo ========================================

echo 🔍 Verificando dependências...

REM Verificar Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado!
    pause
    exit /b 1
)

echo 📦 Instalando PyInstaller...
cd backend
call venv\Scripts\activate
pip install pyinstaller

echo 🏗️ Criando executável do backend...
pyinstaller --onefile ^
    --name "JARVIS-V2-Backend" ^
    --icon="../assets/jarvis-icon.ico" ^
    --add-data "auth.py;." ^
    --add-data "firebase_config.py;." ^
    --add-data "telemetry.py;." ^
    --add-data "datadog_metrics.py;." ^
    --hidden-import "uvicorn" ^
    --hidden-import "fastapi" ^
    --hidden-import "firebase_admin" ^
    --hidden-import "opentelemetry" ^
    --hidden-import "prometheus_client" ^
    --hidden-import "datadog" ^
    simple_main.py

if %errorlevel% neq 0 (
    echo ❌ Erro ao criar executável do backend
    pause
    exit /b 1
)

echo ✅ Executável do backend criado: dist\JARVIS-V2-Backend.exe

cd ..

echo 📦 Preparando frontend para build...
cd frontend
if not exist node_modules (
    npm install
)

echo 🏗️ Fazendo build do frontend...
npm run build

if %errorlevel% neq 0 (
    echo ❌ Erro ao fazer build do frontend
    pause
    exit /b 1
)

echo ✅ Build do frontend criado: dist\

cd ..

echo 📁 Criando estrutura de distribuição...
if exist "JARVIS-V2-Portable" rmdir /s /q "JARVIS-V2-Portable"
mkdir "JARVIS-V2-Portable"
mkdir "JARVIS-V2-Portable\backend"
mkdir "JARVIS-V2-Portable\frontend"
mkdir "JARVIS-V2-Portable\config"
mkdir "JARVIS-V2-Portable\monitoring"

echo 📋 Copiando arquivos...
copy "backend\dist\JARVIS-V2-Backend.exe" "JARVIS-V2-Portable\backend\"
xcopy "frontend\dist" "JARVIS-V2-Portable\frontend\" /E /I
copy "otel-config.yaml" "JARVIS-V2-Portable\config\"
copy "datadog-config.yaml" "JARVIS-V2-Portable\config\"
copy "monitoring-dashboard.html" "JARVIS-V2-Portable\"
copy "MONITORING.md" "JARVIS-V2-Portable\"

echo 🚀 Criando launcher executável...

REM Criar executável do launcher
pyinstaller --onefile ^
    --windowed ^
    --name "JARVIS-V2-Launcher" ^
    --icon="assets/jarvis-icon.ico" ^
    --add-data "monitoring-dashboard.html;." ^
    --add-data "MONITORING.md;." ^
    jarvis-launcher.py

if %errorlevel% neq 0 (
    echo ❌ Erro ao criar launcher
    pause
    exit /b 1
)

echo ✅ Launcher criado: dist\JARVIS-V2-Launcher.exe

echo 📋 Copiando launcher para distribuição...
copy "dist\JARVIS-V2-Launcher.exe" "JARVIS-V2-Portable\"

echo 📝 Criando arquivos de configuração...
echo # JARVIS V2 - Configuração > "JARVIS-V2-Portable\README.txt"
echo. >> "JARVIS-V2-Portable\README.txt"
echo 🚀 Para iniciar: Execute JARVIS-V2-Launcher.exe >> "JARVIS-V2-Portable\README.txt"
echo. >> "JARVIS-V2-Portable\README.txt"
echo 📊 Monitoramento: >> "JARVIS-V2-Portable\README.txt"
echo   - Dashboard: monitoring-dashboard.html >> "JARVIS-V2-Portable\README.txt"
echo   - Datadog: https://app.ddog-gov.com >> "JARVIS-V2-Portable\README.txt"
echo. >> "JARVIS-V2-Portable\README.txt"
echo 🔧 Configuração: >> "JARVIS-V2-Portable\README.txt"
echo   - Use o botão Configurações no launcher >> "JARVIS-V2-Portable\README.txt"
echo   - Ou edite config\jarvis-config.json >> "JARVIS-V2-Portable\README.txt"

echo 🎯 Criando instalador...
echo @echo off > "JARVIS-V2-Portable\install.bat"
echo echo ======================================== >> "JARVIS-V2-Portable\install.bat"
echo echo  JARVIS V2 - Instalador >> "JARVIS-V2-Portable\install.bat"
echo echo ======================================== >> "JARVIS-V2-Portable\install.bat"
echo echo. >> "JARVIS-V2-Portable\install.bat"
echo echo 📁 Criando atalho na área de trabalho... >> "JARVIS-V2-Portable\install.bat"
echo powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%%USERPROFILE%%\Desktop\JARVIS V2.lnk'); $Shortcut.TargetPath = '%%CD%%\JARVIS-V2-Launcher.exe'; $Shortcut.WorkingDirectory = '%%CD%%'; $Shortcut.IconLocation = '%%CD%%\JARVIS-V2-Launcher.exe'; $Shortcut.Save()" >> "JARVIS-V2-Portable\install.bat"
echo echo ✅ Atalho criado na área de trabalho! >> "JARVIS-V2-Portable\install.bat"
echo echo. >> "JARVIS-V2-Portable\install.bat"
echo echo 🚀 Execute "JARVIS V2" na área de trabalho para iniciar >> "JARVIS-V2-Portable\install.bat"
echo pause >> "JARVIS-V2-Portable\install.bat"

echo 📦 Criando arquivo ZIP...
if exist "JARVIS-V2-Portable.zip" del "JARVIS-V2-Portable.zip"
powershell "Compress-Archive -Path 'JARVIS-V2-Portable\*' -DestinationPath 'JARVIS-V2-Portable.zip'"

echo.
echo ========================================
echo  🎯 Build Completo!
echo ========================================
echo.
echo 📁 Arquivos criados:
echo   • JARVIS-V2-Portable\ (pasta completa)
echo   • JARVIS-V2-Portable.zip (arquivo compactado)
echo   • JARVIS-V2-Launcher.exe (launcher principal)
echo.
echo 🚀 Para distribuir:
echo   1. Envie o arquivo JARVIS-V2-Portable.zip
echo   2. Descompacte e execute install.bat
echo   3. Use o atalho "JARVIS V2" na área de trabalho
echo.
echo 💡 Ou execute diretamente: JARVIS-V2-Launcher.exe
echo.
pause
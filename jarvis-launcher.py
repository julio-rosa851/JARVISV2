#!/usr/bin/env python3
"""
JARVIS V2 - Launcher Executável
==============================
Launcher principal para o sistema JARVIS V2
"""

import os
import sys
import time
import subprocess
import threading
import webbrowser
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
from auto_update import check_updates_gui

class JarvisLauncher:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🤖 JARVIS V2 - Launcher")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Variáveis de controle
        self.backend_process = None
        self.frontend_process = None
        self.otel_process = None
        self.is_running = False
        
        # Configurar interface
        self.setup_ui()
        
        # Configurar paths
        self.base_path = Path(__file__).parent
        self.backend_exe = self.base_path / "backend" / "JARVIS-V2-Backend.exe"
        self.frontend_path = self.base_path / "frontend"
        self.config_path = self.base_path / "config"
        
    def setup_ui(self):
        """Configura a interface do usuário"""
        
        # Estilo
        style = ttk.Style()
        style.theme_use('clam')
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        title_label = ttk.Label(main_frame, text="🤖 JARVIS V2", font=("Arial", 24, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        subtitle_label = ttk.Label(main_frame, text="Assistente Empresarial com IA", font=("Arial", 12))
        subtitle_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # Frame de controles
        control_frame = ttk.LabelFrame(main_frame, text="Controles", padding="10")
        control_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Botões de controle
        self.start_button = ttk.Button(control_frame, text="🚀 Iniciar JARVIS", command=self.start_system)
        self.start_button.grid(row=0, column=0, padx=(0, 10))
        
        self.stop_button = ttk.Button(control_frame, text="⏹️ Parar Sistema", command=self.stop_system, state="disabled")
        self.stop_button.grid(row=0, column=1, padx=(0, 10))
        
        self.dashboard_button = ttk.Button(control_frame, text="📊 Dashboard", command=self.open_dashboard)
        self.dashboard_button.grid(row=0, column=2, padx=(0, 10))
        
        self.config_button = ttk.Button(control_frame, text="⚙️ Configurações", command=self.open_config)
        self.config_button.grid(row=0, column=3, padx=(0, 10))
        
        self.update_button = ttk.Button(control_frame, text="🔄 Verificar Atualizações", command=self.check_updates)
        self.update_button.grid(row=0, column=4)
        
        # Frame de status
        status_frame = ttk.LabelFrame(main_frame, text="Status dos Serviços", padding="10")
        status_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Status indicators
        self.backend_status = ttk.Label(status_frame, text="🔴 Backend: Parado")
        self.backend_status.grid(row=0, column=0, sticky=tk.W)
        
        self.frontend_status = ttk.Label(status_frame, text="🔴 Frontend: Parado")
        self.frontend_status.grid(row=1, column=0, sticky=tk.W)
        
        self.otel_status = ttk.Label(status_frame, text="🔴 Monitoramento: Parado")
        self.otel_status.grid(row=2, column=0, sticky=tk.W)
        
        # Frame de links
        links_frame = ttk.LabelFrame(main_frame, text="Links Rápidos", padding="10")
        links_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Links
        ttk.Button(links_frame, text="🌐 Frontend", command=lambda: webbrowser.open("http://localhost:3000")).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(links_frame, text="🔧 API", command=lambda: webbrowser.open("http://localhost:8001")).grid(row=0, column=1, padx=(0, 5))
        ttk.Button(links_frame, text="📚 Docs", command=lambda: webbrowser.open("http://localhost:8001/docs")).grid(row=0, column=2, padx=(0, 5))
        ttk.Button(links_frame, text="📊 Métricas", command=lambda: webbrowser.open("http://localhost:8889/metrics")).grid(row=0, column=3, padx=(0, 5))
        ttk.Button(links_frame, text="🐕 Datadog", command=lambda: webbrowser.open("https://app.ddog-gov.com")).grid(row=0, column=4)
        
        # Frame de logs
        logs_frame = ttk.LabelFrame(main_frame, text="Logs do Sistema", padding="10")
        logs_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Área de logs
        self.log_text = scrolledtext.ScrolledText(logs_frame, height=15, width=80)
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar redimensionamento
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)
        logs_frame.columnconfigure(0, weight=1)
        logs_frame.rowconfigure(0, weight=1)
        
    def log_message(self, message):
        """Adiciona mensagem ao log"""
        timestamp = time.strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        self.root.update()
        
    def start_system(self):
        """Inicia o sistema JARVIS"""
        if self.is_running:
            return
            
        self.log_message("🚀 Iniciando JARVIS V2...")
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.is_running = True
        
        # Iniciar em thread separada
        threading.Thread(target=self._start_services, daemon=True).start()
        
    def _start_services(self):
        """Inicia os serviços em background"""
        try:
            # 1. Iniciar OpenTelemetry Collector
            self.log_message("📊 Iniciando OpenTelemetry Collector...")
            otel_exe = self.base_path / "monitoring" / "otelcol-contrib.exe"
            config_file = self.config_path / "otel-config.yaml"
            
            if otel_exe.exists() and config_file.exists():
                self.otel_process = subprocess.Popen([
                    str(otel_exe), 
                    f"--config={config_file}"
                ], creationflags=subprocess.CREATE_NO_WINDOW)
                self.otel_status.config(text="🟢 Monitoramento: Rodando")
                self.log_message("✅ OpenTelemetry Collector iniciado")
            else:
                self.log_message("⚠️ OpenTelemetry Collector não encontrado")
            
            time.sleep(2)
            
            # 2. Iniciar Backend
            self.log_message("🔧 Iniciando Backend...")
            if self.backend_exe.exists():
                self.backend_process = subprocess.Popen([
                    str(self.backend_exe)
                ], creationflags=subprocess.CREATE_NO_WINDOW)
                self.backend_status.config(text="🟢 Backend: Rodando")
                self.log_message("✅ Backend iniciado na porta 8001")
            else:
                self.log_message("❌ Executável do backend não encontrado!")
                return
            
            time.sleep(3)
            
            # 3. Iniciar Frontend (servidor HTTP simples)
            self.log_message("🌐 Iniciando Frontend...")
            if (self.frontend_path / "index.html").exists():
                # Usar servidor HTTP simples do Python
                self.frontend_process = subprocess.Popen([
                    sys.executable, "-m", "http.server", "3000"
                ], cwd=str(self.frontend_path), creationflags=subprocess.CREATE_NO_WINDOW)
                self.frontend_status.config(text="🟢 Frontend: Rodando")
                self.log_message("✅ Frontend iniciado na porta 3000")
            else:
                self.log_message("❌ Frontend não encontrado!")
            
            self.log_message("🎯 JARVIS V2 iniciado com sucesso!")
            self.log_message("🔗 Acesse: http://localhost:3000")
            
            # Abrir dashboard automaticamente
            time.sleep(2)
            self.open_dashboard()
            
        except Exception as e:
            self.log_message(f"❌ Erro ao iniciar sistema: {e}")
            self.stop_system()
            
    def stop_system(self):
        """Para o sistema JARVIS"""
        if not self.is_running:
            return
            
        self.log_message("⏹️ Parando JARVIS V2...")
        
        # Parar processos
        for process_name, process in [
            ("Frontend", self.frontend_process),
            ("Backend", self.backend_process),
            ("OpenTelemetry", self.otel_process)
        ]:
            if process and process.poll() is None:
                try:
                    process.terminate()
                    process.wait(timeout=5)
                    self.log_message(f"✅ {process_name} parado")
                except subprocess.TimeoutExpired:
                    process.kill()
                    self.log_message(f"🔪 {process_name} forçado a parar")
                except Exception as e:
                    self.log_message(f"⚠️ Erro ao parar {process_name}: {e}")
        
        # Resetar status
        self.backend_status.config(text="🔴 Backend: Parado")
        self.frontend_status.config(text="🔴 Frontend: Parado")
        self.otel_status.config(text="🔴 Monitoramento: Parado")
        
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.is_running = False
        
        self.log_message("✅ Sistema parado")
        
    def open_dashboard(self):
        """Abre o dashboard de monitoramento"""
        dashboard_file = self.base_path / "monitoring-dashboard.html"
        if dashboard_file.exists():
            webbrowser.open(f"file://{dashboard_file.absolute()}")
        else:
            messagebox.showwarning("Aviso", "Dashboard não encontrado!")
            
    def check_updates(self):
        """Verifica atualizações"""
        check_updates_gui(self.root)
        
    def open_config(self):
        """Abre janela de configurações"""
        ConfigWindow(self.root, self.config_path)
        
    def on_closing(self):
        """Chamado quando a janela é fechada"""
        if self.is_running:
            if messagebox.askokcancel("Sair", "JARVIS está rodando. Deseja parar e sair?"):
                self.stop_system()
                self.root.destroy()
        else:
            self.root.destroy()
            
    def run(self):
        """Executa o launcher"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.log_message("🤖 JARVIS V2 Launcher iniciado")
        self.log_message("💡 Clique em 'Iniciar JARVIS' para começar")
        self.root.mainloop()

class ConfigWindow:
    def __init__(self, parent, config_path):
        self.config_path = config_path
        self.window = tk.Toplevel(parent)
        self.window.title("⚙️ Configurações JARVIS V2")
        self.window.geometry("600x400")
        self.window.resizable(True, True)
        
        self.setup_config_ui()
        self.load_config()
        
    def setup_config_ui(self):
        """Configura interface de configurações"""
        notebook = ttk.Notebook(self.window)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Aba Datadog
        datadog_frame = ttk.Frame(notebook)
        notebook.add(datadog_frame, text="🐕 Datadog")
        
        ttk.Label(datadog_frame, text="API Key:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.datadog_api_key = ttk.Entry(datadog_frame, width=50)
        self.datadog_api_key.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(datadog_frame, text="Site:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.datadog_site = ttk.Entry(datadog_frame, width=50)
        self.datadog_site.grid(row=1, column=1, padx=5, pady=5)
        
        # Aba Firebase
        firebase_frame = ttk.Frame(notebook)
        notebook.add(firebase_frame, text="🔥 Firebase")
        
        ttk.Label(firebase_frame, text="Service Account Path:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.firebase_path = ttk.Entry(firebase_frame, width=50)
        self.firebase_path.grid(row=0, column=1, padx=5, pady=5)
        
        # Botões
        button_frame = ttk.Frame(self.window)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(button_frame, text="💾 Salvar", command=self.save_config).pack(side=tk.RIGHT, padx=(5, 0))
        ttk.Button(button_frame, text="❌ Cancelar", command=self.window.destroy).pack(side=tk.RIGHT)
        
    def load_config(self):
        """Carrega configurações existentes"""
        # Valores padrão
        self.datadog_api_key.insert(0, "401c3160ae0a60569c3070239ee296c4")
        self.datadog_site.insert(0, "ddog-gov.com")
        
    def save_config(self):
        """Salva configurações"""
        config = {
            "datadog": {
                "api_key": self.datadog_api_key.get(),
                "site": self.datadog_site.get()
            },
            "firebase": {
                "service_account_path": self.firebase_path.get()
            }
        }
        
        config_file = self.config_path / "jarvis-config.json"
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
            
        messagebox.showinfo("Sucesso", "Configurações salvas!")
        self.window.destroy()

if __name__ == "__main__":
    launcher = JarvisLauncher()
    launcher.run()
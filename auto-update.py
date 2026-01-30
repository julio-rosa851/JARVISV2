#!/usr/bin/env python3
"""
JARVIS V2 - Auto Update
======================
Sistema de atualização automática
"""

import os
import sys
import json
import requests
import zipfile
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox
import threading

class AutoUpdater:
    def __init__(self):
        self.current_version = "2.0.0"
        self.update_url = "https://api.github.com/repos/jarvis-v2/releases/latest"
        self.base_path = Path(__file__).parent
        
    def check_for_updates(self):
        """Verifica se há atualizações disponíveis"""
        try:
            response = requests.get(self.update_url, timeout=10)
            if response.status_code == 200:
                release_data = response.json()
                latest_version = release_data.get("tag_name", "").replace("v", "")
                
                if self.is_newer_version(latest_version, self.current_version):
                    return {
                        "available": True,
                        "version": latest_version,
                        "download_url": self.get_download_url(release_data),
                        "changelog": release_data.get("body", "")
                    }
            
            return {"available": False}
            
        except Exception as e:
            print(f"Erro ao verificar atualizações: {e}")
            return {"available": False, "error": str(e)}
    
    def is_newer_version(self, latest, current):
        """Compara versões"""
        try:
            latest_parts = [int(x) for x in latest.split('.')]
            current_parts = [int(x) for x in current.split('.')]
            
            # Preencher com zeros se necessário
            max_len = max(len(latest_parts), len(current_parts))
            latest_parts.extend([0] * (max_len - len(latest_parts)))
            current_parts.extend([0] * (max_len - len(current_parts)))
            
            return latest_parts > current_parts
        except:
            return False
    
    def get_download_url(self, release_data):
        """Obtém URL de download"""
        assets = release_data.get("assets", [])
        for asset in assets:
            if "portable" in asset["name"].lower() and asset["name"].endswith(".zip"):
                return asset["browser_download_url"]
        return None
    
    def download_update(self, download_url, progress_callback=None):
        """Baixa atualização"""
        try:
            response = requests.get(download_url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            
            update_file = self.base_path / "update.zip"
            downloaded = 0
            
            with open(update_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        
                        if progress_callback and total_size > 0:
                            progress = (downloaded / total_size) * 100
                            progress_callback(progress)
            
            return str(update_file)
            
        except Exception as e:
            raise Exception(f"Erro ao baixar atualização: {e}")
    
    def apply_update(self, update_file):
        """Aplica atualização"""
        try:
            # Criar backup
            backup_dir = self.base_path / "backup"
            if backup_dir.exists():
                shutil.rmtree(backup_dir)
            
            backup_dir.mkdir()
            
            # Fazer backup dos arquivos importantes
            important_files = ["config", "data", "logs"]
            for item in important_files:
                item_path = self.base_path / item
                if item_path.exists():
                    if item_path.is_dir():
                        shutil.copytree(item_path, backup_dir / item)
                    else:
                        shutil.copy2(item_path, backup_dir / item)
            
            # Extrair atualização
            with zipfile.ZipFile(update_file, 'r') as zip_ref:
                zip_ref.extractall(self.base_path / "temp_update")
            
            # Aplicar atualização
            temp_dir = self.base_path / "temp_update"
            for item in temp_dir.iterdir():
                dest = self.base_path / item.name
                if dest.exists():
                    if dest.is_dir():
                        shutil.rmtree(dest)
                    else:
                        dest.unlink()
                
                if item.is_dir():
                    shutil.copytree(item, dest)
                else:
                    shutil.copy2(item, dest)
            
            # Restaurar arquivos importantes
            for item in important_files:
                backup_item = backup_dir / item
                if backup_item.exists():
                    dest_item = self.base_path / item
                    if dest_item.exists():
                        if dest_item.is_dir():
                            shutil.rmtree(dest_item)
                        else:
                            dest_item.unlink()
                    
                    if backup_item.is_dir():
                        shutil.copytree(backup_item, dest_item)
                    else:
                        shutil.copy2(backup_item, dest_item)
            
            # Limpeza
            shutil.rmtree(temp_dir)
            os.remove(update_file)
            
            return True
            
        except Exception as e:
            raise Exception(f"Erro ao aplicar atualização: {e}")

class UpdateDialog:
    def __init__(self, parent, update_info):
        self.update_info = update_info
        self.updater = AutoUpdater()
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("🔄 Atualização Disponível")
        self.dialog.geometry("500x400")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        self.setup_ui()
        
    def setup_ui(self):
        """Configura interface do diálogo"""
        main_frame = ttk.Frame(self.dialog, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(main_frame, text="🔄 Nova Versão Disponível!", font=("Arial", 16, "bold"))
        title_label.pack(pady=(0, 10))
        
        # Informações da versão
        info_frame = ttk.Frame(main_frame)
        info_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(info_frame, text=f"Versão Atual: {self.updater.current_version}").pack(anchor=tk.W)
        ttk.Label(info_frame, text=f"Nova Versão: {self.update_info['version']}", font=("Arial", 10, "bold")).pack(anchor=tk.W)
        
        # Changelog
        changelog_label = ttk.Label(main_frame, text="📝 Novidades:")
        changelog_label.pack(anchor=tk.W, pady=(10, 5))
        
        changelog_frame = ttk.Frame(main_frame)
        changelog_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        changelog_text = tk.Text(changelog_frame, height=10, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(changelog_frame, orient=tk.VERTICAL, command=changelog_text.yview)
        changelog_text.configure(yscrollcommand=scrollbar.set)
        
        changelog_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        changelog_text.insert(tk.END, self.update_info.get('changelog', 'Sem informações de changelog disponíveis.'))
        changelog_text.config(state=tk.DISABLED)
        
        # Barra de progresso
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(main_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(fill=tk.X, pady=(0, 10))
        self.progress_bar.pack_forget()  # Esconder inicialmente
        
        # Status
        self.status_label = ttk.Label(main_frame, text="")
        self.status_label.pack(pady=(0, 10))
        
        # Botões
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X)
        
        self.update_button = ttk.Button(button_frame, text="🔄 Atualizar Agora", command=self.start_update)
        self.update_button.pack(side=tk.RIGHT, padx=(5, 0))
        
        ttk.Button(button_frame, text="❌ Cancelar", command=self.dialog.destroy).pack(side=tk.RIGHT)
        
    def start_update(self):
        """Inicia processo de atualização"""
        self.update_button.config(state="disabled")
        self.progress_bar.pack(fill=tk.X, pady=(0, 10))
        
        # Executar em thread separada
        threading.Thread(target=self.perform_update, daemon=True).start()
        
    def perform_update(self):
        """Executa atualização"""
        try:
            # Download
            self.status_label.config(text="📥 Baixando atualização...")
            download_url = self.update_info['download_url']
            
            def progress_callback(progress):
                self.progress_var.set(progress)
                self.dialog.update()
            
            update_file = self.updater.download_update(download_url, progress_callback)
            
            # Aplicar
            self.status_label.config(text="🔧 Aplicando atualização...")
            self.progress_var.set(0)
            
            self.updater.apply_update(update_file)
            
            # Sucesso
            self.status_label.config(text="✅ Atualização concluída!")
            self.progress_var.set(100)
            
            messagebox.showinfo("Sucesso", "Atualização aplicada com sucesso!\nReinicie o JARVIS V2 para usar a nova versão.")
            self.dialog.destroy()
            
        except Exception as e:
            self.status_label.config(text=f"❌ Erro: {e}")
            messagebox.showerror("Erro", f"Erro durante atualização:\n{e}")
            self.update_button.config(state="normal")

def check_updates_gui(parent=None):
    """Verifica atualizações com interface gráfica"""
    updater = AutoUpdater()
    
    # Mostrar diálogo de verificação
    checking_dialog = tk.Toplevel(parent) if parent else tk.Tk()
    checking_dialog.title("🔍 Verificando Atualizações")
    checking_dialog.geometry("300x100")
    checking_dialog.resizable(False, False)
    
    if parent:
        checking_dialog.transient(parent)
        checking_dialog.grab_set()
    
    ttk.Label(checking_dialog, text="🔍 Verificando atualizações...").pack(pady=20)
    progress = ttk.Progressbar(checking_dialog, mode='indeterminate')
    progress.pack(fill=tk.X, padx=20, pady=(0, 20))
    progress.start()
    
    def check_in_background():
        update_info = updater.check_for_updates()
        
        checking_dialog.after(0, lambda: progress.stop())
        checking_dialog.after(0, lambda: checking_dialog.destroy())
        
        if update_info.get("available"):
            if parent:
                UpdateDialog(parent, update_info)
            else:
                root = tk.Tk()
                root.withdraw()
                UpdateDialog(root, update_info)
                root.mainloop()
        else:
            if parent:
                messagebox.showinfo("Atualizações", "Você já está usando a versão mais recente!")
            else:
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Atualizações", "Você já está usando a versão mais recente!")
                root.destroy()
    
    threading.Thread(target=check_in_background, daemon=True).start()
    
    if not parent:
        checking_dialog.mainloop()

if __name__ == "__main__":
    check_updates_gui()
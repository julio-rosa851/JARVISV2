#!/usr/bin/env python3
"""
Cria um ícone simples para o JARVIS V2
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_jarvis_icon():
    """Cria ícone do JARVIS V2"""
    
    # Criar imagem 256x256
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Fundo circular azul
    margin = 20
    draw.ellipse([margin, margin, size-margin, size-margin], 
                fill=(102, 126, 234, 255), outline=(76, 94, 176, 255), width=4)
    
    # Texto JARVIS
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()
    
    # Texto "J"
    text = "J"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - 20
    
    draw.text((x, y), text, fill=(255, 255, 255, 255), font=font)
    
    # Texto "AI" menor
    try:
        small_font = ImageFont.truetype("arial.ttf", 20)
    except:
        small_font = ImageFont.load_default()
    
    ai_text = "AI"
    bbox = draw.textbbox((0, 0), ai_text, font=small_font)
    ai_width = bbox[2] - bbox[0]
    
    ai_x = (size - ai_width) // 2
    ai_y = y + 50
    
    draw.text((ai_x, ai_y), ai_text, fill=(255, 215, 0, 255), font=small_font)
    
    # Salvar como ICO
    icon_path = "assets/jarvis-icon.ico"
    img.save(icon_path, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
    
    print(f"✅ Ícone criado: {icon_path}")
    
    # Também salvar como PNG
    png_path = "assets/jarvis-icon.png"
    img.save(png_path, format='PNG')
    print(f"✅ PNG criado: {png_path}")

if __name__ == "__main__":
    try:
        create_jarvis_icon()
    except ImportError:
        print("⚠️ PIL não encontrado. Instalando...")
        os.system("pip install Pillow")
        create_jarvis_icon()
import requests
from bs4 import BeautifulSoup
import time
import random

# (c) 2026 Guillermo Roger Hernandez Chandia - ADS
# Versão 5.0 PRO - Sistema Completo com Link de Afiliado e Resiliência

class HunterADS:
    """
    Sistema profissional de monitoramento de preços.
    Focado em agilizar vendas com links de afiliado.
    """
    def __init__(self, url, link_afiliado):
        self.url = url
        self.afiliado = link_afiliado
        self.session = requests.Session()
        # Lista de identidades para evitar bloqueios do servidor
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ]

    def capturar_preco(self):
        """Busca o preço na Amazon tratando erros 500/404"""
        headers = {
            "User-Agent": random.choice(self.user_agents),
            "Accept-Language": "pt-BR,pt;q=0.9"
        }
        try:
            print(f"[{time.strftime('%H:%M:%S')}] 📡 Sincronizando com servidor...")
            response = self.session.get(self.url, headers=headers, timeout=20)
            
            # Se o servidor estiver instável, o robô apenas avisa e espera
            if response.status_code != 200:
                print(f"⚠️ Servidor instável (Status {response.status_code}). Tentando novamente em breve...")
                return None
                
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Seletores de preço (Fallback)
            tag_preco = soup.select_one("span.a-price-whole") or soup.select_one(".a-offscreen")

            if tag_preco:
                texto = tag_preco.get_text().strip().replace('.', '').replace(',', '.')
                # Filtra apenas os números para a lógica de comparação
                valor_limpo = "".join(c for c in texto if c.isdigit() or c == '.')
                return float(valor_limpo)
            
            return None

        except Exception as e:
            print(f"❌ Falha técnica no motor: {e}")
            return None

    def imprimir_post(self, preco):
        """Gera o post pronto para o seu canal de vendas"""
        print("\n" + "🚀" * 10)
        print("🚨 OFERTA DETECTADA - ADS HUNTER 🚨")
        print(f"📦 SSD Kingston NV3 1TB")
        print(f"💰 Preço de Oportunidade: R$ {preco:.2f}")
        print(f"🛒 Compre agora pelo meu link: {self.afiliado}")
        print("🚀" * 10 + "\n")

    def executar(self, meta):
        """Loop de vigilância contínua"""
        print(f"✅ Motor Ativo! Vigilância ligada para valores abaixo de R$ {meta:.2f}")
        print(f"🔗 Link de Afiliado configurado: {self.afiliado}")
        
        while True:
            valor_atual = self.capturar_preco()
            
            if valor_atual:
                print(f"💰 No Radar: R$ {valor_atual:.2f}")
                if valor_atual <= meta:
                    self.imprimir_post(valor_atual)
                    print("🔔 BINGO! Post gerado acima. Copie e fature!")
                    break 
                else:
                    print("⏳ Valor ainda alto para o funil. Continuando varredura...")
            else:
                print("⚠️ Não foi possível capturar o preço nesta rodada.")

            # Pausa aleatória (Anti-Ban)
            pausa = random.randint(60, 120)
            print(f"💤 Descanso tático de {pausa}s para evitar detecção...\n")
            time.sleep(pausa)

if __name__ == "__main__":
    # --- CONFIGURAÇÃO FINAL ---
    PRODUTO = "https://www.amazon.com.br/dp/B0D9S16K4H"
    MEU_LINK = "https://amzn.to/4tSHTht" 
    PRECO_ALVO = 930.00 
    
    # Inicializa e liga o sistema
    bot = HunterADS(PRODUTO, MEU_LINK)
    bot.executar(PRECO_ALVO)
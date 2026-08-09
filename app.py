import streamlit as st

# ==========================================
# 1. MOTOR DE MEMÓRIA E ESTADO
# ==========================================
if 'cena_atual' not in st.session_state:
    st.session_state.cena_atual = "cap1_parte1"
    
if 'memoria' not in st.session_state:
    st.session_state.memoria = [] # Aqui o jogo "lembra" das suas escolhas

def processar_escolha(nova_cena, memoria_ganha=None, reiniciar=False):
    st.session_state.cena_atual = nova_cena
    
    # Se a escolha gerar uma memória nova, guardamos ela
    if memoria_ganha and memoria_ganha not in st.session_state.memoria:
        st.session_state.memoria.append(memoria_ganha)
        
    # Se for Game Over e o jogador quiser reiniciar
    if reiniciar:
        st.session_state.memoria = []

# ==========================================
# 2. ROTEIRO DO JOGO (COM PAGINAÇÃO)
# ==========================================
historia = {
    "cap1_parte1": {
        "texto": "Você acorda com um solavanco.\n\nPor alguns segundos, não abre os olhos. Há um ruído constante ao seu redor. Metal contra metal. O som distante de rodas correndo sobre trilhos.\n\nVocê verifica o horário. **00:16**. O relógio do trem também marca **00:16**. \n\nMas os segundos do seu celular continuam passando... e o relógio do trem permanece imóvel.",
        "imagem": "https://placehold.co/800x400/111111/FFFFFF?text=O+Despertar",
        "opcoes": [
            {"label": "Levantar a cabeça e olhar ao redor...", "destino": "cap1_parte2"} # Apenas avança o texto
        ]
    },
    "cap1_parte2": {
        "texto": "Você não está sozinho. Do outro lado do corredor, uma mulher chora silenciosamente. Mais à frente, um policial mantém a cabeça baixa, com uma mancha escura de sangue na camisa.\n\nNo fundo do vagão, um homem de sobretudo olha diretamente para você. Sem piscar. E perto da porta, uma senhora muito velha segura uma bolsa contra o peito.",
        "imagem": "https://placehold.co/800x400/222222/FFFFFF?text=Os+Passageiros",
        "opcoes": [
            {"label": "Continuar observando...", "destino": "cap1_parte3"}
        ]
    },
    "cap1_parte3": {
        "texto": "Um alto-falante chia. Uma voz distorcida anuncia:\n— Próxima estação... Santa Lúcia.\n\nO trem começa a desacelerar. Pela janela escura, você vê uma plataforma vazia. A velha senhora abre os olhos e olha diretamente para você.\n\n— Escute com atenção. Não importa o que você ouvir... quando o trem parar, não olhe pela janela.\n\nMas já é tarde. Há alguém na plataforma. De costas. Usando a mesma roupa que você.",
        "imagem": "https://placehold.co/800x400/050505/FFFFFF?text=A+Estacao+Santa+Lucia",
        "opcoes": [
            # AQUI ESTÁ A MÁGICA: Cada escolha salva uma memória diferente no st.session_state
            {"label": "A) Continuar olhando pela janela para ver o rosto.", "destino": "cena_janela", "ganha_memoria": "olhou_janela"},
            {"label": "B) Afastar-se imediatamente e exigir respostas da velha.", "destino": "cena_velha", "ganha_memoria": "obedeceu_velha"},
            {"label": "C) Ir até a criança adormecida.", "destino": "cena_crianca", "ganha_memoria": "falou_crianca"},
            {"label": "D) Ignorar todos e correr para o próximo vagão.", "destino": "cena_fuga", "ganha_memoria": "fugiu_vagao"}
        ]
    },
    "cena_janela": {
        "texto": "Você ignora a velha.\n\nA pessoa na plataforma começa a virar o rosto. Devagar. Primeiro o ombro. Depois o pescoço. Então o rosto aparece sob a luz amarelada de um dos postes.\n\nSeu corpo inteiro esfria. É você. Mas muito mais velho. O rosto marcado, um corte profundo atravessando a sobrancelha esquerda. A roupa coberta por manchas que parecem sangue seco.\n\nEle caminha acompanhando o trem. Vocês alinham as mãos no vidro. Imagens invadem sua mente: Fogo. Uma mulher caída. A criança. O policial atirando. A velha gritando. E você... ajoelhado diante de dezenas de corpos.",
        "imagem": "https://placehold.co/800x400/111111/FFFFFF?text=O+Seu+Futuro",
        "opcoes": [
            {"label": "Tentar ouvir o que ele diz...", "destino": "cena_janela_mulher"}
        ]
    },
    
    "cena_janela_mulher": {
        "texto": "Seu outro eu aproxima o rosto do vidro. Você lê seus lábios:\n\n**NÃO DESÇA.**\n\nO trem para na Estação Santa Lúcia. A mulher que chorava se levanta, desesperada, e corre para a plataforma ignorando os avisos do policial.\n\nEla ri de alívio por estar fora. Até que outra mulher, idêntica a ela, aparece na escuridão. A cópia sussurra algo no ouvido da passageira original, que imediatamente para de lutar e sorri de forma macabra para você.\n\nAs portas se fecham. A mulher fica para trás, junto com a sua cópia.",
        "imagem": "https://placehold.co/800x400/220000/FFFFFF?text=A+Copia+Na+Plataforma",
        "opcoes": [
            {"label": "Olhar o celular vibrando no seu bolso...", "destino": "cena_janela_celular"}
        ]
    },
    
    "cena_janela_celular": {
        "texto": "Sem sinal. Mas as mensagens chegam. Remetente: **VOCÊ**.\n\n*EU AVISEI PARA NÃO OLHAR.*\n*AGORA ELE SABE ONDE VOCÊ ESTÁ.*\n*NÃO CONFIE NA VELHA.*\n*E NÃO DEIXE A CRIANÇA CHEGAR À ESTAÇÃO FINAL.*\n\nA velha pede para ver o seu telefone. A criança diz para não entregar. O policial questiona sobre o aparelho e o homem de sobretudo apenas ri.\n\nUma última mensagem pisca na tela, seguida por uma contagem que se move em tempo real:\n**VOCÊ TEM 3 MINUTOS PARA DECIDIR EM QUEM ACREDITAR.**\n\n02:59... 02:58... 02:57...",
        "imagem": "https://placehold.co/800x400/002200/FFFFFF?text=02:59",
        "opcoes": [
            {"label": "A1) Mostrar as mensagens para a velha", "destino": "cena_a1", "ganha_memoria": "confiou_velha"},
            {"label": "A2) Esconder o celular e confiar nas mensagens", "destino": "cena_a2", "ganha_memoria": "confiou_mensagens"},
            {"label": "A3) Interrogar a criança", "destino": "cena_a3", "ganha_memoria": "interrogou_crianca"},
            {"label": "A4) Confrontar o homem de sobretudo", "destino": "cena_a4", "ganha_memoria": "enfrentou_sobretudo"}
        ]
    },
    
    # === ADICIONE ESTAS CENAS AQUI PARA CORRIGIR O ERRO ===
    "cena_velha": {
        "texto": "Você se afasta da janela e encara a velha senhora. 'O que está acontecendo?', você exige saber. Ela suspira, parecendo mais cansada do que antes. 'Eles sempre olham...', ela sussurra, antes que as luzes se apaguem completamente.",
        "imagem": "https://placehold.co/800x400/222222/FFFFFF?text=A+Velha",
        "opcoes": [{"label": "Recomeçar", "destino": "cap1_parte1", "reiniciar": True}]
    },
    "cena_crianca": {
        "texto": "Você caminha até a criança. Os olhos dela são escuros demais, profundos demais para a idade. 'Eu estava esperando por você', ela repete, segurando sua mão com dedos que parecem gelo. 'O cobrador já vem.'",
        "imagem": "https://placehold.co/800x400/111133/FFFFFF?text=A+Crianca",
        "opcoes": [{"label": "Recomeçar", "destino": "cap1_parte1", "reiniciar": True}]
    },
    "cena_fuga": {
        "texto": "Ignorando todos, você corre para a porta do fundo. Tenta girar a maçaneta com toda a força, mas ela está soldada. Atrás de você, o som de passos pesados começa a se aproximar pelo corredor.",
        "imagem": "https://placehold.co/800x400/441111/FFFFFF?text=Sem+Saida",
        "opcoes": [{"label": "Recomeçar", "destino": "cap1_parte1", "reiniciar": True}]
    }
}

# ==========================================
# 3. INTERFACE (UI)
# ==========================================
st.set_page_config(page_title="O Último Trem", layout="centered")

# Barra lateral para testes (depois você pode esconder isso dos jogadores)
with st.sidebar:
    st.markdown("### 🧠 Memória do Jogo (Debug)")
    st.write(st.session_state.memoria)

# Renderiza a cena
cena_dados = historia[st.session_state.cena_atual]

st.image(cena_dados["imagem"], use_container_width=True)
st.markdown(f"### {cena_dados['texto']}")
st.divider()

# Renderiza os botões dinamicamente
colunas = st.columns(len(cena_dados["opcoes"]))

for i, opcao in enumerate(cena_dados["opcoes"]):
    with colunas[i]:
        st.button(
            label=opcao["label"], 
            on_click=processar_escolha, 
            kwargs={
                "nova_cena": opcao["destino"],
                "memoria_ganha": opcao.get("ganha_memoria"),
                "reiniciar": opcao.get("reiniciar", False)
            },
            key=f"btn_{st.session_state.cena_atual}_{i}"
        )

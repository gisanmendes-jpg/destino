import streamlit as st

# ==========================================
# 1. ROTEIRO DO JOGO (DICIONÁRIO DE CENAS)
# ==========================================
# Cada chave é o ID da cena. Dentro, temos o texto, a imagem e as opções.
historia = {
    "inicio": {
        "texto": "A chuva cai pesada sobre a cidade. Você está parado em frente a um galpão abandonado. Seu contato disse que o alvo está lá dentro. Você nota duas entradas: a porta principal (meio arrombada) e uma janela estreita no segundo andar.",
        "imagem": "https://placehold.co/800x400/222222/FFFFFF?text=Galpao+Abandonado",
        "opcoes": [
            {"label": "Chutar a porta principal e entrar com tudo", "destino": "porta_principal"},
            {"label": "Escalar até a janela silenciosamente", "destino": "janela_andar2"}
        ]
    },
    "porta_principal": {
        "texto": "Você chuta a porta. Makima está sentada em uma poltrona no centro do galpão, com um sorriso enigmático. 'Você faz muito barulho', ela diz. Vários capangas saem das sombras.",
        "imagem": "https://placehold.co/800x400/8B0000/FFFFFF?text=Emboscada",
        "opcoes": [
            {"label": "Tentar lutar contra todos", "destino": "final_derrota_luta"},
            {"label": "Jogar uma granada de fumaça e fugir", "destino": "final_fuga"}
        ]
    },
    "janela_andar2": {
        "texto": "Você escala com dificuldade, mas consegue entrar sem fazer barulho. Lá de cima, você vê Denji amarrado em uma cadeira e os capangas distraídos jogando cartas. A chave das algemas está na mesa.",
        "imagem": "https://placehold.co/800x400/00008B/FFFFFF?text=Infiltracao",
        "opcoes": [
            {"label": "Descer sorrateiramente para pegar a chave", "destino": "pegar_chave"},
            {"label": "Puxar o alarme de incêndio para assustá-los", "destino": "alarme"}
        ]
    },
    "pegar_chave": {
        "texto": "Você pega a chave e liberta Denji. Juntos, vocês derrotam os capangas facilmente e escapam pela porta dos fundos.",
        "imagem": "https://placehold.co/800x400/006400/FFFFFF?text=Vitoria",
        "opcoes": [
            {"label": "Jogar Novamente", "destino": "inicio"}
        ]
    },
    "alarme": {
        "texto": "O alarme soa alto. Os capangas entram em pânico, mas um deles, assustado, atira na sua direção. Você é atingido no ombro e precisa recuar sem salvar o refém.",
        "imagem": "https://placehold.co/800x400/222222/FFFFFF?text=Derrota",
        "opcoes": [
            {"label": "Tentar Novamente", "destino": "inicio"}
        ]
    },
    "final_derrota_luta": {
        "texto": "Eram muitos. Você é capturado e agora está amarrado ao lado do refém.",
        "imagem": "https://placehold.co/800x400/222222/FFFFFF?text=Game+Over",
        "opcoes": [
            {"label": "Tentar Novamente", "destino": "inicio"}
        ]
    },
    "final_fuga": {
        "texto": "Você tosse com a fumaça, mas consegue escapar. Infelizmente, a missão falhou.",
        "imagem": "https://placehold.co/800x400/222222/FFFFFF?text=Fuga",
        "opcoes": [
            {"label": "Tentar Novamente", "destino": "inicio"}
        ]
    }
}

# ==========================================
# 2. MOTOR DO JOGO E CALLBACKS
# ==========================================
# Inicializa a cena atual. Se o jogo acabou de abrir, vai para "inicio".
if 'cena_atual' not in st.session_state:
    st.session_state.cena_atual = "inicio"

def mudar_cena(nova_cena):
    """Função callback para alterar o estado da cena com segurança."""
    st.session_state.cena_atual = nova_cena

# ==========================================
# 3. INTERFACE DE USUÁRIO (UI)
# ==========================================
st.set_page_config(page_title="Ficção Interativa", layout="centered")

# Puxa os dados da cena atual do dicionário
cena_dados = historia[st.session_state.cena_atual]

# Mostra a imagem da cena
st.image(cena_dados["imagem"], use_container_width=True)

# Mostra o texto da cena (usando markdown para ficar bonito)
st.markdown(f"### {cena_dados['texto']}")

st.divider()

# Cria os botões de escolha dinamicamente
st.write("**O que você faz?**")

colunas = st.columns(len(cena_dados["opcoes"]))

for i, opcao in enumerate(cena_dados["opcoes"]):
    with colunas[i]:
        # O botão usa o on_click para chamar a função mudar_cena
        # e kwargs para passar o destino exato
        st.button(
            label=opcao["label"], 
            on_click=mudar_cena, 
            kwargs={"nova_cena": opcao["destino"]},
            key=f"btn_{st.session_state.cena_atual}_{i}" # Key única para evitar conflitos
        )

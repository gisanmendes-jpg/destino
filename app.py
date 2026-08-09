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
        "texto": "Você ignora o aviso da velha. A curiosidade é mais forte que o medo.\n\nA figura na plataforma termina de se virar. O sangue congela nas suas veias.\n\nO rosto é o seu. Exatamente o seu.\n\nMas há algo profundamente errado. Os olhos são perfeitamente brancos, sem íris ou pupilas. A boca está esticada em um sorriso que parece rasgar as bochechas.\n\nO seu 'duplo' levanta a mão e encosta um dedo longo no vidro, pelo lado de fora.\n\n*TOC.*\n\nO vidro trinca.\nA velha grita: 'Abaixe-se!'\n\nAs portas do trem se abrem com um chiado violento. O vento gelado invade o vagão, apagando as luzes. A coisa que tem o seu rosto acabou de entrar.",
        "imagem": "https://placehold.co/800x400/1a1a2e/FFFFFF?text=A+Invasao",
        "opcoes": [
            {"label": "Obedecer à velha e se jogar no chão", "destino": "cena_chao"},
            {"label": "Correr desesperadamente para o próximo vagão", "destino": "cena_fuga_vagao2"},
            {"label": "Pegar o extintor de incêndio na parede para se defender", "destino": "cena_luta"}
        ]
    },

    # === RAMIFICAÇÕES QUE NASCEM DA CENA DA JANELA ===
    "cena_chao": {
        "texto": "Você se atira no chão entre os bancos, prendendo a respiração. No escuro, ouve passos pesados arrastando pelo corredor. *Shh... shh... shh...*\n\nOs passos param exatamente ao seu lado. Você vê dois pés pálidos descalços a centímetros do seu rosto.",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=No+Escuro",
        "opcoes": [
            {"label": "Ficar completamente imóvel", "destino": "cap2_sobrevivencia"} # Cena a ser escrita depois
        ]
    },
    
    "cena_fuga_vagao2": {
        "texto": "Você gira nos calcanhares e corre. O corredor parece infinito. Você passa pelo homem de sobretudo, que agora está rindo alto. Alcança a porta do próximo vagão, gira a trava e entra com tudo, trancando-a atrás de si.",
        "imagem": "https://placehold.co/800x400/221111/FFFFFF?text=Fuga+Para+Frente",
        "opcoes": [
            {"label": "Olhar o que tem no Vagão 2", "destino": "cap2_vagao2"} # Cena a ser escrita depois
        ]
    },
    
    "cena_luta": {
        "texto": "Adrenalina pura. Você arranca o extintor vermelho da parede. No momento em que a luz pisca, a criatura está bem na sua frente. Você balança o cilindro de metal com toda a força em direção à cabeça dela.",
        "imagem": "https://placehold.co/800x400/550000/FFFFFF?text=Reacao",
        "opcoes": [
            {"label": "Ver o resultado do golpe", "destino": "cap2_consequencia_luta"} # Cena a ser escrita depois
        ]
    }
    
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

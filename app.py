import streamlit as st
import random
from PIL import Image

# Inicia a variável de carreira INDEPENDENTE do jogo estar rodando
if 'casos_resolvidos' not in st.session_state:
    st.session_state.casos_resolvidos = 0

# ==========================================
# 1. BANCOS DE DADOS (COM IMAGENS)
# ==========================================
banco_capangas = [
    {"nome": "Gabi Aura Monster", "sexo": "F", "cabelo": "Castanho", "olho" : "Castanho", "detalhes": "Jóia", "imagem": "gabi.png", "imagem_preso": "gabi_triste.png", "imagem_fuga": "gabi_feliz.png"},
    {"nome": "Denji",  "sexo": "M", "cabelo": "Loiro", "olho" : "Castanho", "detalhes": "Tapa olho", "imagem": "denji.jpg", "imagem_preso": "denji_triste.jpg", "imagem_fuga": "denji_feliz.jpg"},
    {"nome": "Nana",  "sexo": "F", "cabelo": "Ruivo", "olho" : "Amarelo", "detalhes": "Jóia", "imagem": "https://placehold.co/300x400/555555/FFFFFF?text=Nana"},
    {"nome": "Gisa Estrela",  "sexo": "F", "cabelo": "Castanho", "olho" : "Castanho", "detalhes": "Tatuagem", "imagem": "gisa.png"},
    {"nome": "Scarlet",  "sexo": "F", "cabelo": "Preto", "olho" : "Vermelho", "detalhes": "Cicatriz", "imagem": "https://placehold.co/300x400/8B0000/FFFFFF?text=Scarlet"},
    {"nome": "Ryan",  "sexo": "M", "cabelo": "Preto", "olho" : "Vermelho", "detalhes": "Jóia", "imagem": "https://placehold.co/300x400/555555/FFFFFF?text=Ryan"},
    {"nome": "Mayah",  "sexo": "F", "cabelo": "Preto", "olho" : "Vermelho", "detalhes": "Tapa olho", "imagem": "https://placehold.co/300x400/555555/FFFFFF?text=Mayah"},
    {"nome": "Elsa",  "sexo": "F", "cabelo": "Preto", "olho" : "Azul", "detalhes": "Jóia", "imagem": "elsa.jpg"},
    {"nome": "Douma",  "sexo": "M", "cabelo": "Loiro", "olho" : "Amarelo", "detalhes": "Tatuagem", "imagem": "douma.jpg"},
    {"nome": "Haru",  "sexo": "M", "cabelo": "Branco", "olho" : "Amarelo", "detalhes": "Tapa olho", "imagem": "haru.jpg"},
    {"nome": "Roger",  "sexo": "M", "cabelo": "Preto", "olho" : "Vermelho", "detalhes": "Tatuagem", "imagem": "https://placehold.co/300x400/555555/FFFFFF?text=Roger"},
    {"nome": "Clara",  "sexo": "F", "cabelo": "Preto", "olho" : "Azul", "detalhes": "Cicatriz", "imagem": "https://placehold.co/300x400/555555/FFFFFF?text=Clara"},
    {"nome": "Loira Burrinha",  "sexo": "F", "cabelo": "Loiro", "olho" : "Azul", "detalhes": "Jóia", "imagem": "lb.jpg"},
    {"nome": "Victor",  "sexo": "M", "cabelo": "Branco", "olho" : "Castanho", "detalhes": "Cicatriz", "imagem": "victor.jpg"}
]

banco_chefes = [
    {"nome": "Makima",  "sexo": "F", "cabelo": "Ruivo", "olho" : "Amarelo", "detalhes": "Tatuagem", "imagem": "makima.jpg"},
    {"nome": "Muzan",  "sexo": "M", "cabelo": "Branco", "olho" : "Vermelho", "detalhes": "Cicatriz", "imagem": "muzan.jpg"}
]

banco_suspeitos = banco_capangas + banco_chefes

mapa_mundi = {
    # ================= AMÉRICAS =================
    "Rio de Janeiro": {
        "conexoes": ["Lima", "Nova York", "Tóquio", "Buenos Aires", "Cidade do Cabo"],
        "imagem": "rj.jpg",
        "fatos": [
            "O suspeito queria ver o Cristo Redentor.",
            "Trocou dinheiro por Reais.",
            "Disse que pretendia subir de bondinho até o Pão de Açúcar.",
            "Foi visto caminhando pelo calçadão de Copacabana.",
            "Perguntou onde poderia assistir a um desfile de escolas de samba.",
            "Comprou uma camisa de futebol perto do Maracanã.",
            "Perguntou como chegar à Baía de Guanabara.",
            "Foi visto fotografando os Arcos da Lapa.",
            "Perguntou onde ficava a Floresta da Tijuca.",
            "Comentou que queria assistir ao pôr do sol na Pedra do Arpoador."
        ]
    },
    "Lima": {
        "conexoes": ["Rio de Janeiro", "Nova York", "Cidade do México", "Buenos Aires", "Sydney"],
        "imagem": "lima.jpg",
        "fatos": [
            "Queria conhecer o estádio Monumental onde o Flamengo foi campeão.",
            "Perguntou sobre as ruínas de Machu Picchu.",
            "Trocou seu dinheiro por Soles Peruanos.",
            "Foi visto comendo um Ceviche tradicional.",
            "Falou sobre sobrevoar as misteriosas Linhas de Nazca.",
            "Queria ver lhamas e alpacas de perto.",
            "Tinha um guia turístico sobre a Cordilheira dos Andes."
        ]
    },
    "Nova York": {
        "conexoes": ["Rio de Janeiro", "Lima", "Paris", "Cidade do México", "Toronto", "Londres", "Los Angeles"],
        "imagem": "ny.jpg",
        "fatos": [
            "Perguntou onde ficava a balsa para a Estátua da Liberdade.",
            "Tinha um mapa detalhado da ilha de Manhattan.",
            "Trocou toda a sua moeda por Dólares Americanos.",
            "Foi visto comendo um cachorro-quente nas escadarias da Times Square.",
            "Disse que iria assistir a um famoso musical na Broadway.",
            "Perguntou como alugar uma bicicleta no Central Park.",
            "Disse que estava indo para a 'cidade que nunca dorme'."
        ]
    },
    "Cidade do México": {
        "conexoes": ["Lima", "Londres", "Nova York", "Toronto", "Buenos Aires", "Los Angeles"],
        "imagem": "mx.jpg",
        "fatos": [
            "Comeu muitos tacos com pimenta e guacamole.",
            "Comprou um sombreiro gigante em uma feira de rua.",
            "Trocou dinheiro por Pesos Mexicanos.",
            "Perguntou como chegar às enormes pirâmides de Teotihuacán.",
            "Disse que queria visitar a casa azul da artista Frida Kahlo.",
            "Comentou sobre assistir a uma luta mascarada de Lucha Libre.",
            "Tinha um mapa mostrando antigas ruínas do império asteca."
        ]
    },
    "Buenos Aires": {
        "conexoes": ["Rio de Janeiro", "Lima", "Cidade do México"],
        "imagem": "ba.jpg",
        "fatos": [
            "Foi visto comendo um alfajor de doce de leite.",
            "Perguntou onde poderia assistir a um show de Tango.",
            "Trocou seu dinheiro por Pesos Argentinos.",
            "Queria tirar uma foto em frente ao enorme Obelisco da cidade.",
            "Perguntou como chegar ao bairro colorido do Caminito.",
            "Disse que queria ver a Casa Rosada."
        ]
    },
    "Toronto": {
        "conexoes": ["Nova York", "Cidade do México"],
        "imagem": "toro.jpg",
        "fatos": [
            "Reclamou do frio e comprou um casaco muito pesado.",
            "Tinha um broche com uma folha de bordo (maple) vermelha.",
            "Trocou o dinheiro por Dólares Canadenses.",
            "Perguntou como subir na famosa CN Tower.",
            "Foi visto comprando ingressos para um jogo de hóquei no gelo.",
            "Disse que iria visitar as Cataratas do Niágara no fim de semana.",
            "Estava tomando xarope de bordo com panquecas."
        ]
    },
    "Los Angeles": {
        "conexoes": ["Nova York", "Cidade do México", "Sydney", "Tóquio"],
        "imagem": "la.jpg",
        "fatos": [
            "Estava procurando o letreiro gigante de Hollywood nas colinas.",
            "Perguntou onde ficava a Calçada da Fama.",
            "Foi visto andando de patins em Venice Beach.",
            "Reclamou muito do trânsito nas autoestradas (Freeways).",
            "Tinha um mapa das casas dos astros de cinema.",
            "Disse que iria visitar o primeiro parque da Disneylândia.",
            "Trocou seu dinheiro por Dólares Americanos e foi surfar."
        ]
    },

    # ================= EUROPA =================
    "Paris": {
        "conexoes": ["Nova York", "Londres", "Roma", "Berlim"],
        "imagem": "paris.jpg",
        "fatos": [
            "Disse que faria um piquenique aos pés da Torre Eiffel.",
            "Tinha um broche com uma bandeira listrada em azul, branco e vermelho.",
            "Trocou seu dinheiro por Euros.",
            "Foi visto comendo um croissant em uma padaria local.",
            "Disse que queria ver de perto o quadro da Mona Lisa no Louvre.",
            "Foi visto passeando de barco pelas águas do Rio Sena.",
            "Comentou sobre o trânsito caótico em volta do Arco do Triunfo."
        ]
    },
    "Londres": {
        "conexoes": ["Paris", "Cidade do México", "Nova York", "Berlim", "Roma", "Nova Délhi", "Dubai"],
        "imagem": "londres.jpg",
        "fatos": [
            "Estava tomando chá preto pontualmente às 17h.",
            "Queria ajustar o relógio para bater com o horário do Big Ben.",
            "Pagou a conta da pousada usando Libras Esterlinas.",
            "Foi visto andando no segundo andar de um ônibus vermelho.",
            "Perguntou se a guarda real estava marchando no Palácio de Buckingham.",
            "Entrou em uma clássica cabine telefônica vermelha para fazer uma ligação.",
            "Comentou que precisava pegar o 'Tube', o famoso metrô local."
        ]
    },
    "Roma": {
        "conexoes": ["Paris", "Londres", "Cairo", "Berlim"],
        "imagem": "roma.jpg",
        "fatos": [
            "Perguntou como chegar às ruínas do Coliseu.",
            "Foi visto jogando uma moeda na Fonte de Trevi.",
            "Pediu uma autêntica pizza margherita no almoço.",
            "Queria visitar o menor país do mundo, a sede da Igreja Católica.",
            "Trocou dinheiro por Euros.",
            "Disse que adoraria ver artefatos do antigo Império Romano.",
            "Estava tomando um gelato de pistache."
        ]
    },
    "Berlim": {
        "conexoes": ["Paris", "Londres", "Roma", "Moscou"],
        "imagem": "berlim.jpg",
        "fatos": [
            "Perguntou onde ficavam os restos do famoso muro que dividiu a cidade.",
            "Foi tirar uma foto no Portão de Brandemburgo.",
            "Estava comendo salsichão (Bratwurst) e bebendo cerveja local.",
            "Trocou o dinheiro por Euros.",
            "Queria visitar o prédio do Parlamento (Reichstag).",
            "Falou sobre a rica história da Segunda Guerra Mundial.",
            "Tinha um dicionário de alemão no bolso."
        ]
    },
    "Moscou": {
        "conexoes": ["Tóquio", "Berlim", "Pequim"],
        "imagem": "moscou.jpg",
        "fatos": [
            "Comprou um conjunto de bonecas Matrioscas.",
            "Queria passear pela famosa Praça Vermelha.",
            "Trocou o dinheiro por Rublos.",
            "Reclamou do frio congelante e comprou um chapéu de pele.",
            "Perguntou como agendar uma visita ao Kremlin.",
            "Tinha um guia sobre a antiga União Soviética.",
            "Foi visto observando a arquitetura colorida da Catedral de São Basílio."
        ]
    },

    # ================= ÁSIA, ÁFRICA E OCEANIA =================
    "Tóquio": {
        "conexoes": ["Rio de Janeiro", "Moscou", "Pequim", "Sydney", "Los Angeles"],
        "imagem": "toquio.jpg",
        "fatos": [
            "Estava estudando o alfabeto japonês.",
            "Mencionou que queria escalar o Monte Fuji.",
            "Trocou notas grandes por Ienes.",
            "Perguntou o horário de partida do trem-bala (Shinkansen).",
            "Foi visto comprando mangás em Akihabara.",
            "Queria tirar uma foto no movimentado cruzamento de Shibuya.",
            "Disse que iria comer sushi e sashimi no jantar."
        ]
    },
    "Pequim": {
        "conexoes": ["Tóquio", "Sydney", "Moscou", "Nova Délhi", "Bangkok"],
        "imagem": "pequim.jpg",
        "fatos": [
            "Perguntou qual era o melhor trecho para visitar a Grande Muralha.",
            "Queria entrar no palácio imperial da Cidade Proibida.",
            "Trocou dinheiro por Yuans.",
            "Tinha um chaveiro com um Urso Panda de pelúcia.",
            "Foi visto comendo pato laqueado tradicional.",
            "Comprou decorações em formato de dragões vermelhos.",
            "Comentou que o país tem mais de 1 bilhão de habitantes."
        ]
    },
    "Nova Délhi": {
        "conexoes": ["Londres", "Cairo", "Pequim", "Dubai", "Bangkok"],
        "imagem": "nd.jpg",
        "fatos": [
            "Tinha um bilhete de trem para ver o Taj Mahal.",
            "Trocou o dinheiro por Rúpias.",
            "Comentou que o trânsito de tuk-tuks era uma loucura.",
            "Foi visto comendo frango ao curry bem apimentado.",
            "Perguntou sobre os rituais sagrados no Rio Ganges.",
            "Estudava sobre meditação e a cultura hindu.",
            "Tirou fotos de vacas andando livremente pelas ruas."
        ]
    },
    "Bangkok": {
        "conexoes": ["Pequim", "Nova Délhi", "Sydney"],
        "imagem": "bk.jpg",
        "fatos": [
            "Reclamou do forte calor tropical.",
            "Tinha um guia sobre templos budistas cheios de ouro.",
            "Foi visto negociando com o motorista de um tuk-tuk colorido.",
            "Pediu um Pad Thai bem temperado no mercado de rua.",
            "Trocou a sua moeda por Bahts.",
            "Perguntou como chegar aos famosos Mercados Flutuantes.",
            "Disse que iria fazer uma massagem tailandesa depois da viagem."
        ]
    },
    "Dubai": {
        "conexoes": ["Cairo", "Nova Délhi", "Londres"],
        "imagem": "dubai.jpg",
        "fatos": [
            "Perguntou se o elevador para o prédio mais alto do mundo demorava muito.",
            "Trocou seu dinheiro por Dirhams.",
            "Agendou um passeio de luxo pelas dunas do deserto.",
            "Queria ver as ilhas artificiais construídas em formato de palmeira.",
            "Foi visto entrando em um hotel em formato de vela de barco.",
            "Comentou sobre a impressionante riqueza da cidade.",
            "Estava observando carros superesportivos passando na avenida."
        ]
    },
    "Cairo": {
        "conexoes": ["Roma", "Cidade do Cabo", "Nova Délhi", "Dubai"],
        "imagem": "cairo.jpg",
        "fatos": [
            "Queria fazer um passeio de camelo ao entardecer.",
            "Tinha um mapa detalhado das Grandes Pirâmides de Gizé.",
            "Foi visto navegando em um barco tradicional pelo Rio Nilo.",
            "Perguntou sobre a máscara de ouro do faraó Tutancâmon.",
            "Trocou a moeda por Libras Egípcias.",
            "Tirou uma foto na frente de uma gigantesca estátua de Esfinge.",
            "Comentou que o calor do deserto era implacável."
        ]
    },
    "Cidade do Cabo": {
        "conexoes": ["Rio de Janeiro", "Cairo"],
        "imagem": "cc.jpg",
        "fatos": [
            "Perguntou como subir a famosa Table Mountain (Montanha da Mesa).",
            "Agendou um safári para tentar ver leões e elefantes.",
            "Trocou o dinheiro por Rands.",
            "Disse que queria visitar a ilha onde Nelson Mandela ficou preso.",
            "Foi fotografar uma colônia de pinguins na praia.",
            "Tinha um livro sobre o extremo sul do continente africano.",
            "Comentou que iria ver o encontro dos oceanos Atlântico e Índico."
        ]
    },
    "Sydney": {
        "conexoes": ["Tóquio", "Lima", "Pequim", "Los Angeles", "Bangkok"],
        "imagem": "sy.jpg",
        "fatos": [
            "Queria ir a um santuário ver cangurus e coalas.",
            "Foi fotografar a famosa Casa de Ópera com formato de velas.",
            "Comprou uma prancha de surfe e foi para Bondi Beach.",
            "Disse que iria mergulhar na Grande Barreira de Corais.",
            "Trocou seu dinheiro por Dólares Australianos.",
            "Comprou um bumerangue artesanal em uma feira.",
            "Comentou sobre viajar pelo grande deserto do Outback."
        ]
    }
}

locais_fisicos = ["Hotel", "Clube Esportivo", "Restaurante", "Cafeteria", "Spa"]
locais_geograficos = ["Banco", "Aeroporto", "Porto", "Livraria", "Mercado Central", "Museu", "Agência de Turismo"]

# ==========================================
# 2. SISTEMA DE PROGRESSÃO E PATENTES
# ==========================================
def calcular_dificuldade(casos):
    if casos == 0:
        return "Recruta", 4, 120, False
    elif casos == 1:
        return "Detetive Júnior", 5, 110, False
    elif casos == 2:
        return "Detetive Particular", 6, 100, False
    elif casos == 3:
        return "Investigador", 7, 90, False
    elif casos == 4:
        return "Detetive de Elite", 8, 80, False
    else:
        return "Super Detetive", 9, 80, True

def sortear_locais():
    st.session_state.locais_cidade = random.sample(locais_fisicos, 1) + random.sample(locais_geograficos, 2)
    random.shuffle(st.session_state.locais_cidade)

def iniciar_nova_partida(venceu_anterior=False):
    if 'casos_resolvidos' not in st.session_state:
        st.session_state.casos_resolvidos = 0
    elif venceu_anterior:
        st.session_state.casos_resolvidos += 1

    # Zera as seleções do computador da Interpol
    st.session_state.interpol_sexo = "---"
    st.session_state.interpol_cabelo = "---"
    st.session_state.interpol_olho = "---"
    st.session_state.interpol_detalhe = "---"

    patente, tamanho_rota, horas_restantes, enfrenta_chefe = calcular_dificuldade(st.session_state.casos_resolvidos)
    
    if enfrenta_chefe:
        vilao = random.choice(banco_chefes) if random.choice([True, False]) else random.choice(banco_capangas)
    else:
        vilao = random.choice(banco_capangas)

    todas_cidades = list(mapa_mundi.keys())
    cidade_atual_setup = random.choice(todas_cidades)
    rota_fuga = [cidade_atual_setup]

    while len(rota_fuga) < tamanho_rota:
        opcoes = [c for c in mapa_mundi[rota_fuga[-1]]["conexoes"] if c not in rota_fuga]
        if not opcoes:
            break
        proxima = random.choice(opcoes)
        rota_fuga.append(proxima)

    st.session_state.patente = patente
    st.session_state.vilao = vilao
    st.session_state.rota_fuga = rota_fuga
    st.session_state.local_atual = rota_fuga[0]
    st.session_state.horas_restantes = horas_restantes
    st.session_state.mandado_ativo = None
    st.session_state.jogo_acabou = False
    st.session_state.mensagem_tela = ""
    st.session_state.venceu_atual = False
    sortear_locais()

# Inicia o jogo na primeira vez que a página carrega
if 'horas_restantes' not in st.session_state:
    iniciar_nova_partida()

# ==========================================
# 3. INTERFACE STREAMLIT
# ==========================================
st.set_page_config(page_title="DIE - Investigações", page_icon="🕵️", layout="wide")

# Banner de Título
try:
    imagem_original = Image.open("banner.jpg")
    imagem_achatada = imagem_original.resize((1200, 400))
    st.image(imagem_achatada)
except:
    st.warning("Banner não encontrado.")

# Cabeçalho Superior
col_header1, col_header2 = st.columns([3, 1])
with col_header1:
    st.markdown("### Painel Operacional Ativo")
with col_header2:
    st.metric(label="Casos Resolvidos", value=st.session_state.casos_resolvidos)
    st.caption(f"Patente: **{st.session_state.patente.upper()}**")

st.divider()

# Fim de Jogo por Tempo
if st.session_state.horas_restantes <= 0 and not st.session_state.jogo_acabou:
    st.session_state.mensagem_tela = f"⏰ O TEMPO ACABOU! O vilão escapou. O culpado era: {st.session_state.vilao['nome']}."
    st.session_state.jogo_acabou = True
    st.session_state.venceu_atual = False

# --- BARRA LATERAL: INTERPOL ---
st.sidebar.header("💻 Computador da Interpol")
st.sidebar.write("Cruze os dados para emitir o mandado. Custa 1h.")

# Passando o parâmetro key para forçar o reset ao iniciar nova partida
p_sex = st.sidebar.selectbox("Sexo", ["---", "F", "M"], key="interpol_sexo")
p_cab = st.sidebar.selectbox("Cabelo", ["---", "Castanho", "Preto", "Loiro", "Ruivo", "Branco"], key="interpol_cabelo")
p_olh = st.sidebar.selectbox("Cor dos Olhos", ["---", "Castanho", "Amarelo", "Vermelho", "Azul"], key="interpol_olho")
p_det = st.sidebar.selectbox("Detalhe", ["---", "Jóia", "Tatuagem", "Cicatriz", "Tapa olho"], key="interpol_detalhe")

if st.sidebar.button("🚨 Emitir Mandado", disabled=st.session_state.jogo_acabou):
    st.session_state.horas_restantes -= 1
    
    sexo_filtro = p_sex if p_sex != "---" else None
    cabelo_filtro = p_cab if p_cab != "---" else None
    olho_filtro = p_olh if p_olh != "---" else None
    detalhe_filtro = p_det if p_det != "---" else None

    filtrados = [s for s in banco_suspeitos if 
                 (sexo_filtro is None or s["sexo"] == sexo_filtro) and
                 (cabelo_filtro is None or s["cabelo"] == cabelo_filtro) and
                 (olho_filtro is None or s["olho"] == olho_filtro) and
                 (detalhe_filtro is None or s["detalhes"] == detalhe_filtro)]
    
    if len(filtrados) == 1:
        st.session_state.mandado_ativo = filtrados[0]["nome"]
        st.sidebar.success(f"🚨 MANDADO EMITIDO: {filtrados[0]['nome'].upper()}")
        st.sidebar.image(filtrados[0]["imagem"], caption=f"FOTO ARQUIVO: {filtrados[0]['nome']}")
    else:
        st.session_state.mandado_ativo = None
        st.sidebar.warning(f"Inconclusivo. {len(filtrados)} suspeitos na lista.")
        for s in filtrados:
            st.sidebar.caption(f"- {s['nome']}")

# --- TELA PRINCIPAL ---
st.subheader(f"📍 Local Atual: {st.session_state.local_atual.upper()}")

url_imagem_cidade = mapa_mundi[st.session_state.local_atual]["imagem"]
try:
    st.image(url_imagem_cidade, use_container_width=True)
except:
    st.warning(f"Imagem da cidade não encontrada: {url_imagem_cidade}")

st.progress(max(0, st.session_state.horas_restantes) / 120) 
st.write(f"⏳ Horas Restantes: **{st.session_state.horas_restantes}h**")

if st.session_state.mensagem_tela:
    st.info(st.session_state.mensagem_tela)

# Se o jogo ainda está rolando
if not st.session_state.jogo_acabou:
    col_inv, col_via = st.columns(2)
    
    # INVESTIGAR
    with col_inv:
        st.markdown("### 🔍 Investigar (2h)")
        for local in st.session_state.locais_cidade:
            if st.button(f"🏢 Ir para: {local}"):
                st.session_state.horas_restantes -= 2
                
                if st.session_state.local_atual in st.session_state.rota_fuga:
                    indice = st.session_state.rota_fuga.index(st.session_state.local_atual)
                    
                    if indice == len(st.session_state.rota_fuga) - 1:
                        st.session_state.mensagem_tela = f"🕵️ Você invadiu o(a) {local} e achou o esconderijo do vilão!"
                        st.session_state.jogo_acabou = True
                        
                        if st.session_state.mandado_ativo == st.session_state.vilao["nome"]:
                            st.session_state.mensagem_tela += f"\n🎉 PARABÉNS! Você prendeu {st.session_state.vilao['nome']} com sucesso!"
                            st.session_state.venceu_atual = True
                            st.balloons()
                        else:
                            st.session_state.mensagem_tela += "\n❌ O vilão escapou! A polícia não tinha um mandado de prisão válido no nome dele."
                            st.session_state.venceu_atual = False
                            
                        st.rerun()
                    else:
                        proximo_destino = st.session_state.rota_fuga[indice + 1]
                        
                        if local in locais_fisicos: 
                            dicas_fisicas = [
                                f"Notei que era uma pessoa do sexo {st.session_state.vilao['sexo']}.",
                                f"A pessoa tinha cabelo {st.session_state.vilao['cabelo']}.",
                                f"Reparei que a pessoa tinha olhos de cor {st.session_state.vilao['olho']}."
                            ]
                            if st.session_state.vilao["detalhes"] == "---":
                                dicas_fisicas.append("Não notei nenhuma joia, tatuagem, cicatriz ou tapa olho.")
                            else:
                                dicas_fisicas.append(f"Me chamou a atenção que a pessoa tinha um(a) {st.session_state.vilao['detalhes']}.")
                                
                            dica = random.choice(dicas_fisicas)
                        else: 
                            dica = random.choice(mapa_mundi[proximo_destino]["fatos"])
                            
                        st.session_state.mensagem_tela = f"Testemunha no(a) {local}: '{dica}'"
                else:
                    st.session_state.mensagem_tela = f"Testemunha no(a) {local}: 'Não vi ninguém suspeito por aqui.'"
                st.rerun()

    # VIAJAR
    with col_via:
        st.markdown("### ✈️ Viajar (8h)")
        destinos = mapa_mundi[st.session_state.local_atual]["conexoes"]
        
        for dest in destinos:
            if st.button(f"🛫 Voo para {dest}"):
                st.session_state.local_atual = dest
                st.session_state.horas_restantes -= 8
                st.session_state.mensagem_tela = f"Você viajou para {dest}."
                sortear_locais() 
                st.rerun()

    # ABANDONAR O CASO
    st.divider()
    if st.button("🚪 Abandonar o Caso (Entregar Distintivo)"):
        st.session_state.jogo_acabou = True
        st.session_state.venceu_atual = False
        st.session_state.mensagem_tela = f"Você entregou seu distintivo e abandonou a investigação. O culpado era: {st.session_state.vilao['nome']}."
        st.rerun()

# ==========================================
# TELA FINAL (MUDANÇA DE IMAGEM)
# ==========================================
else:
    st.divider()
    
    if st.session_state.venceu_atual:
        imagem_final = st.session_state.vilao.get("imagem_preso", st.session_state.vilao["imagem"])
        try:
            st.image(imagem_final, width=250, caption=f"VILÃO CAPTURADO: {st.session_state.vilao['nome'].upper()}")
        except:
            st.warning(f"Imagem não encontrada: {imagem_final}")
        st.success("Você solucionou o caso! O seu registro foi atualizado.")
    else:
        imagem_final = st.session_state.vilao.get("imagem_fuga", st.session_state.vilao["imagem"])
        try:
            st.image(imagem_final, width=250, caption=f"VILÃO FORAGIDO: {st.session_state.vilao['nome'].upper()}")
        except:
            st.warning(f"Imagem não encontrada: {imagem_final}")
        st.error("Caso encerrado sem sucesso. O seu registro permanecerá o mesmo.")
        
    # === AQUI ESTÁ A CORREÇÃO ===
    st.button("🚔 Solicitar Novo Caso à DIE", on_click=iniciar_nova_partida, kwargs={"venceu_anterior": st.session_state.venceu_atual})

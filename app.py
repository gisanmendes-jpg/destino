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
    
    "cena_velha": {
        "texto": "Você se afasta da janela e exige respostas.\n\nA velha olha fixamente para você. *'Não olhe para a janela'*, ela avisa, com a voz baixa e firme.\n\nQuase no mesmo instante, alguma coisa bate do lado de fora.\n\n*TOC.*\n\nVocê congela. *TOC. TOC.* Alguém bate mais forte.\n\nUma voz abafada pelo vidro sussurra: *'Ei...'*",
        "imagem": "https://placehold.co/800x400/111122/FFFFFF?text=As+Batidas",
        "opcoes": [
            {"label": "Perguntar quem está aí", "destino": "cena_regras_1"}
        ]
    },
    
    "cena_regras_1": {
        "texto": "Seu coração dispara. A voz é sua. Exatamente a sua.\n\n*Abre a porta*, a voz pede. A velha empalidece. *'Ele nunca aparece tão cedo'*, ela murmura. Ela segura seu braço com uma força surpreendente.\n\n*'Primeiro você precisa entender uma coisa. Existem regras. Se quiser chegar vivo ao fim da linha.'*\n\nEla aponta para a janela: *'Regra 1: Quando alguém do lado de fora souber seu nome, não olhe.'*\n\nAponta para a porta: *'Regra 2: Nunca desembarque onde exista alguém esperando por você. Porque não está esperando você chegar. Está esperando você sair.'*",
        "imagem": "https://placehold.co/800x400/221111/FFFFFF?text=As+Regras",
        "opcoes": [
            {"label": "Ouvir o resto das regras...", "destino": "cena_regras_2"}
        ]
    },

    "cena_regras_2": {
        "texto": "A velha continua: *'Regra 3: Se o relógio do trem marcar 00:17, não confie em ninguém neste vagão.'*\n\nVocê olha o painel. 00:16. *E quando ele mudar?* você pergunta. *'Significa que estamos perto da última estação.'*\n\nVocê percebe algo estranho e conta as pessoas no vagão. Seis pessoas. Mas a velha diz que há sete.\n\n*'Você consegue ver seis'*, ela diz. O homem de sobretudo ri. Antes que ela explique, a voz do lado de fora sussurra: *'Eu sou o sétimo.'*",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=O+Setimo+Passageiro",
        "opcoes": [
            {"label": "Mas a porta está abrindo...", "destino": "cena_pegadas"}
        ]
    },

    "cena_pegadas": {
        "texto": "O trem para. O sinal toca.\n\n*'Regra 4: Nunca seja a primeira pessoa a sair'*, a velha avisa.\n\nA porta abre. Não há ninguém. Então, água pinga no chão. *TIC.* Pegadas invisíveis molhadas começam a entrar no vagão e param exatamente diante dos seus pés.\n\nUma respiração gélida toca sua orelha. A sua própria voz sussurra: *'Você não deveria ter acordado.'*\n\nAs luzes apagam. Alguém grita. Quando voltam, o trem está andando... e no banco onde você acordou, há alguém sentado de costas, usando a sua roupa.",
        "imagem": "https://placehold.co/800x400/1a1a3a/FFFFFF?text=A+Invasao+Invisivel",
        "opcoes": [
            # AQUI DEFINIMOS AS MEMÓRIAS DA ROTA B
            {"label": "B1) Exigir que a velha conte todas as regras.", "destino": "cena_b1", "ganha_memoria": "pressionou_velha"},
            {"label": "B2) Ignorar a velha e ir até a pessoa sentada no seu lugar.", "destino": "cena_b2", "ganha_memoria": "enfrentou_copia"},
            {"label": "B3) Perguntar à criança o que ela quis dizer.", "destino": "cena_b3", "ganha_memoria": "interrogou_crianca"},
            {"label": "B4) Perguntar ao policial se ele também vê a cópia.", "destino": "cena_b4", "ganha_memoria": "falou_policial"}
        ]
    },
    "cena_crianca": {
        "texto": "Você ignora a velha e vai até a criança. Os olhos dela encontram os seus. Sem confusão, sem susto.\n\n*'Você demorou'*, ela diz.\n\nVocê para diante do banco e se agacha. *'Por que estava esperando por mim?'*\n\nA criança olha para o seu rosto, depois para suas mãos. *'Porque você prometeu voltar.'*\n\nUma pressão surge atrás dos seus olhos. Uma tentativa de lembrar de um sonho. *'Eu nunca vi você antes'*, você diz.\n\nO rosto da criança muda para uma expressão triste. *'Você sempre fala isso.'*",
        "imagem": "https://placehold.co/800x400/1a1a2e/FFFFFF?text=A+Crianca",
        "opcoes": [
            {"label": "Tentar lembrar...", "destino": "cena_passado_1"}
        ]
    },

    "cena_passado_1": {
        "texto": "*'Ainda não lembra da casa?'*, a criança pergunta. *'A nossa casa. Você morava lá comigo.'*\n\nSeu coração acelera. É impossível. Mas quando tenta formar a imagem da sua infância ou de onde morava, nada aparece. Como um rosto apagado em uma fotografia.\n\n*'Qual o seu nome?'* você pergunta. Ela hesita. *'Você disse para eu nunca contar. Antes de acontecer. Numa terça-feira... chovendo. Você ficou bravo. E foi embora.'*\n\nImagens explodem na sua mente: Chuva. Faróis. Gritos. Vidro quebrando. Você dirigindo. E uma voz infantil implorando para você não ir.",
        "imagem": "https://placehold.co/800x400/223344/FFFFFF?text=As+Lembrancas",
        "opcoes": [
            {"label": "Olhar para o relógio do celular...", "destino": "cena_passado_2"}
        ]
    },

    "cena_passado_2": {
        "texto": "Seu celular marca 00:17. A criança fica pálida e manda você guardar. *'Foi essa hora. Do acidente.'*\n\nMais flashes: Asfalto molhado. Um caminhão. Uma buzina. A criança gritando *NÃO!*\n\nVocê recua, respirando rápido. *'Nós sofremos um acidente? Você morreu? Eu morri?'*\n\nA criança olha para você e responde com frieza: *'Eu não sei qual de nós morreu primeiro.'*\n\nAs portas do trem se abrem em Santa Lúcia. A criança vira a cabeça. *'É aqui. Onde começou. Viemos buscar minha mãe... Sua esposa.'*",
        "imagem": "https://placehold.co/800x400/440000/FFFFFF?text=O+Acidente",
        "opcoes": [
            {"label": "Ouvir a discussão no vagão...", "destino": "cena_passado_3"}
        ]
    },

    "cena_passado_3": {
        "texto": "O homem de sobretudo levanta, aterrorizado. *'Não diga o nome dela!'* A criança segura sua mão e aponta para ele. *'Ele estava lá. No carro atrás da gente.'*\n\nO homem recua: *'Alguém que deveria ter morrido naquela noite. Mas não morreu.'*\n\nDe repente, uma voz feminina chama da plataforma: *'Miguel.'* A criança congela. Você segura o menino. *'É minha mãe!'*\n\nVocê olha para a silhueta na plataforma. A dor atravessa seu peito. Uma lembrança: uma porta vermelha. Uma aliança no chão.\n\nVocê sussurra o nome: *'Helena...'*",
        "imagem": "https://placehold.co/800x400/111111/FFFFFF?text=Helena",
        "opcoes": [
            {"label": "Observar o relógio do trem...", "destino": "cena_passado_4"}
        ]
    },

    "cena_passado_4": {
        "texto": "O vagão inteiro fica em silêncio. Miguel para de lutar.\n\nEntão, o relógio do trem muda pela primeira vez: **00:17**.\n\nO alto-falante chia e diz apenas: *'Memória reconhecida.'*\n\nA mulher na plataforma sorri. Mas você percebe algo terrível: Helena nunca sorria daquele jeito.\n\nMiguel olha para você: *'É ela?'*",
        "imagem": "https://placehold.co/800x400/550000/FFFFFF?text=Memoria+Reconhecida",
        "opcoes": [
            # AQUI ESTÃO AS MEMÓRIAS DA ROTA C
            {"label": "C1) Segurar Miguel e exigir que ele conte sobre o acidente.", "destino": "cena_c1", "ganha_memoria": "segurou_miguel"},
            {"label": "C2) Chamar por Helena para testar se é ela mesma.", "destino": "cena_c2", "ganha_memoria": "chamou_helena"},
            {"label": "C3) Confrontar o homem de sobretudo sobre o acidente.", "destino": "cena_c3", "ganha_memoria": "interrogou_sobretudo"},
            {"label": "C4) Soltar Miguel e permitir que ele saia.", "destino": "cena_c4", "ganha_memoria": "soltou_miguel"}
        ]
    },
    "cena_fuga": {
        "texto": "Você ignora todos. Ignora o aviso da velha. Apenas destranca a porta e atravessa a ponte metálica entre os vagões. Atrás de você, a velha grita para não fechar a porta, mas um solavanco do trem a bate com violência.\n\nAgora você está sozinho.\n\nVocê entra no próximo vagão. As luzes acendem. Há cerca de quarenta passageiros, mas ninguém responde aos seus chamados.\n\nVocê toca o ombro de um senhor de terno. O corpo cai para o lado. Os olhos estão abertos e acinzentados. Estão todos mortos.",
        "imagem": "https://placehold.co/800x400/101010/FFFFFF?text=O+Vagao+Dos+Mortos",
        "opcoes": [
            {"label": "Olhar para o que ele segurava...", "destino": "cena_arquivo_1"}
        ]
    },

    "cena_arquivo_1": {
        "texto": "Um jornal cai no chão. A manchete diz: *ACIDENTE DE ÔNIBUS DEIXA 18 MORTOS*. A data: **1998**. O homem do banco é um dos mortos da foto.\n\nNos outros bancos: recortes de 2011, 2007. Pessoas que desapareceram ou morreram. Todos possuem uma etiqueta:\n*PASSAGEIRO 097 - DESTINO: CONCLUÍDO.*\n\nVocê corre para o final do vagão e encontra uma porta onde se lê: **ARQUIVO**.\n\nDentro, há uma sala com pastas. No centro de uma mesa, seis pastas se destacam. Você reconhece as fotos. A mulher. O policial. A criança. O homem de sobretudo. A velha. E a sua.",
        "imagem": "https://placehold.co/800x400/332211/FFFFFF?text=O+Arquivo",
        "opcoes": [
            {"label": "Ler a pasta da mulher e do policial", "destino": "cena_arquivo_2"}
        ]
    },

    "cena_arquivo_2": {
        "texto": "LAURA MENEZES. Status Original: FALECIDA.\nRICARDO ALMEIDA. Status Original: FALECIDO.\n\nSua mão treme ao pegar a do menino. *MIGUEL*. Status Original: INDETERMINADO. Observação: *NÃO DEVE CHEGAR AO TERMINAL.*\n\nDANIEL VASCONCELOS (O sobretudo). Status Original: SOBREVIVENTE. Observação: *EMBARQUE NÃO AUTORIZADO.*\n\nTERESA (A velha). Não tem idade, mas uma foto de 1964. Status: CONDUTORA. Observação: *NÃO PERMITIR QUE DESEMBARQUE.*",
        "imagem": "https://placehold.co/800x400/443322/FFFFFF?text=O+Passado+Escrito",
        "opcoes": [
            {"label": "Abrir a sua própria pasta", "destino": "cena_arquivo_3"}
        ]
    },

    "cena_arquivo_3": {
        "texto": "Você abre a sua. Na classificação diz: **PARADOXO**. O status original foi raspado com gilete.\n\n*MEMÓRIA SUPRIMIDA: SIM. MOTIVO: PROTEÇÃO DA LINHA.*\n\nNa última página, um aviso em vermelho: *SE ELE RECUPERAR A MEMÓRIA ANTES DA ESTAÇÃO FINAL, O CICLO RECOMEÇA.*\n\nEmbaixo de tudo, há uma 7ª pasta. *PASSAGEIRO 007. Identidade: Variável. Forma: Não definida.*\n\nObservação: *ASSUME A IDENTIDADE DE QUEM O RECONHECE.*",
        "imagem": "https://placehold.co/800x400/8B0000/FFFFFF?text=Passageiro+007",
        "opcoes": [
            {"label": "Ouvir o barulho na porta...", "destino": "cena_arquivo_4"}
        ]
    },

    "cena_arquivo_4": {
        "texto": "*TOC. TOC. TOC.*\n\nUma voz vem do corredor dos mortos. *'Abre, sou eu.'* É o policial.\n\nMas logo atrás vem a voz da velha: *'Não abra!'*\nE a de Miguel: *'Ele não está sozinho!'*\n\nTodos começam a gritar e bater ao mesmo tempo. Você recua. Até que ouve uma quarta voz. Da sua própria garganta? Não, vem do outro lado da porta.\n\nA sua voz diz: *'Não abre para eles.'*\n\nO trinco da porta do Arquivo começa a girar sozinho.",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=Batem+Na+Porta",
        "opcoes": [
            # AQUI ESTÃO AS MEMÓRIAS DA ROTA D
            {"label": "D1) Abrir a porta rapidamente para o policial.", "destino": "cena_d1", "ganha_memoria": "confiou_policial"},
            {"label": "D2) Segurar a maçaneta e investigar a pasta apagada.", "destino": "cena_d2", "ganha_memoria": "buscou_verdade"},
            {"label": "D3) Perguntar por trás da porta algo que só Miguel saiba.", "destino": "cena_d3", "ganha_memoria": "testou_entidade"},
            {"label": "D4) Procurar outra saída dentro do Arquivo.", "destino": "cena_d4", "ganha_memoria": "fugiu_arquivo"}
        ]
    },
    
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

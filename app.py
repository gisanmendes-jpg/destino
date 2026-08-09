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
        "texto": "O celular continua vibrando em sua mão.\n\n*NÃO CONFIE NA VELHA.*\n*NÃO DEIXE A CRIANÇA CHEGAR À ESTAÇÃO FINAL.*\n\nA contagem regressiva continua.\n02:31...\n02:30...\n\nTeresa se aproxima.\n— O que apareceu nesse telefone?\n\nMiguel observa você do outro lado do vagão. O homem de sobretudo não sorri mais. Pela janela, Santa Lúcia desaparece lentamente na escuridão. Então chega uma nova mensagem.\n\n*NÃO MOSTRE ISSO A ELA.*\n*ELA JÁ ME ENTREGOU UMA VEZ.*",
        "imagem": "https://placehold.co/800x400/001100/FFFFFF?text=As+Mensagens",
        "opcoes": [
            {"label": "Olhar para o reflexo na tela...", "destino": "cena_a_decisao"}
        ]
    },

    "cena_a_decisao": {
        "texto": "Você sente o estômago revirar. Teresa estende a mão.\n— Me dê o telefone.\n\nAntes que você responda, surge a última mensagem:\n**VOCÊ PRECISA ESCOLHER EM QUEM ACREDITAR ANTES QUE ELE ENTRE.**\n\n01:59...\n01:58...\n\nVocê olha para Teresa. Depois para Miguel. E percebe uma coisa perturbadora. A tela apagada do celular reflete seu rosto. Mas por uma fração de segundo... o reflexo parece muito mais velho.",
        "imagem": "https://placehold.co/800x400/110000/FFFFFF?text=O+Reflexo",
        "opcoes": [
            {"label": "A1) Esconder o celular e confiar nas mensagens", "destino": "cena_a1_mensagens", "ganha_memoria": "confiou_futuro"},
            {"label": "A2) Entregar o celular e confiar em Teresa", "destino": "cena_a2_teresa", "ganha_memoria": "entregou_celular"}
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
        "texto": "O trem para. A porta abre. Não há ninguém. Então, água pinga no chão. *TIC.* Pegadas invisíveis molhadas começam a entrar no vagão e param exatamente diante dos seus pés.\n\nUma respiração gélida toca sua orelha. A sua própria voz sussurra: *'Você não deveria ter acordado.'*\n\nAs luzes apagam. Alguém grita. Quando voltam, o trem está andando... e no banco onde você acordou, há alguém sentado de costas, usando a sua roupa.",
        "imagem": "https://placehold.co/800x400/1a1a3a/FFFFFF?text=A+Invasao+Invisivel",
        "opcoes": [
            {"label": "Observar a figura no banco...", "destino": "cena_b_copia"}
        ]
    },

    "cena_b_copia": {
        "texto": "As pegadas molhadas desapareceram. Mas a pessoa sentada no seu antigo banco continua ali. Imóvel.\n\nTeresa não tira os olhos dela.\n— Não fale com ele.\nMiguel observa do outro lado do vagão.\n— Ainda não.\n\nVocê olha para os dois. — 'Ainda' quando?\n\nNenhum responde. Então a pessoa no banco inclina lentamente a cabeça. Não chega a se virar. Apenas o suficiente para mostrar parte do rosto. Seu rosto.",
        "imagem": "https://placehold.co/800x400/111122/FFFFFF?text=Seu+Rosto",
        "opcoes": [
            {"label": "Tentar falar algo...", "destino": "cena_b_nome"}
        ]
    },

    "cena_b_nome": {
        "texto": "Você recua. Teresa segura seu braço.\n— Não reconheça. Não diga quem você acha que ele é.\n\nO homem de sobretudo se levanta, parecendo realmente preocupado. — Ela tem razão.\n\nA figura no banco levanta uma das mãos. Aponta para você. Bate duas vezes no próprio peito. *TOC. TOC.* Depois aponta para você novamente.\n\nMiguel sussurra: — Ele quer que você diga.\n— Diga o quê?\n— Seu nome. Porque algumas coisas aqui não têm nome até alguém dar um.",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=O+Nome",
        "opcoes": [
            {"label": "Ver a figura se mover...", "destino": "cena_b_decisao"}
        ]
    },

    "cena_b_decisao": {
        "texto": "Silêncio. A figura começa a se virar.\n\nTeresa aperta seu braço.\n— Escolha agora.\n\nVocê precisa decidir: aceitar que obedecer às regras é a única coisa mantendo você vivo (e interrogar Teresa sobre a origem delas), ou ignorar os avisos, aproximar-se e descobrir o que é essa entidade.",
        "imagem": "https://placehold.co/800x400/220000/FFFFFF?text=A+Regra",
        "opcoes": [
            {"label": "B1) Afastar-se da figura e exigir respostas de Teresa", "destino": "cena_b1_obedecer", "ganha_memoria": "obedeceu_regras"},
            {"label": "B2) Ignorar Teresa e se aproximar da cópia", "destino": "cena_b2_quebrar", "ganha_memoria": "quebrou_regra"}
        ]
    },

    # === CONSEQUÊNCIA IMEDIATA DA QUEBRA DE REGRA (Gatilho) ===
    "cena_b2_quebrar": {
        "texto": "Você ignora Teresa e dá o primeiro passo na direção da figura. Você não pretende dizer o seu nome. Só quer ver o rosto dela.\n\nMas, quando você avança... a figura fala sem se virar, com a sua exata voz:\n\n— Você sempre chega mais perto. Foi assim que eu entrei da primeira vez.\n\nTeresa empalidece. — Não escute.\nA figura começa a virar o rosto.\n— Pergunta para ela o que aconteceu com os outros seis.",
        "imagem": "https://placehold.co/800x400/331111/FFFFFF?text=Os+Outros+Seis",
        "opcoes": [
            {"label": "Encarar a figura...", "destino": "cap2_entidade_revela"} # Cena a ser escrita depois
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
        "texto": "O vagão inteiro fica em silêncio. Miguel para de lutar.\n\nEntão, o relógio do trem muda pela primeira vez: **00:17**.\nO alto-falante chia e diz apenas: *'Memória reconhecida.'*\n\nA mulher na plataforma sorri. Mas você percebe algo terrível: Helena nunca sorria daquele jeito.\n\nMiguel olha para você: *'É ela?'*",
        "imagem": "https://placehold.co/800x400/550000/FFFFFF?text=Memoria+Reconhecida",
        "opcoes": [
            {"label": "Tentar lembrar do rosto dela...", "destino": "cena_c_conflito"}
        ]
    },

    "cena_c_conflito": {
        "texto": "Uma lembrança surge: Helena rindo. Miguel correndo. Felicidade. Mas logo muda para uma memória violenta: Helena chorando. Uma mala. Você gritando: *'Se sair agora, não precisa voltar.'*\n\nMiguel aperta sua mão: *'Foi a última coisa que você falou para ela.'*\n\nDaniel se aproxima, tenso. *'Não continue. Lembrar não significa que aconteceu exatamente daquele jeito.'*\n\nTeresa reage rispidamente quando a mulher chama por Miguel: *'Eu sei o que acontece quando os mortos chamam pelo nome dos vivos.'*",
        "imagem": "https://placehold.co/800x400/221111/FFFFFF?text=Os+Mortos",
        "opcoes": [
            {"label": "Encarar a mulher na plataforma...", "destino": "cena_c_revelacao"}
        ]
    },

    "cena_c_revelacao": {
        "texto": "Sob a luz, você reconhece Helena. Ela sorri. *'Você finalmente lembrou de mim. Está com medo?'*\n\nDaniel faz a pergunta que gela seu sangue: *'A pergunta é: quem morreu naquela estrada?'*\n\nHelena começa a rir baixo, um som que não combina com ela. Miguel hesita. Então você percebe algo impossível: Helena está descalça sobre o chão molhado, mas **não produz reflexo nas poças**.\n\nTeresa sussurra: *'Agora escolha.'*",
        "imagem": "https://placehold.co/800x400/111122/FFFFFF?text=Sem+Reflexo",
        "opcoes": [
            {"label": "C1) Proteger Miguel e obrigar Daniel a revelar a verdade", "destino": "cena_c1_proteger", "ganha_memoria": "protegeu_miguel"},
            {"label": "C2) Confiar na memória e soltar Miguel para a mãe", "destino": "cena_c2_soltar", "ganha_memoria": "acreditou_helena"}
        ]
    },

    # === CONSEQUÊNCIA IMEDIATA DA ESCOLHA C2 (Gatilho) ===
    "cena_c2_soltar": {
        "texto": "Você aceita que é Helena e decide soltá-lo. Mas pensa em fazer uma única pergunta que só sua verdadeira esposa saberia.\n\nHelena sorri antes mesmo de você abrir a boca e diz:\n— A porta era vermelha.\n\nSeu sangue esfria. Era exatamente o que você ia perguntar.\nDaniel sussurra: *'Ela está dentro da sua cabeça.'*\n\nDo lado de fora, Helena abre os braços para Miguel. E atrás dela... por um único segundo... você vê alguma coisa muito alta se mover na escuridão.",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=A+Coisa+Na+Escuridao",
        "opcoes": [
            {"label": "Ver o que acontece a seguir...", "destino": "cap2_miguel_helena"} # Cena a ser escrita depois
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
        "texto": "A porta do Arquivo treme. Vozeirões se sobrepõem: o policial, a velha, a criança. E pior: a sua própria voz dizendo para não acreditar neles.\n\nVocê olha para a pasta do **PASSAGEIRO 007**: *Identidade: Variável. Forma: Não definida. Assume a identidade de quem o reconhece.*\n\nUma voz infantil do outro lado chora chamando por socorro. Você se aproxima e diz: *'Miguel?'*\n\nTeresa grita para você não dizer o nome! A voz lá fora muda de tom e sussurra: *'Você me reconheceu.'*",
        "imagem": "https://placehold.co/800x400/110000/FFFFFF?text=O+Passageiro+007",
        "opcoes": [
            {"label": "Olhar as marcas na porta...", "destino": "cena_arquivo_marcas"}
        ]
    },

    "cena_arquivo_marcas": {
        "texto": "Você recua e repara nas inscrições riscadas no metal da porta:\n*• Não responda à primeira voz.*\n*• Não diga nomes.*\n*• Ele não tem rosto até você dar um.*\n*• Se ele usar sua voz, não olhe nos olhos dele.*\n\nVocê corre de volta para a sua pasta. Encontra páginas rasgadas: *Causa da morte: Arrancada. Corpo recuperado: Não. Declaração de óbito: Não emitida. Ele não morreu na primeira vez. Foi devolvido.*",
        "imagem": "https://placehold.co/800x400/221100/FFFFFF?text=A+Ficha+Rasgada",
        "opcoes": [
            {"label": "Alguém empurra a porta...", "destino": "cena_arquivo_porta"}
        ]
    },

    "cena_arquivo_porta": {
        "texto": "A porta se abre alguns centímetros. Uma mão ensanguentada com unhas quebradas se agarra ao batente. É Ricardo, o policial, com vidro na bochecha e ferimentos de acidente.\n\nEnquanto ele implora para entrar, seu rosto pisca rapidamente: vira Miguel, vira Teresa, vira Laura, vira você mesmo.\n\nA porta se fecha de repente. Na pasta do Passageiro 007, uma nova linha surge: *Modelo mais provável: VOCÊ.*\n\nVocê se vira e vê o seu reflexo na estante de vidro. Ele sorri. Você fecha os olhos e ouve sua própria voz: *'Não olha para mim.'*",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=O+Reflexo+Sorri",
        "opcoes": [
            # AQUI ESTÃO AS DUAS ESCOLHAS FINAIS DA LINHA D
            {"label": "D1) Continuar investigando sua pasta (Descobrir a verdade)", "destino": "cena_d1_verdade", "ganha_memoria": "investigou_origem"},
            {"label": "D2) Abandonar o Arquivo e enfrentar a criatura", "destino": "cena_d2_enfrentar", "ganha_memoria": "enfrentou_007"}
        ]
    },

    # === CONSEQUÊNCIA IMEDIATA DA ESCOLHA D2 (Gatilho) ===
    "cena_d2_enfrentar": {
        "texto": "Você decide largar os papéis, farto de mentiras, e toca a maçaneta da porta para enfrentar o que quer que esteja do outro lado.\n\nMas, no instante em que sua mão aperta o metal, uma voz sussurra bem perto do seu ouvido, de dentro do próprio cômodo escuro:\n\n— *Não precisa abrir. Eu já entrei.*",
        "imagem": "https://placehold.co/800x400/550000/FFFFFF?text=Ele+Ja+Entrou",
        "opcoes": [
            {"label": "Virar-se para encarar a entidade...", "destino": "cap2_confronto_final"} # Cena a ser escrita
        ]
    },
    "cena_a1_mensagens": {
        "texto": "Você apaga a tela e esconde o celular. Teresa abaixa a mão, desconfiada, mas se afasta.\n\nO aparelho vibra novamente. Você checa disfarçadamente.\n**CERTO. ELA NÃO PODE SABER QUE ESTAMOS FALANDO.**\n\nVocê digita: *Quem é você?*\n**VOCÊ.**\n*Prova.*\n**VOCÊ TEM UMA CICATRIZ DEBAIXO DO JOELHO DIREITO. AOS 11 ANOS VOCÊ CAIU DO MURO DOS FUNDOS.**\n\nVocê toca a perna instintivamente. É verdade. É a primeira lembrança clara da sua infância. *Como sabe disso?*\n**PORQUE EU ESTAVA LÁ.**",
        "imagem": "https://placehold.co/800x400/001122/FFFFFF?text=A+Cicatriz",
        "opcoes": [
            {"label": "Perguntar sobre os outros passageiros...", "destino": "cena_a1_foto"}
        ]
    },

    "cena_a1_foto": {
        "texto": "O celular vibra:\n**OLHE PARA MIGUEL. ELE NÃO PODE CHEGAR AO TERMINAL.**\n*Por quê?*\n**PORQUE FOI ASSIM QUE TUDO COMEÇOU.**\n\nDaniel se aproxima e pergunta com quem você está falando. Você guarda o telefone. Daniel dá um sorriso triste: *'Então começou mais cedo desta vez.'*\n\nO celular vibra. **NÃO ESCUTE DANIEL. ELE É A RAZÃO DE EU TER FICADO PRESO AQUI.**\n\nA contagem dispara no celular: **01:28... 01:27...**\n*O que acontece em São Gabriel?*\n**VOCÊ VAI ME VER DE NOVO. DENTRO DO TREM. QUANDO AS LUZES APAGAREM, NÃO DEIXE NINGUÉM TOCAR EM VOCÊ. PORQUE ELE AINDA NÃO TEM SEU ROSTO COMPLETO.**\n\nVocê digita: *Quem?*\nA resposta é uma fotografia. O interior do vagão. Atrás de você, há uma figura muito alta. Sem rosto. Inclinada sobre o seu ombro.",
        "imagem": "https://placehold.co/800x400/110000/FFFFFF?text=A+Fotografia",
        "opcoes": [
            {"label": "Olhar para trás e confrontar Teresa...", "destino": "cena_a1_escuro"}
        ]
    },

    "cena_a1_escuro": {
        "texto": "Você se vira imediatamente. Não há nada. O celular avisa: **NÃO PROCURE POR ELE. ELA TRABALHA PARA ELE.**\n\nTeresa percebe. *'Entregue o telefone. Alguma coisa está usando você para entrar.'*\n\nA contagem chega a **00:19**. A voz do futuro manda você ir para o último banco. Teresa entra na sua frente, desesperada: *'Se você obedecer, vai repetir a sua morte.'*\n\n**00:10... 00:07... 00:05...**\n\nTeresa grita a mesma regra da mensagem: *'NÃO DEIXEM NINGUÉM TOCAR EM VOCÊ!'*\n\nAs luzes apagam. Escuridão total. Alguma coisa corre pelo teto. Vozes com o seu timbre ecoam pelo vagão discutindo.\nAlguém toca o seu ombro.",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=Blecaute",
        "opcoes": [
            {"label": "Afastar-se violentamente...", "destino": "cena_a1_encontro"}
        ]
    },

    "cena_a1_encontro": {
        "texto": "As luzes retornam. Há uma pessoa a mais no último banco. Seu eu mais velho, com a cicatriz na sobrancelha.\n\nO celular vibra. **NÃO TENHA MEDO.** O homem sorri.\n\nEntão, uma nova mensagem chega. O remetente não é VOCÊ. É o **CONDUTOR**.\n\n**OBRIGADO POR TRAZÊ-LO DE VOLTA.**\n\nO sorriso do homem velho desaparece. Ele sussurra um 'Não...'. O alto-falante chia: *'Estação São Gabriel. Dois passageiros com a mesma identidade detectados.'*\n\nTeresa fecha os olhos: *'Outra vez não.'*",
        "imagem": "https://placehold.co/800x400/331111/FFFFFF?text=O+Encontro",
        "opcoes": [
            {"label": "A1.1) Aproximar-se do seu eu mais velho", "destino": "cena_a1_1", "ganha_memoria": "aproximou_futuro"},
            {"label": "A1.2) Destruir o celular e romper o contato", "destino": "cena_a1_2", "ganha_memoria": "destruiu_celular"}
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

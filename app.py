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
        "texto": "Você acorda com um solavanco violento, sua cabeça lateja.\n\nPor alguns segundos, você não abre os olhos, tentando lembrar como foi parar ali. A última lembrança é um borrão de chuva e faróis... nada mais. Há um ruído constante ao seu redor. Metal contra metal. O som rítmico e distante de rodas correndo sobre trilhos.\n\nVocê está em um trem. Mas como? E para onde?\n\nVocê tateia o bolso e puxa o celular para verificar as horas. O visor brilha: **00:16**. Você levanta os olhos para o painel digital na parede do vagão; o relógio oficial também marca **00:16**.\n\nVocê espera o tempo passar. Os segundos do seu celular continuam correndo... mas o relógio do trem permanece imóvel, congelado naquele minuto.",
        "imagem": "https://placehold.co/800x400/111111/FFFFFF?text=O+Despertar",
        "opcoes": [
            {"label": "Levantar a cabeça e olhar ao redor...", "destino": "cap1_parte2"} 
        ]
    },
    "cap1_parte2": {
        "texto": "Você força o corpo a levantar e olha o corredor do vagão. Você não está sozinho.\n\nDo outro lado, uma mulher chora silenciosamente, escondendo o rosto nas mãos. Mais à frente, um policial mantém a cabeça baixa, fixo no chão, com uma mancha escura de sangue secando na camisa.\n\nNo fundo do vagão, um homem de sobretudo escuro olha diretamente para você. Sem piscar. Perto dele, um **menino pequeno**, de uns nove anos, dorme encolhido no banco, abraçado a uma mochila.\n\nE bem perto de você, na poltrona da frente, uma senhora muito velha segura uma bolsa de mão contra o peito, observando tudo com olhos alertas.",
        "imagem": "https://placehold.co/800x400/222222/FFFFFF?text=Os+Passageiros",
        "opcoes": [
            {"label": "Continuar observando...", "destino": "cap1_parte3"}
        ]
    },
    "cap1_parte3": {
        "texto": "Um alto-falante chia, quebrando o silêncio opressor do vagão. Uma voz distorcida e mecânica anuncia:\n— Próxima estação... Santa Lúcia.\n\nO trem começa a desacelerar, o ranger dos freios é ensurdecedor. Pela janela escura, onde antes só havia rastros de velocidade, você vê uma plataforma vazia e mal iluminada se aproximar.\n\nA velha senhora na sua frente quebra o próprio protocolo e se vira para você. Seus olhos transmitem um terror genuíno.\n\n— Escute com atenção, rapaz — ela sussurra apressada. — Meu nome é Teresa. Não importa o que você ouvir... quando o trem parar, **não olhe** pela janela.\n\nMas é tarde. O trem para. Instintivamente, você olha. Há alguém na plataforma. Alguém em pé, de costas, sob a luz amarelada do poste. Usando exatamente a mesma roupa que você veste agora.",
        "imagem": "https://placehold.co/800x400/050505/FFFFFF?text=A+Estacao+Santa+Lucia",
        "opcoes": [
            {"label": "A) Continuar olhando pela janela para ver o rosto da figura.", "destino": "cena_janela", "ganha_memoria": "olhou_janela"},
            {"label": "B) Afastar-se imediatamente e exigir respostas de Teresa.", "destino": "cena_velha", "ganha_memoria": "obedeceu_velha"},
            {"label": "C) Ir até o menino adormecido no fundo do vagão.", "destino": "cena_crianca", "ganha_memoria": "falou_crianca"},
            {"label": "D) Ignorar todos e correr para o próximo vagão.", "destino": "cena_fuga", "ganha_memoria": "fugiu_vagao"}
        ]
    },

    # ===============================
    # LINHA A (JANELA/FUTURO)
    # ===============================
    "cena_janela": {
        "texto": "Você ignora o aviso de Teresa e cola o rosto no vidro frio.\n\nA pessoa na plataforma começa a virar o rosto. Devagar. Primeiro o ombro. Depois o pescoço. O medo trava sua respiração quando o rosto aparece sob a luz.\n\nÉ você. Mas não como você é agora. É uma versão muito mais velha, com o rosto marcado pelo tempo e por cicatrizes, um corte profundo atravessando a sobrancelha esquerda. A roupa está suja, coberta por manchas que parecem sangue seco.\n\nO seu 'eu' velho caminha pela plataforma, acompanhando o vagão parado. Ele para diante da sua janela e vocês alinham as mãos no vidro. Nesse toque impossível, imagens violentas invadem sua mente como flashes: Fogo. Um grito de mulher. O choro de uma criança. E você... ajoelhado diante de destroços.\n\nO pânico faz você recuar.",
        "imagem": "https://placehold.co/800x400/111111/FFFFFF?text=O+Seu+Futuro",
        "opcoes": [
            {"label": "Recuperar o fôlego...", "destino": "cena_janela_vibracao"}
        ]
    },
    "cena_janela_vibracao": {
        "texto": "Enquanto você tenta processar a visão, algo começa a vibrar violentamente no bolso da sua calça. É o seu celular.\n\nA tela acende. Não há número de chamada, apenas um texto grande e vermelho pairando sobre o fundo preto:\n\n**02:31... 02:30...**\n\nÉ uma contagem regressiva. Começou agora. E está correndo rápido.\n\nTeresa, a velha senhora, se aproxima de você, o rosto pálido. Ela viu o aparelho.\n— O que apareceu nesse telefone? — ela exige, sua voz tremendo.\n\nDo outro lado do vagão, o homem de sobretudo e o policial observam você. Até o **menino adormecido** acordou e olha em sua direção com olhos vazios. Pela janela, a plataforma de Santa Lúcia desaparece lentamente enquanto o trem volta a andar.\n\nUma nova mensagem pisca na tela do celular, sobrepondo a contagem:\n*NÃO MOSTRE ISSO A TERESA.*",
        "imagem": "https://placehold.co/800x400/001100/FFFFFF?text=As+Mensagens",
        "opcoes": [
            {"label": "Olhar para o reflexo na tela apagada...", "destino": "cena_a_decisao"}
        ]
    },
    "cena_a_decisao": {
        "texto": "Você sente o estômago revirar. Teresa estende a mão enrugada para você.\n— Me dê o telefone, agora!\n\nAntes que você responda, surge a última mensagem no visor, como um aviso final:\n**VOCÊ PRECISA ESCOLHER EM QUEM ACREDITAR ANTES QUE O CONDUTOR ENTRE.**\n\nO cronômetro marca **01:58**.\n\nVocê olha para Teresa. Depois para os outros passageiros estranhos. Miguel, o menino no fundo, parece estar chorando sem fazer som. Você percebe uma coisa perturbadora: a tela do celular reflete seu rosto. Mas por uma fração de segundo... o reflexo não é o seu, mas o daquele homem velho na plataforma.",
        "imagem": "https://placehold.co/800x400/110000/FFFFFF?text=O+Reflexo",
        "opcoes": [
            {"label": "A1) Esconder o celular e confiar nas mensagens misteriosas", "destino": "cena_a1_mensagens", "ganha_memoria": "confiou_futuro"},
            {"label": "A2) Entregar o celular e confiar em Teresa", "destino": "cena_a2_teresa", "ganha_memoria": "entregou_celular"}
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
    "cena_a1_1": {
        "texto": "Você dá um passo na direção do seu eu mais velho.\n\nSe ele realmente enviou as mensagens, finalmente poderá explicar o que aconteceu nas viagens anteriores e por que Miguel não pode chegar ao terminal.\n\nMas as palavras do alto-falante ecoam na sua cabeça. O Condutor acabou de agradecer por ele estar ali. Talvez você não o tenha encontrado. Talvez tenha acabado de trazê-lo para dentro.",
        "imagem": "https://placehold.co/800x400/221100/FFFFFF?text=A+Isca",
        "opcoes": [
            {"label": "Encarar o seu destino...", "destino": "cap2_a1_decisao_final"} 
        ]
    },
    "cena_a1_2": {
        "texto": "Você recua. Decide destruir o celular e impedir que novas mensagens conduzam suas decisões.\n\nVocê escolhe confiar no único aviso que Teresa e o 'eu do futuro' deram em comum: alguma coisa está tentando assumir sua identidade.\n\nMas, antes de desligar e quebrar o aparelho, a tela acende com uma última mensagem:\n\n**SE VOCÊ PARAR DE ME OUVIR, EU VOU MORRER DE NOVO.**\n\nO futuro encontrou o presente.",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=O+Fim+Do+Contato",
        "opcoes": [
            {"label": "Encarar o seu destino...", "destino": "cap2_a1_decisao_final"} 
        ]
    },
    "cap2_a1_decisao_final": {
        "texto": "Independentemente de quem mandou as mensagens, o ciclo se fechou. O trem chega ao seu limite.\n\nAs portas se abrem para a noite chuvosa do acidente. O carro destruído. Sirenes ao longe. O seu 'eu mais velho' aponta para Miguel, depois para você. A mesma escolha de todas as outras viagens se apresenta.\n\nVocê vai desfazer o acordo e morrer na estrada, ou vai aceitar continuar vivo e se transformar no próximo Condutor?",
        "imagem": "https://placehold.co/800x400/330000/FFFFFF?text=O+Terminal",
        "opcoes": [
            {"label": "A) LEVAR MIGUEL ATÉ O TERMINAL (Aceitar a morte)", "destino": "final_sacrificio", "reiniciar": True},
            {"label": "B) PEGAR A MÃO DO SEU EU MAIS VELHO (Aceitar a vida)", "destino": "final_egoista", "reiniciar": True}
        ]
    },
    "cena_a2_teresa": {
        "texto": "Você decide não confiar na coisa que usa o seu rosto. Estende a mão e entrega o aparelho para Teresa.\n\nMas, no exato instante em que os dedos dela tocam o metal frio do celular... a tela pisca e muda.\n\nSurge apenas uma frase em letras maiúsculas:\n\n**VOCÊ FEZ ISSO DA ÚLTIMA VEZ TAMBÉM.**",
        "imagem": "https://placehold.co/800x400/8B0000/FFFFFF?text=O+Ciclo+Se+Repete",
        "opcoes": [
            {"label": "Ver a reação de Teresa...", "destino": "cap2_teresa_explica"} 
        ]
    },
    "cap2_teresa_explica": {
        "texto": "No instante em que Teresa toca o celular, a tela fica preta.\n\n— *Ele sabe que eu toquei*, ela diz. O aparelho vibra na mão dela e acende.\n\n**OLÁ, TERESA.**\n**AINDA ESTÁ TENTANDO CONSERTAR 1964?**\n\nO rosto da velha perde a cor. Você pega o telefone de volta: — *Quem morreu em 1964?*\nTeresa implora para você não usar a palavra *'morreu'*. As luzes piscam duas vezes.\n\nOutra mensagem chega para você: **ELA NÃO CONTA PORQUE TEM VERGONHA.**",
        "imagem": "https://placehold.co/800x400/111111/FFFFFF?text=O+Segredo+De+1964",
        "opcoes": [
            {"label": "Exigir explicações de Teresa...", "destino": "cap2_o_ciclo"}
        ]
    },
    "cap2_o_ciclo": {
        "texto": "Você exige que Teresa explique. Ela respira fundo.\n— *Existem maneiras de os mortos permanecerem presos. Um lugar. Uma pessoa. Culpa. Medo...*\n\nEla segura seu pulso e revela a verdade: Aquilo na plataforma não era seu futuro. Era algo que já aconteceu muitas vezes. Você já esteve aqui.\n\n— *Quantas vezes?* — você pergunta, sentindo o corpo perder a força.\n— *Eu parei de contar depois da décima segunda.*\n\nVocê está revivendo esse pesadelo. Você pergunta o motivo de não se lembrar, e Teresa diz: — *Porque você pediu. Toda vez.*",
        "imagem": "https://placehold.co/800x400/220000/FFFFFF?text=A+Decima+Segunda+Vez",
        "opcoes": [
            {"label": "Perguntar o motivo do pedido...", "destino": "cap2_revelacao_miguel"}
        ]
    },
    "cap2_revelacao_miguel": {
        "texto": "Teresa hesita antes de responder. — *Porque na primeira vez que você lembrou de tudo... você tentou matar Miguel.*\n\nA criança recua. O celular vibra violentamente com 4 mensagens seguidas:\n**MENTIRA. MENTIRA. MENTIRA. MENTIRA.**\n\nTeresa explica que alguém convenceu você de que, se Miguel chegasse à estação final, tudo começaria novamente. Exatamente o que a mensagem no celular orienta: **'NÃO DEIXE A CRIANÇA CHEGAR À ESTAÇÃO FINAL'**.\n\nDaniel se levanta furioso. — *Ela sabe o porquê. Porque foi ela quem começou isso. Pergunta quem era a criança de 1964!*",
        "imagem": "https://placehold.co/800x400/331111/FFFFFF?text=O+Alvo",
        "opcoes": [
            {"label": "Olhar a tela do celular...", "destino": "cap2_foto_1964"}
        ]
    },
    "cap2_foto_1964": {
        "texto": "O celular recebe uma foto em preto e branco. Uma plataforma ferroviária. Santa Lúcia - 17/08/1964. Teresa, jovem, segurando a mão de uma menina de seis anos.\n\nOutra mensagem: **DIGA O NOME, TERESA.**\nEla treme. — *Nomes chamam os mortos.*\n\nA foto no celular muda. A menina agora está pálida e macabra atrás de Teresa. O trem começa a frear fora de hora. \n\n— *São Gabriel não deveria vir agora,* — Teresa diz em pânico. — *Alguém mudou a rota.*",
        "imagem": "https://placehold.co/800x400/111111/FFFFFF?text=A+Mudanca+De+Rota",
        "opcoes": [
            {"label": "Olhar pela janela do trem...", "destino": "cap2_estacao_gabriel"}
        ]
    },
    "cap2_estacao_gabriel": {
        "texto": "Na tela, o remetente confessa: **EU. ELA ME DEVE UMA PASSAGEIRA.**\n\nNa plataforma de São Gabriel, há uma menina esperando. Cabelos molhados, vestido antigo. Ela sorri e a voz atravessa o vidro:\n— *Mãe. Você prometeu voltar.*\n\nO nome do remetente no celular muda de VOCÊ para **CONDUTOR**.\nUma única frase surge: **UMA DÍVIDA PRECISA SER PAGA.**",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=A+Divida",
        "opcoes": [
            {"label": "A2.1) Ficar ao lado de Teresa e impedir que ela saia", "destino": "cena_a2_1_proteger", "ganha_memoria": "protegeu_teresa"},
            {"label": "A2.2) Usar Teresa como isca para revelar o Condutor", "destino": "cena_a2_2_isca", "ganha_memoria": "usou_isca"}
        ]
    },
    "cena_a2_1_proteger": {
        "texto": "Você puxa Teresa de volta. *'NÃO.'*\nEla tenta se soltar, furiosa e aos prantos. *'É minha filha! Ela estava morrendo. Os médicos disseram que não passaria daquela noite.'*\n\nVocê começa a entender. *'E o trem apareceu. Às 00:17.'*\n\nTeresa confessa que ouviu a voz do Condutor oferecendo salvá-la em troca de uma vida. *'Qualquer uma.'*\nVocê recua, horrorizado: *'Você entregou alguém?'*\n*'Eu não sabia! Eu queria minha filha viva!'*\n\nO grito dela ecoa. E, lá fora, a menina começa a rir. Uma risada profunda e distorcida.",
        "imagem": "https://placehold.co/800x400/111122/FFFFFF?text=O+Acordo+de+Teresa",
        "opcoes": [
            {"label": "Olhar para a coisa na plataforma...", "destino": "cap2_a2_1_monstro"}
        ]
    },
    "cap2_a2_1_monstro": {
        "texto": "O rosto da menina começa lentamente a se deformar. Os olhos escurecem. A boca fica larga demais.\n\nA criatura na plataforma fala com a voz da menina: *'Você me deu um nome.'*\nDepois com voz masculina: *'E uma vida.'*\nDepois... com a **sua** voz: *'Foi assim que começou.'*\n\nTeresa parece compreender. Ela olha para você: *'Você também fez um acordo. Na primeira viagem. Você pediu para esquecer.'*\n\nO celular vibra no seu bolso: **NÃO ESCUTE.**\nVocê olha para Miguel, chorando no corredor. E Teresa continua: *'Na estrada...'*",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=A+Criatura",
        "opcoes": [
            {"label": "Lembrar do acidente...", "destino": "cap2_a2_1_lembranca"}
        ]
    },
    "cap2_a2_1_lembranca": {
        "texto": "Uma imagem explode na sua cabeça: Chuva. Faróis. Miguel gritando. O carro rodando. Silêncio. Escuridão.\n\nVocê está preso às ferragens. Miguel imóvel ao seu lado. Uma sombra no banco traseiro pergunta: *'Você quer viver?'*\nVocê grita para salvar Miguel. A voz responde: *'Não foi isso que perguntei.'*\n\nVocê fecha os olhos, mas a lembrança continua: *'Você quer viver?'*\nE a sua própria voz responde: *'Sim.'*\n\nVocê abre os olhos no trem. Miguel olha para você: *'Pai...'* \n\nTeresa chora: *'Ele deveria ter sobrevivido. Você não o sacrificou conscientemente, mas aceitou. E ele ficou preso entre os dois destinos.'*",
        "imagem": "https://placehold.co/800x400/440000/FFFFFF?text=A+Escolha",
        "opcoes": [
            {"label": "Ouvir o alto-falante...", "destino": "cap2_a2_1_condutor"}
        ]
    },
    "cap2_a2_1_condutor": {
        "texto": "O alto-falante chia: **Próxima estação... Terminal.**\nO celular vibra freneticamente: **NÃO DEIXE ELE CHEGAR LÁ. EU SOU VOCÊ. SE ELE ATRAVESSAR, NÓS ACABAMOS.**\n\nVocê finalmente entende: o seu 'eu do futuro' não queria salvar Miguel, queria **se salvar**.\n\nUma figura sem rosto usando uniforme ferroviário aparece no fundo do vagão. A cada passo, o rosto muda, até parar no seu. Muito mais velho. O Condutor sorri com seu rosto: *'Chegamos.'*\n\nAs portas se abrem para a noite chuvosa do acidente. O carro destruído. Sirenes ao longe. O Condutor aponta para Miguel: *'Ele atravessa... e você permanece.'*",
        "imagem": "https://placehold.co/800x400/221111/FFFFFF?text=O+Terminal",
        "opcoes": [
            {"label": "Encarar o Condutor...", "destino": "cap2_a2_1_decisao"}
        ]
    },
    "cap2_a2_1_decisao": {
        "texto": "Miguel segura sua mão: *'Eu não quero ir sem você.'*\nVocê se ajoelha: *'Talvez você precise.'*\n\nO Condutor estende a mão: *'Ou podemos fazer como antes.'* Atrás dele, dezenas de versões suas, de todas as viagens anteriores. Todas escolheram viver.\n\nTeresa sussurra: *'É assim que ele escolhe o próximo Condutor. Cada vez que você prefere sua vida à dele... fica menos humano.'*\n\nVocê entende. O homem velho não é o seu futuro. É o seu **destino** se continuar escolhendo o egoísmo.\n\nO relógio marca: **00:17**.\nPela primeira vez... os segundos começam a correr.",
        "imagem": "https://placehold.co/800x400/550000/FFFFFF?text=A+Decisao+Final",
        "opcoes": [
            {"label": "A) LEVAR MIGUEL ATÉ O TERMINAL (Desfazer o acordo e aceitar sua morte)", "destino": "final_sacrificio", "reiniciar": True},
            {"label": "B) ACEITAR O ACORDO NOVAMENTE (Impedir Miguel de atravessar e viver)", "destino": "final_egoista", "reiniciar": True}
        ]
    },
    "cena_a2_2_isca": {
        "texto": "Você segura a mão de Teresa e a impede de sair do trem, usando-a como isca para a coisa na plataforma. *'Você quer me usar como isca'*, ela ri, sem humor. *'Você sempre acha que pode ser mais inteligente que ele.'*\n\nA menina chama: *'Mãe... mais perto.'*\nTeresa para. *'Não. Minha filha morreu em 1964. E você não é ela.'*\n\nO sorriso da menina desaparece. As luzes da estação apagam, uma por uma. Resta apenas o poste acima dela. Então, seu corpo começa a crescer. Os braços se alongam. O vestido se rasga. O corpo fica alto demais. Magro demais. Impossível.",
        "imagem": "https://placehold.co/800x400/050505/FFFFFF?text=A+Criatura+Cresce",
        "opcoes": [
            {"label": "Ouvir a voz da criatura...", "destino": "cap2_a2_2_divida"}
        ]
    },
    "cap2_a2_2_divida": {
        "texto": "A criatura abre a boca, mas a voz vem dos alto-falantes do trem:\n**— PASSAGEIRA TERESA. DÍVIDA PENDENTE DESDE 1964. UMA VIDA.**\n\nTeresa chora, dizendo que tentou salvar a filha. A criatura sorri: **— E DEU OUTRA PESSOA EM TROCA. ESSA É A MENTIRA QUE ELA CONTA HÁ SESSENTA E DOIS ANOS.**\n\nAs luzes apagam. Quando voltam, a menina monstruosa sumiu. No lugar dela está VOCÊ. Mais velho. Com a cicatriz no rosto.\nO seu celular vibra: **NÃO ACREDITE NELE.**\nO homem na plataforma tira um telefone do bolso e mostra a tela para você: **NÃO ACREDITE EM MIM.**",
        "imagem": "https://placehold.co/800x400/220000/FFFFFF?text=O+Reflexo+Falso",
        "opcoes": [
            {"label": "Perguntar quem ele é...", "destino": "cap2_a2_2_funcao"}
        ]
    },
    "cap2_a2_2_funcao": {
        "texto": "O rosto da figura muda rapidamente: Daniel. Ricardo. Helena. Miguel. Teresa. E volta a ser o seu.\n*'Qual deles você prefere?'*\n\nVocê recua. *'Você é o Condutor?'*\n*'Ainda não'*, ele responde. *'Condutor é uma função. Alguém precisa manter os passageiros entre o último segundo da vida e o primeiro da morte.'*\n\nA criatura ergue os braços. As janelas do trem deixam de mostrar a estação e mostram dezenas de viagens passadas. Em uma, você ataca Miguel. Em outra, implora. Em outra... você está sentado na cabine. Conduzindo.",
        "imagem": "https://placehold.co/800x400/111133/FFFFFF?text=As+Janelas+Do+Passado",
        "opcoes": [
            {"label": "Lembrar do acidente...", "destino": "cap2_a2_2_memoria"}
        ]
    },
    "cap2_a2_2_memoria": {
        "texto": "A estrada. O acidente. Você preso no carro. Miguel ao lado. Uma voz pergunta: *'Você quer viver?'*\nVocê fecha os olhos: *'Não.'*\nA memória continua: *'Sim.'*\n\nVocê abre os olhos no trem. Miguel diz: *'Pai?'*. A memória voltou. Você percebe que deixou o menino aqui, preso entre a vida e a morte, em todas as viagens.\n\nA voz da entidade fica suave, quase humana: *'Humanos fazem coisas extraordinárias quando percebem que vão morrer.'*\nO alto-falante chia: **Próxima estação... Terminal.**\nO cenário da plataforma muda para a exata cena do acidente, paralisada no tempo.",
        "imagem": "https://placehold.co/800x400/331100/FFFFFF?text=O+Terminal",
        "opcoes": [
            {"label": "Olhar para o homem velho...", "destino": "cap2_a2_2_decisao"}
        ]
    },
    "cap2_a2_2_decisao": {
        "texto": "A entidade sorri: *'Basta ele atravessar. Ele volta, e você finalmente termina de morrer.'*\n\nSeu celular vibra: **NÃO FAÇA ISSO. NÓS CONSEGUIMOS SAIR DE NOVO.**\nVocê olha para trás. O homem velho agora está DENTRO do vagão. *'Eu sobrevivi'*, diz a sua versão egoísta, cujas roupas estão se transformando lentamente no uniforme do ferroviário.\n\nTeresa sussurra: *'Esta é sua última viagem. Na próxima, não haverá mais diferença entre vocês.'*\n\nO painel apaga e acende com a mensagem final:\n**SUBSTITUIÇÃO DO CONDUTOR DISPONÍVEL. ACEITAR?**",
        "imagem": "https://placehold.co/800x400/550000/FFFFFF?text=A+Decisao+Final",
        "opcoes": [
            {"label": "A) SOLTAR O PASSADO E LEVAR MIGUEL (Aceitar sua morte e salvar o menino)", "destino": "final_sacrificio", "reiniciar": True},
            {"label": "B) PEGAR A MÃO DO SEU EU MAIS VELHO (Recusar a morte e virar o Condutor)", "destino": "final_egoista", "reiniciar": True}
        ]
    },

    "final_sacrificio": {
        "texto": "Miguel segura sua mão. Do outro lado da porta, a estrada permanece congelada no instante do acidente. Chuva suspensa no ar. O Condutor estende a mão: *'Ainda dá tempo.'*\n\nVocê olha para aquela versão velha de si mesmo. O celular vibra: **NÃO FAÇA ISSO. VOCÊ NÃO SABE O QUE EXISTE DEPOIS.**\n\nVocê sorri tristemente e guarda o telefone.\n— *Esse sempre foi o problema. Eu tive medo demais de descobrir.*",
        "imagem": "https://placehold.co/800x400/111122/FFFFFF?text=O+Medo+De+Descobrir",
        "opcoes": [
            {"label": "Olhar para Miguel...", "destino": "final_sacrificio_2"}
        ]
    },
    "final_sacrificio_2": {
        "texto": "Agora você lembra de tudo. O primeiro passo. A bicicleta. Miguel pedindo para você não ir. Você se ajoelha diante do seu filho.\n\n— *Eu deveria ter protegido você naquela noite. O acidente foi um acidente. O que veio depois não.*\n\nVocê segura o rosto dele. Teresa observa de longe, chorando. Daniel e Ricardo permanecem em silêncio.\n— *Eu fiz uma escolha porque estava com medo. E você pagou por ela. Não vai pagar de novo.*",
        "imagem": "https://placehold.co/800x400/223344/FFFFFF?text=A+Despedida",
        "opcoes": [
            {"label": "Levantar-se e encarar o Condutor...", "destino": "final_sacrificio_3"}
        ]
    },
    "final_sacrificio_3": {
        "texto": "O Condutor avisa, irritado: *'Você não sabe o que acontece quando atravessar. Você deixa de existir.'*\nVocê olha para a estrada: *'Não. Eu termino.'*\n\nAs luzes piscam. As paredes do trem vibram. Dezenas de versões suas aparecem refletidas nas janelas, batendo no vidro e implorando:\n— *NÃO FAZ ISSO! VOCÊ VAI MATAR TODOS NÓS!*\n\nElas não são fantasmas. São restos de decisões egoístas que só continuam existindo se o ciclo continuar. Você olha para elas.\n— *Desculpa.*\n\nVocê segura a mão de Miguel e atravessa.",
        "imagem": "https://placehold.co/800x400/331111/FFFFFF?text=O+Fim+Do+Ciclo",
        "opcoes": [
            {"label": "Ouvir o som do impacto...", "destino": "final_sacrificio_4"}
        ]
    },
    "final_sacrificio_4": {
        "texto": "No instante em que seu pé toca a estrada... o mundo volta a se mover. A chuva cai. A buzina explode. Metal se contorce.\n\nEscuridão. Depois, luzes, sirenes, homens correndo. *'Temos pulso! Retira a criança primeiro!'*\nMiguel abre os olhos no asfalto. Um socorrista segura seu rosto. Miguel procura por você, desesperado. Mas a resposta é apenas um lençol sendo colocado sobre o banco do motorista.\n\nAo lado da estrada, um relógio digital muda. **00:17... 00:18**.\n\nNo trem, Teresa olha para o painel. Pela primeira vez em sessenta e dois anos... ele também muda. **00:18**. As luzes dos vagões se apagam lentamente.",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=00:18",
        "opcoes": [
            {"label": "Anos depois...", "destino": "final_sacrificio_epilogo"}
        ]
    },
    "final_sacrificio_epilogo": {
        "texto": "Miguel está adulto. Encontra a fotografia da família. No verso: *'Volto antes da meia-noite.'*\n\nEle escuta um trem. Sem trilhos, sem fazer barulho, uma composição antiga atravessa lentamente a rua lá fora. Na última janela, há alguém sentado. Você. Com a mesma idade da noite do acidente. Em paz.\n\nVocê sorri e acena. Miguel acena de volta. O trem desaparece na escuridão. O celular dele acende sobre a mesa: **00:18**. Nenhuma mensagem.\n\nMuito longe, um alto-falante chia. Uma voz quase inaudível anuncia:\n— *Passageiro liberado.*\n\n**FINAL: O SACRIFÍCIO**\n*Você finalmente chegou ao minuto seguinte.*",
        "imagem": "https://placehold.co/800x400/001100/FFFFFF?text=PASSAGEIRO+LIBERADO",
        "opcoes": [
            {"label": "🎬 Investigar outra linha do tempo (Jogar Novamente)", "destino": "cap1_parte1", "reiniciar": True}
        ]
    },
    "final_egoista": {
        "texto": "A estrada está diante de vocês. A morte esperando. O Condutor estende a mão. O celular vibra: **NÓS CONSEGUIMOS SAIR DE NOVO.**\n\nVocê olha para o próprio cadáver no carro e sente o mesmo terror de todas as outras vezes. *'Eu não consigo'*, você sussurra. Você solta a mão de Miguel.\n\n*'Pai, por favor!'* A criança tenta agarrar você, mas você o empurra para trás. As portas se fecham entre vocês. Miguel bate no vidro, desesperado: *'VOCÊ PROMETEU!'*\n\nA plataforma desaparece. A voz dele some na escuridão: *'Você prometeu voltar...'*",
        "imagem": "https://placehold.co/800x400/110000/FFFFFF?text=A+Traicao",
        "opcoes": [
            {"label": "Acordar...", "destino": "final_egoista_2"}
        ]
    },
    "final_egoista_2": {
        "texto": "Você desperta com violência. Luz branca. *'Temos pulso!'*\n\nVocê sobreviveu. O médico se aproxima no hospital. Você pergunta por Miguel. O médico hesita e baixa os olhos. Você entende.\n\nOs anos passam. Você muda de cidade, evita trens, envelhece consumido pela culpa. Uma cirurgia tardia deixa uma cicatriz familiar atravessando sua sobrancelha direita.\n\nDécadas depois. Chove lá fora. Você está sozinho em casa. O relógio marca **00:16**. Três batidas soam na sua janela. *TOC. TOC. TOC.*",
        "imagem": "https://placehold.co/800x400/222222/FFFFFF?text=Os+Anos+Passam",
        "opcoes": [
            {"label": "Olhar o celular vibrar...", "destino": "final_egoista_3"}
        ]
    },
    "final_egoista_3": {
        "texto": "Não existe número, apenas um nome na tela: **MIGUEL**.\n\n**VOCÊ PROMETEU VOLTAR.**\n**PAI?**\n**ESTOU ESPERANDO.**\n\nVocê atira o telefone no chão. O relógio muda para **00:17**. Escuridão total. O som de metal contra metal invade a sala.\n\nAs luzes acendem. Você não está em casa. Está sentado em uma cabine estreita, cheia de manômetros e alavancas. No vidro à frente, seu reflexo exibe o rosto com a cicatriz. O rosto da plataforma.\n\nA voz da entidade sussurra atrás de você: *'Toda vida devolvida precisa ser cobrada. Você não foi escolhido. Você se ofereceu.'*",
        "imagem": "https://placehold.co/800x400/1a1a3a/FFFFFF?text=A+Cabine",
        "opcoes": [
            {"label": "Olhar para o banco ao lado...", "destino": "final_egoista_4"}
        ]
    },
    "final_egoista_4": {
        "texto": "Miguel, ainda com nove anos, molhado e com sangue seco no rosto, está sentado ali.\n*'Agora posso ir embora?'*, ele pergunta.\n\nA porta da cabine se abre para uma luz branca. Miguel se levanta. *'Dessa vez é você que fica.'* Ele atravessa e a porta se fecha.\n\nO painel muda: **PASSAGEIRO MIGUEL: LIBERADO.**\n\nO microfone liga sozinho. A sombra atrás de você ordena que anuncie a próxima estação. Seu reflexo perde a humanidade, restando apenas olhos negros. Você pega o microfone, com uma voz distorcida, e diz: *'Próxima estação... Santa Lúcia.'*",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=A+Substituicao",
        "opcoes": [
            {"label": "Olhar pela janela do trem...", "destino": "final_egoista_5"}
        ]
    },
    "final_egoista_5": {
        "texto": "Na plataforma, você vê a mulher, o policial, a velha, a criança e... VOCÊ. Mais jovem. Acabando de acordar.\n\nVocê acompanha o trem, bate no vidro e grita *'NÃO DESÇA!'*, percebendo finalmente que o homem velho nunca foi o seu futuro, mas você mesmo. Condenado.\n\nVocê sente um celular no bolso da farda de ferroviário. Uma mensagem pronta: **NÃO DEIXE A CRIANÇA CHEGAR À ESTAÇÃO FINAL.**\nVocê hesita. Poderia dizer a verdade... mas vê Miguel no trem. O medo egoísta vence de novo. Você aperta ENVIAR.\n\nO relógio da cabine volta para: **00:16**.\nNo painel: **CONDUTOR. VIAGEM 13 INICIADA.**\n\n**FINAL: O CONDUTOR**\n*Algumas pessoas têm medo de morrer. Outras fazem do medo uma eternidade.*",
        "imagem": "https://placehold.co/800x400/110000/FFFFFF?text=VIAGEM+13+INICIADA",
        "opcoes": [
            {"label": "🎬 Iniciar a Viagem 13 (Jogar Novamente)", "destino": "cap1_parte1", "reiniciar": True}
        ]
    },

    # ===============================
    # LINHA B (REGRAS / OS MORTOS)
    # ===============================
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
    "cena_b1_obedecer": {
        "texto": "Você recua. Não olha novamente para a figura sentada no seu antigo lugar. Teresa segura seu braço: *'Isso. Não reconheça.'*\n\n— *Eu obedeci. Agora você vai falar.* — você diz. Desde que acordou, ela só impõe proibições. Teresa hesita, mas acaba cedendo e enumerando as regras que protegem os passageiros.\n\n— *Primeira: se alguém do lado de fora souber seu nome, não olhe, porque chama aquilo que você ainda acredita ser. Segunda: nunca desembarque onde alguém o espera, porque morto nenhum deveria estar esperando outro morto...*",
        "imagem": "https://placehold.co/800x400/112233/FFFFFF?text=As+Regras+Dos+Mortos",
        "opcoes": [
            {"label": "Questionar a palavra 'morto'...", "destino": "cap2_b1_ricardo"}
        ]
    },
    "cap2_b1_ricardo": {
        "texto": "Você trava ao ouvir 'outro morto'. Ricardo também ouve e entra em pânico. Teresa tenta contornar, mas faz Ricardo lembrar de seu plantão e de sua viatura.\n\nUma imagem violenta atravessa a mente do policial. As luzes apagam. O som de metal retorcido, vidro quebrado e uma buzina ecoam na escuridão. Quando as luzes voltam, Ricardo está limpo de novo, mas a verdade foi revelada: as regras impedem que os mortos lembrem de suas mortes antes de estarem prontos.",
        "imagem": "https://placehold.co/800x400/331111/FFFFFF?text=A+Memoria+De+Ricardo",
        "opcoes": [
            {"label": "Encarar a cópia e Teresa...", "destino": "cap2_b1_arquivo"}
        ]
    },
    "cap2_b1_arquivo": {
        "texto": "A cópia atrás de você zomba com a sua voz: *'Primeiro esquece como morreu. Depois esquece quem amava. Depois esquece o próprio nome... até sobrar só a vontade de continuar.'*\n\nTeresa revela que a criatura é o **Passageiro 007**, um arquivo daqueles que ficaram tempo demais e começaram a roubar voz, rosto e memórias dos outros.\n\nVocê percebe que Teresa nunca respirou cansada, nunca soltou vapor de frio. *'Há quanto tempo você está nesse trem?'*\nEla sussurra: *'Tempo suficiente. Desde antes de você nascer.'*",
        "imagem": "https://placehold.co/800x400/221122/FFFFFF?text=O+Passageiro+007",
        "opcoes": [
            {"label": "Exigir saber a sétima regra...", "destino": "cap2_b1_restauracao"}
        ]
    },
    "cap2_b1_restauracao": {
        "texto": "A cópia insiste para que Teresa revele a última regra. Sob pressão, Teresa confessa: *'A sétima regra não serve para proteger vocês. É para proteger o trem. De quê? De nós.'*\n\nSe muitos passageiros lembrarem ao mesmo tempo, o trem não consegue mantê-los separados de suas mortes. Fora do vagão, dezenas de vozes começam a chamar e a bater nas portas. *'Mãe... Filho... Me ajuda...'* \n\nO alto-falante chia: **NÍVEL DE CONSCIÊNCIA ACIMA DO PERMITIDO. RESTAURAÇÃO NECESSÁRIA.** As luzes ficam vermelhas. Os nomes dos passageiros piscam na tela até parar em um só: **VOCÊ**.",
        "imagem": "https://placehold.co/800x400/550000/FFFFFF?text=Restauracao+Necessaria",
        "opcoes": [
            {"label": "Ver a contagem regressiva...", "destino": "cap2_b1_decisao"}
        ]
    },
    "cap2_b1_decisao": {
        "texto": "O trem freia violentamente. O painel muda:\n**RESTAURAÇÃO EM 60 SEGUNDOS**\n**00:59... 00:58...**\n\nTeresa segura você: *'Precisamos escolher agora.'*\nA cópia sussurra atrás de você: *'Ou pode finalmente perguntar quem escreveu as regras. Porque ela nunca contou a parte mais importante: alguém está do outro lado delas.'*\n\nO cronômetro avança: **00:30**.",
        "imagem": "https://placehold.co/800x400/770000/FFFFFF?text=00:30",
        "opcoes": [
            {"label": "B1.1) Continuar obedecendo Teresa e exigir a sétima regra", "destino": "cena_b1_1_regra", "ganha_memoria": "obedeceu_teresa_fim"},
            {"label": "B1.2) Exigir saber quem criou as regras e confrontar a origem", "destino": "cena_b1_2_recusa", "ganha_memoria": "questionou_criador"}
        ]
    },
    "cena_b1_1_regra": {
        "texto": "O painel pisca em vermelho: **RESTAURAÇÃO EM 00:30**. Você exige que Teresa cumpra sua parte e revele a sétima regra.\n\nCom a voz trêmula, Teresa confessa:\n— *A sétima regra diz o que fazer quando a Restauração escolhe alguém: não tente salvá-lo, não diga o nome dele, não toque nele e, quando terminar... finja que ele nunca existiu.*\n\nO relógio do vagão para de contagem regressiva e trava exatamente em **00:17**. As luzes ficam vermelhas e o alto-falante anuncia: **RESTAURAÇÃO INICIADA**.",
        "imagem": "https://placehold.co/800x400/550000/FFFFFF?text=A+Setima+Regra",
        "opcoes": [
            {"label": "Descobrir o que é o Passageiro 007...", "destino": "cap2_b1_1_007"}
        ]
    },
    "cap2_b1_1_007": {
        "texto": "Teresa revela que o trem restaura os passageiros quando eles começam a lembrar demais, apagando lembranças, nomes e rostos para mantê-los na negação de que estão mortos. \n\nA cópia se levanta, mudando de rosto constantemente — homens, crianças, idosos — e diz: *'Não existe um único Passageiro 007. Nós somos o que restou de todos aqueles que o trem apagou. O medo, a culpa, a vontade de continuar existindo.'*\n\nO painel exibe: **PASSAGEIRO SELECIONADO: VOCÊ**. A Fase 1 da Identidade começa.",
        "imagem": "https://placehold.co/800x400/220000/FFFFFF?text=O+Passageiro+007",
        "opcoes": [
            {"label": "Enfrentar a perda de identidade...", "destino": "cap2_b1_1_esquecimento"}
        ]
    },
    "cap2_b1_1_esquecimento": {
        "texto": "A dor de cabeça é súbita. Você olha para Miguel, mas por alguns segundos esquece seu próprio sobrenome. Ricardo, Daniel e a mulher na janela começam a perder o reconhecimento de quem você é.\n\nTeresa puxa um caderno velho com centenas de nomes de pessoas que ela anotou ao longo de décadas para não esquecer. Entre as páginas, o seu próprio nome aparece dezenas de vezes, sempre datado às **00:17**.\n\nTeresa confessa a verdade final: *'Nas primeiras viagens... você não tentava sair. Você tentava entrar para encontrar alguém. Mas o nome dessa pessoa desapareceu.'*",
        "imagem": "https://placehold.co/800x400/111122/FFFFFF?text=O+Caderno+De+Teresa",
        "opcoes": [
            {"label": "Ouvir a revelação sobre a Restauração...", "destino": "cap2_b1_1_verdade"}
        ]
    },
    "cap2_b1_1_verdade": {
        "texto": "O painel marca **IDENTIDADE: 5%**. O 007 está ficando totalmente sólido, assumindo perfeitamente seu rosto e sua voz, enquanto você desbota.\n\nVocê percebe a verdade terrível: **Cada pessoa restaurada alimenta o Passageiro 007**, tornando-o maior e mantendo-o existente. Teresa chorando percebe que, ao obedecer à sétima regra por sessenta anos, ela estava apenas alimentando o monstro.\n\nAo seu redor, os outros passageiros começam a se lembrar de que morreram. Ricardo sangra de novo. A mulher grita. As janelas racham e vozes de milhares de mortos ecoam de fora.",
        "imagem": "https://placehold.co/800x400/770000/FFFFFF?text=Alimentando+O+Monstro",
        "opcoes": [
            {"label": "B1.1-A) Obedecer à Sétima Regra (Aceitar a Restauração e virar 007)", "destino": "final_b1_obedecer", "reiniciar": True},
            {"label": "B1.1-B) Quebrar a Sétima Regra (Acordar todos os mortos e colapsar o trem)", "destino": "final_b1_quebrar", "reiniciar": True}
        ]
    },
    "final_b1_obedecer": {
        "texto": "Você para de lutar. A cópia estende a mão com um sorriso acolhedor: *'Não dói por muito tempo.'*\n\nVocê permite que a Restauração termine. Sua identidade se desfaz completamente. Suas lembranças evaporam. Os passageiros esquecem que você existiu. E o que restou de você passa a integrar o corpo do Passageiro 007, tornando a entidade mais forte para a próxima viagem.\n\nO trem continua correndo pela escuridão eterna, embalando os mortos em sua doce negação.\n\n**FINAL: O NOVO 007**\n*Algumas regras existem para proteger o esquecimento.*",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=O+Novo+007",
        "opcoes": [
            {"label": "🎬 Explorar outra linha do tempo (Jogar Novamente)", "destino": "cap1_parte1", "reiniciar": True}
        ]
    },
    "final_b1_quebrar": {
        "texto": "Você recua da Restauração. Teresa abandona as regras e ajuda a fazer todos os passageiros lembrarem de suas mortes simultaneamente.\n\nO trem entra em colapso total. O painel grita: **CONTENÇÃO DO TREM: FALHA**. As portas de todos os vagões destravam ao mesmo tempo. O alto-falante anuncia: **OS MORTOS ESTÃO ACORDANDO**.\n\nDo lado de fora, milhares de braços e vozes batem nas janelas. As amarras do trem se despedaçam e, pela primeira vez em séculos, os passageiros cruzam o véu para o que existe de verdade do outro lado.\n\n**FINAL: A QUEDA DO TREM**\n*A negação chegou ao fim.*",
        "imagem": "https://placehold.co/800x400/220033/FFFFFF?text=Os+Mortos+Acordando",
        "opcoes": [
            {"label": "🎬 Explorar outra linha do tempo (Jogar Novamente)", "destino": "cap1_parte1", "reiniciar": True}
        ]
    },
    "cena_b1_2_recusa": {
        "texto": "Você se recusa a aceitar as regras cegamente e exige saber quem as criou. Teresa tenta impedi-lo, mas a cópia zomba: *'Essa é uma pergunta muito melhor.'*\n\nSob pressão, Teresa confessa que foi ela quem escreveu as regras após fazer um pacto em 1964 para salvar sua filha que estava morrendo. Mas ao ser questionada sobre quem as ditou, ela aponta para o teto e sussurra: *'O Condutor.'*",
        "imagem": "https://placehold.co/800x400/221122/FFFFFF?text=Quem+Escreveu+As+Regras",
        "opcoes": [
            {"label": "Abrir a porta da Cabine do Condutor...", "destino": "cap2_b1_2_cabine"}
        ]
    },
    "cap2_b1_2_cabine": {
        "texto": "Uma porta de metal negro sem janela surge na frente do vagão com os dizeres: **CABINE DO CONDUTOR**. A fechadura gira sozinha.\n\nVocê entra e encontra apenas uma cadeira e um livro de couro antigo: **REGULAMENTO DE PASSAGEIROS**. Ao abrir, você descobre que todas as regras foram assinadas pela mesma pessoa. Ao comparar com o documento na sua carteira, você percebe, horrorizado, que **a assinatura é a sua**.",
        "imagem": "https://placehold.co/800x400/110000/FFFFFF?text=A+Assinatura",
        "opcoes": [
            {"label": "Encarar o seu eu mais velho...", "destino": "cap2_b1_2_velho"}
        ]
    },
    "cap2_b1_2_velho": {
        "texto": "A cadeira não está mais vazia. Uma versão sua muito mais velha, com a cicatriz e o uniforme de ferroviário, está sentada nela. *'Você estava sentado onde está agora'*, ele diz.\n\nEle mostra a janela da cabine. Fora dali, existem milhares de trens. Alguns sem Condutor, onde os passageiros lembram que morreram, entram em colapso e se fundem em massas disformes — as origines reais do Passageiro 007.\n\nO velho explica: *'As regras impedem que os mortos percam a identidade, mas também os impedem de partir. Sem passageiros não há trem, e sem trem não existe Condutor. O Condutor não é uma pessoa... é a parte de cada morto que diz: Ainda não.'*",
        "imagem": "https://placehold.co/800x400/331111/FFFFFF?text=O+Velho+Condutor",
        "opcoes": [
            {"label": "Ouvir o desaparecimento e a escolha...", "destino": "cap2_b1_2_decisao"}
        ]
    },
    "cap2_b1_2_decisao": {
        "texto": "O velho desaparece, deixando apenas o uniforme e o boné na cadeira. O painel cancela a Restauração e exibe o **PROTOCOLO DE SUBSTITUIÇÃO**.\n\nVocê tem duas opções definitivas: **Manter o Sistema** (assumindo o cargo de Condutor para manter os mortos anestesiados e contidos pelas regras) ou **Encerrar o Sistema** (rasgar o Regulamento e fazer todos os passageiros lembrarem de sua morte de uma vez por todas, colapsando o trem).\n\nAté o Passageiro 007 parece aterrorizado com a segunda opção.",
        "imagem": "https://placehold.co/800x400/550000/FFFFFF?text=Protocolo+De+Substituicao",
        "opcoes": [
            {"label": "B1.2-A) Assumir o lugar do Condutor (Manter as regras e o trem funcionando)", "destino": "final_b1_2_condutor", "reiniciar": True},
            {"label": "B1.2-B) Destruir as regras (Rasgar o regulamento e acordar todos os mortos)", "destino": "final_b1_2_destruir", "reiniciar": True}
        ]
    },
    "final_b1_2_condutor": {
        "texto": "Você veste o uniforme e senta na cadeira de comando. Aceita que as regras, por mais cruéis que sejam, evitam o colapso dos mortos.\n\nOs passageiros continuarão esquecendo. O 007 continuará contido. Mas você ficará sozinho na cabine, eternamente consciente, sabendo que todos ali estão mortos, vigiando o eterno vai e vem entre estações.\n\n**FINAL: O NOVO CONDUTOR**\n*Você se tornou o 'Ainda não' de todos os outros.*",
        "imagem": "https://placehold.co/800x400/050505/FFFFFF?text=O+Novo+Condutor",
        "opcoes": [
            {"label": "🎬 Explorar outra linha do tempo (Jogar Novamente)", "destino": "cap1_parte1", "reiniciar": True}
        ]
    },
    "final_b1_2_destruir": {
        "texto": "Você recusa o cargo e rasga o Regulamento de Passageiros. Contenção falha. A Restauração cessa e todos os passageiros nos milhares de trens ao redor recuperam as memórias simultaneamente.\n\nAs amarras se quebram. O 007 desmancha-se em gritos e o trem deixa de existir como uma prisão. Milhares de vozes cruzam o véu dizendo: *'Eu lembro. Eu morri.'*\n\nAs regras acabaram. O medo foi encarado. E, pela primeira vez, os passageiros finalmente puderam partir.\n\n**FINAL: O FIM DA LINHA**\n*A negação terminou. A viagem chegou ao fim.*",
        "imagem": "https://placehold.co/800x400/220033/FFFFFF?text=O+Fim+Da+Linha",
        "opcoes": [
            {"label": "🎬 Explorar outra linha do tempo (Jogar Novamente)", "destino": "cap1_parte1", "reiniciar": True}
        ]
    },
    "cena_b2_quebrar": {
        "texto": "Você ignora Teresa e dá o primeiro passo na direção da figura. Você não quer dizer o seu nome, só quer ver o rosto dela.\n\nMas, quando você avança... a figura fala sem se virar, usando a sua exata voz:\n\n— *Você sempre chega mais perto. Foi assim que eu entrei da primeira vez.*\n\nTeresa empalidece. — *Não escute.*\n\nA figura começa a virar o rosto lentamente e diz:\n— *Pergunta para ela o que aconteceu com os outros seis.*",
        "imagem": "https://placehold.co/800x400/331111/FFFFFF?text=Os+Outros+Seis",
        "opcoes": [
            {"label": "Encarar a figura...", "destino": "cap2_entidade_revela"}
        ]
    },
    "cap2_entidade_revela": {
        "texto": "Você se aproxima e olha nos olhos da cópia. No instante em que o reconhecimento é mútuo, algo terrível acontece.\n\nA entidade não ataca você com violência. Ela começa a **roubar**. Primeiro o rosto, depois o timbre da voz, as lembranças, o jeito de respirar. Cada segundo que passa torna a cópia mais real, mais vívida... enquanto você começa a desbotar, tornando-se uma silhueta borrada.\n\nMiguel olha da cópia para você, completamente perdido, sem saber qual de vocês é o verdadeiro pai. O horror se instala: o 007 não precisa matar você. Ele só precisa fazer com que todos acreditem que ele é você.",
        "imagem": "https://placehold.co/800x400/110000/FFFFFF?text=O+Roubo+De+Identidade",
        "opcoes": [
            {"label": "B2.1) Tentar provar aos passageiros que você é o verdadeiro", "destino": "cena_b2_1_provar", "ganha_memoria": "tentou_provar"},
            {"label": "B2.2) Parar de disputar a identidade e seguir a cópia", "destino": "cena_b2_2_seguir", "ganha_memoria": "seguiu_copia"}
        ]
    },
    "cena_b2_1_provar": {
        "texto": "Você tenta provar quem é, citando lembranças que só você tem. Mas a cópia usa a mesma voz, com os mesmos detalhes exatos.\n\nDaniel franze a testa: *'Ambos sabem das mesmas coisas.'* Miguel recua, aterrorizado com os dois rostos idênticos. O trem inteiro começa a tratar você como o intruso, enquanto a cópia assume seu lugar por completo.",
        "imagem": "https://placehold.co/800x400/330000/FFFFFF?text=Quem+E+O+Verdadeiro",
        "opcoes": [
            {"label": "Ver o desate da sua identidade...", "destino": "final_b2_perdeu", "reiniciar": True}
        ]
    },
    "cena_b2_2_seguir": {
        "texto": "Você desiste de lutar pela máscara. Se a entidade quer ser você, que carregue o peso disso. Você se vira e decide segui-la até o fundo do vagão, rumo ao escuro de onde ela veio.\n\nTeresa grita para você voltar, mas as portas se abrem para um silêncio absoluto.",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=Seguindo+A+Copia",
        "opcoes": [
            {"label": "Atravessar para o desconhecido...", "destino": "final_b2_seguiu", "reiniciar": True}
        ]
    },
    "final_b2_perdeu": {
        "texto": "Ninguém mais reconhece você. O trem o silencia como uma anomalia e a cópia assume sua vida dentro do vagão.\n\n**FINAL: O INTRUSO**\n*Quando você perde o seu rosto, o mundo esquece que você existiu.*",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=O+Intruso",
        "opcoes": [
            {"label": "🎬 Explorar outra linha do tempo (Jogar Novamente)", "destino": "cap1_parte1", "reiniciar": True}
        ]
    },
    "final_b2_seguiu": {
        "texto": "Você caminha junto à sua cópia para dentro da escuridão dos trilhos, aceitando que a identidade nunca foi fixa.\n\n**FINAL: ALÉM DO ESPELHO**\n*O reflexo tornou-se o dono do caminho.*",
        "imagem": "https://placehold.co/800x400/111122/FFFFFF?text=Alem+Do+Espelho",
        "opcoes": [
            {"label": "🎬 Explorar outra linha do tempo (Jogar Novamente)", "destino": "cap1_parte1", "reiniciar": True}
        ]
    },

    # ===============================
    # LINHA C (CRIANÇA / ACIDENTE)
    # ===============================
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
        "texto": "Sob a luz, você reconhece Helena. Ela sorri: *'Você finalmente lembrou de mim. Está com medo?'*\n\nDaniel faz a pergunta que gela seu sangue: *'A pergunta é: quem morreu naquela estrada?'*\n\nHelena começa a rir baixo, um som que não combina com ela. Miguel hesita. Então você percebe algo impossível: Helena está descalça sobre o chão molhado, mas **não produz reflexo nas poças**.\n\nTeresa sussurra: *'Agora escolha.'*",
        "imagem": "https://placehold.co/800x400/220000/FFFFFF?text=O+Reflexo+Ausente",
        "opcoes": [
            {"label": "C1) Proteger Miguel e obrigar Daniel a revelar a verdade", "destino": "cena_c1_acidente", "ganha_memoria": "investigou_daniel"},
            {"label": "C2) Confiar na memória e soltar Miguel para a mãe", "destino": "cena_c2_plataforma", "ganha_memoria": "confiou_helena"}
        ]
    },
    "cena_c1_acidente": {
        "texto": "Você puxa Miguel para trás. A mulher na plataforma é Helena... ou pelo menos usa o rosto dela. Mas os pés não refletem nas poças do chão. Daniel se aproxima e começa a contar a verdade daquela noite chuvosa de estrada.\n\nUma chuva forte começa a cair *dentro* do vagão. O cheiro de asfalto molhado e borracha queimada toma o ar. A memória do acidente invade o espaço. Daniel confirma: seu carro perdeu o controle, vocês bateram, e naquela noite fria... você morreu no banco do motorista.",
        "imagem": "https://placehold.co/800x400/111133/FFFFFF?text=A+Noite+Do+Acidente",
        "opcoes": [
            {"label": "Enfrentar a memória do acordo...", "destino": "cap2_c1_acordo"}
        ]
    },
    "cap2_c1_acordo": {
        "texto": "Na memória que toma conta do vagão, você ouve a voz na escuridão às **00:17**: *'Você quer viver?'*\n\nVocê lembra de ter respondido que sim, e o milagre aconteceu: seus ferimentos sumiram, mas as marcas e a morte recaíram sobre Miguel. Daniel revela a verdade brutal: Helena não estava no carro naquela noite. Ela sobreviveu. O que está na plataforma usando o rosto dela não é sua esposa, mas uma criatura faminta por completar a troca.\n\nO painel exibe: **VIDA DEVOLVIDA: 1 | VIDA PENDENTE: 1**.",
        "imagem": "https://placehold.co/800x400/331111/FFFFFF?text=O+Acordo+Original",
        "opcoes": [
            {"label": "Ver a escolha final da Linha C1...", "destino": "cap2_c1_decisao"}
        ]
    },
    "cap2_c1_decisao": {
        "texto": "O painel pulsa em **00:17**. A estrada surge do outro lado das portas do trem, congelada no instante original.\n\nTeresa e Daniel alertam sobre os perigos: se você entrar na lembrança, Miguel terá que reviver a própria morte. Se apagar a memória para protegê-lo, a criatura vence usando o esquecimento, como fez das outras vezes.\n\nMiguel olha para você com lágrimas nos olhos e diz: *'Não esquece de mim de novo. Foi assim que ela ganhou da última vez.'*",
        "imagem": "https://placehold.co/800x400/550000/FFFFFF?text=A+Escolha+Final+C1",
        "opcoes": [
            {"label": "C1.1) Lembrar até o fim (Entrar na lembrança e confrontar o acordo)", "destino": "final_c1_lembrar", "reiniciar": True},
            {"label": "C1.2) Proteger Miguel e apagar a memória (Recusar o passado para salvar o garoto)", "destino": "final_c1_apagar", "reiniciar": True}
        ]
    },
    "final_c1_lembrar": {
        "texto": "Você aceita mergulhar de volta no instante exato do acidente, revivendo a escolha que condenou seu filho. Ao confrontar o Condutor conscientemente na lembrança, o pacto de egoísmo é desfeito.\n\nA ilusão do trem estilhaça. A negação se quebra e a verdadeira noite da estrada absorve o impacto. Você e Miguel finalmente atravessam para o lado de lá, encarando as consequências reais daquela escolha, mas livres da prisão infinita.\n\n**FINAL: A VERDADE DA ESTRADA**\n*O passado não pode ser desfeito, mas pode deixar de ser uma mentira.*",
        "imagem": "https://placehold.co/800x400/220033/FFFFFF?text=A+Verdade+Da+Estrada",
        "opcoes": [
            {"label": "🎬 Explorar outra linha do tempo (Jogar Novamente)", "destino": "cap1_parte1", "reiniciar": True}
        ]
    },
    "final_c1_apagar": {
        "texto": "Você recusa a dor de reviver o acidente e opta por apagar as memórias, protegendo Miguel de sofrer a morte de novo.\n\nAs lembranças se esvaem como fumaça, e a falsa Helena na plataforma desaparece na escuridão. O trem continua sua viagem silenciosa pelas trevas, e você abraça seu filho no banco do vagão, ignorando o que aconteceu no mundo real.\n\n**FINAL: O ABRAÇO NO ESCURO**\n*Algumas vezes, a ignorância é o único refúgio que resta aos mortos.*",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=O+Abraco+No+Escuro",
        "opcoes": [
            {"label": "🎬 Explorar outra linha do tempo (Jogar Novamente)", "destino": "cap1_parte1", "reiniciar": True}
        ]
    },
    "cena_c2_plataforma": {
        "texto": "Você aceita que é Helena e decide soltá-lo. Mas pensa em fazer uma única pergunta que só sua verdadeira esposa saberia.\n\nHelena sorri antes mesmo de você abrir a boca e diz: — A porta vermelha.\n\nSeu sangue esfria. Era exatamente o que você ia perguntar. Daniel sussurra: *'Ela está dentro da sua cabeça.'*\n\nDo lado de fora, Helena abre os braços para Miguel. E atrás dela... por um único segundo... você vê alguma coisa muito alta se mover na escuridão.",
        "imagem": "https://placehold.co/800x400/220000/FFFFFF?text=A+Coisa+Na+Escuridao",
        "opcoes": [
            {"label": "Ver o que acontece a seguir...", "destino": "cap2_c2_culpa"}
        ]
    },
    "cap2_c2_culpa": {
        "texto": "Miguel cruza a porta e abraça a figura. Mas logo o corpo do garoto trava, os olhos ficam negros e a voz perde a vida. O disfarce desmorona: uma criatura escura, alta e deformada usa Helena como uma máscara. O painel avisa: **VIDA PENDENTE: 1 | VÍNCULO DE GUARDA EM PROCESSAMENTO**.\n\nA criatura revela a arma mais cruel: o esquecimento não foi causado pelo acidente. **Foi você quem pediu.** Após a morte de Miguel, incapaz de suportar a dor, você implorou: *'Tira os dois de mim.'*",
        "imagem": "https://placehold.co/800x400/440000/FFFFFF?text=O+Pedido+Original",
        "opcoes": [
            {"label": "C2.1) Atravessar a porta vermelha e recuperar a verdade (Encarar o passado e a culpa)", "destino": "final_c2_verdade", "reiniciar": True},
            {"label": "C2.2) Ficar com 'Helena' e aceitar a nova memória (Escolher a mentira e a família perfeita)", "destino": "final_c2_mentira", "reiniciar": True}
        ]
    },
    "final_c2_verdade": {
        "texto": "Você recusa a ilusão e atravessa a porta vermelha de volta à noite do acidente. Encarar a dor de ter pedido para esquecer o próprio filho rompe o domínio da entidade. \n\nA farsa da casa desmorona. A verdadeira Helena continua viva lá fora, e você, embora marcado pelo peso do que fez, liberta Miguel das amarras da culpa infinita.\n\n**FINAL: O PESO DA VERDADE**\n*A memória pode quebrar o coração, mas é a única coisa que permite o recomeço.*",
        "imagem": "https://placehold.co/800x400/220033/FFFFFF?text=O+Peso+Da+Verdade",
        "opcoes": [
            {"label": "🎬 Explorar outra linha do tempo (Jogar Novamente)", "destino": "cap1_parte1", "reiniciar": True}
        ]
    },
    "final_c2_mentira": {
        "texto": "Você para de lutar. Aceita a casa azul, o jantar quente, o sorriso de Helena e a presença de Miguel. Você escolhe a mentira que devolve tudo o que perdeu, aceitando que a ignorância é um refúgio doce contra o horror de lembrar.\n\nAs portas do trem se fecham para o mundo real, enquanto você abraça a família perfeita construída sobre a sua própria negação.\n\n**FINAL: A CASA DOS MORTOS**\n*Algumas mentiras são quentes o suficiente para congelar a alma para sempre.*",
        "imagem": "https://placehold.co/800x400/111122/FFFFFF?text=A+Casa+Dos+Mortos",
        "opcoes": [
            {"label": "🎬 Explorar outra linha do tempo (Jogar Novamente)", "destino": "cap1_parte1", "reiniciar": True}
        ]
    },

    # ===============================
    # LINHA D (FUGA / ARQUIVO)
    # ===============================
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
            {"label": "D1) Continuar investigando sua pasta (Descobrir a verdade)", "destino": "cena_d1_investigar", "ganha_memoria": "investigou_origem"},
            {"label": "D2) Abandonar o Arquivo e enfrentar a criatura", "destino": "cena_d2_enfrentar", "ganha_memoria": "enfrentou_007"}
        ]
    },
    "cena_d1_investigar": {
        "texto": "Você senta à mesa e começa a folhear a pasta do Arquivo. Relatórios de 1997, 2004, 2013... em todas as fotografias, você aparece com a mesma idade. O documento revela a verdade aterradora: **você foi devolvido 12 vezes**. Na duodécima, houve uma falha de integração. Você não é o original; você é uma reconstrução feita com material residual do Arquivo.\n\nA criatura que estava nas suas costas se vira e revela ter a cicatriz do original. Ela diz: *'Depois de tantas devoluções, ninguém mais sabe qual versão foi a primeira.'*",
        "imagem": "https://placehold.co/800x400/110000/FFFFFF?text=O+Substituto+Devolvido",
        "opcoes": [
            {"label": "Ler a carta deixada no envelope...", "destino": "cap2_d1_carta"}
        ]
    },
    "cap2_d1_carta": {
        "texto": "No fundo da pasta, você encontra um envelope escrito à mão por uma versão sua anterior: *'Não procure descobrir qual de nós é o original. Essa pergunta é a armadilha. O trem precisa que exista um verdadeiro e uma cópia para nos manter trazendo de volta. Não salve a identidade. Salve a decisão.'*\n\nA parede do Arquivo se abre, revelando dois caminhos:\n1. **A Cadeira de Devolução**: para retornar aos vivos e reconstruir a identidade usando partes do Passageiro 007.\n2. **A Porta Branca de Encerramento**: para apagar todas as instâncias do paradoxo de uma vez por todas.",
        "imagem": "https://placehold.co/800x400/330000/FFFFFF?text=Paradoxo+Consciente",
        "opcoes": [
            {"label": "D1.1) Aceitar outra devolução (Reconstruir a identidade e continuar o ciclo)", "destino": "final_d1_devolucao", "reiniciar": True},
            {"label": "D1.2) Encerrar o paradoxo (Apagar todas as versões e restaurar a linha original)", "destino": "final_d1_encerramento", "reiniciar": True}
        ]
    },
    "final_d1_devolucao": {
        "texto": "Você senta na cadeira de devolução. O Arquivo reconstrói o que restou de você usando as lembranças disponíveis e partes do Passageiro 007. Você retorna ao mundo dos vivos com um nome e uma história, mas sem nunca saber quem realmente foi.\n\nO trem continua rodando nos trilhos invisíveis, e o ciclo se recompõe para mais uma viagem.\n\n**FINAL: O CICLO COMPLETO**\n*Um nome é apenas uma máscara que usamos para esconder o vazio.*",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=O+Ciclo+Completo",
        "opcoes": [
            {"label": "🎬 Explorar outra linha do tempo (Jogar Novamente)", "destino": "cap1_parte1", "reiniciar": True}
        ]
    },
    "final_d1_encerramento": {
        "texto": "Você recusa a reconstrução e abre a porta branca. Ao acionar o encerramento, todas as versões criadas pelas devoluções — inclusive você e o Passageiro 007 — são apagadas.\n\nA realidade retorna ao instante anterior à primeira alteração: Miguel sobrevive ao acidente, o homem original morre às 00:17, e o paradoxo deixa de existir. Ninguém jamais saberá quem tomou a decisão, mas a escolha finalmente foi salva.\n\n**FINAL: FIM DO PARADOXO**\n*A identidade não importa quando a decisão certa finalmente liberta o futuro.*",
        "imagem": "https://placehold.co/800x400/220033/FFFFFF?text=Fim+Do+Paradoxo",
        "opcoes": [
            {"label": "🎬 Explorar outra linha do tempo (Jogar Novamente)", "destino": "cap1_parte1", "reiniciar": True}
        ]
    },
    "cena_d2_enfrentar": {
        "texto": "Você decide largar os papéis, farto de mentiras, e toca a maçaneta da porta para enfrentar o que quer que esteja do outro lado.\n\nMas, no instante em que sua mão aperta o metal, uma voz sussurra bem perto do seu ouvido, de dentro do próprio cômodo escuro:\n\n— *Não precisa abrir. Eu já entrei.*",
        "imagem": "https://placehold.co/800x400/550000/FFFFFF?text=Ele+Ja+Entrou",
        "opcoes": [
            {"label": "Virar-se para encarar a entidade...", "destino": "cap2_confronto_final"} 
        ]
    },
    "cap2_confronto_final": {
        "texto": "Esta cena (D2) é a última peça do quebra-cabeça que ainda precisamos escrever e fechar!\n\nA entidade finalmente vai revelar a sua verdadeira forma.",
        "imagem": "https://placehold.co/800x400/000000/FFFFFF?text=Em+Breve",
        "opcoes": [
            {"label": "Voltar ao início", "destino": "cap1_parte1", "reiniciar": True}
        ]
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

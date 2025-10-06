import streamlit as st
import pandas as pd

generos = ['POP','FUNK', 'MPB', 'FORRO', 'TRAP']

artistas = {'POP': ["Michael Jackson","Jão","Beyoncé"],
            'FUNK':["MC Hariel","MC Paiva","MC Daleste"],
            'MPB':["Anavitória","Gilberto Gil","Chico Buarque"],
            'FORRO':["Wesley Safadão","Zé Vaqueiro","João Gomes"],
            'TRAP': ["Travis Scott","Matuê","WIU"]

}
st.sidebar.title("JaoList")
st.sidebar.image('logo.png')


genero_selecionado = st.sidebar.selectbox("Selecione o Genêro da Música", generos)

if genero_selecionado:
    musica_selecionada = st.sidebar.selectbox(
        "Selecione a Música:", 
        artistas[genero_selecionado]
    )


if genero_selecionado and musica_selecionada:
    st.write(f"**Livro selecionado:** {musica_selecionada}")
    st.write(f"**Gênero:** {genero_selecionado}")
    st.title(f"{musica_selecionada}")
    st.image(f"{musica_selecionada}.png",width=500)
    # st.write(f" O artista {musica_selecionada} foi um dos maiores do genero {genero_selecionado}")


#--------------------------------------------- JÃO -----------------------------------------------------------

if genero_selecionado== "POP" and musica_selecionada == "Jão":
    st.markdown("""
## 🌟 Quem é Jão?

**Jão** (João Vitor Romania Balbino, nascido em 1994) é um cantor e compositor brasileiro, um dos maiores nomes da música pop atual no Brasil.  
Ele se destaca pelas letras intensas, emocionais e pela mistura de pop, MPB e elementos eletrônicos.

### 🎶 Principais conquistas:
- Álbuns de sucesso como **"LOBOS" (2018)**, **"ANTI-HERÓI" (2019)**, **"PIRATA" (2021)** e **"SUPER" (2023)**.  
- Turnês lotadas pelo Brasil, reunindo milhares de fãs.  
- Reconhecido por transformar sentimentos pessoais em músicas que tocam o público.  

### 🏆 Legado
Jão representa uma nova geração da música brasileira, trazendo autenticidade e identidade única ao pop nacional.
""")
    st.video('https://www.youtube.com/watch?v=46w_wj1hXac')

#--------------------------------------------- MICHAEL JACKSON -----------------------------------------------------------
elif genero_selecionado== "POP" and musica_selecionada == "Michael Jackson":
    st.markdown("""
## 🌟 Quem foi Michael Jackson?

Michael Jackson (1958 – 2009) foi um cantor, compositor e dançarino norte-americano, conhecido como o **"Rei do Pop"**.  
Sua carreira revolucionou a música, a dança e o entretenimento mundial, tornando-o uma das figuras mais icônicas da cultura popular.

### 🎶 Principais contribuições:
- Vendeu **milhões de discos** ao redor do mundo.  
- Criou videoclipes históricos como *Thriller*, *Beat It* e *Billie Jean*.  
- Popularizou passos de dança como o **Moonwalk**.  

### 🏆 Legado
Michael Jackson deixou uma marca eterna na música e na cultura, sendo inspiração para artistas de diversas gerações.
""")
    st.video('https://www.youtube.com/watch?v=Zi_XLOBDo_Y')
#--------------------------------------------- BEYONCE -----------------------------------------------------------

elif genero_selecionado== "POP" and musica_selecionada == "Beyoncé":
    st.markdown("""
## 🌟 Quem é Beyoncé?

**Beyoncé Giselle Knowles-Carter** (nascida em 1981) é uma cantora, compositora, atriz e produtora norte-americana, considerada uma das maiores artistas da música mundial.  
Ela é conhecida como **"Queen B"**, referência à sua influência e poder cultural.

### 🎶 Principais conquistas:
- Ex-integrante do grupo **Destiny's Child**, um dos maiores grupos femininos de todos os tempos.  
- Carreira solo marcada por álbuns de sucesso como **"Dangerously in Love" (2003)**, **"Lemonade" (2016)** e **"Renaissance" (2022)**.  
- Detentora de **mais de 30 prêmios Grammy**, sendo uma das artistas mais premiadas da história.  
- Shows icônicos, como a performance no **Coachella 2018** ("Beychella").  

### 🏆 Legado
Beyoncé é um ícone global que representa força, feminismo, ancestralidade e inovação artística, influenciando gerações inteiras de artistas e fãs.
""")
    st.video('https://www.youtube.com/watch?v=4m1EFMoRFvY')
#--------------------------------------------- MC Hariel -----------------------------------------------------------
if genero_selecionado== "FUNK" and musica_selecionada == "MC Hariel":
    st.markdown("""
## 🌟 Quem é MC Hariel?

**MC Hariel** (Hariel Denaro, nascido em 1997 em São Paulo) é um cantor e compositor de funk brasileiro, considerado um dos maiores nomes do **funk consciente**.  
Suas letras falam sobre realidade social, superação, amor e o cotidiano das periferias.

### 🎶 Principais conquistas:
- Reconhecido como um dos pioneiros do **funk consciente** moderno.  
- Sucessos como *Tem Café*, *Cracolândia*, *Maçã Verde* e *Mundo da Lua*.  
- Colaborações com artistas de diversos gêneros, expandindo o alcance do funk.  
- Shows lotados e milhões de streams nas plataformas digitais.  

### 🏆 Legado
MC Hariel é visto como voz da periferia, levando reflexões sociais através da música e mantendo viva a autenticidade do funk.
""")
    st.video('https://www.youtube.com/watch?v=O3iA0mly6io')
    #--------------------------------------------- MC Paiva -----------------------------------------------------------
elif genero_selecionado== "FUNK" and musica_selecionada == "MC Paiva":
    st.markdown("""
## 🌟 Quem é MC Paiva?

**MC Paiva** (Paiva LH, nascido em São Paulo) é um cantor e compositor de funk brasileiro, conhecido por suas letras marcantes e pelo estilo autêntico dentro do funk paulista.  
Ele se destaca principalmente na vertente do **funk consciente** e no **funk de quebrada**, trazendo histórias reais e mensagens que dialogam com a juventude das periferias.

### 🎶 Principais conquistas:
- Músicas de destaque como *Versace*, *Jordan 4*, *Imagina Nós Dois na Praia* e várias colaborações com artistas do funk.  
- Reconhecido pela habilidade de rimar de forma criativa e direta.  
- Presença forte em plataformas digitais, com milhões de views e streams.  

### 🏆 Legado
MC Paiva é uma das vozes em ascensão do funk, representando a **cultura da favela** e fortalecendo o movimento musical nas periferias do Brasil.
""")
    st.video('https://www.youtube.com/watch?v=2IGH-Xwuw-o')
   #--------------------------------------------- MC Daleste -----------------------------------------------------------
elif genero_selecionado== "FUNK" and musica_selecionada == "MC Daleste":
   st.markdown("""
## 🌟 Quem foi MC Daleste?

**MC Daleste** (Daniel Pedreira Senna Pellegrine, 1992 – 2013) foi um cantor e compositor brasileiro, considerado um dos maiores nomes do **funk paulista**.  
Ele ficou conhecido como o **"rei do funk paulista"**, por suas músicas de grande impacto e letras que misturavam **romance, ostentação e realidade de quebrada**.

### 🎶 Principais conquistas:
- Sucessos como *Mina de Vermelho*, *Mais Amor, Menos Recalque*, *Angra dos Reis* e *Gosto Mais do Que Lasanha*.  
- Grande influência na popularização do **funk ostentação** em São Paulo.  
- Conquistou milhões de fãs antes de sua carreira ser interrompida precocemente.  

### 🏆 Legado
MC Daleste se tornou um **ícone eterno do funk brasileiro**, lembrado até hoje por sua autenticidade, talento e pela revolução que trouxe ao movimento.
""")
   st.video('https://www.youtube.com/watch?v=2NrYvjffX-E')
    #--------------------------------------------- Anavitória -----------------------------------------------------------
if genero_selecionado== "MPB" and musica_selecionada == "Anavitória":  
    st.markdown("""
## 🌟 Quem é Anavitória?

**Anavitória** é uma dupla musical brasileira formada por **Ana Caetano** e **Vitória Falcão**, criada em 2014.  
Elas se tornaram conhecidas por unir **pop, MPB e folk**, conquistando uma legião de fãs com músicas sensíveis e poéticas.

### 🎶 Principais conquistas:
- Álbuns de destaque como **"Anavitória" (2016)**, **"O Tempo é Agora" (2018)**, **"Cor" (2021)** e **"Dói no Tanto" (2024)**.  
- Sucessos como *Trevo (Tu)*, *Fica*, *Pupila* e *Ai, Amor*.  
- Vencedoras de prêmios importantes, incluindo o **Grammy Latino**.  
- Parcerias com artistas como **Tiago Iorc** e **Vitor Kley**.  

### 🏆 Legado
Anavitória é um dos maiores fenômenos da música brasileira contemporânea, levando mensagens de amor, amizade e autoconhecimento em suas canções.
""")
    st.video('https://www.youtube.com/watch?v=dXcxDI95hM4')
    #--------------------------------------------- Gilberto Gil -----------------------------------------------------------
elif genero_selecionado== "MPB" and musica_selecionada == "Gilberto Gil":  
    st.markdown("""
## 🌟 Quem é Gilberto Gil?

**Gilberto Gil** (nascido em 1942, na Bahia) é um cantor, compositor e multi-instrumentista brasileiro, considerado um dos maiores nomes da música nacional e mundial.  
Foi um dos líderes do movimento **Tropicália**, ao lado de Caetano Veloso, revolucionando a música brasileira nos anos 1960.

### 🎶 Principais conquistas:
- Obras icônicas como *Aquele Abraço*, *Expresso 2222*, *Andar com Fé* e *Toda Menina Baiana*.  
- Mais de **60 anos de carreira**, com dezenas de discos lançados.  
- Vencedor de prêmios nacionais e internacionais, incluindo o **Grammy**.  
- Atuou como **Ministro da Cultura do Brasil** (2003–2008).  

### 🏆 Legado
Gilberto Gil é símbolo de inovação, diversidade e resistência cultural, sendo reconhecido como um **patrimônio vivo da música brasileira**.
""")
    st.video('https://www.youtube.com/watch?v=fxhrak32GUY')
    #--------------------------------------------- Chico Buarque -----------------------------------------------------------
elif genero_selecionado== "MPB" and musica_selecionada == "Chico Buarque":  
    st.markdown("""
## 🌟 Quem é Chico Buarque?

**Francisco Buarque de Hollanda** (nascido em 1944, no Rio de Janeiro) é cantor, compositor, dramaturgo e escritor brasileiro.  
É reconhecido como um dos maiores nomes da **MPB** e também como uma voz de resistência durante o período da ditadura militar no Brasil.

### 🎶 Principais conquistas:
- Canções marcantes como *Construção*, *Cálice*, *A Banda*, *João e Maria* e *Apesar de Você*.  
- Autor de peças teatrais e romances premiados.  
- Vencedor de diversos prêmios nacionais e internacionais, incluindo o **Prêmio Camões** (2019).  
- Suas músicas transitam entre amor, política, crítica social e poesia.  

### 🏆 Legado
Chico Buarque é um dos maiores ícones culturais do Brasil, símbolo de **arte engajada, poesia e sensibilidade musical**, influenciando gerações.
""")
    st.video('https://www.youtube.com/watch?v=wBfVsucRe1w')
    #--------------------------------------------- Wesley Safadão -----------------------------------------------------------
if genero_selecionado== "FORRO" and musica_selecionada == "Wesley Safadão":
    st.markdown("""
## 🌟 Quem é Wesley Safadão?

**Wesley Oliveira da Silva** (nascido em 1988, no Ceará) é um cantor e compositor brasileiro, conhecido por seu trabalho no **forró eletrônico** e na música pop brasileira.  
Ele conquistou grande popularidade com seu estilo animado e suas músicas contagiantes.

### 🎶 Principais conquistas:
- Sucessos como *Camarote*, *Ar Condicionado no 15*, *Meu Coração Deu PT* e *Só Pra Castigar*.  
- Um dos artistas mais tocados em rádios e plataformas digitais no Brasil.  
- Realizou grandes turnês nacionais e internacionais, com shows lotados.  
- Premiações importantes, incluindo prêmios **Multishow** de música.  

### 🏆 Legado
Wesley Safadão é um dos principais representantes do **forró moderno**, levando alegria e música dançante para milhões de fãs.
""")
    st.video('https://www.youtube.com/watch?v=PvM_YAabhkk')
    #--------------------------------------------- Zé Vaqueiro -----------------------------------------------------------
elif genero_selecionado== "FORRO" and musica_selecionada == "Zé Vaqueiro":
    st.markdown("""
## 🌟 Quem é Zé Vaqueiro?

**José Vaqueiro de Lima**, conhecido como **Zé Vaqueiro** (nascido em 1998, na Paraíba), é um cantor brasileiro de **forró e piseiro**.  
Ele se destacou por misturar ritmos tradicionais nordestinos com elementos modernos, conquistando grande popularidade entre jovens e fãs de música nordestina.

### 🎶 Principais conquistas:
- Sucessos como *Letícia*, *Tá Rocheda*, *Cangote* e *Se For Amor*.  
- Um dos artistas mais ouvidos em plataformas de streaming no Brasil.  
- Participações em festivais e shows com grandes públicos.  
- Reconhecido por popularizar o **piseiro** nacionalmente.  

### 🏆 Legado
Zé Vaqueiro representa a nova geração da música nordestina, mantendo viva a tradição do forró enquanto conquista o público jovem com ritmos modernos e dançantes.
""")
    st.video('https://www.youtube.com/watch?v=-WloA4ia7aI')

    with open("angolano.png", "rb") as file:
        img_bytes = file.read()
        st.download_button(
            label="Surpresa",
            data=img_bytes,
            file_name="angolano.png",
            mime="image/png",  # especifica o tipo do arquivo
            icon=":material/download:",
)
    #--------------------------------------------- João Gomes -----------------------------------------------------------
elif genero_selecionado== "FORRO" and musica_selecionada == "João Gomes":
    st.markdown("""
## 🌟 Quem é João Gomes?

**João Fernando Gomes Valério** (nascido em 2002, na Bahia) é um cantor brasileiro de **forró e piseiro**, conhecido por sua voz marcante e estilo jovem.  
Ele ganhou destaque rapidamente com músicas que misturam ritmos nordestinos e elementos modernos do pop.

### 🎶 Principais conquistas:
- Sucessos como *Meu Pedaço de Pecado*, *Se For Amor* e *Dormindo Sozinho*.  
- Um dos artistas mais ouvidos nas plataformas de streaming no Brasil.  
- Shows e turnês com grande público, especialmente no Nordeste.  
- Popularização do **piseiro** entre o público jovem.  

### 🏆 Legado
João Gomes é um dos representantes da nova geração do forró e piseiro, conectando a tradição nordestina com tendências musicais atuais.
""")
    st.video('https://www.youtube.com/watch?v=3IcyRLeZDIs')
    #--------------------------------------------- Travis Scott -----------------------------------------------------------
if genero_selecionado== "TRAP" and musica_selecionada == "Travis Scott":
    st.markdown("""
## 🌟 Quem é Travis Scott?

**Jacques Berman Webster II**, conhecido como **Travis Scott** (nascido em 1992, nos EUA), é um rapper, cantor, compositor e produtor musical.  
Ele é um dos artistas mais influentes do **hip hop e trap contemporâneo**, famoso por suas produções inovadoras e performances explosivas.

### 🎶 Principais conquistas:
- Álbuns de sucesso como *Rodeo* (2015), *Birds in the Trap Sing McKnight* (2016) e *Astroworld* (2018).  
- Hits globais como *Sicko Mode*, *Goosebumps* e *Highest in the Room*.  
- Colaborações com grandes nomes da música, incluindo Drake, Kanye West e The Weeknd.  
- Premiações importantes, incluindo **MTV Video Music Awards** e indicações ao **Grammy**.  

### 🏆 Legado
Travis Scott é conhecido por revolucionar o **hip hop moderno**, combinando música, moda e experiências visuais em shows únicos, influenciando uma geração de artistas e fãs.
""")
    st.video('https://www.youtube.com/watch?v=B9synWjqBn8')
    #--------------------------------------------- Matuê -----------------------------------------------------------
elif genero_selecionado== "TRAP" and musica_selecionada == "Matuê":
    st.markdown("""
## 🌟 Quem é Matuê?

**Matuê** (Mateus Aleluia, nascido em 1996, no Brasil) é um rapper e cantor brasileiro, considerado um dos principais nomes do **trap nacional**.  
Ele se destacou por misturar letras de ostentação, experiências pessoais e produções modernas, conquistando rapidamente o público jovem.

### 🎶 Principais conquistas:
- Hits de sucesso como *Kenny G*, *Anos Luz*, *Máquina do Tempo* e *Tudo Igual*.  
- Álbum aclamado *Máquina do Tempo* (2020).  
- Um dos artistas mais ouvidos no Brasil em plataformas de streaming.  
- Colaborações com outros nomes do trap e rap brasileiro.  

### 🏆 Legado
Matuê é referência do **trap brasileiro**, trazendo inovação, estilo e autenticidade para o gênero, e influenciando a nova geração de rappers no país.
""")
    st.video('https://www.youtube.com/watch?v=zctKiN-okXI')
    #--------------------------------------------- WIU -----------------------------------------------------------
elif genero_selecionado== "TRAP" and musica_selecionada == "WIU":
    st.markdown("""
## 🌟 Quem é WIU?

**WIU** (nome verdadeiro: Vinicius William Sales de Lima) é um rapper, cantor, compositor e produtor musical brasileiro, nascido em Fortaleza, Ceará, em 16 de fevereiro de 2002. :contentReference[oaicite:1]{index=1}

WIU ganhou destaque na cena do trap nacional com suas produções autorais e colaborações com artistas como Matuê e Teto. Em 2022, lançou seu álbum de estreia, *Manual de Como Amar Errado*, que consolidou sua posição no cenário musical brasileiro. :contentReference[oaicite:2]{index=2}

### 🎶 Principais conquistas:
- Sucessos como *Coração de Gelo*, *Felina*, *Flow Espacial* e *Rainha da Finesse*.
- Colaborações com artistas renomados do trap nacional, incluindo Matuê e Teto.
- Lançamento do segundo álbum de estúdio, *Vagabundo de Luxo*, em 2024, que mistura trap com influências de forró eletrônico, reggaeton e funk carioca. :contentReference[oaicite:3]{index=3}

### 🏆 Legado
WIU é reconhecido por sua versatilidade musical e por trazer inovação ao trap brasileiro, incorporando elementos de diferentes gêneros e conquistando uma base de fãs fiel.
""")
    st.video('https://www.youtube.com/watch?v=frfd45-rEHE')
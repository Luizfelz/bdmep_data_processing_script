# Projeto_Pesquisa_PIBIC-UFPB

**Contexto**
A utilização de fontes renováveis é de extrema importância diante do cenário de mudanças climáticas que o mundo está enfrentando. A matriz energética brasileira é constituída por muitas fontes renováveis para geração de energia, mas infelizmente essas fontes dependem de algumas variáveis climáticas, como temperatura, pluviosidade, velocidade do vento, radiação, entre outras. Nesse contexto, o estudo das variáveis climáticas é essencial, porém a quantidade exorbitante de dados brutos a serem analisados torna necessário o auxílio de ferramentas capazes de realizar essa função de maneira rápida e efetiva. O uso de algoritmos para tratamento de bancos de dados é bastante comum e vem crescendo significativamente nos últimos anos, ainda mais quando considerado o uso mais frequente de linguagens de programação para realização e automação de tarefas que anteriormente eram realizadas de maneira manual.

O [Python](https://www.python.org/) é uma linguagem de programação de alto nível e uma das mais utilizadas para tratamento de banco de dados, pois além de permitir que seus algoritmos sejam leves e rápidos, permite uma fácil criação e interpretação de sequências de comandos lógicos que servirão para o tratamento dos dados brutos.

O [Banco de Dados Meteorológicos](https://bdmep.inmet.gov.br/) do [Instituto Nacional de Meteorologia](https://portal.inmet.gov.br/) (BDMEP - INMET) é um banco de dados digital que agrupa dados meteorológicos de séries históricas de estações meteorológicas automáticas e convencionais, conforme normas técnicas internacionais da [Organização Meteorológica Mundial](https://news.un.org/pt/tags/organizacao-meteorologica-mundial).

O [NASA POWER](https://power.larc.nasa.gov/data-access-viewer/) é um projeto da [NASA](https://www.nasa.gov/) que fornece parâmetros relacionados ao Sol e meteorologia habilitada geoespacialmente que permitem avaliação e projeção de sistemas de energia renovável.

**Objetivo**
O objetivo deste projeto é a criação de um algoritmo capaz de tratar os dados brutos retirados do BDMEP e da NASA. O algoritmo ainda está em desenvolvimento e, atualmente, consegue realizar o processamento apenas de dados diários e mensais, retirados do BDMEP (para uma ou mais variáveis simultâneamente), e dados mensais retirados da NASA (para apenas uma variável por vez). No entanto, o objetivo futuro é que seja capaz de fazer o processamento de qualquer intervalo de dados (horários, diários ou mensais) e para qualquer quantidade de variáveis.

**Justificativa**
A criação do algoritmo foi pensada para que fosse possível ser utilizado por qualquer pessoa, com ou sem nenhum conhecimento prévio em programação, em pesquisas que fizessem uso dos dados disponibilizados pelo BDMEP e pela NASA. Ainda, a utilização de ferramentas computacionais para cálculos e processamento de dados ajuda na diminuição de erros propagados por análises manuais e na diminuição do tempo de processamento, permitindo uma análise mais rápida, eficiente e precisa.

# Explicações gerais sobre o algoritmo

As informações, à respeito do uso, podem ser encontradas no próprio arquivo do algoritmo, juntamente a um vídeo com breves explicações da sua utilização.

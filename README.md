# Modulos
Aula sobre modulos


## Módulos nativos em Python

O Python já vem com uma filosofia clássica chamada "batteries included" (baterias inclusas). Isso significa que a biblioteca padrão dele é gigantesca e muito poderosa.

Para facilitar a sua vida, separei os módulos nativos mais importantes e utilizados no dia a dia, organizados por categorias:

* Manipulação de Arquivos e Sistema Operacional
Esses módulos servem para você conversar com o sistema do seu computador (criar pastas, listar arquivos, ler caminhos).

***os***: Permite interagir com o sistema operacional (criar/deletar pastas, alterar permissões, ler variáveis de ambiente).

***sys***: Fornece variáveis e funções que interagem diretamente com o próprio interpretador do Python (como ler argumentos passados via linha de comando com sys.argv).

***pathlib***: A forma moderna (e muito mais elegante) de trabalhar com caminhos de arquivos como se fossem objetos, sem se preocupar se o sistema é Windows, Mac ou Linux.

* Formatos de Dados e Web
Essenciais se você precisa salvar dados ou fazer pequenas integrações na internet.

***json***: Fundamental hoje em dia. Serve para converter dicionários do Python para strings JSON e vice-versa.

***csv***: Para ler e escrever arquivos de planilhas básicas (separados por vírgula) sem precisar instalar o Pandas.

***urllib***: Uma coleção de módulos para trabalhar com URLs e fazer requisições web (embora a biblioteca externa requests seja mais famosa, o urllib quebra um galho se você não puder instalar nada).

* Matemática e Ferramentas Numéricas
Para quando as operações básicas de ***+, -, *, /*** não são suficientes.

***math***: Dá acesso a funções matemáticas complexas (trigonometria, logaritmos, teto, chão, pi, etc.).

***random***: Gerador de números pseudoaleatórios. Ótimo para embaralhar listas, escolher itens aleatórios ou gerar números de teste.

***datetime***: O módulo oficial para manipular datas e horários, calcular diferenças de dias e formatar relógios.

* Estruturas de Dados Avançadas e Utilitários
Ferramentas que deixam o seu código mais limpo, rápido e inteligente.

***collections***: Oferece tipos de dados além dos básicos (list, dict, tuple). Destaco o Counter (para contar elementos facilmente) e o defaultdict (dicionário que não quebra se a chave não existir).

***itertools***: Uma fábrica de iteradores de alta performance. Excelente para criar combinações, permutações e loops infinitos controlados.

***re***: Módulo para trabalhar com Expressões Regulares (Regex). Essencial para buscar, validar ou extrair padrões complexos dentro de textos.

💡 Dica de ouro: Antes de sair correndo para instalar uma biblioteca externa usando o pip, dê uma olhada na documentação oficial do Python. Muitas vezes, o que você precisa já está lá dentro de forma nativa e super otimizada.
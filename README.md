
# Aura - Assistant for Understanding and Response in Ambient

Um sistema local de interpretação de comandos verbais com base em análise gramatical e árvore de decisão, permitindo a execução de comandos como abrir programas, reproduzir músicas e automatizar tarefas no computador.





---
## Lógica

O sistema recebe o audio convertido por um Speech-to-Text e em seguida é feito tratamento para facilitar a busca das palavra, assim descobrindo se é verbo, substantivo e derivados.

Realizado a busca de cada palavra, em um dicionario, o dicionario mostra os caminhos relacionados que o sistema terá que levar para a execução do comando.

Exemplo: Toque música no Spotify

Toque - Verbo Tocar
Tocar o que? - Musica
A onde? - Spotify

Retorno esperado "despausar musica do spotify"


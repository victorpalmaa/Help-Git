Guia Rápido de Comandos (Git, macOS, Linux & Windows)
Este é um script simples em Python (usando Tkinter) que cria uma janela flutuante "sempre no topo" para servir como um guia rápido e interativo de comandos do Git e do Terminal.

É perfeito para quem está aprendendo ou precisa de uma "cola" rápida sem sair da janela principal de trabalho.

🚀 Funcionalidades
Sempre no Topo: A janela flutua sobre seus outros aplicativos (como o VS Code ou o Terminal) para referência rápida.

Interface Simples: Uma lista de botões à esquerda permite navegar rapidamente entre os tópicos.

Guias de Ajuda: Inclui guias para:

Rotinas comuns do Git (novo repo, rotina diária, trocar remotos).

Comandos úteis do Terminal para macOS (zsh/bash).

Comandos úteis do Terminal para Linux (bash/zsh).

Comandos úteis do Terminal para Windows (cmd).

Atalho de Terminal: Pode ser configurado para ser iniciado de qualquer lugar do terminal com um comando simples (ex: helpgit).

📋 Pré-requisitos
Você precisa ter o Python 3 instalado em seu sistema.

Tkinter: Esta é a biblioteca que desenha a janela.

macOS/Windows: O Tkinter geralmente já vem instalado por padrão com o Python.

Linux: Pode ser necessário instalar separadamente (ex: sudo apt-get install python3-tk para sistemas baseados em Debian/Ubuntu).

Você pode testar se o Tkinter está instalado rodando:

Bash

python3 -m tkinter
(Uma pequena janela de teste deve aparecer).

⚙️ Instalação e Configuração
Para fazer o script funcionar em qualquer lugar, siga o guia para o seu sistema operacional:

 macOS (Terminal zsh ou bash)
O objetivo é criar um "alias" (atalho) que execute o script.

1. Salve o Arquivo

Salve o arquivo git_helper.py em um local permanente no seu computador.

Exemplo de local: /Users/seu-usuario/scripts/git_helper.py

2. Crie o Atalho (Alias)

Vamos criar o comando helpgit. Abra o arquivo de configuração do seu shell. (O padrão no macOS moderno é o .zshrc).

Bash

nano ~/.zshrc
Use as setas para ir até o final do arquivo e adicione a seguinte linha. Importante: Ajuste o caminho para onde você salvou o script!

Bash

# Atalho para o Guia Rápido de Git
alias helpgit="python3 '/Users/seu-usuario/scripts/git_helper.py' > /dev/null 2>&1 &"
Nota 1: As aspas simples ('...') são essenciais se o seu caminho tiver espaços. Nota 2: O > /dev/null 2>&1 & faz com que o script rode em segundo plano e libere seu terminal imediatamente.

3. Recarregue o Terminal

Salve o arquivo no nano: Control + O (Enter) e saia: Control + X. Aplique as mudanças no seu terminal:

Bash

source ~/.zshrc
4. Teste

Feche e reabra seu terminal. De qualquer pasta, digite helpgit e a janela deve aparecer.

🐧 Linux (Terminal bash ou zsh)
O processo é quase idêntico ao do macOS.

1. Salve o Arquivo

Salve o arquivo git_helper.py em um local permanente no seu computador.

Exemplo de local: /home/seu-usuario/scripts/git_helper.py

2. Crie o Atalho (Alias)

Vamos criar o comando helpgit. Abra o arquivo de configuração do seu shell.

Bash

# Para o shell bash (padrão na maioria das distros)
nano ~/.bashrc

# Se você usa zsh
# nano ~/.zshrc
Use as setas para ir até o final do arquivo e adicione a seguinte linha. Importante: Ajuste o caminho para onde você salvou o script!

Bash

# Atalho para o Guia Rápido de Git
alias helpgit="python3 '/home/seu-usuario/scripts/git_helper.py' > /dev/null 2>&1 &"
Nota: O > /dev/null 2>&1 & faz com que o script rode em segundo plano e libere seu terminal imediatamente.

3. Recarregue o Terminal

Salve o arquivo no nano: Control + O (Enter) e saia: Control + X. Aplique as mudanças no seu terminal (use o comando do shell que você editou):

Bash

# Se você editou .bashrc
source ~/.bashrc

# Se você editou .zshrc
# source ~/.zshrc
4. Teste

Feche e reabra seu terminal. De qualquer pasta, digite helpgit e a janela deve aparecer.

🪟 Windows (cmd ou PowerShell)
O objetivo é criar um arquivo .bat e adicioná-lo ao PATH do sistema.

1. Salve o Arquivo

Salve o arquivo git_helper.py em um local permanente.

Exemplo de local: C:\Users\SeuUsuario\scripts\git_helper.py

2. Crie o Atalho (.bat)

Na mesma pasta onde você salvou o script (ex: C:\Users\SeuUsuario\scripts\), crie um novo arquivo de texto.

Renomeie este novo arquivo para helpgit.bat.

Clique com o botão direito em helpgit.bat e escolha "Editar". Cole o seguinte conteúdo dentro dele (ajuste o caminho se for diferente):

Snippet de código

@echo off
pythonw "C:\Users\SeuUsuario\scripts\git_helper.py"
Nota: Usamos pythonw.exe (em vez de python.exe) porque ele executa o script Python sem abrir uma janela de console (terminal) preta ao fundo.

Salve e feche o arquivo.

3. Adicione ao PATH do Sistema

Para que o Windows encontre seu atalho helpgit.bat de qualquer lugar:

Pressione a tecla Windows e digite "Variáveis de ambiente".

Clique em "Editar as variáveis de ambiente do sistema".

Na janela que abrir, clique no botão "Variáveis de Ambiente...".

Na seção "Variáveis de usuário para [SeuUsuario]", encontre a variável chamada Path e clique em "Editar...".

Clique em "Novo".

Cole o caminho da sua pasta de scripts (ex: C:\Users\SeuUsuario\scripts\).

Clique "OK" em todas as janelas para salvar.

4. Teste

Feche e reabra completamente todas as janelas do seu terminal (cmd ou PowerShell). De qualquer pasta, digite helpgit e a janela deve aparecer.
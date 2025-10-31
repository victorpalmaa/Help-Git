import tkinter as tk
from tkinter import ttk

# --- Dicionário com os textos de ajuda ---
GUIAS_AJUDA = {
    "NOVO_REPO": """
### 1. Criando um Novo Repositório (do zero)

Passos para iniciar um projeto local e enviá-lo 
ao GitHub/GitLab pela primeira vez.

# 1. Inicia o repositório na pasta atual
git init

# 2. Adiciona todos os arquivos para o Git
git add .

# 3. Cria o primeiro "commit" (um ponto de salvamento)
git commit -m "Commit inicial"

# 4. Conecta seu repositório local ao remoto 
# (Copie a URL do seu repositório no GitHub/GitLab)
git remote add origin SUA_URL_AQUI

# 5. Envia seus arquivos para o repositório remoto
git push -u origin main
""",
    
    "ROTINA_DIARIA": """
### 2. Rotina Diária (Trabalhando em um projeto)

Passos para criar uma nova funcionalidade (branch) 
e enviá-la.

# 1. Garanta que você está na branch principal
git checkout main

# 2. Baixe as atualizações mais recentes
git pull origin main

# 3. Crie uma nova branch para sua alteração
git checkout -b nome-da-nova-branch

# 4. Faça suas alterações no código...
# 5. Adicione os arquivos que você modificou
git add .

# 6. Crie o commit (ponto de salvamento)
git commit -m "O que eu fiz (ex: Adiciona tela de login)"

# 7. Envie sua branch para o repositório remoto
git push -u origin nome-da-nova-branch
""",

    "ATUALIZAR": """
### 3. Atualizar e Sincronizar

Como baixar atualizações de outros devs 
ou trocar de branch.

# 1. Para baixar atualizações da branch ATUAL
git pull

# 2. Para ver todas as branches
git branch -a

# 3. Para trocar para uma branch que já existe
git checkout nome-da-branch-existente

# 4. Para baixar o que outros fizeram e 
# atualizar sua branch atual com a 'main'
git pull origin main
""",

    # --- GUIA TROCAR REMOTO ---
    "TROCAR_REMOTO": """
### 4. Trocar Repositório Remoto (Origem)

Cenário: Você clonou o repositório 'X',
mas quer enviar seu código para o repositório 'Y'.

# 1. Veja quais remotos estão configurados
# (Você deve ver 'origin' apontando para a URL 'X')
git remote -v

# 2. Remove o link para o repositório antigo (X)
git remote remove origin

# 3. Adiciona o link para o NOVO repositório (Y)
# (Pegue a URL do repositório 'Y')
git remote add origin SUA_NOVA_URL_Y

# 4. Verifique se a mudança funcionou
# (Agora deve apontar para a URL 'Y')
git remote -v

# 5. Envie seus arquivos para o novo repositório 'Y'
git push -u origin main
""",

    "OUTROS_GIT": """
### 5. Comandos Git Úteis

# Vê o status atual (o que foi modificado)
git status

# Vê o histórico de commits (versão curta)
git log --oneline

# Vê o histórico de commits (com detalhes)
git log --graph --pretty=format:'%h -%d %s (%cr) <%an>'

# Descarta alterações em um arquivo (CUIDADO!)
git checkout -- nome-do-arquivo.txt
""",

    "TERMINAL_MAC_NAV": """
### 6. Navegação (Terminal macOS)

Comandos básicos para se mover no terminal (zsh/bash).
(Idêntico ao Linux)

# Mostra o caminho da pasta atual
pwd

# Lista arquivos e pastas da pasta atual
ls

# Lista com mais detalhes (permissões, dono, tamanho)
ls -l

# Lista todos os arquivos (incluindo ocultos)
ls -la

# Mudar de diretório
cd nome-da-pasta

# Voltar um nível
cd ..

# Voltar para a pasta "Home" do usuário
cd ~
""",
    
    "TERMINAL_MAC_UTIL": """
### 7. Utilitários (Terminal macOS)

Comandos úteis e específicos do macOS.

# (Homebrew) Gerenciador de pacotes. 
brew install [pacote]
brew update
brew upgrade

# Procurar arquivos via Spotlight (MUITO RÁPIDO)
mdfind "nome-do-arquivo.py"

# Copiar arquivos
cp arquivo-original.txt copia.txt

# Mover ou Renomear arquivos
mv arquivo-antigo.txt novo-nome.txt

# Criar uma nova pasta
mkdir nome-da-pasta
""",
    
    # --- NOVO GUIA (TERMINAL LINUX) ---
    "TERMINAL_LINUX_UTIL": """
### 8. Utilitários (Terminal Linux)

Comandos úteis para distribuições Linux.
(Nota: Navegação 'ls', 'cd', 'pwd' é idêntica à do macOS)

# Gerenciador de Pacotes (Debian/Ubuntu)
sudo apt-get update
sudo apt-get install [pacote]
sudo apt-get remove [pacote]

# Gerenciador de Pacotes (RedHat/Fedora)
sudo dnf install [pacote]  # (Moderno)
sudo yum install [pacote]  # (Antigo)

# Mudar permissões de arquivos (ler=4, w=2, x=1)
# Ex: 755 = (dono:rwx, grupo:r-x, outros:r-x)
chmod 755 seu_script.sh

# Mudar o dono de um arquivo
sudo chown usuario:grupo nome_do_arquivo.txt

# Procurar texto dentro de arquivos (MUITO útil)
grep "texto para buscar" arquivo.txt
""",

    # --- GUIA (TERMINAL WINDOWS) ---
    "TERMINAL_WINDOWS": """
### 9. Comandos (Terminal Windows)

Comandos básicos para o Prompt de Comando (cmd.exe).

# Lista arquivos e pastas da pasta atual
dir

# Limpa a tela do terminal
cls

# Mudar de diretório
cd nome-da-pasta

# Voltar um nível
cd ..

# Criar uma nova pasta
mkdir nome-da-pasta

# Copiar arquivos
copy arquivo-original.txt copia.txt

# Mover ou Renomear arquivos
move arquivo-antigo.txt novo-nome.txt
ren arquivo-antigo.txt novo-nome.txt

# Deletar um arquivo
del nome-do-arquivo.txt
"""
}

# --- Classe principal da Aplicação ---
class GitHelperApp:
    def __init__(self, root):
        self.root = root
        # --- Título Atualizado ---
        root.title("Guia Rápido (Git, macOS, Linux & Windows)")

        # --- Posição e "Sempre no Topo" ---
        app_width = 700
        # --- Altura Aumentada ---
        app_height = 550 
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = screen_width - app_width - 40
        y = 40
        root.geometry(f"{app_width}x{app_height}+{x}+{y}")
        root.attributes('-topmost', True)
        
        # --- Layout Principal ---
        self.frame_botoes = ttk.Frame(root, padding="10")
        self.frame_botoes.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_texto = ttk.Frame(root, padding="10")
        self.frame_texto.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # --- Área de Texto (Direita) ---
        self.texto_ajuda = tk.Text(self.frame_texto, 
                                   wrap="word", 
                                   width=60, 
                                   height=20, 
                                   font=("Courier New", 10),
                                   padx=10,
                                   pady=10)
                                   
        self.scrollbar = ttk.Scrollbar(self.frame_texto, 
                                       command=self.texto_ajuda.yview)
        self.texto_ajuda['yscrollcommand'] = self.scrollbar.set
        
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.texto_ajuda.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.texto_ajuda.config(state=tk.DISABLED)

        # --- Botões (Esquerda) ---
        label_git = ttk.Label(self.frame_botoes, 
                              text="Ajuda Git", 
                              font=("Arial", 12, "bold"))
        label_git.pack(pady=(0, 5))

        # --- Renumerados ---
        self.criar_botao("1. Novo Repositório", "NOVO_REPO")
        self.criar_botao("2. Rotina Diária", "ROTINA_DIARIA")
        self.criar_botao("3. Atualizar / Trocar", "ATUALIZAR")
        self.criar_botao("4. Trocar Repositório (Remoto)", "TROCAR_REMOTO")
        self.criar_botao("5. Outros Comandos Git", "OUTROS_GIT") 

        separator_mac = ttk.Separator(self.frame_botoes, orient='horizontal')
        separator_mac.pack(fill='x', pady=15, padx=5)

        label_mac = ttk.Label(self.frame_botoes, 
                              text="Terminal macOS", 
                              font=("Arial", 12, "bold"))
        label_mac.pack(pady=(0, 5))

        # --- Renumerados ---
        self.criar_botao("6. Navegação (macOS)", "TERMINAL_MAC_NAV") 
        self.criar_botao("7. Utilitários (macOS)", "TERMINAL_MAC_UTIL")

        # --- NOVO: Seção Linux ---
        separator_lin = ttk.Separator(self.frame_botoes, orient='horizontal')
        separator_lin.pack(fill='x', pady=15, padx=5)

        label_lin = ttk.Label(self.frame_botoes, 
                              text="Terminal Linux", 
                              font=("Arial", 12, "bold"))
        label_lin.pack(pady=(0, 5))

        self.criar_botao("8. Utilitários (Linux)", "TERMINAL_LINUX_UTIL") # NOVO

        # --- Seção Windows ---
        separator_win = ttk.Separator(self.frame_botoes, orient='horizontal')
        separator_win.pack(fill='x', pady=15, padx=5)

        label_win = ttk.Label(self.frame_botoes, 
                              text="Terminal Windows", 
                              font=("Arial", 12, "bold"))
        label_win.pack(pady=(0, 5))

        self.criar_botao("9. Comandos (Windows)", "TERMINAL_WINDOWS") # Renumerado
        
        # --- Fim das adições ---

        # Inicia mostrando o primeiro tópico
        self.mostrar_ajuda("NOVO_REPO")

    def criar_botao(self, texto, topico_id):
        """Cria um botão padronizado"""
        botao = ttk.Button(
            self.frame_botoes,
            text=texto,
            command=lambda: self.mostrar_ajuda(topico_id)
        )
        botao.pack(fill=tk.X, pady=4) 

    def mostrar_ajuda(self, topico_id):
        """Atualiza a caixa de texto com o conteúdo do tópico"""
        
        texto = GUIAS_AJUDA.get(topico_id, "Tópico não encontrado.")
        
        self.texto_ajuda.config(state=tk.NORMAL)
        self.texto_ajuda.delete('1.0', tk.END)
        self.texto_ajuda.insert('1.0', texto.strip())
        self.texto_ajuda.config(state=tk.DISABLED)

# --- Inicia a aplicação ---
if __name__ == "__main__":
    main_window = tk.Tk()
    style = ttk.Style(main_window)
    # (Mantendo o tema nativo do sistema)
    
    app = GitHelperApp(main_window)
    main_window.mainloop()


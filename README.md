# 🎵 MdoU

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PySide6](https://img.shields.io/badge/PySide6-6.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

Uma aplicação desktop moderna para buscar e baixar beatmaps do osu! diretamente do seu computador, sem precisar abrir o navegador.

</div>

---

## 📋 Sobre o Projeto

O **osu! Beatmap Finder & Downloader** é uma interface gráfica intuitiva que permite aos jogadores de osu! buscar, visualizar e baixar beatmaps usando a API oficial do osu!. Desenvolvido com PySide6, oferece uma experiência moderna e responsiva.

### ✨ Principais Diferenciais

- 🔍 **Busca Avançada** - Filtre por modo de jogo e status
- 📥 **Download Automático** - Baixe beatmaps com um clique
- 📊 **Barra de Progresso** - Acompanhe seus downloads em tempo real
- 🎨 **Interface Moderna** - Dark theme e design responsivo
- ⚡ **Performance** - Operações assíncronas sem travar a UI
- 🔒 **Seguro** - Usa OAuth2 oficial do osu!

---

## 🎯 Recursos

### Busca de Beatmaps
- ✅ Pesquisa por título, artista ou mapper
- ✅ Filtros por modo (osu!, taiko, catch, mania)
- ✅ Filtros por status (Ranked, Qualified, Loved, Pending)
- ✅ Resultados com informações detalhadas
- ✅ Estatísticas (plays, favoritos, dificuldades)

### Sistema de Download
- ✅ Download direto sem abrir navegador
- ✅ Barra de progresso em tempo real
- ✅ Downloads simultâneos suportados
- ✅ Pasta de destino configurável
- ✅ Formato .osz (pronto para o osu!)
- ✅ Notificação ao concluir
- ✅ Botão para abrir pasta de downloads

### Interface
- ✅ Dark theme moderno
- ✅ Cards informativos por beatmap
- ✅ Indicadores visuais de estado
- ✅ Status bar com informações úteis
- ✅ Scrolling suave
- ✅ Hover effects

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Conta no osu! (para obter credenciais OAuth)

### Passo 1: Clone o Repositório

```bash
git clone https://github.com/Fa1kerXd/MdoU.git
cd MdoU
```

### Passo 2: Crie um Ambiente Virtual (Recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instale as Dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Execute o Aplicativo

```bash
python main.py
```

---

## ⚙️ Configuração

### Obter Credenciais OAuth do osu!

Para usar este aplicativo, você precisa criar uma aplicação OAuth no site do osu!:

1. **Acesse** o site do osu!
   - URL: https://osu.ppy.sh/home/account/edit

2. **Navegue até a seção OAuth**
   - Role a página até encontrar "OAuth"
   - Clique em "New OAuth Application"

3. **Preencha os dados**
   ```
   Application Name: osu! Beatmap Finder
   Application Callback URL: http://localhost
   ```

4. **Copie as credenciais**
   - **Client ID** (número)
   - **Client Secret** (string longa)

5. **Cole no aplicativo**
   - Na primeira execução, um diálogo aparecerá
   - Insira suas credenciais
   - Escolha a pasta de downloads

### Pasta de Downloads

Por padrão, os beatmaps são salvos em:
```
Windows: C:\Users\SeuUsuario\Downloads\osu_beatmaps
Linux:   /home/seuusuario/Downloads/osu_beatmaps
Mac:     /Users/seuusuario/Downloads/osu_beatmaps
```

Você pode alterar durante a configuração inicial.

---

## 📖 Como Usar

### 1. Buscar Beatmaps

```
1. Digite o nome da música, artista ou mapper na barra de busca
2. (Opcional) Selecione um modo de jogo no dropdown
3. (Opcional) Selecione um status (Ranked, Loved, etc.)
4. Pressione Enter ou clique em "Buscar"
5. Aguarde os resultados aparecerem
```

### 2. Visualizar Informações

Cada card de beatmap mostra:
- 🎵 **Título e Artista**
- 👤 **Nome do Mapper**
- ▶️ **Número de Plays**
- ❤️ **Favoritos**
- 🎼 **Quantidade de Dificuldades**

### 3. Baixar Beatmap

```
1. Localize o beatmap desejado nos resultados
2. Clique no botão "📥 Baixar"
3. Acompanhe o progresso na barra
4. Aguarde a notificação de conclusão
5. (Opcional) Clique em "Abrir Pasta" para ver o arquivo
```

### 4. Abrir no Site

```
1. Clique no botão "Abrir no Site" no card
2. O beatmap será aberto no navegador padrão
3. Você pode ver mais detalhes, comentários, etc.
```

---

## 📸 Screenshots

### Tela Principal
```
┌─────────────────────────────────────────────────────────┐
│  🎵 osu! Beatmap Finder & Downloader                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  [Digite sua busca...] [Modo▼] [Status▼] [Buscar]     │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │ 🎵  Freedom Dive                                 │  │
│  │     Por: xi                                      │  │
│  │     Mapper: Nakagawa-Kanon                       │  │
│  │     ▶ 1,500,000 plays | ❤ 2,500 favs           │  │
│  │     [Abrir no Site] [📥 Baixar]                 │  │
│  │     [████████░░] 80%                             │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
│  [Mais beatmaps...]                                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Diálogo de Configuração
```
┌──────────────────────────────────────┐
│  Configurar API do osu!              │
├──────────────────────────────────────┤
│                                      │
│  Instruções:                         │
│  1. Acesse osu.ppy.sh...            │
│  2. Crie OAuth Application...        │
│                                      │
│  Client ID: [12345_________]         │
│  Client Secret: [**************]     │
│                                      │
│  Pasta de Download:                  │
│  [C:\Users\...\osu_beatmaps] [...]  │
│                                      │
│  [Conectar]  [Cancelar]              │
└──────────────────────────────────────┘
```

---

## 🗂️ Estrutura do Projeto

```
MDOU/
├── src/                 
    ├── BeatmapCard.py
    ├── ConfigDialog.py    
    ├── DownloadThread.py
    ├── MainWindow.py
    ├── OsuAPIClient.py   # Cliente da API do osu!
    └── SearchThread.py
├── main.py                 # Aplicação principal
├── requirements.txt        # Dependências Python
├── README.md              # Este arquivo
├── LICENSE                # Licença do projeto
├── .gitignore            # Arquivos ignorados pelo Git
└── assets/               # (Opcional) Imagens e ícones
    └── icon.png
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
|-----------|---------|-----------|
| [Python](https://python.org) | 3.8+ | Linguagem principal |
| [PySide6](https://doc.qt.io/qtforpython/) | 6.0+ | Framework de interface gráfica |
| [Requests](https://requests.readthedocs.io/) | 2.31+ | Cliente HTTP para API |
| [osu! API v2](https://osu.ppy.sh/docs/) | - | API oficial do osu! |

---

## 📦 Dependências

### requirements.txt
```txt
certifi==2026.1.4
charset-normalizer==3.4.4
idna==3.11
PySide6==6.10.1
PySide6_Addons==6.10.1
PySide6_Essentials==6.10.1
requests==2.32.5
shiboken6==6.10.1
urllib3==2.6.2
```

### Instalação Rápida
```bash
pip install PySide6 requests
```

---

## 🐛 Problemas Conhecidos

### Issue #1: Download Sem Login
- **Problema**: Downloads funcionam sem login no osu!
- **Limitação**: Apenas versão sem vídeo disponível
- **Solução**: Para versão com vídeo, login completo seria necessário

### Issue #2: Rate Limiting
- **Problema**: API tem limite de requisições
- **Limitação**: 60 requisições por minuto
- **Solução**: Aplicativo gerencia automaticamente

### Issue #3: Previews de Áudio
- **Status**: Em desenvolvimento
- **Previsão**: Próxima versão (v2.0)

---

## 🔜 Roadmap

### Versão 2.0 (Planejada)
- [ ] 🎵 Preview de áudio dos beatmaps
- [ ] 🖼️ Carregamento de capas
- [ ] 📊 Filtros avançados (BPM, duração, etc.)
- [ ] ⭐ Sistema de favoritos local
- [ ] 📁 Organização automática por artista/mapper

### Versão 3.0 (Futuro)
- [ ] 🔐 Login completo do osu!
- [ ] 💬 Sistema de comentários
- [ ] 📈 Estatísticas pessoais
- [ ] 🎮 Integração com osu! local
- [ ] 🌐 Suporte a múltiplos idiomas

---


### Diretrizes

- ✅ Siga o estilo de código existente
- ✅ Adicione comentários em código complexo
- ✅ Teste suas alterações
- ✅ Atualize a documentação se necessário
- ✅ Um commit por funcionalidade

### Reportar Bugs

Encontrou um bug? Abra uma [Issue](https://github.com/Fa1KerXd/MdoU/issues) com:
- Descrição clara do problema
- Passos para reproduzir
- Comportamento esperado vs atual
- Screenshots (se aplicável)
- Sistema operacional e versão do Python

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

```
MIT License

Copyright (c) 2025 [Seu Nome]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👤 Autor

**[Augusto Cesar Da Silva]**

- GitHub: [@Fa1kerXd](https://github.com/Fa1kerXd)
- Email: fa1ker@icloud.com

---

## 🙏 Agradecimentos

- [osu!](https://osu.ppy.sh/) - Pelo jogo incrível e API aberta
- [ppy](https://github.com/ppy) - Por manter o osu! open source
- [Qt/PySide6](https://www.qt.io/) - Framework de UI
- Comunidade osu! - Por todo o suporte

---

## 💬 Suporte

Precisa de ajuda? Há várias formas de obter suporte:

- 📖 [Documentação da API do osu!](https://osu.ppy.sh/docs/)
- 💬 [Discord do osu!](https://discord.gg/osu)
- 🐛 [Issues do GitHub](https://github.com/Fa1kerXd/MdoU/issues)
---

## ⚠️ Disclaimer

Este projeto **NÃO é afiliado** ao osu! ou ppy Pty Ltd. É um projeto da comunidade que usa a API pública oficial. Use por sua conta e risco.

**Respeite os Termos de Serviço do osu!:**
- Não abuse da API
- Não distribua conteúdo protegido por direitos autorais
- Use apenas para fins pessoais e educacionais

---

## 📊 Status do Projeto

![GitHub last commit](https://img.shields.io/github/last-commit/Fa1kerXd/MdoU)
![GitHub issues](https://img.shields.io/github/issues/Fa1kerXd/MdoU)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Fa1kerXd/MdoU)
![GitHub stars](https://img.shields.io/github/stars/Fa1kerXd/MdoU?style=social)

---

<div align="center">

**⭐ Se este projeto te ajudou, considere dar uma estrela! ⭐**

Feito com ❤️ e ☕ por [Augusto]

[⬆ Voltar ao topo](#MdoU)

</div>

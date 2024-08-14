# data-quality-project

## Pyenv

Instalação no Windows: https://github.com/pyenv-win/pyenv-win

Rodar comando no PowerShell para permitir executar os scripts:

`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

E depois restringir dessa forma:

`Set-ExecutionPolicy Restricted -Scope CurrentUser`

## Poetry

No PowersShell executar

`
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
`

Configurar variáveis de ambiente do poetry no PATH:
* Após a instalação, você precisará adicionar o diretório do Poetry ao seu PATH, caso o instalador não tenha feito isso automaticamente.
* Normalmente, o Poetry é instalado em C:\Users\SeuUsuario\AppData\Roaming\Python\Scripts. Para adicionar isso ao PATH:
* Abra o Painel de Controle -> Sistema e Segurança -> Sistema -> Configurações avançadas do sistema.
* Clique em "Variáveis de Ambiente" e em "Variáveis de usuário", selecione a variável Path e clique em "Editar".
* Adicione o caminho C:\Users\SeuUsuario\AppData\Roaming\Python\Scripts (substitua SeuUsuario pelo seu nome de usuário do Windows).
* Clique em "OK" para salvar as mudanças.

Rodar no diretório do projeto:
`
poetry init
poetry shell
poetry add mkdocs
poetry add mkdocs-mermaid2-plugin
poetry add mkdocs-material
poetry add 'mkdocstrings[python]'
poetry add taskipy 
poetry add isort
poetry add black
poetry add pytest


`

## Mkdocs

Comandos do mkdocs 

`
mkdocs new .
poetry run mkdocs serve -- renderiza o mkdocs no http://127.0.0.1:8000/
`

## Marmeid

Renderiza fluxogramas que pode ser gerado no Excalidraw e gera uma boa documentação no MkDocs

## Taskipy

Facilita na hora de rodar comandos no terminal

`
poetry run task doc
poetry run task run
poetry run task test
poetry run task kill
poetry run task format
`

Exceuta comandos configurados no pyproject.toml

## Configurar CI/CD

`
mkdir .github
cd .github
mkdir workflows
cd workflows
`

Criar CI.yml dentro de .github/workflows

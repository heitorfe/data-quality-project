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
`poetry init`

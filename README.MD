EXECUTANDO O PROGRAMA

Para executar o programa baixe a a pasta "next_version" localizada em "compilados"
e utilize o atalho "main"

-----------------------------------------

Ativando o ambiente virtual

.\virtualEnv\Scripts\Activate.ps1

Desativando o ambiente virtual

deactivate

Instalação das bibliotecas

pip install nome_da_biblioteca

-----------------------------------------

pyinstaller --windowed nome do arquivo com extenção

pyinstaller --onefile -w nome do arquivo com extenção {para programas com janelas}

pyinstaller --onefile nome do arquivo com extenção {para programas cmd}

pyinstaller --add-data="" caminho total da pasta;nome da pasta

pyinstaller --add-data="" caminho total do arquivo

pyinstaller --add-data="" caminho total do arquivo/pasta:pasta onde ficara o arquivo/pasta

pyinstaller --name="" Nome do arquivo executavel

pyinstaller --noconsole 

pyinstaller --icon="" caminho total do arquivo

-----------------------------------------

lista de comandos do GIT

git config

git status

git add .

git commit -m "Descrição do commit"

git push

git clone {url do repositorio}

git branch

git branch nome da ramificação

git branch -d nome da raamificação

git checkout nome da ramificação

git log --oneline

-----------------------------------------

VIDEOS

CUSTOMTKINTER: 
 https://youtu.be/sSHpbce70z8?si=p4sSeB_HrGgSslzI
"# sheet_work_python" 

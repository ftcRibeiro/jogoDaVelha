# Teste Prático DTI - Felipe Ribeiro
           __                  ____       _    __     ____         
          / /___  ____ _____  / __ \____ | |  / /__  / / /_  ____ _
     __  / / __ \/ __ `/ __ \/ / / / __ `/ | / / _ \/ / __ \/ __ `/
    / /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /| |/ /  __/ / / / / /_/ / 
    \____/\____/\__, /\____/_____/\__,_/ |___/\___/_/_/ /_/\__,_/  
               /____/                                             

# Ambiente
É necessário que uma versão python 3.7+ esteja instalada na máquina a rodar esta aplicação. Para a instalação das dependências de bibliotecas utilizadas, pasta rodar o comando na raiz do arquivo "api.py"

    pip install requirements.txt

Caso este comando não funcione, devido a possíveis versões de pip e python instalados, pode-se utilizar:

    python -m pip install requirements.txt

Após sucesso na instalação, basta utilizar executar o arquivo principal do sistema:

    python api.py

# Execução
Para execução do sistema, basta acessar a pasta src e executar o comando:

    python api.py

# Funcionamento
Para o correto funcionamento do sistema, é de suma importância que a arquitetura de pastas seja mantida.
## database
Nesta pasta são criados os arquivos para armazenamento de dados de partida. Para cada partida é criado um .csv com as informações necessárias.

## constants
Nesta pasta estão as referências de dados de vitórias possíveis. São utilizados para a validação de término de partida.

# Dos módulos
## api.py
Módulo que possui os endpoints e a criação de uma aplicação.
## validation.py
Módulo que possui os métodos para validação das requisições.
## service.py
Camada de regras de negócio. Nela é definido o fluxo de cada endpoint do sistema.
## dataInterface.py
Camada correspondente à de acesso a banco de dados. Como nesta demanda não era permitida a utilização de banco de dados, nesta camada está toda a lógica de registro de partidas e movimentos.
## utilities.py
Possui métodos para gerar a chave da partida, bem como para escolha aleatória de jogador a iniciar a partida.

# Considerações
Devido ao curto espaço de tempo para execução desta aplicação, não foram implementados testes unitários.

Outra consideração é dada quanto a etapa de validações de requições: não foram implementadas todas as concebidas, pelo caráter MVP necessário nessa demanda. Foram implementadas somente as mínimas.

# Endpoints
São dados pelos requeridos no escopo da demanda, bem como seus respectivos bodys. São eles:
## newGame

    localhost:5000/game

## newMovement

    localhost:5000/game/movement


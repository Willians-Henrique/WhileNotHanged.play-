# WhileNotHanged.play-
Jogo interativo educacional de forca em python

## COMO RODAR

### CRIAR AMBIENTE DEV
Abra o terminal e navegue até a pasta do projeto
Digite o seguinte comando para iniar um ambiente de desenvolvimento:
```bash
python -m venv venv
```
Acessamos nosso ambiente de desenvolvimento, usando o comando: 
```bash
venv\Scripts\activate
```

Após a criação do ambiente, vamos instalar a biblioteca pygames, execute o seguinte comando:
```bash
python -m pip install -U pygame==2.6.0
```
Após a biblioteca instalada, devemos salvar nossas dependências criando o arquivo requirements.txt

```bash
pip freeze > environments.txt
```

Para sair do ambiente virtual de desenvolvimento:
```bash
deactivate
```
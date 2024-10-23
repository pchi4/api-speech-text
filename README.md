
# Speech-to-Text API

Esta é uma API simples para conversão de fala em texto, desenvolvida em Python utilizando o Flask e o modelo Vosk. A API aceita arquivos de áudio e retorna o texto transcrito.

## Tecnologias

- Python
- Flask
- Vosk Speech Recognition

## Instalação

### Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)

### Passos para instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/pchi4/speech-to-text-api.git
   cd speech-to-text-api
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Baixe o modelo Vosk para o idioma desejado (exemplo para inglês):

   ```bash
   mkdir -p models
   wget -O models/vosk-model-en-us-0.22.zip https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip
   unzip models/vosk-model-en-us-0.22.zip -d models/
   ```

## Uso

1. Inicie a API:

   ```bash
   python app.py
   ```

   A API estará disponível em `http://localhost:5000`.

2. Envie uma requisição POST para transcrever um arquivo de áudio:

   - **Endpoint**: `/transcribe`
   - **Método**: POST
   - **Body**: Um arquivo de áudio (formato WAV, MP3, etc.)

   ### Exemplo usando `curl`:

   ```bash
   curl -X POST -F "file=@caminho/para/seu/arquivo.wav" http://localhost:5000/transcribe
   ```

   ### Exemplo de resposta:

   ```json
   {
       "transcription": "Texto transcrito da fala"
   }
   ```

## Estrutura do Projeto

```
speech-to-text-api/
│
├── app.py               # Arquivo principal da API
├── requirements.txt     # Dependências do projeto
└── models/              # Diretório para modelos Vosk
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

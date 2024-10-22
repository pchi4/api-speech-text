from flask import Flask, request, jsonify
import wave
from vosk import Model, KaldiRecognizer
import json


app = Flask(__name__)

model_path = "./vosk-model-small-en-us-0.15"
model = Model(model_path)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "Arquivo de áudio não enviado'"}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        wf = wave.open(file.stream, "rb") 
    except Exception as e:
        return jsonify({"error": f"Failed to read audio file: {str(e)}"}), 400

    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
        return jsonify({"error": "Audio must be mono PCM 16 bit 16kHz"}), 400
    
    print(f"Channels: {wf.getnchannels()}")
    print(f"Sample width: {wf.getsampwidth()}")
    print(f"Frame rate: {wf.getframerate()}")

    recognizer = KaldiRecognizer(model, wf.getframerate())
    results = []
    resultado_final = ""


    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            print(recognizer.Result())
            resultado = recognizer.Result()
            resultado_json = json.loads(resultado)
            resultado_final += resultado_json.get('text', '')
        else:
          resultado_parcial = recognizer.PartialResult()
          resultado_parcial_json = json.loads(resultado_parcial)
          resultado_final += resultado_parcial_json.get('partial', '')


    if not resultado_final:
        return jsonify({'error': 'Nenhum texto reconhecido'}), 400

    return jsonify({'transcription': resultado_final})


if __name__ == '__main__':
    app.run(port=5000)

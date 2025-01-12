import whisper

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]

if __name__ == "__main__":
    file_path = "path_to_audio_or_video_file"
    print(transcribe_audio(file_path))

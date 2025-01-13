import os
import whisper
import subprocess

def transcribe_audio(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Handle video files by extracting audio
    if file_path.lower().endswith((".mp4", ".mkv", ".avi", ".mov")):
        audio_path = file_path.rsplit(".", 1)[0] + ".mp3"
        # Use FFmpeg to extract audio
        subprocess.run(
            ["ffmpeg", "-i", file_path, "-q:a", "0", "-map", "a", audio_path, "-y"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        file_path = audio_path

    # Load Whisper model
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]

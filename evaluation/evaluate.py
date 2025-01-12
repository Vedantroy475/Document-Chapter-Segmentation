from src.transcription import transcribe_audio
from src.segmentation import segment_text

def evaluate(file_path):
    transcription = transcribe_audio(file_path)
    chapters = segment_text(transcription)
    return chapters

if __name__ == "__main__":
    file_path = "path_to_sample_file"
    chapters = evaluate(file_path)
    for idx, chapter in enumerate(chapters):
        print(f"Chapter {idx+1}:\n{chapter}\n")

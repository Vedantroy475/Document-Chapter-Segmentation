**Project Title:** Document Chapter Segmentation.

## Overview
This project processes large documents, including **audio files**, **video files**, and **text files**, and segments them into meaningful chapters. It utilizes **Google’s Gemini AI models** for transcription and chapter segmentation.

---

**Approach:**

* Transcription of audio/video.
* Text segmentation using NLP techniques.
* Evaluation pipeline for testing robustness.

---

## Features
1. **Transcription and Segmentation**:
   - Transcribes audio (`.mp3`) and video (`.mp4`) files.
   - Segments transcriptions or raw text files into meaningful chapters.

2. **Gemini API Integration**:
   - Uses Google’s Gemini AI model (`gemini-1.5-pro-001`) for accurate transcription and segmentation.

3. **Output Storage**:
   - Segmented chapters are saved as Markdown files in the `results/` directory.

4. **Retry Logic**:
   - Ensures robust transcription with multiple attempts in case of failures.

---

## Project Structure
```
Document-Chapter-Segmentation/
│
├── data/
│   ├── samples/                   # Sample input files for testing
│       ├── audio.mp3              # Test audio file
│       ├── video.mp4              # Test video file
│       ├── document.txt           # Test text file
│
├── results/                       # Segmented chapter outputs
│   ├── audio file/
│       ├── audio_segmented_chapters.md
│   ├── video file/
│       ├── video_segmented_chapters.md
│   ├── document file/
│       ├── document_segmented_chapters.md
│
├── notebooks/
│   ├── evaluation.ipynb           # Jupyter Notebook for running tests
│
├── .env                           # Contains API keys (excluded from Git)
├── .gitignore                     # Excludes sensitive files like .env
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
```

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Document-Chapter-Segmentation.git
   cd Document-Chapter-Segmentation
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   venv\Scripts\activate           # On Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your **Gemini API Key** to a `.env` file in the root directory:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

---

## Usage
### Run Tests via Jupyter Notebook
1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Open `notebooks/evaluation.ipynb` and run the cells to process sample files.

---

### Run the Script for Each File Type
#### **Audio File**
```python
# Path: data/samples/audio.mp3
transcription_result = transcribe_audio_with_segmented_chapters(audio_file_path)
```

#### **Video File**
```python
# Path: data/samples/video.mp4
transcription_result = transcribe_video_with_segmented_chapters(video_file_path)
```

#### **Text File**
```python
# Path: data/samples/document.txt
transcription_result = transcribe_document_with_segmented_chapters(text_file_path)
```



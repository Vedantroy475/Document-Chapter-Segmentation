**# Document Chapter Segmentation

## Overview
This project processes large documents, including **audio files**, **video files**, and **text files**, and segments them into meaningful chapters. It integrates **Google’s Gemini AI models** for transcription and chapter segmentation while incorporating **evaluation metrics** to assess segmentation accuracy.

---

## Approach
- **Transcription & Segmentation:**
  - Audio/video transcription using **AssemblyAI**.
  - Text segmentation via **Google Gemini AI** and NLP techniques.
  - Splits long videos into manageable segments to fit model constraints.

- **Evaluation Pipeline:**
  - **Semantic Consistency**: Measures coherence within segments.
  - **Relevance Score**: Assesses how well the segmentation captures key ideas.
  - Compares automated segmentation with human-annotated benchmarks.

---

## Features
### **1. Multi-Format Processing**
- Supports **audio (`.mp3`)**, **video (`.mp4`)**, and **text (`.txt`)** files.
- Automatically splits video files exceeding model constraints.

### **2. AI-Based Segmentation**
- **AssemblyAI**: Transcribes video/audio into text.
- **Gemini AI**: Segments transcriptions into structured chapters with bullet points.

### **3. Robust Data Collection Pipeline**
- Fetches diverse datasets (lectures, podcasts, educational content) for testing.
- Preprocesses and standardizes data before analysis.

### **4. Evaluation & Validation**
- Implements **semantic consistency** and **relevance scoring** to assess segmentation quality.
- Outputs structured evaluation metrics for each segment.

### **5. Storage & Output Handling**
- Saves segmented chapters as **Markdown files** in `results/` directory.
- Handles **file naming issues for non-ASCII characters**.

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
│   ├── document file/
│       ├── document_segmented_chapters.md
│   ├── video file/
│       ├── video_segmented_chapters.md
│   ├── audio file/
│       ├── audio_segmented_chapters.md
│   ├── youtube transcription/
│       ├── youtube_segmented_chapters.md
│
├── notebooks/
│   ├── evaluation.ipynb           # Jupyter Notebook for evaluation metrics
│
├── .env                           # API keys and environment variables
├── .gitignore                     # Excludes sensitive files like .env
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
```

---

## Installation
### **1. Clone the Repository**
```bash
git clone https://github.com/<your-username>/Document-Chapter-Segmentation.git
cd Document-Chapter-Segmentation
```

### **2. Create and Activate Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Configure API Keys**
Create a `.env` file in the root directory and add:
```ini
GEMINI_API_KEY=your_api_key_here
ASSEMBLYAI_API_KEY=your_api_key_here
```

---

## Usage
### **Run Tests via Jupyter Notebook**
```bash
jupyter notebook
```
Open `notebooks/evaluation.ipynb` and run the cells to evaluate segmentation quality.

### **Transcribing & Segmenting Files**
#### **Audio File Processing**
```python
transcription_result = transcribe_audio_with_segmented_chapters("data/samples/audio.mp3")
```

#### **Video File Processing**
```python
transcription_result = transcribe_video_with_segmented_chapters("data/samples/video.mp4")
```

#### **Text File Processing**
```python
transcription_result = transcribe_document_with_segmented_chapters("data/samples/document.txt")
```

---

## Evaluation Metrics
After processing, the system outputs **segmentation quality scores**:
```bash
Evaluating segmentation quality...
Average Semantic Consistency: 0.54
Average Relevance Score: 0.78
```
- **Semantic Consistency**: Ensures coherence within a segment.
- **Relevance Score**: Checks if segmentation accurately captures key content.

The scores help refine the segmentation algorithm and improve accuracy.

---

## Future Improvements
- Optimize segmentation logic for better **accuracy & efficiency**.
- Explore **cheaper alternative models** to reduce processing costs.
- Collect human-labeled evaluation datasets for **benchmarking**.

---

## Contribution
Pull requests are welcome! If you find a bug or have feature requests, open an issue or submit a PR.

---

## License
This project is licensed under the MIT License.


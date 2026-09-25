<div align="center">
  <a href="https://youtu.be/nwx4ph8iELA">
    <img src="https://img.youtube.com/vi/nwx4ph8iELA/0.jpg" alt="Parakeet Redux: Nvidia's 178MB AI Beats Whisper Running 113× Faster on CPU!">
  </a>
  <h3>📺 <a href="https://youtu.be/nwx4ph8iELA">Watch the full video on YouTube</a></h3>
</div>

# ⚡ Parakeet Redux Local Transcriber

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B.svg?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Moondream AI](https://img.shields.io/badge/Moondream-Parakeet--Redux-7C3AED.svg?style=flat)](https://huggingface.co/moondream/parakeet-redux)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC--BY--4.0-10B981.svg?style=flat)](https://creativecommons.org/licenses/by/4.0/)

A lightweight, private speech-to-text application powered by `moondream/parakeet-redux`. Automatically converts uploaded video or audio files into timestamped text transcripts locally on your computer at 113× real-time speed.

| Step 1: Input | Step 2: AI Action | Step 3: Result |
| :--- | :--- | :--- |
| **Media Upload**<br>Upload any video (`.mp4`, `.mov`) or audio (`.mp3`, `.wav`) file. | **1.58-Bit AI Processing**<br>System FFmpeg standardizes audio; Parakeet Redux transcribes instantly on CPU. | **Timestamped Transcript**<br>View sentence segments with time codes and download `.md` output. |

---

## 🛠️ System Requirements & Prerequisites

Before running the application, make sure your computer has Python 3.9 or higher and system-level **FFmpeg** installed to extract audio from video containers.

### Installing FFmpeg
* **Windows (PowerShell Admin / Chocolatey or Winget):**
  ```powershell
  winget install --id FFmpeg-FFmpeg.FFmpeg -e
  ```
* **Ubuntu / Debian:**
  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```
* **macOS:**
  ```bash
  brew install ffmpeg
  ```

---

## 🚀 Quick Setup & Installation

Run the following single PowerShell command to install all required dependencies:

```powershell
pip install streamlit moondream numpy
```

---

## 💻 Running the Application

Launch the Streamlit web interface with the following command:

```powershell
streamlit run app.py
```

The web interface will open automatically in your browser at `http://localhost:8501`. On the first upload, the application downloads the lightweight 178 MB model weights directly into your local cache.

---

## 📁 Repository Structure

```
├── app.py
├── requirements.txt
└── README.md
```

---

## 🌟 5 Practical Real-World Use Cases

1. 🎙️ **Local Meeting & Podcast Transcription:** Convert multi-hour meeting recordings into text locally with zero cloud API costs or privacy leaks.
2. 🔍 **Voice Note Search Vault:** Turn scattered voice memos into searchable text files for personal knowledge management.
3. 📚 **Lecture Chapter Indexing:** Automatically split long university lectures into readable notes using built-in pause detection.
4. 🌐 **Global Accent & Language Testing:** Test transcription accuracy across 25 supported global languages natively.
5. 💻 **Hands-Free Developer Voice Notes:** Speak technical thoughts or bug descriptions directly into local structured markdown logs.

---

## 🔮 5 Future Planned Features

1. ⏱️ **Word-Level Precision Timestamps:** Highlight exact spoken words in real time as media plays back.
2. 🏷️ **Speaker Identification (Diarization):** Automatically label different speakers in multi-person meetings.
3. 📊 **Interactive Transcript Search & Filter:** Instantly filter transcript lines by keyword or timestamp range.
4. 📝 **Automated AI Meeting Summarization:** Feed generated transcripts into local LLMs to produce executive summaries.
5. 📂 **Batch Folder Processing:** Drag and drop an entire directory of audio files for background processing.

---

## 🏷️ Keywords & SEO
`moondream` `parakeet-redux` `1.58-bit-ai` `ternary-quantization` `local-speech-to-text` `ffmpeg-audio-extraction` `streamlit-transcriber` `cpu-speech-recognition` `faster-than-whisper`

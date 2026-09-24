import streamlit as st
import tempfile
import os
import time
import subprocess
# pyrefly: ignore [missing-import]
import moondream as md

st.set_page_config(
    page_title="Parakeet-Redux Local Transcriber",
    page_icon="⚡",
    layout="wide"
)

def convert_to_wav(input_path: str, output_path: str) -> float:
    """Uses system FFmpeg to convert media input to a clean 16kHz Mono PCM WAV audio file. Returns conversion duration in seconds."""
    start_time = time.time()
    command = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        output_path
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise Exception(f"FFmpeg conversion failed: {result.stderr.decode('utf-8', errors='ignore')}")
    return time.time() - start_time

@st.cache_resource
def load_speech_model():
    """Initializes Moondream Photon engine downloading 178MB ternary weights on first run."""
    return md.photon("moondream/parakeet-redux")

st.title("⚡ Local Meeting & Podcast Transcriber")
st.markdown("Powered by `moondream/parakeet-redux` (1.58-Bit Ternary AI). 113× CPU real-time transcription speed.")

SUPPORTED_FORMATS = [
    "mp4", "mkv", "avi", "mov", "webm", "flv",
    "mp3", "wav", "m4a", "flac", "aac", "ogg"
]

uploaded_file = st.file_uploader(
    "Upload a Video or Audio file for Instant Local Transcription",
    type=SUPPORTED_FORMATS
)

if uploaded_file is not None:
    file_ext = uploaded_file.name.split('.')[-1].lower()
    total_start_time = time.time()
    
    with tempfile.TemporaryDirectory() as temp_dir:
        input_file_path = os.path.join(temp_dir, f"input.{file_ext}")
        wav_file_path = os.path.join(temp_dir, "audio.wav")
        
        with open(input_file_path, "wb") as f:
            f.write(uploaded_file.read())
            
        st.info("Extracting and standardizing audio to 16kHz WAV format...")
        
        try:
            conversion_time = convert_to_wav(input_file_path, wav_file_path)
        except Exception as e:
            st.error(f"Audio processing error: {e}")
            st.stop()
            
        st.success(f"Audio standardized in {conversion_time:.2f}s! Transcribing locally...")
        
        with st.spinner("Transcribing speech with 1.58-bit Ternary model..."):
            try:
                model_start_time = time.time()
                speech_model = load_speech_model()
                result = speech_model.transcribe(audio=wav_file_path, timestamps="segment")
                transcription_time = time.time() - model_start_time
                total_execution_time = time.time() - total_start_time
                
                # Display performance metrics
                mcol1, mcol2, mcol3 = st.columns(3)
                mcol1.metric("Audio Extraction Time", f"{conversion_time:.2f} s")
                mcol2.metric("AI Transcription Time", f"{transcription_time:.2f} s")
                mcol3.metric("Total Execution Time", f"{total_execution_time:.2f} s")
                
                st.subheader("Transcription Results")
                
                transcript_lines = []
                for segment in result.get("segments", []):
                    start = segment.get("start", 0.0)
                    end = segment.get("end", 0.0)
                    text = segment.get("text", "").strip()
                    
                    start_str = f"{int(start // 60):02d}:{int(start % 60):02d}"
                    end_str = f"{int(end // 60):02d}:{int(end % 60):02d}"
                    
                    formatted_ui_line = f"**`[{start_str} - {end_str}]`** {text}"
                    st.markdown(formatted_ui_line)
                    transcript_lines.append(f"* **`[{start_str} - {end_str}]`** {text}")
                
                body_transcript = "\n\n".join(transcript_lines)
                
                # Construct single comprehensive Markdown report with clean formatting
                full_report = f"""# ⚡ Parakeet Redux Transcription Report

## ⏱️ Execution Performance Summary
* **Source Media File:** `{uploaded_file.name}`
* **Audio Extraction Time (FFmpeg):** `{conversion_time:.2f} seconds`
* **AI Model Transcription Time:** `{transcription_time:.2f} seconds`
* **Total End-to-End Pipeline Runtime:** `{total_execution_time:.2f} seconds`

---

## 📝 Timestamped Transcript

{body_transcript}
"""
                
                # Save strictly SINGLE output file to outputs directory
                os.makedirs("outputs", exist_ok=True)
                output_md_path = os.path.join("outputs", "outputs.md")
                with open(output_md_path, "w", encoding="utf-8") as omf:
                    omf.write(full_report)
                
                st.download_button(
                    label="📥 Download Full Report (.md)",
                    data=full_report,
                    file_name=f"{uploaded_file.name}_report.md",
                    mime="text/markdown"
                )
                
            except Exception as e:
                st.error(f"Transcription failed: {e}")

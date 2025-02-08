# Media_Transcriber
Media Transcription Automation
# 🎙️ Media File Transcription Script  

## 🚀 Overview  
📌 This Python script **automates** the transcription of **audio and video** files using **OpenAI’s Whisper model**. It scans a folder for media files (**🎵 MP3, 🎥 MP4, 🔊 WAV**) and transcribes them into **📄 text (`.txt`) or 🗂️ JSON (`.json`)** format.  

---

## ✨ Features  
✅ **🔍 Recursive Folder Search** – Automatically detects media files in subdirectories.  
✅ **🧠 AI-Powered Transcription** – Uses **Whisper AI** for accurate speech-to-text conversion.  
✅ **📂 Multiple Output Formats** – Saves transcriptions in **`.txt` and `.json`** formats.  
✅ **⚙️ Error Handling & Logging** – Tracks issues and logs them for debugging.  
✅ **📊 Progress Visualization** – Uses **`tqdm`** to display real-time progress.  

---

## 📌 Prerequisites  
Before running the script, ensure you have the following installed:  

### 🔧 System Requirements  
- 🐍 **Python 3.7+**  
- 📦 **Install Dependencies:**  
  ```bash
  pip install openai-whisper tqdm
  ```

### 🎯 Download Whisper Model:
(e.g., tiny, small, medium, large)
```bash
whisper --model medium
```

---

## 🚀 Usage

1️⃣ **Run the script**:
```bash
python transcribe.py
```

2️⃣ **Provide Input**:
📂 When prompted, enter the folder path where media files are stored.

3️⃣ **Confirm Transcription**:
📜 The script lists all found media files and asks for confirmation before transcription.

4️⃣ **Choose Output Format**:
📝 Select either `txt` or `json` format for the transcription output.

---

## 📂 Output
🗂️ A list of found media files is saved as `found_media_files.txt` in the input folder.
📝 Transcriptions are saved next to each media file with `.txt` or `.json` extensions.

### 📌 Example Output:
```plaintext
/media/sample.mp3   →  /media/sample.mp3.txt
/media/video.mp4    →  /media/video.mp4.json
```

---

## 🚀 Enhancements
Future improvements may include:

⚡ **Multi-threaded Processing** for faster transcription.
🖥️ **GUI Integration** for a more user-friendly experience.
🌍 **Additional Language Support** beyond English.

---

## 📜 License
This project is licensed under the MIT License.

---

## 📬 Contact
📧 For any questions, feel free to reach out via GitHub Issues or email. 🚀

---

## 🌟 Show Your Support
If you find this useful, ⭐ Star this repo on GitHub!

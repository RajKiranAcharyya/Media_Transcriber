import os
import glob
import whisper
import json
import logging
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_folder_path():
    folder_path = input("Enter the folder path where media files are stored: ").strip()
    if not os.path.exists(folder_path):
        logging.error("The provided path does not exist.")
        return None
    return folder_path


def find_media_files(folder_path):
    try:
        media_files = []
        extensions = ["*.mp3", "*.mp4", "*.wav"]
        for ext in extensions:
            media_files.extend(
                glob.glob(os.path.join(folder_path, "**", ext), recursive=True)
            )
        return media_files
    except Exception as e:
        logging.error(f"Error while searching for media files: {e}")
        return []


def save_media_list(media_files, folder_path):
    try:
        output_file = os.path.join(folder_path, "found_media_files.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            for file in media_files:
                f.write(file + "\n")
        logging.info(f"List of media files saved to: {output_file}")
    except Exception as e:
        logging.error(f"Error while saving media list: {e}")


def transcribe_media_files(media_files, output_format="txt"):
    try:
        model = whisper.load_model("tiny")
    except Exception as e:
        logging.error(f"Error loading Whisper model: {e}")
        return

    for file_path in tqdm(media_files, desc="Transcribing Files", unit="file"):
        try:
            logging.info(f"Transcribing: {file_path}")
            result = model.transcribe(file_path)

            if output_format == "txt":
                output_file = f"{file_path}.txt"
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(result["text"])
            elif output_format == "json":
                output_file = f"{file_path}.json"
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(
                        {"file": file_path, "transcription": result["text"]},
                        f,
                        indent=4,
                    )
            else:
                logging.warning(f"Unsupported format: {output_format}")

            logging.info(f"Saved transcription to: {output_file}")
        except Exception as e:
            logging.error(f"Error while transcribing {file_path}: {e}")


def main():
    folder_path = get_folder_path()
    if not folder_path:
        return

    media_files = find_media_files(folder_path)
    if not media_files:
        logging.warning("No media files found in the specified folder.")
        return

    save_media_list(media_files, folder_path)

    confirm = input("Do you want to start transcription? (yes/no): ").strip().lower()
    if confirm != "yes":
        logging.info("Transcription aborted by user.")
        return

    output_format = input("Enter output format (txt/json): ").strip().lower()
    if output_format not in ["txt", "json"]:
        logging.warning("Invalid format selected. Defaulting to 'txt'.")
        output_format = "txt"

    transcribe_media_files(media_files, output_format)


if __name__ == "__main__":
    main()

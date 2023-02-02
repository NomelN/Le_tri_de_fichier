from pathlib import Path

dossier_extension = {".mp3": "Musique",
                     ".waw": "Musique",
                     ".flac": "Musique",
                     ".avi": "Videos",
                     ".mp4": "Videos",
                     ".gif": "Videos",
                     ".bmp": "Images",
                     ".png": "Images",
                     ".jpg": "Images",
                     ".txt": "Documents",
                     ".pptx": "Documents",
                     ".csv": "Documents",
                     ".xls": "Documents",
                     ".odp": "Documents",
                     ".pages": "Documents"}

dossier_data = Path.home()/"Downloads"/"sources"/"data"

fichiers = [f for f in dossier_data.iterdir() if f.is_file()]
for f in fichiers:
    autres_dossier = dossier_data / dossier_extension.get(f.suffix, "Divers")
    autres_dossier.mkdir(exist_ok=True)
    f.rename(autres_dossier / f.name)


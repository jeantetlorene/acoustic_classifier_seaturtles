from pathlib import Path
import shutil

# ==================================================
# PATHS
# ==================================================

WAV_SOURCE = r"C:\Users\cheva\Desktop\recapted add backup\IMB_05_CC-09-72_01.02.2023\new_segments\IMB_05_08h10_08h20.wav"

DATASET_ROOT = r"C:\Users\cheva\Desktop\github_projects\acoustic_classifier_seaturtles\juliana_tests\Dataset_Example"

FILE_NAME = "IMB_05_08h10_08h20"

# ==================================================
# CREATE FOLDERS
# ==================================================

root = Path(DATASET_ROOT)

audio_dir = root / "Audio"
annotations_dir = root / "Annotations"
datafiles_dir = root / "DataFiles"
datasets_dir = root / "Datasets"

audio_dir.mkdir(parents=True, exist_ok=True)
annotations_dir.mkdir(parents=True, exist_ok=True)
datafiles_dir.mkdir(parents=True, exist_ok=True)
datasets_dir.mkdir(parents=True, exist_ok=True)

print("Folders created.")

# ==================================================
# COPY WAV
# ==================================================

destination_wav = audio_dir / f"{FILE_NAME}.wav"

shutil.copy2(
    WAV_SOURCE,
    destination_wav
)

print("WAV copied:")
print(destination_wav)

# ==================================================
# CREATE TRAIN / VAL / TEST
# ==================================================

for split in ["train", "val", "test"]:

    txt_file = datafiles_dir / f"{split}.txt"

    with open(txt_file, "w") as f:
        f.write(FILE_NAME)

    print(f"Created {split}.txt")

print()
print("DONE")
import os
LINE = "I am sorry I deleted your mother's voicemail while clearing old messages I thought nobody needed.\nI learned that old does not mean unwanted, so now I ask before I delete anything with a voice in it."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

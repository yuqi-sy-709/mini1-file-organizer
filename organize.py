from pathlib import Path
Map={
    ".jpg":"images",
    ".png":"images",
    ".pdf":"docs",
    ".txt":"docs",
    ".docx":"docs",
    ".mp4":"media",
    ".mp3":"media",
}
for f in Path("test_mess").iterdir():
    if f.is_file():
        ext=f.suffix.lower()
        folder=Map.get(ext,"others")
        print(f.name,"→",folder+"/")
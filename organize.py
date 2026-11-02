import shutil
import sys
from pathlib import Path
mode = "preview" if len(sys.argv) == 1 else "real"
print(f"当前模式：{mode}（预览只打印计划，真搬运才会实际移动文件）")
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
        ext = f.suffix.lower()
        folder = Map.get(ext, "others")
        target_dir = Path(folder)
        target_file = target_dir / f.name
        if mode == "preview":
            print(f"[预览] {f.name} → {folder}/")
        else:
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(f), str(target_file))
            print(f"[已搬] {f.name} → {folder}/")

        
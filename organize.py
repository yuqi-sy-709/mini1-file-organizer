import os
import shutil
import sys
from datetime import datetime
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
BASE = Path(__file__).parent
LOG = BASE / "organize.log"

for f in (BASE / "test_mess").iterdir():
    if f.is_file():
        ext = f.suffix.lower()
        folder = Map.get(ext, "others")
        month=datetime.fromtimestamp(os.path.getmtime(f)).strftime("%Y-%m")
        target_dir = BASE / folder / month
        target_file = target_dir / f.name
        if mode == "preview":
            print(f"[预览] {f.name} → {folder}/{month}/")
        else:
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(f), str(target_file))
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(LOG, "a", encoding="utf-8") as log:
                log.write(f"{now} | {f.name} | {folder}/{month}/\n")
            print(f"[已搬] {f.name} → {folder}/{month}/")   

        
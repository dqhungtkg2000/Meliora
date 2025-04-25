import pyperclip
import time

LOG_FILE = "clipboard_log.txt"
pyperclip.copy("")

def log_clipboard():
    prev_clip = ""
    print("Clipboard logger activated. Ctrl+C to stop")
    
    try:
        while True:
            cur_clip = pyperclip.paste()
            if cur_clip != prev_clip and cur_clip.strip():
                log_entry = f"{cur_clip}\n"
                
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write(log_entry)
                prev_clip = cur_clip
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("Script stopped")

if __name__ == "__main__":
    log_clipboard()    
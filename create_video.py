from moviepy.editor import TextClip, CompositeVideoClip
import datetime
import os

def make_video():
    today = datetime.date.today().strftime('%Y%m%d')
    script_file = f"content/shorts_script_{today}.txt"
    output_file = f"videos/final_short_{today}.mp4"

    if not os.path.exists(script_file):
        print("Script file not found:", script_file)
        return

    with open(script_file, "r", encoding="utf-8") as f:
        text = f.read()

    clip = TextClip(text, fontsize=70, color='white', size=(1080, 1920), method='caption', bg_color='black', duration=15)
    final = CompositeVideoClip([clip])
    final.write_videofile(output_file, fps=24)

if _name_ == "_main_":
    make_video()

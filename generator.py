import os
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
from gtts import gTTS

def create_wisdom_reel(quote_text, output_filename="output/wisdom_reel.mp4"):
    # 1. Generate Voiceover using Google Text-to-Speech (or plug in ElevenLabs later)
    tts = gTTS(text=quote_text, lang='en', tld='com')
    audio_path = "assets/temp_voice.mp3"
    tts.save(audio_path)
    
    # 2. Load background video (vertical 9:16 dark minimalist loop)
    base_clip = VideoFileClip("assets/background/ambient_loop.mp4").subclipped(0, 15)
    
    # 3. Load generated voiceover
    voice_audio = AudioFileClip(audio_path)
    video_duration = min(voice_audio.duration, base_clip.duration)
    base_clip = base_clip.set_duration(video_duration)
    
    # 4. Create kinetic typography / text overlay
    txt_clip = TextClip(
        quote_text, 
        fontsize=40, 
        color='white', 
        font='Arial-Bold', 
        size=(900, 1200), 
        method='caption',
        align='center'
    ).set_duration(video_duration).set_position(('center', 'center'))
    
    # 5. Composite elements
    final_video = CompositeVideoClip([base_clip, txt_clip]).set_audio(voice_audio)
    
    # 6. Export file
    os.makedirs("output", exist_ok=True)
    final_video.write_videofile(output_filename, fps=30, codec='libx264', audio_codec='aac')
    print(f"Reel successfully generated at: {output_filename}")

if __name__ == "__main__":
    sample_text = "The impediment to action advances action. What stands in the way becomes the way."
    create_wisdom_reel(sample_text)

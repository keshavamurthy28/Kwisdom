import streamlit as st
import os
from generator import create_wisdom_reel

st.set_page_config(page_title="Wisdom Reel Generator", page_icon="✨", layout="centered")

st.title("✨ Moral & Philosophical Reel Generator")
st.markdown("Create automated, high-value knowledge reels without touching a video editor.")

# Input area for your ideas/scripts
script_input = st.text_area(
    "Enter your wisdom script or quote (Max 50-60 words for a punchy 15s reel):",
    value="Waste no more time arguing about what a good person should be. Be one."
)

if st.button("🎬 Render Reel"):
    if not script_input.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Synthesizing voice, compiling typography, and rendering video..."):
            try:
                output_path = "output/wisdom_reel.mp4"
                create_wisdom_reel(script_input, output_path)
                st.success("Reel rendered successfully!")
                
                # Display and offer download
                st.video(output_path)
                with open(output_path, "rb") as file:
                    st.download_button(
                        label="📥 Download Final Reel (.mp4)",
                        data=file,
                        file_name="wisdom_reel.mp4",
                        mime="video/mp4"
                    )
            except Exception as e:
                st.error(f"Error during rendering: {e}")

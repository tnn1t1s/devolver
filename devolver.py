"""
Video Splitter and Rearranger

Introduction:
--------------
This script is an exploration into the nature of human perception, pattern recognition,
and meaning-making processes. It draws inspiration from phenomenology, the philosophical
study of consciousness and direct experience. 

Human beings have a remarkable ability to recognize patterns and draw meaning from seemingly
incoherent or fragmented information. This capacity allows us to make sense of our world,
even when presented with incomplete or scrambled data. Our brains are constantly working
to construct coherent narratives and find order in chaos.

This tool challenges our perceptual and cognitive processes by taking a coherent video,
breaking it into pieces based on audio transients (sudden changes in sound), and then
randomly rearranging these pieces. The result is a new video that, while composed of
familiar elements, presents them in an unfamiliar order.

From a phenomenological perspective, this process invites us to reflect on:

1. The nature of temporal experience: How do we perceive and make sense of time when
   familiar sequences are disrupted?

2. The relationship between audio and visual perception: How does the reorganization
   of audio cues affect our interpretation of visual information?

3. The process of meaning-making: How does our mind attempt to construct a coherent
   narrative or meaning from the rearranged segments?

4. The role of expectation in perception: How do our expectations, based on our original
   understanding of the video, influence our experience of the rearranged version?

By engaging with the output of this tool, users are invited to become aware of their
own perceptual processes, the assumptions they make when interpreting sensory input,
and the fascinating ability of the human mind to find patterns and create meaning,
even in seemingly chaotic or random arrangements.

This script serves not just as a video processing tool, but as a catalyst for
reflection on the nature of human consciousness, perception, and meaning-making.

Usage:
------
python video_splitter_rearranger.py input_video.mp4 output_video.mp4 [-t THRESHOLD] [-p]

Arguments:
  input             Path to the input video file
  output            Path for the output video file
  -t, --threshold   Threshold for transient detection (range: 0.0 to 1.0, default: 0.5)
  -p, --play        Play the output video after processing

Dependencies:
-------------
- moviepy
- librosa
- numpy

Make sure to install these dependencies using pip:
pip install moviepy librosa numpy

Note: This script requires FFmpeg to be installed on your system.

"""

import random
import numpy as np
import argparse
import subprocess
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import librosa

def split_video_on_transients(video_path, threshold=0.5):
    """
    Split a video into clips based on audio transients.

    This function performs the following steps:
    1. Load the video and extract its audio.
    2. Detect onsets (sudden changes in audio) using librosa.
    3. Apply a threshold to filter the detected onsets.
    4. Split the video at the points of the filtered onsets.

    Parameters:
    video_path (str): Path to the input video file.
    threshold (float): A value between 0.0 and 1.0 that determines the sensitivity
                       of onset detection. Lower values result in more splits.

    Returns:
    list: A list of VideoFileClip objects, each representing a segment of the original video.
    """
    # Load the video
    video = VideoFileClip(video_path)
    
    # Extract audio from the video
    audio = video.audio.to_soundarray(fps=44100)
    if audio.ndim == 2:
        audio = audio.mean(axis=1)  # Convert stereo to mono
    
    # Detect onsets
    onset_env = librosa.onset.onset_strength(y=audio, sr=44100)
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=44100)
    
    # Apply threshold
    onset_env_thresh = onset_env[onset_frames]
    onset_frames = onset_frames[onset_env_thresh > threshold * onset_env_thresh.max()]
    
    onset_times = librosa.frames_to_time(onset_frames, sr=44100)
    
    # Split video at onsets
    clips = []
    for i in range(len(onset_times)):
        start_time = onset_times[i]
        end_time = onset_times[i+1] if i+1 < len(onset_times) else video.duration
        clip = video.subclip(start_time, end_time)
        clips.append(clip)
    
    return clips

def rearrange_clips(clips):
    """
    Randomly rearrange the order of video clips.

    This function shuffles the list of clips, creating a new, random arrangement.
    This step is crucial in challenging our perception and meaning-making processes.

    Parameters:
    clips (list): A list of VideoFileClip objects.

    Returns:
    list: A shuffled list of the input VideoFileClip objects.
    """
    return random.sample(clips, len(clips))

def play_video(video_path):
    """
    Attempt to play the video using an available video player.

    This function tries to open the video with VLC, IINA, or QuickTime Player,
    in that order of preference.

    Parameters:
    video_path (str): Path to the video file to be played.
    """
    if os.path.exists('/Applications/VLC.app'):
        subprocess.Popen(['/Applications/VLC.app/Contents/MacOS/VLC', video_path])
    elif os.path.exists('/Applications/IINA.app'):
        subprocess.Popen(['/Applications/IINA.app/Contents/MacOS/IINA', video_path])
    else:
        subprocess.Popen(['open', '-a', 'QuickTime Player', video_path])

def main(input_path, output_path, threshold, play):
    """
    Main function to process the video.

    This function orchestrates the entire process:
    1. Split the video based on audio transients.
    2. Rearrange the resulting clips randomly.
    3. Concatenate the rearranged clips into a new video.
    4. Optionally play the resulting video.

    Parameters:
    input_path (str): Path to the input video file.
    output_path (str): Path where the output video will be saved.
    threshold (float): Threshold for transient detection.
    play (bool): Whether to play the output video after processing.
    """
    # Split the video into clips based on transients
    clips = split_video_on_transients(input_path, threshold)
    
    # Rearrange the clips randomly
    rearranged_clips = rearrange_clips(clips)
    
    # Concatenate the rearranged clips
    final_video = concatenate_videoclips(rearranged_clips)
    
    # Write the final video to file
    final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')
    
    if play:
        play_video(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split and rearrange video based on transients.")
    parser.add_argument("input", help="Path to the input video file")
    parser.add_argument("output", help="Path for the output video file")
    parser.add_argument("-t", "--threshold", type=float, default=0.5,
                        help="Threshold for transient detection (range: 0.0 to 1.0, default: 0.5). "
                             "Lower values result in more splits, higher values in fewer splits.")
    parser.add_argument("-p", "--play", action="store_true",
                        help="Play the output video after processing")
    
    args = parser.parse_args()
    
    if not 0.0 <= args.threshold <= 1.0:
        parser.error("Threshold must be between 0.0 and 1.0")
    
    main(args.input, args.output, args.threshold, args.play)

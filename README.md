# devolver
Devolver: Unravel perception through algorithmic video deconstruction. This tool splits videos based on audio transients and rearranges the segments, challenging our understanding of time, audiovisual coherence, and meaning-making. Explore the boundaries of human cognition and dive into a unique phenomenological experiment.

Devo's Whip It @
* Zero Point One: https://youtu.be/9zeKQMSQq5g
* Zero Point Two: https://youtu.be/2PoHQBRFW0g
* Zero Point Three: https://www.youtube.com/watch?v=9d7ytN3CEcU
* Zero Point Four: https://youtu.be/Lal8lqZ2dEQ
* Zero Point Five: https://youtu.be/0BojNbVYYQQ

Eno Here Come The Warm Jets
* Whip Up the Jets: [https://youtu.be/Lal8lqZ2dEQ](https://www.youtube.com/watch?v=ANXnBqHhMzw)

## Description

This project provides a Python script that splits a video based on audio transients and then randomly rearranges the segments. It serves as a tool for exploring human perception, pattern recognition, and meaning-making processes, drawing inspiration from phenomenology.

The script challenges our perceptual and cognitive processes by taking a coherent video, breaking it into pieces based on sudden changes in sound, and then randomly rearranging these pieces. The result is a new video that, while composed of familiar elements, presents them in an unfamiliar order.

## Motivation

From a phenomenological perspective, this project invites us to reflect on:

1. The nature of temporal experience: How do we perceive and make sense of time when familiar sequences are disrupted?
2. The relationship between audio and visual perception: How does the reorganization of audio cues affect our interpretation of visual information?
3. The process of meaning-making: How does our mind attempt to construct a coherent narrative or meaning from the rearranged segments?
4. The role of expectation in perception: How do our expectations, based on our original understanding of the video, influence our experience of the rearranged version?

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/video-transient-splitter.git
   cd video-transient-splitter
   ```

2. Install the required dependencies:
   ```
   pip install moviepy librosa numpy
   ```

3. Ensure FFmpeg is installed on your system. If not, install it using your system's package manager or download it from the [official FFmpeg website](https://ffmpeg.org/download.html).

## Usage

Basic usage:
```
python video_splitter_rearranger.py input_video.mp4 output_video.mp4 [-t THRESHOLD] [-p]
```

Arguments:
- `input_video.mp4`: Path to the input video file
- `output_video.mp4`: Path for the output video file
- `-t, --threshold`: Threshold for transient detection (range: 0.0 to 1.0, default: 0.5)
- `-p, --play`: Play the output video after processing (optional)

Example:
```
python video_splitter_rearranger.py myvideo.mp4 output.mp4 -t 0.3 -p
```

This command will process `myvideo.mp4` with a threshold of 0.3, save the result as `output.mp4`, and then play the resulting video.

## Batch Processing

To create multiple outputs with different thresholds, you can use the following bash script:

```bash
for i in {1..5}; do
  threshold=$(echo "scale=1; $i / 10" | bc)
  python video_splitter_rearranger.py input.mp4 "output$i.mp4" -t $threshold
done
```

This will create 5 output files with thresholds ranging from 0.1 to 0.5.

## Contributing

Contributions to this project are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- This project was inspired by concepts from phenomenology and cognitive science.
- Thanks to the developers of moviepy and librosa for their excellent libraries.
>>>>>>> 0e9333c (drafts)

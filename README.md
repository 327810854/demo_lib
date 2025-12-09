# README for demo

This repository contains a simple interactive demo program that showcases how to use the video processing functions from the dataproc main library.

It is designed for class presentations.
# Structure
dataproc-demo/
 ├── demo.py
 ├── examples/
 │    ├── sample.mp4
 │    └── output_demo.mp4
 ├── README.md
 ├── requirements.txt

# How to Run
git clone https://github.com/327810854/dataproc-demo.git
cd dataproc-demo
pip install -r requirements.txt
python demo.py

# Demo Menu (demo_video.py)
When you run the program, you will see:
=== Video Processing Demo ===
1) Cut Clip
2) Resize Video
3) Convert to Grayscale
4) Change Speed
5) Add Watermark
0) Exit
Users can directly test the functions you implemented in dataproc.
# Usage Examples (Same as main library)
cut_clip("examples/sample.mp4", "examples/out_cut.mp4", 3, 10)
resize_video("examples/sample.mp4", "examples/out_small.mp4", 0.5)
to_grayscale("examples/sample.mp4", "examples/out_gray.mp4")
change_speed("examples/sample.mp4", "examples/out_fast.mp4", 2.0)
add_watermark("examples/sample.mp4", "examples/out_wm.mp4", "logo.png")


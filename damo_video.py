
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATAPROC_ROOT = ROOT / "libs" / "dataproc"
sys.path.append(str(DATAPROC_ROOT))

from video.video_tools import (
    cut_clip,
    resize_video,
    resize_to_resolution,
    to_grayscale,
    change_speed,
    add_watermark,
)


EXAMPLES_DIR = ROOT / "examples"
INPUT_VIDEO = EXAMPLES_DIR / "sample.mp4"


def check_input():
   
    if not INPUT_VIDEO.exists():
        print(f"[ERROR] {INPUT_VIDEO} not found.")
        print("Please name the example video "sample.mp4" and place it in the "demo_lib/examples/" directory.")
        raise SystemExit(1)


def demo_cut():
   
    output = EXAMPLES_DIR / "cut_demo.mp4"
    print(f"[1] Cutting video -> {output.name}")
    cut_clip(str(INPUT_VIDEO), str(output), start_time=5, end_time=10)


def demo_resize_scale():
   
    output = EXAMPLES_DIR / "resize_demo.mp4"
    print(f"[2] Resizing (scale=0.5) -> {output.name}")
    resize_video(str(INPUT_VIDEO), str(output), scale=0.5)


def demo_grayscale():
    
    output = EXAMPLES_DIR / "grayscale_demo.mp4"
    print(f"[3] Grayscale -> {output.name}")
    to_grayscale(str(INPUT_VIDEO), str(output))


def demo_speed():
  
    output = EXAMPLES_DIR / "speed_demo.mp4"
    print(f"[4] Change speed (x1.5) -> {output.name}")
    change_speed(str(INPUT_VIDEO), str(output), factor=1.5)


def demo_watermark():
    
    output = EXAMPLES_DIR / "watermark_demo.mp4"
    print(f"[5] Add watermark -> {output.name}")
    add_watermark(
        str(INPUT_VIDEO),
        str(output),
        text="OSS DEMO",
        fontsize=40,
        position="bottom-right", 
    )


def main():
    print("=== Video Demo for dataproc ===")
    print("Input video:", INPUT_VIDEO)
    check_input()

    EXAMPLES_DIR.mkdir(exist_ok=True)

    demo_cut()
    demo_resize_scale()
    demo_grayscale()
    demo_speed()
    demo_watermark()

    print("\n[Done] All demo videos have been generated in the examples/ directory:")
    print(" - cut_demo.mp4")
    print(" - resize_demo.mp4")
    print(" - grayscale_demo.mp4")
    print(" - speed_demo.mp4")
    print(" - watermark_demo.mp4")


if __name__ == "__main__":
    main()

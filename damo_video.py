from video.video_tools import (
    cut_clip,
    resize_video,
    resize_to_resolution,
    to_grayscale,
    change_speed,
    add_watermark
)
def menu():
    print("\n=== Video Processing Demo ===")
    print("1) Cut Video")
    print("2) Resize Video")
    print("3) Convert to Grayscale")
    print("4) Change Playback Speed")
    print("5) Add Watermark")
    print("0) Exit")
    choice = input("Please choose a function: ").strip()
    return choice



def get_input_output():
    # Input file name
    in_name = input("Input file name(default sample.mp4): ").strip()
    if in_name == "":
        in_name = "sample.mp4"
    elif "." not in in_name:
        in_name += ".mp4"

    # Output file name
    out_name = input("Output file name(default output_demo.mp4): ").strip()
    if out_name == "":
        out_name = "output_demo.mp4"
    elif "." not in out_name:
        out_name += ".mp4"

    return in_name, out_name



def main():
    while True:
        choice = menu()

        # Exit
        if choice == "0":
            print("Exiting Demo。")
            break

        # Cut video
        elif choice == "1":
            in_name, out_name = get_input_output()
            start = float(input("Start time (seconds): "))
            end = float(input("End time (seconds): "))
            cut_clip(in_name, out_name, start, end)

        # Resize video
        elif choice == "2":
            in_name, out_name = get_input_output()

            print("\n=== Resize Video ===")
            print("1) Scale by ratio (0.5 = half size, 2 = double size)")
            print("2) Resize to target resolution (1080p / 720p / 480p / custom)")
            mode = input("Choose 1 or 2: ").strip()

            if mode == "1":
                # Scale directly by ratio
                scale = float(input("Enter scale ratio (e.g., 0.5, 1.0, 2.0): ").strip() or "0.5")
                resize_video(in_name, out_name, scale)

            elif mode == "2":
                print("\nTarget resolution:")
                print("1) 1920 x 1080 (1080p)")
                print("2) 1280 x 720  (720p)")
                print("3) 854 x 480   (480p)")
                print("4) Custom width/height")
                r_choice = input("Choose 1-4: ").strip()

                if r_choice == "1":
                    target_w, target_h = 1920, 1080
                elif r_choice == "2":
                    target_w, target_h = 1280, 720
                elif r_choice == "3":
                    target_w, target_h = 854, 480
                elif r_choice == "4":
                    target_w = int(input("Enter target width (e.g., 1280): ").strip())
                    target_h = int(input("Enter target height (e.g., 720):").strip())
                else:
                    print("Invalid input, returning to main menu.")
                    return

                resize_to_resolution(in_name, out_name, target_w, target_h)

            else:
                print("Invalid input, returning to main menu.")


        # Convert to grayscale
        elif choice == "3":
            in_name, out_name = get_input_output()
            to_grayscale(in_name, out_name)

        # Change playback speed
        elif choice == "4":
            in_name, out_name = get_input_output()
            print("\n=== Change Playback Speed ===")
            print("1) Speed Up")
            print("2) Slow Down")
            mode = input("Choose 1 or 2: ").strip()
            if mode == "1":
                speed_up = float(input("Speed-up factor (e.g., 2 = 2x speed): ").strip())
                factor = speed_up
            elif mode == "2":
                slow_down = float(input("Slow-down factor (e.g., 2 = half speed): ").strip())
                factor = 1.0 / slow_down
            else:
                print("Invalid input, returning to main menu.")
                return
            print(f"\nApplying speed change with factor={factor} ...")
            change_speed(in_name, out_name, factor)

        # Add watermark
        elif choice == "5":
            in_name, out_name = get_input_output()
            text = input("Watermark text (default OSS TEAM): ").strip() or "OSS TEAM"
            fontsize = int(input("Font size (default 30): ").strip() or "30")

            print("\nWatermark position:")
            print("1) Top Left")
            print("2) Top Right")
            print("3) Bottom Left")
            print("4) Bottom Right")
            print("5) Center")
            pos_choice = input("Choose 1–5 (default 4: Bottom Right): ").strip()
            if pos_choice == "":
                pos_choice = "4"
            pos_map = {
                "1": "top-left",
                "2": "top-right",
                "3": "bottom-left",
                "4": "bottom-right",
                "5": "center",
            }
            position = pos_map.get(pos_choice, "bottom-right")

            add_watermark(in_name, out_name, text=text, fontsize=fontsize, position=position)



if __name__ == "__main__":
    main()

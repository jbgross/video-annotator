import cv2
import time

def main(video_path, output_file="timestamps.txt"):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Cannot open video file {video_path}")
        return

    # Get video frame rate
    fps = cap.get(cv2.CAP_PROP_FPS)
    timestamps = []

    print("Press SPACE to record a timestamp. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Reached end of video.")
            break

        # Display the video frame
        cv2.imshow('Video', frame)

        # Wait based on FPS
        key = cv2.waitKey(int(1000 / fps)) & 0xFF

        if key == ord(' '):  # Spacebar pressed
            # Get current frame position in milliseconds
            current_time_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
            current_time_sec = current_time_ms / 1000.0
            timestamps.append(current_time_sec)
            print(f"Timestamp recorded: {current_time_sec:.2f} seconds")

        elif key == ord('q'):  # 'q' to quit
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

    # Save timestamps to a file
    with open(output_file, 'w') as f:
        for ts in timestamps:
            f.write(f"{ts:.2f}\n")

    print(f"Timestamps saved to {output_file}")

if __name__ == "__main__":
    video_file = "dot-equals-method.mp4"  # Replace with your MP4 file path
    main(video_file)

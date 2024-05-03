# YOLOv8 - Person Tracker

This repository contains a Python script to detect and track persons in a video stream or a video file using YOLOv8. The script utilizes the Ultralytics YOLOv5 implementation for object detection.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/AbdulRahmanFares/YOLOv8-PersonTracker.git
    ```

2. Navigate to main.py:

## Usage

1. Run the `main.py` script:

    ```bash
    python main.py
    ```

2. Press `q` to quit the application.

### Options

- To test the script on a video file, uncomment line 12 and comment out line 11 in the script:

    ```python
    # cap = cv2.VideoCapture(0) # Comment this line to test on video
    cap = cv2.VideoCapture("test\\test_video_1.mp4") # Uncomment this line to test on video
    ```

- To track objects other than persons, modify the `classes` parameter in line 18 of the script. For example, to track cars, change `classes = [0]` to `classes = [2]`.

    ```python
    results = yolo_model.track(
        frame,
        classes = [0],  # Track only persons (Comment this line to track every objects or replace "0" with the required class code from coco8.yaml)
        persist = True  # Enable object tracking for better stability
    )
    ```

## Issues and Contributions

If you encounter any issues or have suggestions for improvement, feel free to [open an issue](https://github.com/AbdulRahmanFares/flightTicketBookingApplication/issues) or submit a pull request.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you find this project helpful or would like to contribute to its continued development, consider supporting me with a coffee! Your support is invaluable.

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/farazzrahman)





# Face Swap using InsightFace in Python

## Overview

This project implements a Face Swap application using the **InsightFace** package in Python. It detects faces in images and swaps them with a source face while preserving natural facial features and expressions.

---

## Features

* Face detection using InsightFace's RetinaFace model.
* High-quality face swapping with seamless blending.
* Supports image-to-image face swapping.
* Lightweight and easy to set up.

---

## Requirements

* Python 3.7+
* insightface
* numpy
* opencv-python
* matplotlib (optional for visualization)

### Installation

```bash
pip install insightface numpy opencv-python matplotlib
```

---

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/Monish021/face-swap-insightface.git
cd face-swap-insightface
```

### 2. Download Pre-trained Models

InsightFace will automatically download the required models on the first run. Ensure you have an internet connection.

### 3. Run Face Swap

```bash
python face_swap.py --source source.jpg --target target.jpg --output swapped.jpg
```

### 4. Parameters

| Argument   | Description                                     |
| ---------- | ----------------------------------------------- |
| `--source` | Path to source face image                       |
| `--target` | Path to target image where face will be swapped |
| `--output` | Path to save the output image                   |

---

## Example

```bash
python face_swap.py --source face1.jpg --target group_photo.jpg --output result.jpg
```

---

## Project Structure

```
face-swap-insightface/
├── face_swap.py       # Main face swapping script
├── README.md          # Project documentation
└── requirements.txt   # Package requirements (optional)
```

---

## Notes

* Works best with frontal face images.
* Face detection might fail on low-resolution or heavily occluded faces.
* Performance depends on hardware (GPU recommended for faster processing).

---

## References

* [InsightFace GitHub](https://github.com/deepinsight/insightface)
* [InsightFace Documentation](https://insightface.ai/)

---

## License

This project is for educational purposes. Refer to InsightFace's license for usage of pre-trained models.

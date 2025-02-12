# Potato Leaf Diseases Detection

## Overview

Potato Leaf Diseases Detection is a machine learning project that identifies different diseases in potato leaves using deep learning techniques. The model is trained on an image dataset and deployed as a web application using Streamlit.

## Features

- Detects common potato leaf diseases.
- User-friendly web interface using Streamlit.
- Uses a deep learning model for accurate predictions.

## Installation

Follow these steps to set up and run the project locally:

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/potato-disease-detection.git
   cd potato-disease-detection
   ```
2. **Create a virtual environment** (optional but recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate    # On Windows
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Streamlit application**
   ```sh
   streamlit run web.py
   ```

## Usage

1. Open the web application in your browser.
2. Upload an image of a potato leaf.
3. The model will analyze the image and display the disease detected.

## Dataset

The dataset consists of images of potato leaves with different diseases. It is sourced from Kaggle and preprocessed before training the model.

## Model

- Convolutional Neural Network (CNN) architecture.
- Pretrained models like VGG16 or ResNet may be used.
- Trained on labeled images of healthy and diseased potato leaves.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

- **Developer:** Sakshi Sharma
- **GitHub:** [yourusername](https://github.com/yourusername)
- **Email:** [your-email@example.com](mailto\:your-email@example.com)


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
   git clone https://github.com/sakshi-sharma3/potato-disease-detection.git
   cd potato-disease-detection
   ```
2. **Create a virtual environment** (optional but recommended)
   ```sh
   python -m venv venv
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

The model is trained on a Potato Leaf Dataset obtained from PlantVillage. It contains thousands of labeled images of healthy and diseased potato leaves.

## Model Structure

- Convolutional Neural Network (CNN) architecture.
- Pretrained models like VGG16 or ResNet may be used.
- Trained on labeled images of healthy and diseased potato leaves.
- 📈 Results & Accuracy

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Submit a pull request.

## Future Enhancements

 Improve accuracy with transfer learning (e.g., ResNet, MobileNet)

🔹 Deploy as a mobile app for farmers

🔹 Add multi-class classification for more plant diseases

## License

This project is open-source under the MIT License.



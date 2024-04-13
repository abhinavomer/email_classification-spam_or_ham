# Email Classification App

This Streamlit application titled "Email Classification" allows users to input an email text, and upon submission, it predicts whether the email is categorized as "Ham" (non-spam) or "Spam" based on a pre-trained machine learning model.

## Features

- **Email Input**: Provides a text input field where users can input the text of the email they want to classify.
  
- **Submit Button**: Triggers the classification process based on the input email text.

- **Prediction**: Displays the prediction result below the submit button, indicating whether the input email is classified as "Ham" (non-spam) or "Spam".

## Usage

1. Clone the repository to your local machine:

git clone https://github.com/your-username/email-classification-app.git

2. Install the necessary dependencies:

pip install -r requirements.txt

3. Run the Streamlit app:

streamlit run app.py

4. Access the app in your web browser at `http://localhost:8501`.

## Deployment

The app can be deployed to various platforms to make it accessible to a wider audience. Consider deploying it to platforms like Heroku or Streamlit Sharing.

## Files

- **app.py**: Contains the Streamlit application code for email classification.
- **email.pickle**: Pre-trained machine learning model for email classification.
- **vector.pkl**: Vectorizer for transforming input text data into a format suitable for model prediction.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The machine learning model used in this app was trained using publicly available email datasets.
- Special thanks to [Streamlit](https://streamlit.io/) for providing an easy-to-use framework for building interactive web applications.

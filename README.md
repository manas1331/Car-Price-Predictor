# Car-Price-Predictor

## View the live website 
Click the link to view the website 
[(https://car-price-predictor-yrn6.onrender.com/)](https://car-price-predictor-yrn6.onrender.com/)

## Project Overview
This project provides a web-based application for predicting car prices using machine learning models. Users can interact with the model and view predictions in real-time through a user-friendly interface built using streamlit framework.


## Features

- **Custom UI Styling**: 
  - The interface is enhanced with custom CSS for a modern, polished appearance.
  - Styled buttons and select boxes for an intuitive user experience.
  
- **Title Banner**: 
  - A visually appealing banner that displays the title "Car Price Prediction Using Machine Learning" with gradient styling.
  
- **Introductory Text**: 
  - Brief and user-friendly explanation to guide sellers in estimating the value of their car.

- **User Input Fields**:
  - `Ex-showroom price`: Input for the car's original price (in Lakhs).
  - `Distance driven`: Input for kilometers driven by the car.
  - `Fuel type`: Choose between Petrol, Diesel, or CNG.
  - `Seller type`: Select whether you're a dealer or an individual.
  - `Transmission type`: Choose between Manual or Automatic transmission.
  - `Previous owners`: Select the number of previous owners.
  - `Year of purchase`: Enter the year of car purchase, and the app calculates the car's age.

- **Prediction Button**: 
  - A "Predict Car Price" button triggers the machine learning model to estimate the car’s price.

- **Machine Learning Model**:
  - The app uses an XGBoost regression model to predict the car's price based on the provided inputs.

- **Result Display**: 
  - The predicted price is displayed in a user-friendly format. If the prediction is successful, celebratory balloons are shown.
  
- **Error Handling**: 
  - If something goes wrong with the input or prediction, users are notified with an error message for correction.

## Technologies Used

- **Python**: Core programming language for data analysis and web application development.
- **Pandas & NumPy**: Data manipulation and numerical computations.
- **Scikit-Learn**: Machine learning algorithms and tools.
- **Matplotlib/Seaborn**: Data visualization.
- **Flask/Django/Streamlit**: Web framework for building the user interface.
- **APIs/yfinance**: For fetching real-time stock data.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/car-price-predictor.git
   cd car-price-predictor

2. **Install Dependencies**:
    ```bash
   pip install -r requirements.txt

4. **Setup and Configuration**:

- Configure any necessary API keys or environment variables.
- Adjust any settings for data sources and model parameters.

 4. **Run the Web Application**:
    ```bash
    streamlit run streamlit.py

 5. **Usage**:
- Navigate to  http://localhost:5000 (or the specified port) to access the web application.
- Input stock ticker symbols and view predictions and visualizations.

## Website View

![image](https://github.com/user-attachments/assets/bc8547d5-bff2-40ec-ae74-8f1bd6626481)



## Contribution
Feel free to contribute to this project by submitting issues, feature requests, or pull requests. Please adhere to the project's coding standards and include tests for any new features.

## License
This project is licensed under the APACHE 2.0 License. See the [LICENSE](LICENSE) file for more details

# car-data-app
This web application provides an interactive dashboard for exploring car advertisement data.  Users can visualize price distributions, explore relationships between different features, and filter data based on various criteria.  This allows for a deeper understanding of trends and patterns in the car market.

## Project Description

This project aims to provide a user-friendly way to analyze car data.  It leverages the power of Python, Pandas for data manipulation, and Plotly Express for creating interactive visualizations.  The Streamlit library is used to build the interactive web dashboard, making it easy for users to explore the data without needing any coding experience.

## Technologies Used

*   Python
*   Pandas
*   Plotly Express
*   Streamlit

## Dataset

The data used in this application is stored in `vehicles_us.csv`.  It contains information about various car advertisements, including price, make, model, year, mileage, and other relevant features.

## How to Run Locally

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/vacohud40/car-data-app.git](https://github.com/vacohud40/car-data-app.git)  
    ```

2.  **Navigate to the Project Directory:**
    ```bash
    cd car-data-app
    ```

3.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv my_pillow_env  
    ```

4.  **Activate the Environment:**
    *   Windows:
        ```bash
        my_pillow_env\Scripts\activate
        ```
    
    
        

5.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6.  **Run the Streamlit App:**
    ```bash
    streamlit run app.py
    ```

7.  **Open in Browser:** The app should automatically open in your web browser. If not, you can usually access it at `http://localhost:8501`.

## Deployment

This application is deployed on Render and can be accessed at: [https://car-data-app.onrender.com](https://car-data-app.onrender.com)


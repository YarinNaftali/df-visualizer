# df-visualizer
Welcome to the Streamlit-FastAPI Full Stack Data Visualization and Logging repository! 🚀

# Overview
This open-source project provides a robust and flexible solution for creating a full stack application with streamlined data visualization capabilities. Leveraging the power of Streamlit for the frontend, FastAPI for the backend, and MongoDB for logging operations, this project aims to simplify the process of uploading, visualizing, and logging data for users with diverse needs.

# Features
## Frontend (Streamlit)
1. **Upload Data:** Seamlessly upload a dataframe or .csv file with just a few clicks.
2. **View Dataframe:** Explore the uploaded data with an intuitive interface, allowing quick insights into your dataset.
3. **Dynamic Plotting:** Choose two or more columns and create dynamic plots to visualize relationships within the data.

## Backend (FastAPI)
1. **Data Reception:** Efficiently receive and handle .csv files sent from the frontend.
2. **Local File Saving:** Save the uploaded file locally for further processing and analysis.
3. **MongoDB Integration:** Utilize Beanie for MongoDB integration, logging each operation for future reference.

## Database (MongoDB)
1. **Operation Logging:** Keep track of all operations performed, ensuring a comprehensive history of interactions.
2. **View Operations:** Easily view and analyze the logged operations, aiding in audit trails and data exploration.

# Getting Started
Clone this repository and use Docker Compose to effortlessly orchestrate the entire stack. The modular design allows for easy customization, enabling users to adapt the solution to their specific needs.

# Usage
1. **Clone the Repository:**
```
git clone https://github.com/yarinnaftali/df-visualizer.git
```

3. **Run Docker Compose:**
```
cd df-visualizer
docker-compose up
```


5. **Access the Application:**
Open your web browser and navigate to `http://localhost:8501` to start using the application.

# Contributions
Feel free to contribute to the project by opening issues, proposing new features, or submitting pull requests. Your input is valuable, and together we can enhance this project to benefit the broader community.

# License
This project is licensed under the MIT License, allowing you to use, modify, and distribute the code as needed.

Start exploring and visualizing your data effortlessly with Streamlit-FastAPI Full Stack Data Visualization and Logging! 📊📈

# Capstone Project: A Dying Planet

## Overview
This project explores how climate change is worsening globally over time. Using a dataset from Kaggle, we analyze how different countries are affected by climate trends and visualize these changes through an interactive dashboard.

## Project Structure
- **Backend (Thailand Griffith)**  
  FastAPI + SQLite  
  - Handles data storage and API endpoints  
  - Loads and processes climate data  
  - Provides secure access via API key authentication  

- **Frontend (Charles Simpson)**  
  Streamlit Dashboard  
  - Displays interactive visualizations  
  - Allows filtering by country, time, and climate element  
  - Communicates with backend through API requests  

## Technologies Used
- FastAPI
- SQLite
- Streamlit
- Pandas
- Pytest
- Flake8
- Google Cloud Storage (optional integration)

## Features
- REST API for climate data
- Interactive dashboard with filters
- Authentication (username/password + API key)
- Multiple data visualizations:
  - Climate trends over time
  - Top affected countries
  - Monthly climate patterns
- Clean, PEP8-compliant code
- Unit testing with pytest

## Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
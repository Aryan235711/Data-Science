# Test-Forest-Fires

This repository contains Jupyter Notebooks related to the analysis and modeling of forest fires. The notebooks are designed for exploring datasets, performing data analysis, and potentially building predictive models for forest fire detection, risk assessment, or simulation.

## Features

- **Comprehensive Data Analysis:**  
  - Utilizes the Algerian Forest Fires dataset, covering two regions and several weather/fire indices.
  - Data cleaning, preprocessing, and region-based partitioning.
  - Handles missing values and region annotation.

- **Exploratory Data Analysis (EDA):**  
  - Detailed statistical summaries and visualizations of weather and fire indices.
  - Feature engineering, including adding new columns for region and derived features.

- **Machine Learning Workflow:**  
  - Loads and processes dataset for modeling.
  - Includes model artifacts (e.g., LassoCV regression model and scaler) for Fire Weather Index (FWI) prediction.

- **Interactive Web Application:**  
  - Web interface (Flask/Jinja2 templates) for users to input features such as temperature, humidity, wind speed, rain, and indices (FFMC, DMC, ISI, Classes, Region).
  - Predicts Fire Weather Index (FWI) from user inputs and displays results.

- **Reproducible Notebooks:**  
  - Well-documented Jupyter Notebook for EDA, feature engineering, and ML modeling.
  - Step-by-step code for data loading, transformation, and analysis.

- **Extensible Template Structure:**  
  - Organized template files for home and index pages, simplifying future expansion and UI updates.

- **Model Storage:**  
  - Pre-trained model and scaler files stored in the `models/` directory for easy deployment and reuse.


## Getting Started

### Prerequisites

- Python (recommended: 3.7+)
- Jupyter Notebook or JupyterLab
- Required Python packages (see below)

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Aryan235711/Test-Forest-Fires.git
    cd Test-Forest-Fires
    ```

2. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

Open the Jupyter Notebook you wish to run:

```bash
jupyter notebook
```

Navigate to the notebook in your browser and follow the instructions in the notebook cells.

## Repository Structure

- `*.ipynb` — Jupyter Notebooks for analysis and modeling
- `requirements.txt` — List of Python dependencies (if present)
- `README.md` — Project documentation

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Data sources and libraries used (update this section as needed)

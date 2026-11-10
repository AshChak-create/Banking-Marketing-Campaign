# Banking Marketing Campaign Analysis

### Exploratory Data Analysis | Python · Pandas · Matplotlib · Seaborn

## Overview

This project explores banking customer data to better understand customer demographics, financial characteristics, and marketing campaign outcomes.

The analysis focuses on how factors such as age, occupation, account balance, loan status, and previous campaign interactions relate to customers' decisions to subscribe to a term deposit.

Using Python, I examined the dataset through descriptive statistics, distributions, comparative visualizations, and correlation analysis to identify patterns worth investigating further.

## Objectives

- Examine the demographic and financial characteristics of banking customers.
- Understand how customers were contacted during marketing campaigns.
- Explore previous campaign interactions and their outcomes.
- Compare term deposit subscription rates across occupational groups.
- Investigate relationships between numerical variables and subscription outcomes.

## Tools and Libraries

| Tool | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Data loading, inspection, grouping, and statistical summaries |
| Matplotlib | Data visualization |
| Seaborn | Statistical plots and correlation heatmaps |

## Analysis Performed

### 1. Data Exploration

The initial analysis involved inspecting the dataset structure, reviewing the first few records, and checking for missing values.

### 2. Customer Demographics

Explored customer characteristics including:

- Age distribution
- Occupation
- Marital status
- Education level

These visualizations provide an overview of the customer population represented in the dataset.

### 3. Financial Characteristics

Analysed financial indicators such as:

- Average yearly account balance
- Credit default status
- Housing loan status
- Personal loan status

Descriptive statistics and distribution plots were used to examine variation in customer financial profiles.

### 4. Marketing Campaign Analysis

Examined campaign-related variables, including communication methods, contact months, call duration, and the number of contacts made during a campaign.

The analysis also explored previous contact history and outcomes of earlier campaigns.

### 5. Term Deposit Subscription Analysis

Investigated the distribution of subscription outcomes and compared subscription rates across occupational categories.

The target variable was converted into a binary numerical representation to support correlation analysis.

### 6. Correlation Analysis

Generated a correlation heatmap to examine linear relationships among selected numerical variables and term deposit subscription outcomes.

The analysis included age, balance, call duration, campaign contacts, previous contacts, and days since previous contact.

Correlation was used as an exploratory measure rather than evidence of causation.

## Project Structure

```text
banking-marketing-campaign-analysis/
│
├── banking_analysis.py
├── requirements.txt
├── .gitignore
└── README.md
```

The original analysis script expects a file named `banking_data.csv` in the project directory.

## Running the Project

Install the required libraries:

```bash
pip install -r requirements.txt
```

Place the compatible dataset in the project directory as `banking_data.csv`, then run:

```bash
python banking_analysis.py
```

The script prints descriptive summaries and displays visualizations for the different variables analysed.

## Dataset Availability

The dataset used during the original analysis is not currently included in this repository.

The code follows a banking marketing dataset structure containing customer demographics, financial attributes, campaign history, and a binary term deposit subscription outcome.

The original dataset source and version have not yet been independently verified. The analysis will need to be rerun and validated once a compatible dataset is available.

## Limitations

This project is exploratory and does not include predictive model training or evaluation.

The analysis primarily uses individual variable distributions, group comparisons, and Pearson correlation. These methods can identify associations, but they do not establish causal relationships.

Call duration is also a post-contact variable and would not normally be available when making predictions before a marketing call.

Because the original dataset is currently unavailable, the findings have not been independently reproduced from the retained script.

## Future Improvements

- Recover and verify the dataset used in the original analysis.
- Add numerical summaries supporting the visualizations.
- Explore subscription rates across multiple customer characteristics.
- Investigate whether observed differences between groups are statistically meaningful.
- Assess a baseline classification model with appropriate validation and evaluation metrics.

## Project Note

This project was developed as a practical exercise in exploratory data analysis, with an emphasis on understanding structured data, examining distributions, and interpreting relationships between customer characteristics and marketing outcomes.
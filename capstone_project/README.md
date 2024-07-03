### Home Loan Approval/Denial

**Henrique Martins**

#### Executive summary

#### Rationale

Understanding the factors that lead to mortgage approval or denial is crucial for both borrowers and lenders. For borrowers, it can help them discover their eligibility. For lenders, it can improve risk assessment, make the application process faster, and potentially identify areas where lending practices may need to be adjusted to ensure fairness. Additionally, policymakers and researchers can utilize these insights to address systemic issues and promote equitable access to homeownership.

#### Research Question

This project aims to develop a machine learning model that can predict the approval or denial of home mortgage applications.

#### Data Sources

I will use the [U.S. Home Mortgage Disclosure Act (HMDA) database](https://ffiec.cfpb.gov/) as the source of my datasets. My focus will be on the SF East Bay counties, namely *Alameda County* and *Contra Costa County*, ranging from 2019 to 2022. The dataset can be downloaded [here](https://ffiec.cfpb.gov/data-browser/data/2022?category=states&items=CA), and [here](https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields) is its documentation.

#### Methodology

1) Data cleaning and preprocessing
2) Analysis and further processing
3) Model selection, training, and evaluation
    - Feature engineering
    - Classification methods
    - Search for hyperparameters

#### Results

##### EDA

- The main reason for denial of application is debt-to-income ratio, followed by credit application incomplete and credit history.
- The application success rate depends on the age of the applicant: for ages below 25 the approval rate is around 85%, and it increases to 90% between ages of 25-34. Beyond that it decreases as the age increases, but it still remains above 75% for applicants above 74.
- The approval rate is around 81% for Hispanic/Latino ethnicity and 87% for non Hispanic/Latino ethnicity.
- If the purpose of the loan is to buy or refinance a home the approval rate is high, around 90%, while it sits at 68% for home improvement.
- The approval rate does not change dramatically with income or property value. For a loan below U$400 thousand, however, it drops to 80% from a plateau of 90% at higher amounts.
- The approval rate for Asian and White races is around 86% and higher than for Native Americans, Pacific Islanders, and Blacks/African Americans which sit at 76%.

##### Modeling

- All models are resulting in more or less the same best score, for all classifiers.
- The faster and still very accurate models seem to be Logistic Regression and Decision Tree, achieving around 80% accuracy. They perform very well for the Approved classification, with a recall >0.90, however, they fall short on the recall for the Denied applications with under values under 0.5.

#### Next steps

- Pick best plots and enhance them
- Address class imbalance: undersample or weights
- Test different sets of features
- Group some of the features by quartiles (`pd.qcut`)

#### Outline of project

- [file_1_preprocessing.ipynb](./file_1_preprocessing.ipynb): Loading and pre-processing the data
- [file_2_analysis.ipynb](./file_2_analysis.ipynb): Analysis of the data and further processing
- [file_3_modeling.ipynb](./file_3_modeling.ipynb): Model selection

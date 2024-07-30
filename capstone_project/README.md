### Home mortgage approval/denial in California counties

**Henrique Martins**

#### Executive summary

#### Rationale

Understanding the factors that lead to home mortgage approval or denial is crucial for both borrowers and lenders. For borrowers, it can help them discover their eligibility. For lenders, it can improve risk assessment, make the application process faster, and potentially identify areas where lending practices may need to be adjusted to ensure fairness. Additionally, policymakers and researchers can utilize these insights to address systemic issues and promote equitable access to homeownership.

#### Research Question

What are the reasons and factors that lead to home mortgage approval or denial? This project aims to answer the question by analysing and modeling real world data from California counties using multiple machine learning models.

#### Data Sources

I will use the [U.S. Home Mortgage Disclosure Act (HMDA) database](https://ffiec.cfpb.gov/) as the source of my datasets. My focus will be on the SF East Bay counties, namely *Alameda County* and *Contra Costa County*, ranging from 2019 to 2022. The dataset can be downloaded [here](https://ffiec.cfpb.gov/data-browser/data/2022?category=states&items=CA), and the [documentation] explains all the dataset fields.

#### Methodology

1) Data cleaning and preprocessing

   - Fetched from U.S. HDMA database API
   - Read and preprocessed using *pandas* and *scipy*

2) Analysis and further processing
3) Model selection, training, and evaluation
    - Classification methods
    - Search for hyperparameters
    -

#### Results

##### Data cleaning and preprocessing <small>([file_1_preprocessing.ipynb])</small>

- As fetched the data contains 616388 rows and 99 columns
- All features are mapped into either numbers or categories, converting their values using the data documentation and grouping them into a new value whenever reasonable
- Some features are pre-filtered due to outliers
- All missing values are dealt with
- Output of this step are 549263 rows and 38 columns

##### Data analysis and further processing <small>([file_2_analysis.ipynb])</small>

- The main reason for denial of application is debt-to-income ratio, followed by credit application incomplete and credit history. Most approved applicants have a debt/income ratio of around 0.3, while above 0.5 the applications are mostly all denied
- The application success rate depends on the age of the applicant: for ages below 25 the approval rate is around 50%, and it increases to around 75% between ages of 25-34. Beyond that it decreases as the age increases, going back to 50% for applicants above 74 years old.
- The main applicant’s sex seems to play a role in the application outcome. Male applicants have around 70% approval rate, whereas female applicants are around 57%. If we group both the applicant and co-applicant’s sex together, the approval rate for male-male goes down to 62%, while filing having both sexes has an approval rate of around 73%. Female-female remains around 55%.
- The approval rate is around 81% for Hispanic/Latino ethnicity and 87% for non Hispanic/Latino ethnicity.
- The approval rate for Asian and White races is around 70% and higher than for Native Americans, Pacific Islanders, and Blacks/African Americans which sit at around 42%.
- If the purpose of the loan is to buy a house the approval rate is high, around 80%, while if it is to refinance it or improve it the approval rates goes down to around 60%.
- The approval rate goes above 50% for incomes above US$ 150 thousand per year. Most of the denied applicants have incomes lower than that.
- The property value has a similar distribution to the income, with most denied applicants having used a property valued at less than US$ 1 million to secure the loan.

##### Models

table, figures, sentences

##### EDA



##### Modeling

- All models are resulting in more or less the same best score, for all classifiers.
- The faster and still very accurate models seem to be Logistic Regression and Decision Tree, achieving around 80% accuracy. They perform very well for the Approved classification, with a recall >0.90, however, they fall short on the recall for the Denied applications with under values under 0.5.

#### Next steps

- Pick best plots and enhance them
- Address class imbalance: undersample or weights
- Test different sets of features
- Group some of the features by quartiles (`pd.qcut`)

#### Outline of project

- [file_1_preprocessing.ipynb]: Loading and pre-processing the data
- [file_2_analysis.ipynb]: Analysis of the data and further processing
- [file_3_modeling.ipynb]: Model selection

  [file_1_preprocessing.ipynb]: ./file_1_preprocessing.ipynb
  [file_2_analysis.ipynb]: ./file_2_analysis.ipynb
  [file_3_modeling.ipynb]: ./file_3_modeling.ipynb
  [U.S. Home Mortgage Disclosure Act (HMDA) database]: https://ffiec.cfpb.gov/
  [documentation]: https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields

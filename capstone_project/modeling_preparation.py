import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer


def get_X_y(filename_input, ohe_transform=True):
    # Loads processed data
    df = pd.read_csv(f"../../{filename_input}.csv", index_col=0)

    # Adds new columns
    df["sqrt_income"] = df["income"].apply(np.sqrt)
    df["sqrt_property_value"] = df["property_value"].apply(np.sqrt)
    df["sqrt_loan_amount"] = df["loan_amount"].apply(np.sqrt)

    # All features grouped by type
    tract_features = [x for x in df.columns if x.startswith("tract_")]
    numerical_loan_features = [
        "debt_to_income_ratio",
        # "debt_to_income_ratio_df",
        # "loan_term",
        "loan_to_value_ratio",
    ]
    numerical_currency_features = ["property_value", "income", "loan_amount"]
    numerical_sqrt_currency_features = [
        "sqrt_income",
        "sqrt_property_value",
        "sqrt_loan_amount",
    ]
    categorical_applicant_features = [
        "applicant_sex",
        "applicant_race",
        "applicant_ethnicity",
        "applicant_age",
    ]
    categorical_coapplicant_features = [
        "coapplicant_sex",
        "coapplicant_race",
        "coapplicant_ethnicity",
        "coapplicant_age",
    ]
    categorical_loan_features = [
        # "conforming_loan_limit",
        # "occupancy_type",
        # "hoepa_status",
        # "lien_status",
        "loan_purpose",
        "loan_type",
    ]
    binary_features = [
        "applicant_age_above_62",
        "interest_only_payment",
        "business_or_commercial_purpose",
        "open-end_line_of_credit",
    ]

    derived_features = [
        "derived_sex",
        "derived_race",
        "derived_ethnicity",
        "derived_loan_product_type",
    ]
    target_related_features = ["denial_reason"]
    target_feature = "application_outcome"

    # Choosing which features are included in X
    X = df[
        numerical_loan_features
        + numerical_currency_features
        # + numerical_sqrt_currency_features
        + categorical_applicant_features
        # + categorical_coapplicant_features
        + categorical_loan_features
        # + binary_features
        # + derived_features
    ]
    # Target feature mapped to int
    y = df[target_feature].map({"Approved": 1, "Denied": 0})

    # Replacing <,> (XGBoost requires it)
    numerical_columns = X.select_dtypes(include=float).columns
    categorical_columns = X.select_dtypes(include=object).columns
    for col in categorical_columns:
        X.loc[:, col] = X[col].replace({"<": "lt", ">": "gt"}, regex=True)

    if ohe_transform:
        column_transformer = ColumnTransformer(
            [
                ("ohe", OneHotEncoder(sparse_output=False), categorical_columns),
                ("scaler", StandardScaler(), numerical_columns),
            ],
            remainder="drop",
            verbose_feature_names_out=False,
        ).set_output(transform="pandas")
    else:
        column_transformer = ColumnTransformer(
            [
                ("scaler", StandardScaler(), numerical_columns),
            ],
            remainder="passthrough",
            verbose_feature_names_out=False,
        ).set_output(transform="pandas")

    # Applies column transformer
    X_transformed = column_transformer.fit_transform(X)

    if not ohe_transform: # Converting all objects to categories
        X_transformed.loc[:, categorical_columns] = X_transformed.loc[:, categorical_columns].astype("category")
    
    return train_test_split(
        X_transformed, y, test_size=0.3, stratify=y, random_state=42
    )


def print_dataframe(filtered_cv_results):
    """Pretty print for filtered dataframe"""
    for mean_precision, std_precision, mean_recall, std_recall, params in zip(
        filtered_cv_results["mean_test_precision"],
        filtered_cv_results["std_test_precision"],
        filtered_cv_results["mean_test_recall"],
        filtered_cv_results["std_test_recall"],
        filtered_cv_results["params"],
    ):
        print(
            f"precision: {mean_precision:0.3f} (±{std_precision:0.03f}),"
            f" recall: {mean_recall:0.3f} (±{std_recall:0.03f}),"
            f" for {params}"
        )
    print()
    
def refit_strategy(cv_results):
    """Define the strategy to select the best estimator.

    The strategy defined here is to filter-out all results below a precision threshold
    of 0.98, rank the remaining by recall and keep all models with one standard
    deviation of the best by recall. Once these models are selected, we can select the
    fastest model to predict.
    """
    # print the info about the grid-search for the different scores
    precision_threshold = 0.75

    cv_results_ = pd.DataFrame(cv_results)
    print("All grid-search results:")
    print_dataframe(cv_results_)
    
    _, precision_bins = pd.cut(cv_results_["mean_test_precision"], bins=5, retbins=True)
    precision_threshold = precision_bins[-2]

    # Filter-out top 20% precision results
    high_precision_cv_results = cv_results_[
        cv_results_["mean_test_precision"] > precision_threshold
    ]

    print(f"Models with a precision higher than {precision_threshold}:")
    print_dataframe(high_precision_cv_results)

    high_precision_cv_results = high_precision_cv_results[
        [
            "mean_score_time",
            "mean_test_recall",
            "std_test_recall",
            "mean_test_precision",
            "std_test_precision",
            "rank_test_recall",
            "rank_test_precision",
            "params",
        ]
    ]

    # Select the most performant models in terms of recall
    # (within 1 sigma from the best)
    best_recall_std = high_precision_cv_results["mean_test_recall"].std()
    best_recall = high_precision_cv_results["mean_test_recall"].max()
    best_recall_threshold = best_recall - best_recall_std

    high_recall_cv_results = high_precision_cv_results[
        high_precision_cv_results["mean_test_recall"] > best_recall_threshold
    ]

    print_dataframe(high_recall_cv_results)

    # From the best candidates, select the fastest model to predict
    fastest_top_recall_high_precision_index = high_recall_cv_results[
        "mean_score_time"
    ].idxmin()

    print(
        "\nSelected model:\n\n"
        f"{high_recall_cv_results.loc[fastest_top_recall_high_precision_index]}"
    )

    return fastest_top_recall_high_precision_index

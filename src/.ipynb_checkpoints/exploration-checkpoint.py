# exploration.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re

COLORS = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

def sanitize_filename(title):
    sanitized = re.sub(r'[\\/*?:"<>|]', "", title)
    sanitized = sanitized.replace(" ", "_")
    return f"{sanitized}.png"

def feature_frequency(df, save_path):
    columns = df.columns
    n_cols = 2
    n_rows = (len(columns )+1)//2
    figure, axes = plt.subplots(
                                n_rows ,
                                n_cols,
                                figsize = (10,2*n_rows),
                                constrained_layout=True
                                )
    axes = axes.flatten()
    for i,column in enumerate(columns):
        axes[i].hist(df[column].dropna(), bins=30, color = '#ffcc99')
        axes[i].set_title(column)
        axes[i].set_ylabel("Frequency")
    for j in range(len(columns), len(axes)):
        figure.delaxes(axes[j])
          
    figure.tight_layout()
    
    title = "Features Distributions"
    filename = sanitize_filename(title)
    plt.savefig(os.path.join(save_path, filename))
    print("Distribution figure saved succefully \n")
    plt.close()

def plot_boxplots(df, numeric_cols, save_path):
    for col in numeric_cols:
        plt.figure(figsize=(4, 4))
        # Applied palette here
        sns.boxplot(x=df[col], palette=COLORS)
        title = f'Box plot of {col}'
        plt.title(title)
        
        filename = sanitize_filename(title)
        plt.savefig(os.path.join(save_path, filename))
        plt.close()

def plot_unique_values_bar(df, save_path):
    columns = df.columns
    n_cols = 2
    n_rows = (len(columns) + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(10, 2 * n_rows))
    axes = axes.flatten()

    for i, column in enumerate(columns):
        value_counts = {str(k): v for k, v in df[column].value_counts().items()}
        
        # Applied palette to bars
        axes[i].bar(value_counts.keys(), value_counts.values(), color=COLORS)
        axes[i].set_title(f"{column} unique values count")
        axes[i].set_ylabel("Count")
        axes[i].set_xlabel("Values")
        plt.setp(axes[i].get_xticklabels(), rotation=30, horizontalalignment='right')

    for j in range(len(columns), len(axes)):
        fig.delaxes(axes[j])
        
    fig.tight_layout()
    
    title = "Unique_Value_Counts"
    filename = sanitize_filename(title)
    plt.savefig(os.path.join(save_path, filename))
    plt.close()

def plot_churn_by_category(df, save_path):
    columns = df.drop(columns=["Churn"]).columns
    n_cols = 2
    n_rows = (len(columns) + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(14, 2 * n_rows))
    axes = axes.flatten()

    for i, column in enumerate(columns):
        counts = pd.crosstab(df[column], df['Churn'])
        # Updated color parameter to use palette
        counts.plot(kind='bar', color=COLORS, ax=axes[i])
        
        title = f"Churn distribution by {column}"
        axes[i].set_title(title)
        axes[i].set_ylabel("Count")
        axes[i].set_xlabel(column)
        
    for j in range(len(columns), len(axes)):
        fig.delaxes(axes[j])
    
    fig.tight_layout()
    title = "Churn_Distribution_by_Features"
    filename = sanitize_filename(title)
    plt.savefig(os.path.join(save_path, filename))
    plt.close()


def plot_tenure_churn(df, save_path):
    plt.figure(figsize=(18, 4))
    counts = pd.crosstab(df['tenure'], df['Churn'])
    # Updated color parameter to use palette
    ax = counts.plot(kind='bar', color=COLORS, figsize=(18, 4))
    title = "Churn by Tenure"
    plt.title(title)
    
    filename = sanitize_filename(title)
    plt.savefig(os.path.join(save_path, filename))
    plt.close()


def plot_payment_method_analysis(df, save_path):
    proportions_dictionary = df['PaymentMethod'].value_counts().to_dict()

    plt.figure(figsize=(7, 3))
    # Using the global COLORS list
    plt.pie(proportions_dictionary.values(), autopct='%1.1f%%', pctdistance=0.6, colors=COLORS)
    plt.legend(labels=proportions_dictionary.keys(), bbox_to_anchor=(1, 0, 0.5, 1))
    title_pie = "Proportions of Different Payment Methodes"
    plt.title(title_pie)
    
    filename_pie = sanitize_filename(title_pie)
    plt.savefig(os.path.join(save_path, filename_pie), bbox_inches='tight')
    plt.close()
    
    churn_by_payment = pd.crosstab(df['PaymentMethod'], df['Churn'])
    # Updated color parameter to use palette
    churn_by_payment.plot(kind='bar', figsize=(12, 3), color=COLORS)
    
    title_bar = "Churn By Payment Method"
    plt.title(title_bar, fontsize=16)
    plt.xlabel("Payment method")
    plt.ylabel("Costumers Count")
    plt.legend(title='Churn')
    
    filename_bar = sanitize_filename(title_bar)
    plt.savefig(os.path.join(save_path, filename_bar), bbox_inches='tight')
    plt.close()


def view_binned_feature_by_columns(df, feature, columns, bin_number, save_path):
    n_cols = 2
    n_rows = (len(columns) + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(14, 2.5 * n_rows))
    axes = axes.flatten()

    bins = np.linspace(df[feature].min(), df[feature].max(), bin_number + 1)
    labels = [f"{bins[i]:.0f}-{bins[i+1]:.0f}" for i in range(bin_number)]

    binned_feature_col = f"Binned_{feature}"
    df[binned_feature_col] = pd.cut(df[feature], bins=bins, labels=labels, right=False, include_lowest=True)

    for i, column in enumerate(columns):
        counts = pd.crosstab(df[column], df[binned_feature_col])
        # Added color=COLORS here
        counts.plot(kind='bar', ax=axes[i], legend=False, color=COLORS)
        
        axes[i].set_title(f"{feature} distribution by: {column}")
        axes[i].set_ylabel("Count")
        axes[i].set_xlabel(column)

    for j in range(len(columns), len(axes)):
        fig.delaxes(axes[j])
        
    fig.legend(labels, title=f"{feature} Bins", loc='center right', bbox_to_anchor=(1.15, 0.5))
    fig.suptitle(f"{feature} by Internet Service, Dependents and Contract", fontweight='bold')
    fig.tight_layout(rect=[0, 0, 0.9, 1])

    title = f"{feature}_Distribution_Grouped"
    filename = sanitize_filename(title)
    plt.savefig(os.path.join(save_path, filename))
    plt.close()


def main():
    save_path = "../visualisations"
    
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    try:
        df = pd.read_csv("../data/customer_data.csv").set_index('customerID')
    except FileNotFoundError:
        print("Error: customer_data.csv not found. Make sure it's in the ../data/ directory.")
        return

    # Data Cleaning 
    df['TotalCharges'] = df["TotalCharges"].replace(" ", np.nan)
    df.dropna(subset=['TotalCharges'], inplace=True)
    df['TotalCharges'] = df['TotalCharges'].astype(float)
    df['SeniorCitizen'] = df['SeniorCitizen'].map({1: 'Yes', 0: 'No'})

    print("Generating Visualizations \n")

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    plot_boxplots(df, numeric_cols, save_path)

    plot_unique_values_bar(df.copy(), save_path)
    plot_churn_by_category(df.copy(), save_path)
    plot_payment_method_analysis(df, save_path)
    plot_tenure_churn(df, save_path)

    feature_cols_to_group_by = ["Dependents", "InternetService", "Contract"]
    view_binned_feature_by_columns(df, "MonthlyCharges", feature_cols_to_group_by, 4, save_path)
    view_binned_feature_by_columns(df, "tenure", feature_cols_to_group_by, 4, save_path)
    
    print(f"\nAll visualizations have been saved to the '{save_path}' directory.")


if __name__ == "__main__":
    main()
# Question 1: Age and Gender vs Payment method:
#       do age and/or gender affect the payment method?
#           age, gender, Payment Method
# Question 2: Gender vs Purchase rating & purchase frequency:
#       Does gender affect the rating score or do purchase frequency affect the rating score?
#           gender, payment method, Subscription Status, Previous Purchases, 

import numpy as np
import pandas as pd

def main():
    file_path = "data/shopping_trends_updated.csv"
    question1(file_path)
    return

def question1(file_path):
    data = pd.read_csv(file_path)
    question1_df = data[["Age", "Gender", "Payment Method" ]]

    num = q1_compute(data)
    return print(num)

def question2(file_path):
    visuals = ''
    raw_data = ''
    summary = ''
    return visuals, raw_data, summary

def q1_compute(df):
    counts = df['Gender'].value_counts()
    male_count = counts.get("Male", 0)
    count_male_venmo = compute_payment_method(df)
    return count_male_venmo

def compute_payment_method(df):
    # male payment method numbers
    male_numbers_list = []
    male_venmo = df[(df['Gender'] == 'Male') & (df['Payment Method'] == 'Venmo')]
    count_male_venmo = len(male_venmo)
    male_numbers_list.append(count_male_venmo)

    male_cash = df[(df["Gender"] == "Male") & (df["Payment Method"] == "Cash")]
    count_male_cash = len(male_cash)
    male_numbers_list.append(count_male_cash)

    male_paypal = df[(df["Gender"] == "Male") & (df["Payment Method"] == "PayPal")]
    count_male_paypal = len(male_paypal)
    male_numbers_list.append(count_male_paypal)

    male_credit_card = df[(df["Gender"] == "Male") & (df["Payment Method"] == "Credit Card")]
    count_male_credit_card = len(male_credit_card)
    male_numbers_list.append(count_male_credit_card)

    male_bank_transfer = df[(df["Gender"] == "Male") & (df["Payment Method"] == "Bank Transfer")]
    count_male_bank_transfer = len(male_bank_transfer)
    male_numbers_list.append(count_male_bank_transfer)

    male_debit_card = df[(df["Gender"] == "Male") & (df["Payment Method"] == "Debit Card")]
    count_male_debit_card = len(male_debit_card)
    male_numbers_list.append(count_male_debit_card)

    # Female payment methods numbers
    female_numbers_list = []
    female_venmo = df[(df['Gender'] == 'Female') & (df['Payment Method'] == 'Venmo')]
    count_female_venmo = len(female_venmo)
    female_numbers_list.append(count_female_venmo)

    female_cash = df[(df["Gender"] == "Female") & (df["Payment Method"] == "Cash")]
    count_female_cash = len(female_cash)
    female_numbers_list.append(count_female_cash)

    female_paypal = df[(df["Gender"] == "Female") & (df["Payment Method"] == "PayPal")]
    count_female_paypal = len(female_paypal)
    female_numbers_list.append(count_female_paypal)

    female_credit_card = df[(df["Gender"] == "Female") & (df["Payment Method"] == "Credit Card")]
    count_female_credit_card = len(female_credit_card)
    female_numbers_list.append(count_female_credit_card)

    female_bank_transfer = df[(df["Gender"] == "Female") & (df["Payment Method"] == "Bank Transfer")]
    count_female_bank_transfer = len(female_bank_transfer)
    female_numbers_list.append(count_female_bank_transfer)

    female_debit_card = df[(df["Gender"] == "Female") & (df["Payment Method"] == "Debit Card")]
    count_female_debit_card = len(female_debit_card)
    female_numbers_list.append(count_female_debit_card)
    return male_numbers_list, female_numbers_list


def q2_compute(df):
    return

def get_data(file_path, specified):
    raw_data = ''
    return raw_data

def get_visuals(data):
    return

# data = pd.read_csv("data/shopping_trends_updated.csv")
# # ages = data["Age"]
# # gender = data["Gender"]


# question1_df = data[["Age", "Gender", "Payment Method" ]]
# print(question1_df)
main()
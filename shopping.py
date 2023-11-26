# Question 1: Gender vs Payment method:
#       does gender affect the payment method / what gender should advertisement focus on more?
#           gender, Payment Method
# Question 2: Purchase frequency & Subscription status:
#       Does subscription status affect the purchase frequency / should we focus on promoting a subscription?
#           Subscription Status, Purchases Frequency 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    file_path = "data/shopping_trends_updated.csv"
    question1(file_path)
    question2(file_path)
    return

def question1(file_path):
    data = pd.read_csv(file_path)
    num = q1_compute(data)
    get_visuals(num[0], num[1], "PT")
    num_percentages = payment_data_percentages(num[0], num[1])
    get_visuals(num_percentages[0], num_percentages[1], "PT%")
    return 

def question2(file_path):
    data = pd.read_csv(file_path)
    num = q2_compute(data)
    get_visuals(num[0], num[1], "SS_PF")
    num_percentages = payment_data_percentages(num[0], num[1])
    get_visuals(num_percentages[0], num_percentages[1], "SS_PF%")
    return

def q1_compute(df):
    # counts = df['Gender'].value_counts()
    graphs_raw_data = payment_method_raw_data(df)
    return graphs_raw_data

def payment_method_raw_data(df):
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
    y_sub_list = []
    n_sub_list = []

    yes_subs_fn = df[(df["Subscription Status"] == "Yes") & (df["Frequency of Purchases"] == "Fortnightly")]
    y_sub_list.append(len(yes_subs_fn))
    no_subs_fn = df[(df["Subscription Status"] == "No") & (df["Frequency of Purchases" ] == "Fortnightly")]
    n_sub_list.append(len(no_subs_fn))
    yes_weekly = df[(df["Subscription Status"] == "Yes") & (df["Frequency of Purchases"] == "Weekly")]
    y_sub_list.append(len(yes_weekly))
    no_weekly = df[(df["Subscription Status"] == "No") & (df["Frequency of Purchases"] == "Weekly")]
    n_sub_list.append(len(no_weekly))
    yes_ann = df[(df["Subscription Status"] == "Yes") & (df["Frequency of Purchases"] == "Annually")]
    y_sub_list.append(len(yes_ann))
    no_ann = df[(df["Subscription Status"] == "No") & (df["Frequency of Purchases"] == "Annually")]
    n_sub_list.append(len(no_ann))
    yes_qua = df[(df["Subscription Status"] == "Yes") & (df["Frequency of Purchases"] == "Quarterly")]
    y_sub_list.append(len(yes_qua))
    no_qua =df[(df["Subscription Status"] == "No") & (df["Frequency of Purchases"] == "Quarterly")]
    n_sub_list.append(len(no_qua))
    y_month = df[(df["Subscription Status"] == "Yes") & (df["Frequency of Purchases"] == "Monthly")]
    y_sub_list.append(len(y_month))
    no_month = df[(df["Subscription Status"] == "No") & (df["Frequency of Purchases"] == "Monthly")]
    n_sub_list.append(len(no_month))
    yes_bi = df[(df["Subscription Status"] == "Yes") & (df["Frequency of Purchases"] == "Bi-Weekly")]
    y_sub_list.append(len(yes_bi))
    no_bi = df[(df["Subscription Status"] == "No") & (df["Frequency of Purchases"] == "Bi-Weekly")]
    n_sub_list.append(len(no_bi))
    yes_month3 = df[(df["Subscription Status"] == "Yes") & (df["Frequency of Purchases"] == "Every 3 Months")]
    y_sub_list.append(len(yes_month3))
    no_month3 = df[(df["Subscription Status"] == "No") & (df["Frequency of Purchases"] == "Every 3 Months")]
    n_sub_list.append(len(no_month3))

    return y_sub_list, n_sub_list


def payment_data_percentages(male_numbers, female_numbers):
    male_total = sum(male_numbers)
    female_total = sum(female_numbers)
    m_list = []
    fm_list = []

    # male average numbers
    m_v_average = round((male_numbers[0] / male_total) * 100)
    m_list.append(m_v_average)
    m_cash_average = round((male_numbers[1] / male_total) * 100)
    m_list.append(m_cash_average)
    m_pp_average = round((male_numbers[2] / male_total) * 100)
    m_list.append(m_pp_average)
    m_cc_average = round((male_numbers[3] / male_total) * 100)
    m_list.append(m_cc_average)
    m_bt_average = round((male_numbers[4] / male_total) * 100)
    m_list.append(m_bt_average)
    m_dc_average = round((male_numbers[5] / male_total) * 100)
    m_list.append(m_dc_average)

    # female average numbers
    fm_v_average = round((female_numbers[0] / female_total) * 100)
    fm_list.append(fm_v_average)
    fm_cash_average = round((female_numbers[1] / female_total) * 100)
    fm_list.append(fm_cash_average)
    fm_pp_average = round((female_numbers[2] / female_total) * 100)
    fm_list.append(fm_pp_average)
    fm_cc_average = round((female_numbers[3] / female_total) * 100)
    fm_list.append(fm_cc_average)
    fm_bt_average = round((female_numbers[4] / female_total) * 100)
    fm_list.append(fm_bt_average)
    fm_dc_average = round((female_numbers[5] / female_total) * 100)
    fm_list.append(fm_dc_average)

    if len(male_numbers) > 6:
        m_next = round((male_numbers[6] / male_total) * 100)
        m_list.append(m_next)
        fm_next = round((female_numbers[6] / female_total) * 100)
        fm_list.append(fm_next)
    return m_list, fm_list

def get_visuals(male_numbers, female_numbers, spec):
    categories = ["Venmo", "Cash", "PayPal", "Credit Card", "Bank Transfer", "Debit Card"]
    colors = ["red", "green", "yellow", "blue", "grey", "pink", "orange"]
    categoriesPT = ["Fortnightly", "Weekly", "Annually", "Quarterly", "Monthly", "Bi-Weekly", "3 Months"]


    fig, axs = plt.subplots(1, 2, figsize=(25, 4))
    

    if spec == "PT":
        axs[0].bar(categories, male_numbers, color=colors)
        axs[0].set_title("Male Payment Methods")
        axs[1].bar(categories, female_numbers, color=colors)
        axs[1].set_title("Female Payment Methods")

        plt.tight_layout()
        plt.show()
    elif spec == "PT%":
        axs[0].pie(male_numbers, labels=categories, autopct='%1.1f%%', startangle=90)
        axs[0].set_title("Male Payments Methods %")
        axs[1].pie(female_numbers, labels=categories, autopct='%1.1f%%', startangle=90)
        axs[1].set_title("Female Payments Methods %")
        axs[0].axis('equal')
        axs[1].axis('equal')
        plt.show()
    elif spec == "SS_PF":
        axs[0].bar(categoriesPT, male_numbers, color=colors)
        axs[0].set_title("Subscribed Purchase Frequency")
        axs[1].bar(categoriesPT, female_numbers, color=colors)
        axs[1].set_title("No Subscription Purchase Frequency")

        plt.show()
    elif spec == "SS_PF%":
        axs[0].pie(male_numbers, labels=categoriesPT, autopct='%1.1f%%', startangle=90)
        axs[0].set_title("Subscribed Purchase Frequency %")
        axs[1].pie(female_numbers, labels=categoriesPT, autopct='%1.1f%%', startangle=90)
        axs[1].set_title("No Subscription Purchase Frequency %")
        axs[0].axis('equal')
        axs[1].axis('equal')

        plt.show()
    return

main()
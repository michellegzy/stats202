# this file is the associated analysis script for stats 202 lab 1. it reads in the csv
# files from the desired folder and plots the relevant data using pandas and matplotlib.
# its worth noting in this simple case, it would be easier to simply do this analysis in excel.

# questions
#1 what is the correlation (r^2 value) between income and education?
#2 what is the mean and standard deviation of the rating?
#3 what is the correlation between limit and age?

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# input folder path containing the CSV files
folder_path = '/path/to/your/file'

# read CSV
df = pd.read_csv(os.path.join(folder_path, 'Credit.csv'))

# question 1: r^2 between income and education
r_inc_edu = df['Income'].corr(df['Education'])
# print(f"Q1: Income vs Education  r = {r_inc_edu:.4f},  r^2 = {r_inc_edu**2:.4f}")

# question 2: mean and std dev of rating
rating_mean = df['Rating'].mean()
rating_std  = df['Rating'].std()
# print(f"Q2: Rating  mean = {rating_mean:.2f},  std dev = {rating_std:.2f}")

# question 3: r^2 between limit and age
r_lim_age = df['Limit'].corr(df['Age'])
# print(f"Q3: Limit vs Age         r = {r_lim_age:.4f},  r^2 = {r_lim_age**2:.4f}")

# --- figure 1: plots for Q1, Q2, Q3 ---
fig1, axes1 = plt.subplots(1, 3, figsize=(15, 4))

# Q1: income vs education scatter with r² annotation
axes1[0].scatter(df['Income'], df['Education'], alpha=0.4, edgecolors='none', color='tab:purple', s=20)
m1, b1 = np.polyfit(df['Income'], df['Education'], 1)
x1 = np.linspace(df['Income'].min(), df['Income'].max(), 200)
axes1[0].plot(x1, m1*x1 + b1, color='black', linewidth=1.2)
axes1[0].set_xlabel('Income [$k]')
axes1[0].set_ylabel('Education [years]')
axes1[0].set_title(f'Q1: Income vs Education\n$r^2$ = {r_inc_edu**2:.4f}')

# Q2: histogram of rating with mean and ±1 std lines
axes1[1].hist(df['Rating'], bins=20, color='tab:orange', edgecolor='white', alpha=0.8)
axes1[1].axvline(rating_mean, color='black', linewidth=1.5, label=f'mean = {rating_mean:.1f}')
axes1[1].axvline(rating_mean - rating_std, color='black', linewidth=1, linestyle='--', label=f'±1 std ({rating_std:.1f})')
axes1[1].axvline(rating_mean + rating_std, color='black', linewidth=1, linestyle='--')
axes1[1].set_xlabel('Rating')
axes1[1].set_ylabel('Count')
axes1[1].set_title(f'Q2: Rating distribution\nmean = {rating_mean:.1f},  std dev = {rating_std:.1f}')
axes1[1].legend(fontsize=8)

# Q3: limit vs age scatter with r² annotation
axes1[2].scatter(df['Age'], df['Limit'], alpha=0.4, edgecolors='none', color='tab:green', s=20)
m3, b3 = np.polyfit(df['Age'], df['Limit'], 1)
x3 = np.linspace(df['Age'].min(), df['Age'].max(), 200)
axes1[2].plot(x3, m3*x3 + b3, color='black', linewidth=1.2)
axes1[2].set_xlabel('Age [years]')
axes1[2].set_ylabel('Limit [$]')
axes1[2].set_title(f'Q3: Age vs Limit\n$r^2$ = {r_lim_age**2:.4f}')

fig1.tight_layout()
fig1.savefig(os.path.join(folder_path, 'lab1_questions.png'))

# --- figure 2: scatter plots of 5 features vs balance ---
features = ['Income', 'Limit', 'Rating', 'Age', 'Cards']
colors   = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']

fig2, axes2 = plt.subplots(2, 3, figsize=(14, 8))
axes2 = axes2.flatten()

for i, (feat, color) in enumerate(zip(features, colors)):
    ax = axes2[i]
    ax.scatter(df[feat], df['Balance'], alpha=0.4, edgecolors='none', color=color, s=20)
    m, b = np.polyfit(df[feat], df['Balance'], 1)
    x = np.linspace(df[feat].min(), df[feat].max(), 200)
    ax.plot(x, m*x + b, color='black', linewidth=1.2)
    r = df[feat].corr(df['Balance'])
    ax.set_xlabel(feat)
    ax.set_ylabel('Balance [$]')
    ax.set_title(f'{feat} vs Balance  (r = {r:.3f})')

axes2[-1].set_visible(False)  # hide unused 6th subplot

fig2.tight_layout()
fig2.savefig(os.path.join(folder_path, 'lab1_scatterplots.png'))
plt.show()
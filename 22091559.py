import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df is your DataFrame with 'Country', 'DLRate', and 'populationpercentage' columns
df = pd.read_excel('Computer_Literacy.xlsx')
df = df.dropna(subset=['DLRate'])
df_sorted = df.sort_values(by='DLRate', ascending=False)
totalpopulation = df['Population (est)'].sum()
df_sorted['DLRate'] = (df['DLRate'] * 100).round(2)
df_sorted['populationpercentage'] = (df_sorted['Population (est)'] / totalpopulation) * 100

# Top five
top_five = df_sorted.head(5)
melted_df_top = pd.melt(top_five, id_vars=['Country'], value_vars=['populationpercentage', 'DLRate'],
                        var_name='Variable', value_name='Value')
melted_df_top['Value'] = pd.to_numeric(melted_df_top['Value'], errors='coerce')

plt.figure(figsize=(12, 6))
barplot_top = sns.barplot(x='Country', y='Value', hue='Variable', data=melted_df_top,
                          palette={'DLRate': 'orange', 'populationpercentage': 'skyblue'})

for i, dlrate in enumerate(melted_df_top[melted_df_top['Variable'] == 'DLRate']['Value']):
    plt.text(i + 0.2, dlrate, f' {dlrate:.3f} ', ha='center', va='bottom', color='black', fontweight='bold')

for i, percentage in enumerate(melted_df_top[melted_df_top['Variable'] == 'populationpercentage']['Value']):
    plt.text(i - 0.2, percentage, f' {percentage:.3f} ', ha='center', va='bottom', color='black', fontweight='bold')

plt.xlabel('Country', fontweight='bold')
plt.ylabel('Values', fontweight='bold')
labels_top = ['populationpercentage', 'DLRate']
plt.legend(labels_top, loc='upper center', ncol=2, bbox_to_anchor=(0.5, 1.07), borderaxespad=0.)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.savefig("22091559_1.png", dpi=300)

# Bottom five
bottom_five = df_sorted.tail(5)
melted_df_bottom = pd.melt(bottom_five, id_vars=['Country'], value_vars=['populationpercentage', 'DLRate'],
                           var_name='Variable', value_name='Value')
melted_df_bottom['Value'] = pd.to_numeric(melted_df_bottom['Value'], errors='coerce')

plt.figure(figsize=(12, 6))
barplot_bottom = sns.barplot(x='Country', y='Value', hue='Variable', data=melted_df_bottom,
                             palette={'DLRate': 'orange', 'populationpercentage': 'skyblue'})

for i, dlrate in enumerate(melted_df_bottom[melted_df_bottom['Variable'] == 'DLRate']['Value']):
    plt.text(i + 0.2, dlrate, f' {dlrate:.3f} ', ha='center', va='bottom', color='black', fontweight='bold')

for i, percentage in enumerate(melted_df_bottom[melted_df_bottom['Variable'] == 'populationpercentage']['Value']):
    plt.text(i - 0.2, percentage, f' {percentage:.3f} ', ha='center', va='bottom', color='black', fontweight='bold')

plt.xlabel('Country', fontweight='bold')
plt.ylabel('Values', fontweight='bold')
labels_bottom = ['populationpercentage', 'DLRate']
plt.legend(labels_bottom, loc='upper center', ncol=2, bbox_to_anchor=(0.5, 1.07), borderaxespad=0.)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.savefig("22091559-2.png", dpi=300)

# Pie chart
total_android_users_top = top_five['Android Users'].sum()
total_ios_users_top = top_five['iOS Users'].sum()
labels_top_pie = ['Android Users', 'iOS Users']
sizes_top_pie = [total_android_users_top, total_ios_users_top]

total_android_users_bottom = bottom_five['Android Users'].sum()
total_ios_users_bottom = bottom_five['iOS Users'].sum()
labels_bottom_pie = ['Android Users', 'iOS Users']
sizes_bottom_pie = [total_android_users_bottom, total_ios_users_bottom]

explode = [0, 0.1]
plt.figure(figsize=(10, 10))
plt.pie(sizes_bottom_pie, labels=labels_bottom_pie, autopct='%1.1f%%', startangle=140, explode=explode)
plt.legend(labels_bottom_pie, bbox_to_anchor=(1, 1))
plt.savefig("22091559-3.png", dpi=300)

plt.figure(figsize=(10, 10))
plt.pie(sizes_top_pie, labels=labels_top_pie, autopct='%1.1f%%', startangle=140, explode=explode)
plt.legend(labels_top_pie, bbox_to_anchor=(1, 1))
plt.savefig("22091559-4.png", dpi=300)

totalpopulation_top = top_five['Population (est)'].sum()
mobilephone_top = top_five['Smart Phone Users'].sum()
percentagemobileUser_top = (mobilephone_top / totalpopulation_top) * 100
nonmobileuser_top = 100 - percentagemobileUser_top

totalpopulation_bottom = bottom_five['Population (est)'].sum()
mobilephone_bottom = bottom_five['Smart Phone Users'].sum()
percentagemobileUser_bottom = (mobilephone_bottom / totalpopulation_bottom) * 100
nonmobileuser_bottom = 100 - percentagemobileUser_bottom

user_top = [percentagemobileUser_top, nonmobileuser_top]
labels_top_pie = ['Smart phone user', 'Non Smart Phone User']
explode = [0, 0.1]
plt.figure(figsize=(10, 10))
plt.pie(user_top, autopct='%1.1f%%', explode=explode)
plt.legend(labels_top_pie,  bbox_to_anchor=(1, 1))
plt.savefig("22091559_5.png", dpi=300)

user_bottom = [percentagemobileUser_bottom, nonmobileuser_bottom]
labels_bottom_pie = ['Smart phone user', 'Non Smart Phone User']
plt.figure(figsize=(10, 10))
plt.pie(user_bottom, autopct='%1.1f%%', explode=explode)
plt.legend(labels_bottom_pie,  bbox_to_anchor=(1, 1))
plt.show()



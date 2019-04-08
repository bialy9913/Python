import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
clients = pd.read_csv('D:\\Studia\\kurs_pythona_programy\\obrobka_danych\\clients.csv',index_col='NR_KLIENTA')
purchase = pd.read_csv('D:\\Studia\\kurs_pythona_programy\\obrobka_danych\\purchase.csv')
purchase = purchase.set_index('NR_KLIENTA')
purchase = purchase.rename(columns={'Kupno':'Number of purchases'})
purchase.plot(kind='bar')
plt.show()

amounts = pd.read_csv('D:\\Studia\\kurs_pythona_programy\\obrobka_danych\\amount_of_purchase.csv',index_col='NR_KLIENTA')
the_new_one = clients.join(amounts)
the_new_one = the_new_one.join(purchase)

plt.pie(the_new_one[:]['Number of purchases'],
        startangle=90,
        shadow=True,
        autopct='%1.2f%%',
        labels=[x for x in list(the_new_one.index)],
        colors=[(x,1-x,0) for x in np.arange(0,1,0.1)])
plt.title('Clients who bought the most')
plt.show()

the_new_one.sort_values(by='Wartosc',ascending=True,inplace=True)

plt.pie(the_new_one[:]['Wartosc'],
        startangle=90,
        shadow=True,
        autopct='%1.2f%%',
        labels=[x for x in list(the_new_one.index)],
        colors=[(x,1-x,0) for x in np.arange(0,1,0.1)])
plt.title('Sorted spending grouped by clients number')
plt.show()

the_new_one.loc[:,'Wartosc'].plot(kind='bar')
plt.title('Spending grouped by clients number')
plt.yticks([x for x in np.arange(0e7,1.8e7,0.1e7)])
plt.show()
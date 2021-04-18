import psycopg2
import matplotlib.pyplot as plt
import psycopg2.extras
import pandas as pd

def create_chart():
    conn = psycopg2.connect(
        database="crawler", user='postgres', password='admin', host='localhost', port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute('''SELECT * from pager_runk''')
    result = cursor.fetchall();
    items = [];
    values = [];
    for item in result:
        items.append(item[0].split("/")[2])
        values.append(item[1])
    plt.bar(items, values)
    plt.title('Page Ranks')
    plt.xlabel('sites')
    plt.ylabel('ranks')
    plt.xticks(rotation=90)
    plt.tight_layout(pad=0.8, w_pad=0.5, h_pad=5.0)
    plt.show()


create_chart()
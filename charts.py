import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar_sales_per_product(df):
    """Builds a bar chart for total sales per product (Description)."""
    df['TotalSales'] = df['UnitPrice'] * df['QuantitySold']

    summary = df.groupby('Description')['TotalSales'].sum().reset_index()
    summary = summary.sort_values('TotalSales', ascending=False)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=summary, x='Description', y='TotalSales', palette='magma')
    
    plt.title('Total Revenue per Product')
    plt.xlabel('Product Name')
    plt.ylabel('Total Sales (PHP)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_sales_share_pie(df):
    """Builds a pie chart showing which products contribute most to total revenue."""
    df['TotalSales'] = df['UnitPrice'] * df['QuantitySold']
    summary = df.groupby('Description')['TotalSales'].sum()
    
    plt.figure(figsize=(10, 10))
    summary.plot.pie(
        autopct='%1.1f%%', 
        startangle=140, 
        cmap='Spectral',
        pctdistance=0.85
    )
    
    plt.title('Sales Share by Product Revenue')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    csv_path = 'data/MercuryDrugSales.csv'
    
    try:
        data = pd.read_csv(csv_path)
        print(f"Successfully loaded {csv_path}")
        plot_bar_sales_per_product(data)
        plot_sales_share_pie(data)
        
    except Exception as e:
        print(f"Error: {e}")
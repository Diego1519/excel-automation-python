import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to show menu
def show_menu():
    print("\n--- Menu ---")
    print("1. Load Excel file")
    print("2. Descriptive statistics")
    print("3. Generate graphs")
    print("4. Conclusions")
    print("5. Exit")

# Function to load Excel file
def load_excel():
    file = input("Enter the name of the Excel file (with extension): ")
    try:
        df = pd.read_excel(file)
        print("File loaded successfully.")
        return df
    except FileNotFoundError:
        print("File not found.")
        return None

# Function for descriptive statistics
def descriptive_statistics(df):
    print("\n--- Descriptive Statistics ---")
    print(df.describe())

# Triggering questions function
def trigger_questions(df):
    print("\n--- Triggering Questions ---")

    # 1. Total operational cost by city
    print("\n1. Total operational cost by city:")
    df['Total Cost'] = df['Salario Mensual'] + df['Costo Aproximado del Equipo (Mensual)'] + df['Costo de Capacitación (Mensual)'] + df['Costo de Transporte (Mensual)']
    cost_by_city = df.groupby('Ciudad')['Total Cost'].sum().sort_values(ascending=False)
    print(cost_by_city)

    # 2. Salary distribution
    print("\n2. Salary distribution:")
    salary_distribution = df['Salario Mensual'].value_counts()
    print(salary_distribution)

    # 3. Age group distribution
    print("\n3. Age group distribution:")
    age_distribution = df['Edad'].value_counts(bins=[20, 30, 40, 50, 60], sort=False)
    print(age_distribution)

    # 4. Percentage of total cost represented by equipment, training, and transport
    print("\n4. Cost percentage breakdown:")
    total_cost = df['Costo Aproximado del Equipo (Mensual)'] + df['Costo de Capacitación (Mensual)'] + df['Costo de Transporte (Mensual)']
    percent_cost = total_cost.sum() / df['Total Cost'].sum() * 100
    print(f"Total percentage of cost due to equipment, training, and transport: {percent_cost:.2f}%")

# Function to generate graphs
def generate_graphs(df):
    print("\n--- Generating Graphs ---")
    
    # Graph 1: Operational cost by city
    df['Total Cost'] = df['Salario Mensual'] + df['Costo Aproximado del Equipo (Mensual)'] + df['Costo de Capacitación (Mensual)'] + df['Costo de Transporte (Mensual)']
    cost_by_city = df.groupby('Ciudad')['Total Cost'].sum()
    cost_by_city.plot(kind='bar', title='Total Operational Cost by City')
    plt.ylabel('Total Cost')
    plt.show()

    # Graph 2: Salary distribution
    sns.histplot(df['Salario Mensual'], kde=True)
    plt.title('Salary Distribution')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.show()

    # Graph 3: Age group distribution
    df['Age Group'] = pd.cut(df['Edad'], bins=[20, 30, 40, 50, 60], labels=['20-30', '30-40', '40-50', '50-60'])
    age_group_distribution = df['Age Group'].value_counts()
    age_group_distribution.plot(kind='bar', title='Age Group Distribution')
    plt.ylabel('Number of Employees')
    plt.show()

    # Graph 4: Cost breakdown (equipment, training, transport)
    cost_types = ['Costo Aproximado del Equipo (Mensual)', 'Costo de Capacitación (Mensual)', 'Costo de Transporte (Mensual)']
    total_costs = df[cost_types].sum()
    total_costs.plot(kind='pie', autopct='%1.1f%%', title='Cost Breakdown')
    plt.ylabel('')
    plt.show()

# Main function to run the menu
def main():
    df = None
    while True:
        show_menu()
        option = input("Choose an option: ")
        
        if option == '1':
            df = load_excel()
        elif option == '2' and df is not None:
            descriptive_statistics(df)
        elif option == '3' and df is not None:
            trigger_questions(df)
            generate_graphs(df)
        elif option == '4' and df is not None:
            print("\n--- Conclusions ---")
            print("Based on the analysis, strategic decisions can be made regarding operational costs and workforce distribution.")
        elif option == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid option or data not loaded.")

if __name__ == "__main__":
    main()
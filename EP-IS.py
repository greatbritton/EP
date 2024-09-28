import streamlit as st
import pandas as pd
import time

st.title("5-Year Financial Forecast")

# User inputs
latest_revenue = st.number_input(
    "Latest Annual Revenue ($)",
    min_value=0.0,
    value=1000000.0,
    step=10000.0,
    format="%.2f",
)

revenue_growth_rate = st.number_input(
    "Expected Revenue Growth Rate (%)",
    min_value=0.0,
    max_value=100.0,
    value=10.0,
    step=0.1,
    format="%.2f",
)

ebitda_margin = st.number_input(
    "EBITDA Margin for Year 1 (%)",
    min_value=0.0,
    max_value=100.0,
    value=15.0,
    step=0.1,
    format="%.2f",
)

net_income_margin = st.number_input(
    "Net Income Margin for Year 1 (%)",
    min_value=0.0,
    max_value=100.0,
    value=10.0,
    step=0.1,
    format="%.2f",
)

# Generate Forecast Button
if st.button("Generate Forecast"):
    # Display a progress bar
    with st.spinner('Generating forecast...'):
        # Simulate a delay
        time.sleep(2)
    
    # Initialize lists to store forecast data
    years = []
    revenues = []
    ebitdas = []
    net_incomes = []
    
    # Starting values
    revenue = latest_revenue
    ebitda_margin_year = ebitda_margin
    net_income_margin_year = net_income_margin
    
    # Calculate forecast for 5 years
    for year in range(1, 6):
        years.append(f"Year {year}")
        revenues.append(revenue)
        
        ebitda = revenue * (ebitda_margin_year / 100)
        ebitdas.append(ebitda)
        
        net_income = revenue * (net_income_margin_year / 100)
        net_incomes.append(net_income)
        
        # Update revenue for next year
        revenue *= (1 + revenue_growth_rate / 100)
    
    # Create a DataFrame with the forecast data
    forecast_df = pd.DataFrame({
        "Revenue ($)": revenues,
        "EBITDA ($)": ebitdas,
        "Net Income ($)": net_incomes
    }, index=years)
    
    # Format numbers with commas and two decimal places
    forecast_df = forecast_df.applymap(lambda x: f"${x:,.2f}")
    
    # Transpose the DataFrame so that years are on the x-axis
    forecast_df_transposed = forecast_df.T
    
    # Display the forecast table
    st.success("Forecast generated!")
    st.table(forecast_df_transposed)

else:
    st.write("Please enter the parameters and click **Generate Forecast** to see the results.")

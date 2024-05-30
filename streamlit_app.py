import streamlit as st
import pandas as pd

def is_in_range(value, lower_bound, upper_bound):
    return lower_bound <= value <= upper_bound

def get_sum_of_selected_months_and_years(file,year_from : int, year_to : int, months : list):
    sum = 0
    dict_of_data = dict()
    for line in file:
        _line = str(line.strip().decode('utf-8'))
        _year = int(_line.split('-')[0])
        _month = _line.split('-')[1]
        if is_in_range(_year,year_from,year_to) and _month in months:
            try:
                value = float(_line.split(',')[1])
            except Exception as e:
                value = 0
                st.write(f"Some error on {e}")
                
            if _year not in dict_of_data.keys():
                dict_of_data[_year] = dict()
            else:
                if _month not in dict_of_data[_year].keys():
                    dict_of_data[_year][_month] = 0
                else:
                    dict_of_data[_year][_month] += value
        
    return dict_of_data

def main():
    st.title("Zafirenia Calculator")

    year_bounds = st.slider(
        "Select a range of years",
        1950, 2024, (1950, 2024))

    options_months = st.multiselect(
        "Months",
        ["01", "02", "03", "04","05","06","07","08","09","10","11","12"],)
    
    
    uploaded_file = st.file_uploader("Choose a HTS file", type="hts")
    
    if uploaded_file is not None:
        dict_result = get_sum_of_selected_months_and_years(uploaded_file,year_bounds[0],year_bounds[1],options_months)
        df = pd.DataFrame(dict_result)

        # df = df.T
        st.dataframe(df)
        # st.write(f"The sum is: {sum_result}")

if __name__ == "__main__":
    main()

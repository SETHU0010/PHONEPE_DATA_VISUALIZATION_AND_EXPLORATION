import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('Agg_Trans.csv', index_col=0)
state = pd.read_csv('Longitude_Latitude_State_Table.csv')
districts = pd.read_csv('Data_Map_Districts_Longitude_Latitude.csv')
districts_tran = pd.read_csv('district_map_transaction.csv', index_col=0)
app_opening = pd.read_csv('district_registering_map.csv', index_col=0)
user_device = pd.read_csv('user_by_device.csv', index_col=0)

# Prepare data for visualization
state = state.sort_values(by='state').reset_index(drop=True)
df2 = df.groupby(['State']).sum()[['Transacion_count', 'Transacion_amount']].reset_index()
choropleth_data = state.copy()

for column in df2.columns:
    choropleth_data[column] = df2[column]
    
choropleth_data = choropleth_data.drop(labels='State', axis=1)
df.rename(columns={'State': 'state'}, inplace=True)
sta_list = ['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal']
state['state'] = pd.Series(data=sta_list)
state_final = pd.merge(df, state, how='outer', on='state')
districts_final = pd.merge(districts_tran, districts, how='outer', on=['State', 'District'])

# Streamlit app settings
st.set_page_config(page_title='PhonePe Pulse Data Visualization', layout='wide')
st.balloons()

# Main Streamlit code
with st.container():
    st.title(':violet: PhonePe Pulse Data Visualization (2018-2022)')
    st.write(' ')

# Functions for different sections
def about_the_developer():
    st.header("About the Developer")
    st.subheader("Contact Details")
    st.write("Email: sethumadhavanvelu2002@example.com")
    st.write("Phone: 9159299878")
    st.write("[LinkedIn ID](https://www.linkedin.com/in/sethumadhavan-v-b84890257/)")
    st.write("[github.com](https://github.com/SETHU0010/YouTube_Data_Harvesting_and_Warehousing_using_SQL_and_Streamlit)")

def Technologies_Used ():
    st.header("Technologies_Used")    
    st.caption("Github Cloning")
    st.caption("Python")
    st.caption("Pandas")
    st.caption("MYSQL")
    st.caption("mysql-connector-python")
    st.caption("Streamlit")
    st.caption("Plotly")

def objective():
    st.header("Objective")
    st.write("Develop a comprehensive and user-friendly solution for extracting, transforming, and visualizing data from the PhonePe Pulse GitHub repository.")

def features():
    st.header("Features")
    st.write("Interactive and visually appealing dashboard.")
    st.write("Live geo-visualization using Plotly.")
    st.write("Multiple dropdown options for user interaction.")
    st.write("Dynamic data updates from a MySQL database.")
        
def workflow():
    st.header("Workflow")
    st.write("Clone the PhonePe Pulse GitHub repository.")
    st.write("Clean and preprocess the data.")
    st.write("Store the data in a MySQL database.")
    st.write("Develop an interactive dashboard using Streamlit and Plotly.")
    st.write("Fetch and display data dynamically on the dashboard.")

def Problem_Statement():
    st.header("Problem Statement")
    st.write("Extract, process, and visualize data from the Phonepe Pulse Github repository to provide insights in a user-friendly manner using a dashboard.")

def required_python_libraries():
    st.header("Required Python Libraries")
    st.write("The following Python libraries are required for the project:")
    libraries = ["git", "pandas","mysql.connector", "plotly", "streamlit"]
    st.write(libraries)

def approach():
    st.header("Approach")
    st.write("Data extraction ")
    st.write("Data transformation")
    st.write("Database insertion")
    st.write("Dashboard creation")
    st.write("Data retrieval")
    st.write("Display data in the Streamlit app")

# Add other function definitions for Technologies_Used(), objective(), features(), workflow(), Problem_Statement(),
# required_python_libraries(), and approach() here...
# Home section
col1, col2 = st.columns(2)
with col1:
    sub_options = ["About the Developer", "Technologies Used", "Problem Statement", "Objective", "Approach", "Features", "Workflow", "Required Python Libraries"]
    sub_choice = st.radio("Navigation", sub_options)

with col2:
            if sub_choice == "About the Developer":
                about_the_developer()
            elif sub_choice == "Technologies Used":
                Technologies_Used()
            elif sub_choice == "Problem Statement":
                Problem_Statement()
            elif sub_choice == "Objective":
                objective()
            elif sub_choice == "Features":
                features()
            elif sub_choice == "Workflow":
                workflow()
            elif sub_choice == "Required Python Libraries":
                required_python_libraries()
            elif sub_choice == "Approach":
                approach()

        # Add conditions for other sub-options here...

# Add other sections like Geographical Analysis, User Device Analysis, Payment Types Analysis, Transaction Analysis of States
# with their respective visualizations...

# ------------------------------------------ Streamlit app Plot 1 Scatter plot of registered user and app opening ----------------------------
with st.container():
    st.subheader(':violet[Registered User & App Installed -> State and District-wise:]')
    st.write(' ')
    scatter_year = st.selectbox('Please select the Year', ('2018', '2019', '2020', '2021', '2022'))
    st.write(' ')
    scatter_state = st.selectbox('Please select State', sta_list, index=10)
    scatter_year = int(scatter_year)
    scatter_reg_df = app_opening[(app_opening['Year'] == scatter_year) & (app_opening['State'] == scatter_state)]
    scatter_register = px.scatter(scatter_reg_df, x="District", y="Registered_user", color="District",
                                  hover_name="District", hover_data=['Year', 'Quater', 'App_opening'], size_max=60)
    st.plotly_chart(scatter_register)
st.write(' ')




# ------------------------------------- Streamlit Tabs for various analysis -----------------------------------------------------------------
geo_analysis, Device_analysis, payment_analysis, transac_yearwise = st.tabs(
    ["Geographical Analysis", "User Device Analysis", "Payment Types Analysis", "Transaction Analysis of States"])
# ------------------------------------------- Geo-analysis ----------------------------------------------------------------------------------
with geo_analysis:
    st.subheader(':violet[Transaction Analysis -> State and District-wise:]')
    st.write(' ')
    Year = st.radio('Please select the Year', ('2018', '2019', '2020', '2021', '2022'), horizontal=True)
    st.write(' ')
    Quarter = st.radio('Please select the Quarter', ('1', '2', '3', '4'), horizontal=True)
    st.write(' ')
    Year = int(Year)
    Quarter = int(Quarter)
    plot_district = districts_final[(districts_final['Year'] == Year) & (districts_final['Quater'] == Quarter)]
    plot_state = state_final[(state_final['Year'] == Year) & (state_final['Quater'] == Quarter)]
    plot_state_total = plot_state.groupby(['state', 'Year', 'Quater', 'Latitude', 'Longitude']).sum()
    plot_state_total = plot_state_total.reset_index()
    state_code = ['AN', 'AD', 'AR', 'AS', 'BR', 'CH', 'CG', 'DNHDD', 'DL', 'GA',
                  'GJ', 'HR', 'HP', 'JK', 'JH', 'KA', 'KL', 'LA', 'LD', 'MP', 'MH',
                  'MN', 'ML', 'MZ', 'NL', 'OD', 'PY', 'PB', 'RJ', 'SK', 'TN', 'TS',
                  'TR', 'UP', 'UK', 'WB']
    plot_state_total['code'] = pd.Series(data=state_code)
    # ------------------------------------------- Geo-visualization of transaction data ------------------------------------------------------
    fig1 = px.scatter_geo(plot_district,
                          lon=plot_district['Longitude'],
                          lat=plot_district['Latitude'],
                          color=plot_district['Transaction_amount'],
                          size=plot_district['Transaction_count'],
                          hover_name="District",
                          hover_data=["State", 'Transaction_amount', 'Transaction_count', 'Year', 'Quater'],
                          title='District',
                          size_max=22,)
    fig1.update_traces(marker={'color': "#CC0044", 'line_width': 1})
    fig2 = px.scatter_geo(plot_state_total,
                          lon=plot_state_total['Longitude'],
                          lat=plot_state_total['Latitude'],
                          hover_name='state',
                          text=plot_state_total['code'],
                          hover_data=['Transacion_count', 'Transacion_amount', 'Year', 'Quater'],
                          )
    fig2.update_traces(marker=dict(color="#D5FFCC", size=0.3))
    fig = px.choropleth(
        choropleth_data,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='Transacion_amount',
        color_continuous_scale='twilight',
        hover_data=['Transacion_count', 'Transacion_amount']
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.add_trace(fig1.data[0])
    fig.add_trace(fig2.data[0])
    fig.update_layout(height=800, width=800)
    st.write(' ')
    st.write(' ')
    
    st.plotly_chart(fig)


# --------------------------------------------------- Device analysis statewise ------------------------------------------------------------
with Device_analysis:
    st.subheader(':violet[User Device Analysis -> State-wise:]')
    tree_map_state = st.selectbox('Please select State', sta_list, index=10, key='tree_map_state')
    tree_map_state_year = int(st.radio('Please select the Year', ('2018', '2019', '2020', '2021', '2022'), horizontal=True, key='tree_map_state_year'))
    tree_map_state_quater = int(st.radio('Please select the Quarter', ('1', '2', '3', '4'), horizontal=True, key='tree_map_state_quater'))
    user_device_treemap = user_device[(user_device['State'] == tree_map_state) & (user_device['Year'] == tree_map_state_year) &
                                      (user_device['Quater'] == tree_map_state_quater)]
    user_device_treemap['Brand_count'] = user_device_treemap['Brand_count'].astype(str)
    # ----------------------------------------- Treemap view of user device ----------------------------------------------------------------
    user_device_treemap_fig = px.treemap(user_device_treemap, path=['State', 'Brand'], values='Brand_percentage', hover_data=['Year', 'Quater'],
                                         color='Brand_count',
                                         title='User device distribution in ' + tree_map_state +
                                         ' in ' + str(tree_map_state_year)+' at '+str(tree_map_state_quater)+' quarter',)
    st.plotly_chart(user_device_treemap_fig)
    # ---------------------------------------- Bar chart view of user device -----------------------------------------------------------------
    bar_user = px.bar(user_device_treemap, x='Brand', y='Brand_count', color='Brand',
                      title='Bar chart analysis', color_continuous_scale='sunset',)
    st.plotly_chart(bar_user)


# ----------------------------------------- Payment type analysis of transaction data ----------------------------------------------------------
with payment_analysis:
    st.subheader(':violet[Payment Type Analysis -> 2018 - 2022:]')
    payment_mode = pd.read_csv('Agg_Trans.csv', index_col=0)
    pie_pay_mode_state = st.selectbox('Please select State', sta_list, index=10, key='pie_pay_mode_state')
    pie_pay_mode_year = int(st.radio('Please select the Year', ('2018', '2019', '2020', '2021', '2022'), horizontal=True, key='pie_pay_mode_year'))
    pie_pay_mode_quater = int(st.radio('Please select the Quarter', ('1', '2', '3', '4'), horizontal=True, key='pie_pay_mode_quater'))
    payment_mode = payment_mode[(payment_mode['State'] == pie_pay_mode_state) & (payment_mode['Year'] == pie_pay_mode_year) &
                                (payment_mode['Quater'] == pie_pay_mode_quater)]
    labels = payment_mode['Transacion_type'].unique()
    payment_mode_fig = px.pie(payment_mode, values='Transacion_count', names='Transacion_type', title='Payment Type Distribution in ' +
                              pie_pay_mode_state+' in '+str(pie_pay_mode_year)+' at '+str(pie_pay_mode_quater)+' quarter')
    st.plotly_chart(payment_mode_fig)
    pie2 = px.pie(payment_mode, values='Transacion_amount', names='Transacion_type', title='Payment Amount Distribution in ' +
                 pie_pay_mode_state+' in '+str(pie_pay_mode_year)+' at '+str(pie_pay_mode_quater)+' quarter')
    st.plotly_chart(pie2)
    # ----------------------------------------- Payment type analysis using bar chart ----------------------------------------------------------
    bar_transaction_type = px.bar(payment_mode, x='Transacion_type', y='Transacion_count', color='Transacion_count', title='Transaction Type Bar chart view')
    bar_transaction_amount = px.bar(payment_mode, x='Transacion_type', y='Transacion_amount', color='Transacion_amount', title='Transaction Amount Bar chart view')
    st.plotly_chart(bar_transaction_type)
    st.plotly_chart(bar_transaction_amount)


# -------------------------------------------- Transaction analysis (state-wise) --------------------------------------------------------with transac_yearwise:

with transac_yearwise:
    st.subheader(':violet[Transaction Analysis of each state (2018 - 2022):]')
    select_state_year = st.selectbox('Please select State', sta_list, index=10, key='select_state_year')
    select_state_year_year = int(st.radio('Please select the Year', ('2018', '2019', '2020', '2021', '2022'), horizontal=True, key='select_state_year_year'))
    select_state_year_quater = int(st.radio('Please select the Quarter', ('1', '2', '3', '4'), horizontal=True, key='select_state_year_quater'))
    plot_state_yearly = state_final[(state_final['state'] == select_state_year) & (state_final['Year'] == select_state_year_year) &
                                    (state_final['Quater'] == select_state_year_quater)]
    
    if not plot_state_yearly.empty:
        state_analysis_scatter = px.scatter(plot_state_yearly, x="state", y="Transacion_amount", size="Transacion_count", color="Transacion_count",
                                            hover_name="state", hover_data=['state', 'Transacion_amount', 'Transacion_count', 'Year', 'Quater'])
        state_analysis_bar = px.bar(plot_state_yearly, x='state', y='Transacion_count', color='state',
                                    hover_data=['state', 'Transacion_amount', 'Transacion_count', 'Year', 'Quater'], title='Transaction count Bar chart view')
        state_analysis_bar_amount = px.bar(plot_state_yearly, x='state', y='Transacion_amount', color='state',
                                           hover_data=['state', 'Transacion_amount', 'Transacion_count', 'Year', 'Quater'], title='Transaction amount Bar chart view')
        
        st.plotly_chart(state_analysis_scatter)
        st.plotly_chart(state_analysis_bar)
        st.plotly_chart(state_analysis_bar_amount)
    else:
        st.write("No data available for the selected state, year, and quarter.")



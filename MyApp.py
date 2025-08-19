import pandas as pd
import streamlit as st


st.title("SIM Study Planning App")


option = st.selectbox(
    "Your School: ",
    ("UOW", "RMIT", "UOL"),
    key="school"
)

option = st.selectbox(
    "Your Degree: ",
    ("Finance", "Computer Science", "Business Management"),
    key="degree"
)

option = st.selectbox(
    "Your Year: ",
    ("Year 1", "Year 2", "Year 3", "Pre-U"),
    key="year"
)


if st.button("Generate Plan!"):
    st.markdown("Streamlit is really cool")




# start of graph
# data_df = pd.DataFrame(
#     {
#         "sales": [
#             [0, 4, 26, 80, 100, 40],
#             [80, 20, 80, 35, 40, 100],
#             [10, 20, 80, 80, 70, 0],
#             [10, 100, 20, 100, 30, 100],
#         ],
#     }
# )

# st.data_editor(
#     data_df,
#     column_config={
#         "sales": st.column_config.AreaChartColumn(
#             "Sales (last 6 months)",
#             width="medium",
#             help="The sales volume in the last 6 months",
#             y_min=0,
#             y_max=100,
#          ),
#     },
#     hide_index=True,
# )
# end of graph --------------------------
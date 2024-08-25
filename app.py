import streamlit as st
import pandas as pd

# Project information section
st.title("Arabic NLP: Generating Multiple Choice Questions of Saudi Schoolbooks")
st.write("**Team Members:**")
st.write("1. Yazan Alshuaibi")
st.write("2. Mohanad AlDakheel")
st.write("3. Moayad Alghamdi")
st.write("4. Zyad Alzhrani")

st.markdown("---")  # Line separator

# Load the CSV file
df = pd.read_csv('output.csv')

# Sample 10 random examples
sampled_df = df.sample(10, random_state=10)  # Using random_state for reproducibility

# Function to display options and handle user selection
def display_question(row, index):
#    st.write(f"### Paragraph {index + 1}")
#    st.write(row['chunk'])
    
    st.write(f"**{row['Question']}**")
    
    options = [
        ('A', row['Option_A']),
        ('B', row['Option_B']),
        ('C', row['Option_C']),
        ('D', row['Option_D'])
    ]

    selected_option = st.radio(
        "Choose your answer:",
        options,
        format_func=lambda x: f"{x[0]}: {x[1]}",
        key=f"question_{index}",
        index=None  # This removes the default selection
    )

    if st.button("Submit", key=f"submit_{index}"):
        if selected_option is None:
            st.warning("Please select an answer before submitting.")
        elif selected_option[0] == row['Answer_Key']:
            st.success(f"Correct! The answer is {selected_option[0]}: {selected_option[1]}")
        else:
            st.error(f"Incorrect. You selected {selected_option[0]}: {selected_option[1]}")
            correct_option = next(opt for opt in options if opt[0] == row['Answer_Key'])
            st.success(f"The correct answer is {correct_option[0]}: {correct_option[1]}")

    st.write("---")  # Separator between questions

# Display all 10 questions
for index, row in sampled_df.iterrows():
    display_question(row, index)
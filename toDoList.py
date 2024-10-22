import streamlit as st

# Title of the app
st.title("To-Do List App")

# Text input for the task
task = st.text_input("Enter a task")

# Number input for the task priority
# Ensure min_value and max_value are correctly set
task_priority = st.number_input("Enter task priority (0-10)", min_value=0, max_value=10, value=0)

# Button to add task
if st.button("Add Task"):
    if task:  # Check if the task is not empty
        st.write(f"Task added: {task} with priority {task_priority}")
    else:
        st.error("Please enter a task before adding it.")

# Optional: Display the current task list
st.write("### Current Tasks")
if task:
    st.write(f"- {task} (Priority: {task_priority})")
else:
    st.write("No tasks added yet.")

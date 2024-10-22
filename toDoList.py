import streamlit as st

# List to store tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Title of the app
st.title("To-Do List App")

# Input field to add tasks
task = st.text_input("Add a new task:")

# Add task button
if st.button("Add Task"):
    if task:
        st.session_state.tasks.append(task)
        st.success(f"'{task}' added to your list")
    else:
        st.error("Please enter a task")

# Display the list of tasks
if st.session_state.tasks:
    st.write("Your tasks:")
    for idx, task in enumerate(st.session_state.tasks):
        st.write(f"{idx + 1}. {task}")
else:
    st.write("Your to-do list is empty.")

# Input field to remove tasks by number
task_to_remove = st.number_input("Enter task number to remove:", min_value=1, max_value=len(st.session_state.tasks), step=1)

# Remove task button
if st.button("Remove Task"):
    if st.session_state.tasks:
        task = st.session_state.tasks.pop(task_to_remove - 1)
        st.success(f"'{task}' removed from your list")
    else:
        st.error("No tasks to remove")

import streamlit as st
import functions
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

todos = functions.get_todos()


def add_todo():
    local_todo = st.session_state['add']
    todos.append(local_todo + '\n')
    functions.write_todos(todos)
    st.session_state['add'] = ''


st.title('To-do Web App')
st.write("List of todos:")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        del st.session_state[todo]
        functions.write_todos(todos)
        st.rerun()

st.text_input(label="", placeholder="Enter a to-do...",
              on_change=add_todo, key='add')


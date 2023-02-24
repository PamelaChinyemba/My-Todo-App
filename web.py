import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + '\n'
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader('These are my weekly tasks')
st.write("This will help me be more productive")

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label="", placeholder='Enter a new todo.....',
              on_change=add_todo, key='new_todo')

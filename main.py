import streamlit as st
import function

todos=function.get_todos("todos.txt")

def add_todo():
    todo=st.session_state["new_todo"]+'\n'
    todos.append(todo)
    function.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("My to-do list")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

checkbox={}
for index,todo in enumerate(todos):
    if todo not in checkbox:
        checkbox[todo]=st.checkbox(todo,key=todo)

if st.button("Remove Selected "):
    items_to_remove=[x for x in checkbox if checkbox[x]==True]

    for item in items_to_remove:
        todos.remove(item)
    function.write_todos(todos)
    st.rerun()

st.text_input(label="Enter to-do item",placeholder='add new todo...',key='new_todo', on_change=add_todo)

if st.button("Add Item") and st.session_state["new_todo"]!="":
    add_todo()
    st.rerun()
#st.session_state
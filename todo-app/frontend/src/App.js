import React, { useState } from "react";
import TodoInput from "./controller/TodoInput";
import TodoList from "./controller/TodoList";


function App(){
  const [todos, setTodos] = useState([]);

  const addTodo = (text) => {
    const newTodo = { id: generateRandomId(), text, completed: false};
    setTodos([...todos, newTodo]);
  };

  const toggleComplete = (id) => {
    setTodos(
      todos.map((todo) => {
        console.log("Toggling ID:", id);
        // IDが一致するタスクの完了状態を切り替える
        if (todo.id === id) {
          return { ...todo, completed: !todo.completed };
        }
        return todo;
      })
    );
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id))
  };

  return(
    <div className= "App">
      <h1>My ToDo List</h1>
      <TodoInput addTodo={addTodo} />
      <TodoList todos={todos} toggleComplete={toggleComplete} deleteTodo={deleteTodo} /> 
    </div>
  );
}

function generateRandomId() {
  return Math.floor(Math.random() * 90000) + 10000;
}

export default App;
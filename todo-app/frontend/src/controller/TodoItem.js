import React from 'react';

function TodoItem({ todo, toggleComplete, deleteTodo }) {
  return (
    <li style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}>
      {todo.text}
      <button onClick={() => toggleComplete(todo.id)}>
        {todo.completed ? 'not completed' : 'completed'}
      </button>
      <button onClick={() => deleteTodo(todo.id)}>delete</button>
    </li>
  );
}

export default TodoItem;
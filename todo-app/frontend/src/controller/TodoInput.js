import React, {useState} from 'react';

function TodoInput({ addTodo }) {
    const [text, setText] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if(text){
            addTodo(text);
            setText('');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Please write your task here"
            />
            <button type="submit">Submit</button>
        </form>
    );   
}

export default TodoInput;
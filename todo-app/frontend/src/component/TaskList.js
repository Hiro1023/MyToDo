import React, { useState, useEffect } from 'react';
import '../styles/TaskList.css';

function TaskList() {
    const [tasks, setTasks] = useState([]);
    const [editTaskId, setEditTaskId] = useState(null);
    const [editTaskText, setEditTaskText] = useState("");
    const [editTaskDescription, setEditTaskDescription] = useState(""); // Descriptionの編集用
    const [newTask, setNewTask] = useState("");
    const [errorMessage, setErrorMessage] = useState("");

    useEffect(() => {
        fetchTasks();
    }, []);

    const addTask = () => {
        if (!newTask.trim()) {  
            setErrorMessage("Task content cannot be empty");
            return;
        }

        fetch('http://localhost:5000/todos', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ task: newTask, description: "New task description" }),
        })
        .then(response => {
            if (!response.ok) {
                if (response.status === 400) {
                    throw new Error("Task name already exists. Please choose a different name.");
                } else {
                    throw new Error("Failed to add task. Please try again later.");
                }
            }
            return response.json();
        })
        .then(createdTask => {
            setTasks(prevTasks => [...prevTasks, createdTask]);
            setNewTask("");
            setErrorMessage("");
        })
        .catch(error => {
            console.error('Error adding task:', error);
            setErrorMessage("Failed to add task. Please try again later.");
        });
    };

    const fetchTasks = () => {
        fetch('http://localhost:5000/todos')
            .then(response => response.json())
            .then(data => setTasks(data))
            .catch(error => {
                console.error('Error fetching tasks:', error);
                setErrorMessage("Failed to fetch tasks. Please try again later.");
            });
    };

    const toggleCompleteStatus = (taskId, currentStatus) => {
        fetch(`http://localhost:5000/todos/${taskId}`, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ completed: !currentStatus }),
        })
        .then(response => response.json())
        .then(updatedTask => {
            setTasks(prevTasks =>
                prevTasks.map(task => (task._id === taskId ? updatedTask : task))
            );
            setErrorMessage("");
        })
        .catch(error => {
            console.error('Error updating task:', error);
            setErrorMessage("Failed to update task. Please try again later.");
        });
    };

    const deleteTask = (taskId) => {
        fetch(`http://localhost:5000/todos/${taskId}`, {
            method: 'DELETE',
        })
        .then(() => {
            setTasks(prevTasks => prevTasks.filter(task => task._id !== taskId));
            setErrorMessage("");
        })
        .catch(error => {
            console.error('Error deleting task:', error);
            setErrorMessage("Failed to delete task. Please try again later.");
        });
    };

    const editTask = (taskId, newText, newDescription) => {
        if (!newText.trim()) {
            setErrorMessage("Task content cannot be empty");
            return;
        }
    
        const currentTask = tasks.find(task => task._id === taskId);
    
        fetch(`http://localhost:5000/todos/${taskId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ task: newText, description: newDescription, completed: currentTask.completed }),
        })
        .then(response => response.json())
        .then(updatedTask => {
            setTasks(prevTasks =>
                prevTasks.map(task => (task._id === taskId ? updatedTask : task))
            );
            setEditTaskId(null);
            setEditTaskText("");
            setEditTaskDescription(""); // Descriptionをクリア
            setErrorMessage("");
        })
        .catch(error => {
            console.error('Error updating task:', error);
            setErrorMessage("Failed to update task. Please try again later.");
        });
    };

    return (
        <div className="task-list-container">
            <h1>Task List</h1>
            
            {errorMessage && <div className="error-message">{errorMessage}</div>}
    
            <input
                type="text"
                placeholder="New task"
                value={newTask}
                onChange={(e) => setNewTask(e.target.value)}
            />
            <button onClick={addTask}>Add Task</button>
            <ul>
                {tasks.map(task => (
                    <li key={task._id} className={`task-item ${task.completed ? 'completed' : ''}`}>
                        {editTaskId === task._id ? (
                            <>
                                <input
                                    type="text"
                                    value={editTaskText}
                                    onChange={(e) => setEditTaskText(e.target.value)}
                                />
                                <input
                                    type="text"
                                    value={editTaskDescription}
                                    onChange={(e) => setEditTaskDescription(e.target.value)}
                                />
                                <button onClick={() => editTask(task._id, editTaskText, editTaskDescription)}>Save</button>
                                <button onClick={() => setEditTaskId(null)}>Cancel</button>
                            </>
                        ) : (
                            <>
                                <div>
                                    <span>{task.task}</span>
                                    <div style={{ fontSize: '0.9em', color: 'gray', marginTop: '4px' }}>{task.description}</div>
                                </div>
                                <button onClick={() => toggleCompleteStatus(task._id, task.completed)}>
                                    {task.completed ? "Undo Complete" : "Complete"}
                                </button>
                                <button onClick={() => {
                                    setEditTaskId(task._id);
                                    setEditTaskText(task.task);
                                    setEditTaskDescription(task.description);
                                }}>Edit</button>
                                <button onClick={() => deleteTask(task._id)} className="delete">Delete</button>
                            </>
                        )}
                    </li>
                ))}
            </ul>
        </div>
    );
}
    

export default TaskList;

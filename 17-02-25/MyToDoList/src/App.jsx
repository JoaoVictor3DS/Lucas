import { useState } from 'react';
import TaskForm from "./components/TaskForm";
import TaskList from "./components/TaskList";

import './App.css'

function App() {
  const [tasks, setTask] = useState([])

  const addTask = (text) => {
    setTask([...tasks, { text, completed: false }]);

  };

  const toggleTask = (index) => {
    const newTasks = [...tasks];
    newTasks[index].completed = !newTasks[index].completed;
    setTask(newTasks);
  };

  const deleteTask = (index) => {
    const newTasks = tasks.filter((_, i) => i !== index);
    setTask(newTasks);
  };

  return (
    <div>
      <h1>Lista de Tarefas</h1>
      <TaskForm onAddTask={addTask} />
      <TaskList tasks={tasks} onToggleTask={toggleTask} onDeleteTask={deleteTask} />
    </div>
  )
}

export default App

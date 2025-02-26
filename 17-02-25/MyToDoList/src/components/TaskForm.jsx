import { useState } from "react";

function TaskForm({ onAddTask }) {
    const [task, setTask] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        if (task.trim()) {
            onAddTask(task);
            setTask("");
        }

    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Nova Tarefa..."
                value={task}
                onChange={(e) => setTask(e.target.value)}

            />
            <button type="submit">Add</button>
        </form>
    );
}

export default TaskForm;
import TaskItem from "./TaskItem";

function TaskList({ tasks, onToggleTask, onDeleteTask }) {
    return (
        <ul>
            {tasks.map((task, index) => (
                <TaskItem
                    key={index}
                    tasks={task}
                    onToggle={() => onToggleTask(index)}
                    onDelete={() => onDeleteTask(index)}
                />

            ))}
        </ul>
    );
}

export default TaskList;
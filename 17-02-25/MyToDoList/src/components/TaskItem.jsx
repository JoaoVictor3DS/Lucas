function TaskItem({ tasks, onToggle, onDelete }) {
    return (
        <div>
            <li>
                <span
                    onClick={onToggle}
                    style={{ textDecoration: tasks.completed ? "line-through" : "none", cursor: "pointer" }}
                >
                    {tasks.text}

                </span>
                <button onClick={onDelete}>X</button>
            </li>
        </div>
    )
}
export default TaskItem;
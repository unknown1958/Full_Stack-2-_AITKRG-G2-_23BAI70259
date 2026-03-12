import { useState } from "react";
import useForm from "./useform";

function TaskManager() {

  const { values, handleChange, resetForm } = useForm({
    title: "",
    priority: "Low",
  });

  const [tasks, setTasks] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();

    setTasks([...tasks, values]);

    resetForm();
  };

  return (
    <>
      <h2>Task Tracker</h2>

      <form onSubmit={handleSubmit}>

        <input
          type="text"
          name="title"
          placeholder="Task Title"
          value={values.title}
          onChange={handleChange}
        />

        <select
          name="priority"
          value={values.priority}
          onChange={handleChange}
        >
          <option value="Low">Low</option>
          <option value="Medium">Medium</option>
          <option value="High">High</option>
        </select>

        <button type="submit">Add Task</button>

      </form>

      <h3>Task List</h3>

      <ul>
        {tasks.map((task, index) => (
          <li key={index}>
            {task.title} | {task.priority}
          </li>
        ))}
      </ul>
    </>
  );
}

export default TaskManager;
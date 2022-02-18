import { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom'
// import from files I created
import Header from './components/Header'
import Footer from './components/Footer'
import About from './components/About'
import './index.css';
import Tasks from './components/Tasks'
import AddTask from './components/AddTask'


function App() {
  const [showAddTask, setShowAddTask] = useState(false)
  const [tasks, setTasks] = useState([]);
  useEffect(() => {
    const getTasks = async () => {
      const tasksFromServer = await fetchTasks();
      setTasks(tasksFromServer)
    }
    getTasks()
  }, [])

  // todo: Fetch Tasks
  const fetchTasks = async () => {
    const res = await fetch('http://localhost:5000/tasks')
    const data = await res.json()
    // console.log(data);
    return data
  }

  // todo: Fetch Task
  const fetchTask = async (id) => {
    const res = await fetch(`http://localhost:5000/tasks/${id}`)
    const data = await res.json()
    // console.log(data);
    return data
  }

  // todo: Add Task
  const addTask = async (task) => {
    const res = await fetch('http://localhost:5000/tasks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(task),
    })
    const data = await res.json()
    setTasks([...tasks, data])
  }

  // todo: delete task
  const deleteTask = async (id) => {
    await fetch(`http://localhost:5000/tasks/${id}`, { method: 'DELETE' },)
    setTasks(tasks.filter((task) => task.id !== id))
  }

  // todo: Toggle Reminder
  const toggleReminder = async (id) => {
    const taskToToggle = await fetchTask(id)
    const updTask = {
      ...taskToToggle, reminder: !taskToToggle.reminder
    }
    const res = await fetch(`http://localhost:5000/tasks/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(updTask)
    })

    const data = await res.json()

    setTasks(tasks.map((task) =>
      task.id === id ? {
        ...task, reminder: !data.reminder
      } : (
        task
      )
    ))
  }

  return (
    <Router>
      <div className="container">
        <Header title={'Task Tracker'} onAdd={() => setShowAddTask(!showAddTask)} showAdd={showAddTask} />

        <Route path='/' exact render={(props) => (
          <>
            {showAddTask && <AddTask onAdd={addTask} />}
            {tasks.length > 0 ? (
              <Tasks tasks={tasks} onDelete={deleteTask} onToggle={toggleReminder} />
            ) : (
              'No tasks to show'
            )}
          </>
        )} />
        <Route path='/about' component={About} />
        <Footer />
      </div>
    </Router>
  );
}

export default App;

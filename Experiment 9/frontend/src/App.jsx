import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [user, setUser] = useState(null)
  const [users, setUsers] = useState([])
  const [newUser, setNewUser] = useState({ email: '', name: '', role: 'USER' })
  const [message, setMessage] = useState('')

  useEffect(() => {
    fetchUser()
  }, [])

  const fetchUser = async () => {
    try {
      const response = await axios.get('/api/user')
      setUser(response.data)
    } catch (error) {
      setUser(null)
    }
  }

  const fetchUsers = async () => {
    try {
      const response = await axios.get('/api/users')
      setUsers(response.data)
    } catch (error) {
      setMessage('Error fetching users: ' + error.response?.data || error.message)
    }
  }

  const login = () => {
    window.location.href = 'http://localhost:8080/oauth2/authorization/google'
  }

  const logout = () => {
    setUser(null)
    window.location.href = 'http://localhost:8080/logout'
  }

  const createUser = async () => {
    try {
      await axios.post('/api/users', newUser)
      setNewUser({ email: '', name: '', role: 'USER' })
      fetchUsers()
      setMessage('User created successfully')
    } catch (error) {
      setMessage('Error creating user: ' + error.response?.data || error.message)
    }
  }

  return (
    <div className="App">
      <h1>SecureApp</h1>
      {!user ? (
        <button onClick={login}>Login with Google</button>
      ) : (
        <div>
          <p>{user}</p>
          <button onClick={logout}>Logout</button>
          <button onClick={fetchUsers}>Fetch Users (Admin)</button>
          <h2>Create User (Admin Only)</h2>
          <input
            type="email"
            placeholder="Email"
            value={newUser.email}
            onChange={(e) => setNewUser({ ...newUser, email: e.target.value })}
          />
          <input
            type="text"
            placeholder="Name"
            value={newUser.name}
            onChange={(e) => setNewUser({ ...newUser, name: e.target.value })}
          />
          <select
            value={newUser.role}
            onChange={(e) => setNewUser({ ...newUser, role: e.target.value })}
          >
            <option value="USER">USER</option>
            <option value="ADMIN">ADMIN</option>
          </select>
          <button onClick={createUser}>Create User</button>
        </div>
      )}
      <h2>Users</h2>
      <ul>
        {users.map(u => (
          <li key={u.id}>{u.name} ({u.email}) - {u.role}</li>
        ))}
      </ul>
      <p>{message}</p>
    </div>
  )
}

export default App
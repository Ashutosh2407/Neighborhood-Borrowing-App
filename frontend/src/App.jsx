import react from 'react'
import { BrowserRouter,Routes, Route, Navigate } from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import NotFound from './pages/NotFound'
import Register from './pages/Register'
import ProtectedRoutes from './components/ProtectedRoutes'
import './index.css'

function Logout(){
  localStorage.clear()
  return <Navigate to= "/login" />
}

function RegisterandLogout(){
  localStorage.clear()
  return <Register />
}

function App() {
  

  return (
    
      <BrowserRouter>
        <Routes>
          <Route 
            path = "/"
            element = {
              <ProtectedRoutes>
                <Home/>
              </ProtectedRoutes>
            }
          />
          <Route path = "/login" element = {<Login/>} />
          <Route path = "/register" element = {<Register/>} />
          <Route path = "*" element = {<NotFound/>} />
        </Routes>
      </BrowserRouter>
  )
}

export default App

import React from "react"
import api from "../api"
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants"
import { useNavigate } from "react-router-dom"
import { useState } from "react"




function Form({method, route}){

    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    
    const navigate = useNavigate() 
    const name = "login" === method ? "Login":"Register"

    const handleSubmit = async (e)=>{
        e.preventDefault();
        try{
            const res = await api.post(route, {username,password})
            if (method === "login"){
                localStorage.setItem(ACCESS_TOKEN, res.data.access)
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh)
                navigate("/")
            }
            else{
                navigate("/login")
            }

        }
        catch(error){
            alert(error)
        }
    }

    return (
        <div>
                <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <img className="mx-auto h-10 w-auto" src="image" alt="Borrowing App" />
        <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">{name}</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form class="space-y-6" onSubmit={handleSubmit} method="POST">
        <div>
            <label for="username" class="block text-sm/6 font-medium text-gray-900">Username</label>
            <div class="mt-2">
            <input type="text" name="username" id="text"  required 
            class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" 
            onChange={(e)=>setUsername(e.target.value)}
            value = {username}/>
            </div>
        </div>

        <div>
            <div class="flex items-center justify-between">
            <label for="password" class="block text-sm/6 font-medium text-gray-900">Password</label>
            {name === "Login" && <div class="text-sm">
                <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">
                    Forgot password?
                </a>
            </div>}
            
            </div>
            <div class="mt-2">
            <input type="password" name="password" id="password" 
            required class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" 
            onChange={(e)=>setPassword(e.target.value)}
            value = {password}/>
            </div>
        </div>

        <div>
            <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">{name}</button>
        </div>
        </form>
        {name === "Login" && <p class="mt-10 text-center text-sm/6 text-gray-500">
        Not a member?
        <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500"> Create an Account.</a>
        </p>}
        
    </div>
    </div>
        </div>
    )
}

export default Form
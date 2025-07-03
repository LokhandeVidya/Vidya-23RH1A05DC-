import { useState } from "react";
function Contact(){
    let [name, setName]=useState('');
    let [age, setAge]=useState(0);
    const handledata=()=>{
        console.log(name);
        console.log(age);
    }
    return(<div>
        <h1>Contact Page</h1>
        <input type="text" value={name} onChange={(e)=>setName(e.target.value)} placeholder="Enter name"></input>
        <input type="number" value={age} onChange={(e)=>setAge(e.target.value)} placeholder="Enter age"></input>
        <button onClick={handledata}>Add user</button>
        </div>);
}
export default Contact;
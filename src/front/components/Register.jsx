import { useState } from "react";

export const Register = () => {

    const [formData,setFormData] = useState({
        email:"",
        password:""
    });

    const handleChange = e => {
        setFormData({
            ...formData,
            [e.target.name]:e.target.value
        })
    }

    const handleSubmit = e => {
        e.preventDefault();
        console.log(formData)
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input placeholder="email" type="email" value={formData.email} name="email" onChange={handleChange} />
                <input placeholder="password" type="password" value={formData.password} name="password" onChange={handleChange}/>
                <input type="submit" />
            </form>
        </div>
    )
}
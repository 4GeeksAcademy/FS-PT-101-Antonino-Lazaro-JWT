const url = import.meta.env.VITE_BACKEND_URL

const userServices = {};

userServices.register = async (formData) => {
    try {
        const resp = await fetch(url + '/api/register',{
            headers:{
                'Content-Type' : 'application/json'
            },
            method: "POST",
            body: JSON.stringify(formData)
        })
        if (!resp.ok) throw Error("Something went wrong")
        const data = await resp.json()
    } catch (error) {
        
    }
}

export default userServices
const form= document.getElementById("register_form");

form.addEventListener("submit", async(e)=>{
    e.preventDefault();

    const password= document.getElementById("password").value;
    const check_password= document.getElementById("check_password").value;

    if(password!= check_password){
        alert("Passwords do not match");
        return
    }
    const form_data= new FormData(form);
    data= Object.fromEntries(form_data.entries());

    const response = await fetch("http://127.0.0.1:8000/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: data.email,
            password: data.password
        })
    });

    if(response.ok){
        alert("success")
    }
    else{
        alert("nds")
    }
});
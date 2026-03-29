const form= document.getElementById("register_form");

form.addEventListener("submit", async(e)=>{
    e.preventDefault();

    const password= document.getElementById("password").value;
    const check_password= document.getElementById("check_password").value;

    if(password.length < 8) {
        alert("Password length must be at least 8 character");
        return
    }

    if(password!= check_password){
        alert("Passwords do not match");
        return
    }
    const form_data= new FormData(form);
    const data= Object.fromEntries(form_data.entries());

    const response = await fetch("/register", {
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
        alert("Registration succesful")
        window.location.href="/login";
    }
    else{
        const res= await response.json();
        alert(res.detail);
    }
    
});

const login_form = document.getElementById("loginForm");

login_form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(login_form);
    const form_data = Object.fromEntries(formData.entries());

    

    const res = await fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
            
        },
        body: JSON.stringify(form_data)
    });

    if (res.ok) {
        const data = await res.json(); 
        console.log("Token received:", data.access_token);
        localStorage.setItem("token", data.access_token); 
    
        alert("Success!");
        window.location.href = "/resources";
    } else {
        const errorDetail = await res.json();
        console.error(errorDetail);
        alert("Wrong credentials");
    }
});
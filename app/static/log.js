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
        alert("Success!");
    } else {
        const errorDetail = await res.json();
        console.error(errorDetail);
        alert("Wrong credentials");
    }
});
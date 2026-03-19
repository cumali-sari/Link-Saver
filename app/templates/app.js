const addBtn = document.getElementById("Add");
const form = document.getElementById("resourceForm");

addBtn.addEventListener("click", () => {
    const inputs = document.getElementById("inputs");
    const div= document.createElement("div");

    const nameInput = document.createElement("input");
    nameInput.type= "text";
    nameInput.name= "title";

    const tagsInput = document.createElement("input");
    tagsInput.type= "text";
    tagsInput.name= "tags";

    const urlInput = document.createElement("input");
    urlInput.type= "text";
    urlInput.name= "url";

    const desInput = document.createElement("input");
    desInput.type= "text";
    desInput.name= "description";

    div.appendChild(nameInput);
    div.appendChild(urlInput);
    div.appendChild(tagsInput);
    div.appendChild(desInput);
    inputs.appendChild(div);
});

form.addEventListener("submit", async (e)=> {
    e.preventDefault();

    const formData= new FormData(form);
    const data= Object.fromEntries(formData.entries());

    const response= await fetch("http://127.0.0.1:8000/resources", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    if(response.ok){
        form.reset();
        alert("Links saved successfully");
    }
    else{
        console.error("Error: ", await response.text())
    }
});

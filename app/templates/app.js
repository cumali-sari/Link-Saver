const addBtn = document.getElementById("Add")

addBtn.addEventListener("click", () => {
    const inputs = document.getElementById("inputs");
    const div= document.createElement("div");

    const nameInput = document.createElement("input");
    nameInput.type= "text";
    nameInput.name= "Name";

    const tagsInput = document.createElement("input");
    tagsInput.type= "text";
    tagsInput.name= "Tags";

    const urlInput = document.createElement("input");
    urlInput.type= "text";
    urlInput.name= "Url";

    const desInput = document.createElement("input");
    desInput.type= "text";
    desInput.name= "Description";

    div.appendChild(nameInput);
    div.appendChild(urlInput);
    div.appendChild(tagsInput);
    div.appendChild(desInput);
    inputs.appendChild(div);
});

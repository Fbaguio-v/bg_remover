document.addEventListener("DOMContentLoaded", () => {
    const image = document.getElementById("image");
    image.addEventListener("change", (e) => {
        const file_name = e.target.files[0] ? e.target.files[0].name : 'No files selected';
        document.getElementById("text-output").textContent = file_name;
    });
});
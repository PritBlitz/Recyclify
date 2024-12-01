function showFileName(input) {
  const fileName = input.files[0]?.name || "No file selected";
  document.getElementById("file-name").textContent = fileName;
}

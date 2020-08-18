// Add star rating
const rating = document.querySelector('form[name=rating]');

rating.addEventListener("change", function (e) {
    // Getting data from the form
    let data = new FormData(this);
    fetch(`${this.action}`, {
        method: 'POST',
        body: data
    })
        .then(response => alert("Rating set"))
        .catch(error => alert("Error"))
});
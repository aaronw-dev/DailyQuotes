window.addEventListener("load", (event) => {
    fetch('https://daily-quotes.aw-dev.repl.co/postreq', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    /*body: JSON.stringify(
    { 
        "username": localStorage.getItem("username")
    })*/
  })
  .then(
    response => response.json()
  )
  .then((response) => {
    var quoteblock = document.getElementById("quote")
    quoteblock.innerHTML = response.q
    document.getElementById("author").innerHTML = response.a
    console.log("Response: " + response)
  })
})
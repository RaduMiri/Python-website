//It was done like this to not use Ajax
function deleteNote(noteId) {
    // Send a POST request with the noteID to delete-note endpoint
    fetch('/delete-note',{ //The argument is the endpoint
        method: 'POST', //This is the request type
        body: JSON.stringify({ noteId: noteId}), //This is what it sends, a JSON with noteId
    }).then((_res) => { //And after it gets a response from the endpoint it reloads the window
        window.location.href = "/"; //This is how to reload a window with a GET request, it just says rediredct to home page which will reload the home page
    });
}
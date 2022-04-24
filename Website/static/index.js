function deleteNote(noteId){


//takes the noteId and sends to the delete_note endpoint

    fetch('/delete-note", {

    method="POST",
    body: JSON.stringify({noteId : noteId}),

    }).then((_res) => {
   //reloads the window
        window.location.href = "/";
    });


}
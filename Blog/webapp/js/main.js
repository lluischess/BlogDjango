
function login(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value

    if (username == '' && password == '') {
        alert("You need to insert username and password")
    }

    var data ={
        'username' : username,
        'password' : password
    }

    fetch('/api/login/' ,{
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CRSFToken' : csrf,
        },
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        console.log(response)
    })
 }
var provider = new firebase.auth.GoogleAuthProvider();

var config = 
{
    apiKey: "",
    authDomain: "class-demo-y102020-21.firebaseapp.com",
    databaseURL: "https://class-demo-y102020-21-default-rtdb.firebaseio.com",
    projectId: "class-demo-y102020-21",
    storageBucket: "class-demo-y102020-21.appspot.com",
    messagingSenderId: "976136429898",
    appId: "1:976136429898:web:02cfe54aeca037775b61b3",
    measurementId: "G-QQ5QJEXFNN"
};

firebase.initializeApp(config);


function googleSignin() 
{
    firebase.auth()
    .signInWithPopup(provider)
    .then(function(result) 
    {
        var name = result.user.displayName;
        var email = result.user.email;

        console.log(name);
        console.log(email);

    })
    .catch(function(error) 
    {
        var errorCode = error.code;
        var errorMessage = error.message;
            
        console.log(error.code)
        console.log(error.message)
    });
}

function googleSignout() 
{
    firebase.auth().signOut()
    .then(function() 
    {
        console.log('Signout Succesfull');
        hideInformation();
    }, function(error) 
    {
        console.log('Signout Failed');
    });
}      


function showRoomData(room){
    
}


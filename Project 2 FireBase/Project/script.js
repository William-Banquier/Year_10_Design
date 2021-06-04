var roomID = "WORKS AGAIN"
var items = []

var provider = new firebase.auth.GoogleAuthProvider();

var config = 
{
    apiKey: "AIzaSyAKW3G4dMbBiqXTXLoJDV4Xg_Y9lR_7Ku0",
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
        var token = result.credential.accessToken;
        var user = result.user; 
        var name = result.user.displayName;
        var email = result.user.email;
        var emailVerified = user.emailVerified;

        document.getElementById("buttonForSignIn").onclick = googleSignout;
        document.getElementById("buttonForSignIn").innerHTML = "Sign Out";
        
        console.log(emailVerified);
        console.log(result.user.photoURL);
        console.log(token);
        console.log(user);
        console.log(name);
        console.log(email);
    })
    .catch(function(error) 
    {
        var errorCode = error.code;
        var errorMessage = error.message;
            
        console.log(errorCode)
        console.log(errorMessage)
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
        console.log(error);
    });
}      

function openSignInSection(){
    return
}

function googleSignout(){
    firebase.auth().signOut()
    .then(function() 
    {
        console.log('Signout Succesfull');
        document.getElementById("buttonForSignIn").onclick = googleSignin;
        document.getElementById("buttonForSignIn").innerHTML = "Sign In With Google";
    }, function(error) 
    {
        console.log('Signout Failed');
    });
}

function sendMessage(roomID){
    if (roomID == null){
        return 
    }
    endDate = new Date
    endDate.setDate(endDate.getDate() + 1)

    var message = document.getElementById("messagePage_Input-Input").value;
    if (message.replace(/ /g,'') == ""){
        return
    }
    document.getElementById("messagePage_Input-Input").value = "";
    var user = firebase.auth().currentUser;
    if (user == null){
        var user = "ANON"
        console.log(user)
    }else{
        var user = user.displayName;
        console.log(user)
    }
    
    console.log(message +"  "+ user);




    var database = firebase.database();
    var ref = database.ref('roomIDs');

    var newPostKey = firebase.database().ref('roomIDs').push().key;

    // data = {}
    // data[newPostKey] = {
    //     poster: user,
    //      message: message,
    // }
    // console.log(data)

    data = {
        poster: user,
        message: message,
    }
    
        
        

    ref.child(roomID+"/"+newPostKey).set(data);
    x = new Date
    console.log("Pushed - Data:" + data + x);

    addMessages(user, message)
}


function downloadPosts(roomID){

    var database = firebase.database();
    var ref = database.ref('roomIDs/'+roomID);
    ref.once('value', readAndShowMessages);
}

function readAndShowMessages(data){

    
    data = (data.val());
    if (data == null){
        return;
    }

    keyValues = Object.keys(data);

    n = Math.min(keyValues.length, 10);
    if (keyValues.length > items.length){
        var newKeyValues = new Array
        console.log(keyValues)
        console.log(items)
        keyValues = keyValues.reverse()
        for(var i = 0; i < keyValues.length - items.length; i++){
            newKeyValues.push(keyValues[i])
        }
        n = Math.min(newKeyValues.length, 10);
        newKeyValues = newKeyValues.slice(0,n).reverse()
        console.log("NEW KEY VALUES")
        console.log(newKeyValues)
        
        
        for (var i = 0; i < n; i ++){
            c = data[newKeyValues[i]]
            let poster = (c.poster)
            let message = (c.message)
            addMessages(poster, message);
        }
        return

    }
    for (var i = 0; i < n; i++){
        c = data[keyValues[i]]
        let poster = (c.poster)
        let message = (c.message)
        addMessages(poster, message);
    }
}

function addMessages(poster, message){
    console.log(poster, message)

    var divider = document.createElement("div");
    divider.className = "divider";

    var section = document.createElement("div");
    section.className = "section";

    
    var h6 = document.createElement("H6");
    var h6Text = document.createTextNode(message); 

    var Ltext = document.createElement("label");
    var text = document.createTextNode(poster);

    Ltext.appendChild(text);


    
    h6.appendChild(h6Text);

    section.appendChild(h6);
    section.appendChild(Ltext);


    var element = document.getElementById("text_area");
    element.insertBefore(divider, element.childNodes[0]);
    element.insertBefore(section, element.childNodes[0]);

    items.push([poster, message]);
}


function joinRoom(room_id){
    console.log(room_id)
    document.getElementById("text_area").innerHTML = "";
    document.getElementById("messagePage").style.display = "inline";
    document.getElementById("joinRoom_Form").style.display = "none";
    downloadPosts(room_id);
    return room_id
}

// function loadNewMessages()
// {

    
// }

// (function loadNewMessages (){
//     downloadPosts(roomID);

//     setTimeout(arguments.callee, 10000);
// })();


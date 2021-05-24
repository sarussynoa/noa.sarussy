console.log(`Js loaded`)

function toggleModal(e) {
  e.preventDefault()
  let popup = document.getElementById('popup');
  if (popup) {
    popup.classList.toggle('show')
  }
}

function getUsers(eId) {
    var obj, dbParam, xmlhttp, myObj, x, txt = "";
    obj = { table: "users", limit: 200 };
    dbParam = JSON.stringify(obj);
    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        myObj = JSON.parse(this.responseText);
        txt += "<table border='1'>"
        for (x in myObj.data) {
          txt += "<tr><td>" + myObj.data[x].id + "</td><td>" + myObj.data[x].email + "</td><td>"
          + myObj.data[x].first_name + "</td><td>" + myObj.data[x].last_name + '</td><td><img src="'
          + myObj.data[x].avatar + '" width="512" height="512"></td></tr>';
        }
        txt += "</table>"
        document.getElementById(eId).innerHTML = txt;
      }
    };
    xmlhttp.open("GET", "https://reqres.in/api/users?page=2", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send("x=" + dbParam);

}

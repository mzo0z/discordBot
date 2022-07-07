import os
import assist

privateFiles  = assist.web
transcripts   = privateFiles + 'transcripts'
jsonFile      = privateFiles + 'data.json'
tickjson      = assist.privateFiles + 'system/ticket.json'


dashboard     = privateFiles + 'dashboard.html'
index         = privateFiles + 'index.html'
bot           = privateFiles + 'bot.html'
server        = privateFiles + 'server.html'
islam         = privateFiles + 'islam.html'

#ticket#
ticketManagment  = privateFiles + 'ticketManagment.html'
#
ticket           = privateFiles + 'ticket.html'
transcript       = privateFiles + 'transcript.html'
setCategory      = privateFiles + 'setCategory.html'
moveTicket       = privateFiles + 'moveTicket.html'
########


##system ##
systemManagment = privateFiles + 'systemManagment.html'
cmdsManagment   = privateFiles + 'cmdsManagment.html'
wlcbyeManagment = privateFiles + 'wlcbyeManagment.html'
addAntiWord     = privateFiles + 'addAntiWord.html'
robotManagment  = privateFiles + 'robotManagment.html'
addAutoResponse = privateFiles + 'addAutoResponse.html'
setSuggstions   = privateFiles + 'setSuggstions.html'
setLine         = privateFiles + 'setLine.html'

#games#
gamesManagment = privateFiles + 'gamesManagment.html'
#
setGamesCategory = privateFiles + 'setGamesCategory.html'
setGamesChannel = privateFiles + 'setGamesChannel.html'
########

## server status ##
serverStatusManagement = privateFiles + 'serverStatusManagement.html'


##security##
securityManagment = privateFiles + 'securityManagment.html'


tickethtml = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
	<meta charset="utf-8">
	<title> mzooz bot </title>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>
</head>

<body>      
      <hr/>
      <h2>اختر التيكت المراد حذفه</h2>
      <div class="picker">
        <hr/>
          <div class="custom-select" style="width:100%;text-align: center;">
            <select>
              <section class="cards">
                <option value="اختر التيكت المراد حذفه">اختر التيكت المراد حذفه</option>
                {% for ticket in tickets %}
                <option value={{ticket}}>{{ticket[:ticket.find("_")].replace("[SPACE]", ' ')}}</option>
                {% endfor %}
              </section>
            </select>
          </div>
          <button class="button" id="save" onclick="save()">حذف</button>
          <a href="/ticketsManagment" class="button" id="back" >العودة</a>

      </div>
    </body>


<script>


var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }

        h.click();

    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);

function save(){
  var selectedOption = document.querySelector('select').value;
  location.replace("/delete/"+selectedOption);
  };
</script>

<style>



.custom-select {
  position: relative;
  font-family: Arial;
}

.custom-select select {
  display: none; /*hide original SELECT element: */
}

.select-selected {
  background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
  position: absolute;
  content: "";
  top: 14px;
  right: 10px;
  width: 0;
  height: 0;
  border: 6px solid transparent;
  border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
  border-color: transparent transparent #fff transparent;
  top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
  color: #ffffff;
  padding: 8px 16px;
  border: 1px solid transparent;
  border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
  cursor: pointer;
}

/* Style items (options): */
.select-items {
  position: absolute;
  background-color: #3c5be3;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
  display: none;
}

.select-items div:hover, .same-as-selected {
  background-color: rgba(0, 0, 0, 0.1);
}


input {
  opacity:0;
  position:absolute;
  left:-99999px;
}
 
input:checked + label {
  order: 1;
  z-index:2;
  background: #5c59ff;
  border-top:none;
  position:relative;
  color: white;
}
 
input:checked + label:after {
  content:'';
  width: 0; 
 height: 0; 
 border-left: 5px solid transparent;
 border-right: 5px solid transparent;
 border-top: 5px solid white;
  position:absolute;
  right:10px;
  top:calc(50% - 2.5px);
  pointer-events:none;
  z-index:3;
}
 
input:checked + label:before {
  position:absolute;
  right:0;
  height: 40px;
  width: 40px;
  content: '';
  background: #050505;
}
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  justify-items: center;
}

.card {
  margin: 0.5em;
  display: grid;
  grid-template-rows: 1fr 0.2fr;
  justify-items: center;
}

.card:hover {
  box-shadow: rgba(2, 8, 20, 0.1) 0px 0.35em 1.175em,
    rgba(2, 8, 20, 0.08) 0px 0.175em 0.5em;
  transform: scale(1.1);
}

.card img {
  border-radius: 50%;
  width: 7em;
  height: 7em;
}

h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}



@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}

.button{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}


  .button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button[id="save"]{
  background-color: #4caf4f00;
      display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3ce344;
    border-radius: 10px;
}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}




@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>

"""

serverStatusManagementHtml = """

<!DOCTYPE html>
<html>
  <head>
    <title>mzooz bot</title>
  </head>
  <body>
    <div class="picker">
      <h1>mzooz bot</h1>
      <h2>ادارة نظام بيانات السيرفر</h2>
      <hr/>
        {% if active %}
        <a href="/activeServerStatus/off" class="button" id="back">الغاء التفعيل</a>
        <label class="switch" for="active" ><h3>نظام بيانات السيرفر</h3></label>
        <hr/>
        <h3>عدد الاعضاء فقط</h3>
        <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر القناة">اختر القناة</option>
              {% for channel in channels %}
              <option value={{channel}}>{{channel}}</option>
              {% endfor %}
            </section>
          </select>
        </div>
        <hr/>
        <h3>عدد البوتات فقط</h3>
        <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر القناة">اختر القناة</option>
              {% for channel in channels %}
              <option value={{channel}}>{{channel}}</option>
              {% endfor %}
            </section>
          </select>
        </div>
        <hr/>
        <h3>عدد الاعضاء الكلي</h3>
        <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر القناة">اختر القناة</option>
              {% for channel in channels %}
              <option value={{channel}}>{{channel}}</option>
              {% endfor %}
            </section>
          </select>
        </div>

        {% else %}
        <a href="/activeServerStatus/on" class="button" id="active">تفعيل</a>
        <label class="switch" for="active" ><h3>نظام بيانات السيرفر</h3></label>
        {% endif %}
        <hr/>
      </div>
      <button class="button" id="save" onclick="save()">حفظ</button>
      <button class="button" id="back" onclick="back()">رجوع</button>
  </body>
  
  
  <script>
var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }

        h.click();

    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);

function save(){
  if ("{{active}}" == "True"){
    location.replace("/setServerStatus/" + document.getElementsByClassName("select-selected")[0].innerHTML + "/" + document.getElementsByClassName("select-selected")[1].innerHTML + '/' + document.getElementsByClassName("select-selected")[2].innerHTML);
  }else if ("{{active}}" == "False"){
    location.replace("/setServerStatus/0/0/0");
  }
}

function back(){
    location.replace("/server")
}

</script>


<style>

.custom-select {
position: relative;
font-family: Arial;
}

.custom-select select {
display: none; /*hide original SELECT element: */
}

.select-selected {
background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
position: absolute;
content: "";
top: 14px;
right: 10px;
width: 0;
height: 0;
border: 6px solid transparent;
border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
border-color: transparent transparent #fff transparent;
top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
color: #ffffff;
padding: 8px 16px;
border: 1px solid transparent;
border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
cursor: pointer;
}

/* Style items (options): */
.select-items {
position: absolute;
background-color: #3c5be3;
top: 100%;
left: 0;
right: 0;
z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
display: none;
}

.select-items div:hover, .same-as-selected {
background-color: rgba(0, 0, 0, 0.1);
}



input:checked + label {
order: 1;
z-index:2;
background: #5c59ff;
border-top:none;
position:relative;
color: white;
}

input:checked + label:after {
content:'';
width: 0; 
height: 0; 
border-left: 5px solid transparent;
border-right: 5px solid transparent;
border-top: 5px solid white;
position:absolute;
right:10px;
top:calc(50% - 2.5px);
pointer-events:none;
z-index:3;
}

input:checked + label:before {
position:absolute;
right:0;
height: 40px;
width: 40px;
content: '';
background: #050505;
}


/* The switch - the box around the slider */
.switch {
position: relative;
display: inline-block;
width: 60px;
height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
opacity: 0;
width: 0;
height: 0;
}

/* The slider */
.slider {
position: absolute;
cursor: pointer;
top: 0;
left: 0;
right: 0;
bottom: 0;
background-color: #f32133;
-webkit-transition: .4s;
transition: .4s;
}

.slider:before {
position: absolute;
content: "";
height: 26px;
width: 26px;
left: 4px;
bottom: 4px;
background-color: white;
-webkit-transition: .4s;
transition: .4s;
}

input:checked + .slider {
background-color: #21f34f;
}

input:focus + .slider {
box-shadow: 0 0 1px #21f321;
}

input:checked + .slider:before {
-webkit-transform: translateX(26px);
-ms-transform: translateX(26px);
transform: translateX(26px);
}

.switch h3{
color: #00c292;

}

h3{
color: #00c292;

}

h3[id="untrust"]{
color: #c24e00;

}

h3[id="trust"]{
color: #473ce3;

}


.button{
background-color: #c22d0000;
}

/* Rounded sliders */
.slider.round {
border-radius: 34px;
}

.slider.round:before {
border-radius: 50%;
}

h1{
text-align: center;
color:#3c67e3;
}
h2 {
text-align: center;
color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
margin: 0;
padding: 0;
box-sizing: border-box;
}
body{
font-family: 'Poppins', sans-serif;
background-color: #212534;
display: grid;
place-content: center;
height: 100vh;
}
.button{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#3c67e3;
border-radius: 10px;
}

.picker h3 {
text-align: center;
padding-top: 2%;
font-family: Georgia, "Times New Roman", Times, serif;
font-size: 1.5em;
}

.button[id="untrust"]{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#e3e03c;
border-radius: 10px;

}

.button[id="active"]{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#3ce33c;
border-radius: 10px;
background-color: #4caf4f00;
}

.button[id="deActive"]{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#e33c3c;
border-radius: 10px;
background-color: #4caf4f00;
}

.button:hover{
animation: pulsate 1s 
ease-in-out;
}

@keyframes pulsate {
0%{
    box-shadow: 
    0 0 25px #5ddcff,
    0 0 50px #4e00c2;
}
}


.picker input[type="text"]{
	border: 0;
	background: none;
	display: block;
	margin: 20px auto;
	text-align: center;
	border: 2px solid #3498bd;
	padding: 14px 10px;
	width: 200px;
	outline: none;
	color: white;
	border-radius: 24px;
	transform: 0.25s;

}
.picker input[type="text"]:focus{
	width: 220px;
	border-color: #2ecc71;
}



h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}
.button{
  background-color: #21253400;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}

.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}


.button[id="welcomming"]{
  background-color: #21253400;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 33px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;

}


.button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 45px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button[id="save"]{
  display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 45px;
    border: 3px solid 
    #3ce33c;
    border-radius: 10px;

}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}

@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>

"""


islamHtml = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
	<meta charset="utf-8">
	<title> mzooz bot </title>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>
</head>

<body>      
      <hr/>
      <h2>اختر قناة الاجر</h2>
      <div class="picker">
        <hr/>
          <div class="custom-select" style="width:100%;text-align: center;">
            <select>
              <section class="cards">
                <option value="اختر القناة">اختر القناة</option>
                <option value="عدم تعيين">عدم تعيين</option>
                {% for channel in channels %}
                <option value={{channel}}>{{channel}}</option>
                {% endfor %}
              </section>
            </select>
          </div>
          <button class="button" id="save" onclick="save()">حفظ</button>
          <a href="/server" class="button" id="back" >العودة</a>

      </div>
    </body>


<script>


var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }

        h.click();

    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);

function save(){
  location.replace("/islam/"+ document.getElementsByTagName("select")[0].value);
  };
</script>

<style>



.custom-select {
  position: relative;
  font-family: Arial;
}

.custom-select select {
  display: none; /*hide original SELECT element: */
}

.select-selected {
  background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
  position: absolute;
  content: "";
  top: 14px;
  right: 10px;
  width: 0;
  height: 0;
  border: 6px solid transparent;
  border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
  border-color: transparent transparent #fff transparent;
  top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
  color: #ffffff;
  padding: 8px 16px;
  border: 1px solid transparent;
  border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
  cursor: pointer;
}

/* Style items (options): */
.select-items {
  position: absolute;
  background-color: #3c5be3;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
  display: none;
}

.select-items div:hover, .same-as-selected {
  background-color: rgba(0, 0, 0, 0.1);
}


input {
  opacity:0;
  position:absolute;
  left:-99999px;
}
 
input:checked + label {
  order: 1;
  z-index:2;
  background: #5c59ff;
  border-top:none;
  position:relative;
  color: white;
}
 
input:checked + label:after {
  content:'';
  width: 0; 
 height: 0; 
 border-left: 5px solid transparent;
 border-right: 5px solid transparent;
 border-top: 5px solid white;
  position:absolute;
  right:10px;
  top:calc(50% - 2.5px);
  pointer-events:none;
  z-index:3;
}
 
input:checked + label:before {
  position:absolute;
  right:0;
  height: 40px;
  width: 40px;
  content: '';
  background: #050505;
}
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  justify-items: center;
}

.card {
  margin: 0.5em;
  display: grid;
  grid-template-rows: 1fr 0.2fr;
  justify-items: center;
}

.card:hover {
  box-shadow: rgba(2, 8, 20, 0.1) 0px 0.35em 1.175em,
    rgba(2, 8, 20, 0.08) 0px 0.175em 0.5em;
  transform: scale(1.1);
}

.card img {
  border-radius: 50%;
  width: 7em;
  height: 7em;
}

h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}



@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}

.button{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}


  .button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button[id="save"]{
  background-color: #4caf4f00;
      display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3ce344;
    border-radius: 10px;
}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}




@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>
"""

botHtml ='''

<!DOCTYPE html>
<html>
  <head>
    <title>mzooz bot</title>
  </head>
  <body>
      <h1>mzooz bot</h1>
      <h2>اعدادات البوت</h2>
      <form class="picker" method="POST">
        {% if not CMD %}
        <hr/>
        <h3>اختر الشيء المراد تعديله</h3>
        <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر">اختر</option>
              {% for cmd in cmds %}
              <option value={{cmd}}>{{cmd}}</option>
              {% endfor %}
            </section>
          </select>
        </div>
        {%else%}
        <hr/>
        <input type="text" id="url" name="url" placeholder="{{msg}}">
        <input type="submit" class="button" id="sub" value="تعديل">
        {%endif%}
      </form>
      {% if not CMD %}
      <button class="button" id="sub" onclick="save()">تعديل</button>
      <button class="button" id="back" onclick="back()">رجوع</button>
      {%else%}
      <a href="/bot/0" class="button" id="back">رجوع</a>
      {%endif%}
  </body>
  
  
  <script>
var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }

        h.click();

    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);

function save(){
  if ("{{CMD}}" == "False"){
    if (document.getElementsByClassName("select-selected")[0].innerHTML != 'اختر الامر') {
      location.replace("/bot/" + document.getElementsByClassName("select-selected")[0].innerHTML )}
}else if ("{{CMD}}" == "True"){
  if (document.getElementsByClassName("select-selected")[0].innerHTML != 'اختر الامر') {
      location.replace("/bot/" + document.getElementsByClassName("select-selected")[0].innerHTML)}
}
}

function back(){
    location.replace("/server");
}


</script>


<style>



textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */ 
  border: 1px solid rgb(190, 190, 190); /* Gray border */
  border-radius: 2px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 0px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
}

.custom-select {
position: relative;
font-family: Arial;
}

.custom-select select {
display: none; /*hide original SELECT element: */
}

.select-selected {
background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
position: absolute;
content: "";
top: 14px;
right: 10px;
width: 0;
height: 0;
border: 6px solid transparent;
border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
border-color: transparent transparent #fff transparent;
top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
color: #ffffff;
padding: 8px 16px;
border: 1px solid transparent;
border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
cursor: pointer;
}

/* Style items (options): */
.select-items {
position: absolute;
background-color: #3c5be3;
top: 100%;
left: 0;
right: 0;
z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
display: none;
}

.select-items div:hover, .same-as-selected {
background-color: rgba(0, 0, 0, 0.1);
}



input:checked + label {
order: 1;
z-index:2;
background: #5c59ff;
border-top:none;
position:relative;
color: white;
}

input:checked + label:after {
content:'';
width: 0; 
height: 0; 
border-left: 5px solid transparent;
border-right: 5px solid transparent;
border-top: 5px solid white;
position:absolute;
right:10px;
top:calc(50% - 2.5px);
pointer-events:none;
z-index:3;
}

input:checked + label:before {
position:absolute;
right:0;
height: 40px;
width: 40px;
content: '';
background: #050505;
}


/* The switch - the box around the slider */
.switch {
position: relative;
display: inline-block;
width: 60px;
height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
opacity: 0;
width: 0;
height: 0;
}

/* The slider */
.slider {
position: absolute;
cursor: pointer;
top: 0;
left: 0;
right: 0;
bottom: 0;
background-color: #f32133;
-webkit-transition: .4s;
transition: .4s;
}

.slider:before {
position: absolute;
content: "";
height: 26px;
width: 26px;
left: 4px;
bottom: 4px;
background-color: white;
-webkit-transition: .4s;
transition: .4s;
}

input:checked + .slider {
background-color: #21f34f;
}

input:focus + .slider {
box-shadow: 0 0 1px #21f321;
}

input:checked + .slider:before {
-webkit-transform: translateX(26px);
-ms-transform: translateX(26px);
transform: translateX(26px);
}

.switch h3{
color: #00c292;

}

h3{
color: #00c292;

}

h4{
color: #3c98e3;
text-align: center;

}

h4[id="warnning"]{
  color: #e33c3c;
text-align: center;
}



.button{
  text-align: center;
background-color: #c22d0000;
}

/* Rounded sliders */
.slider.round {
border-radius: 34px;
}

.slider.round:before {
border-radius: 50%;
}

h1{
text-align: center;
color:#3c67e3;
}
h2 {
text-align: center;
color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
margin: 0;
padding: 0;
box-sizing: border-box;
}
body{
font-family: 'Poppins', sans-serif;
background-color: #212534;
display: grid;
place-content: center;
height: 100vh;
}
.button{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 10px 10px;
border: 3px solid 
#3c67e3;
border-radius: 10px;
}

.picker h3 {
text-align: center;
padding-top: 2%;
font-family: Georgia, "Times New Roman", Times, serif;
font-size: 1.5em;
}

.button:hover{
animation: pulsate 1s 
ease-in-out;
}

@keyframes pulsate {
0%{
    box-shadow: 
    0 0 25px #5ddcff,
    0 0 50px #4e00c2;
}
}

.picker input[type="text"] {
	border: 0;
	background: none;
	border: 2px solid #3498bd;
  width: 100%; 
  padding: 12px; 
	text-align: center;
  border-radius: 2px; 
  box-sizing: border-box; 
  margin-top: 0px; 
  margin-bottom: 16px; 
	outline: none;
	color: white;
	transform: 0.25s;
}



h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}
.button{
  background-color: #21253400;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}

.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}



.button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    border: 3px solid 
    #e33c3c;
    border-radius: 0px;
}

.button[id="yellow"]{
display: inline-block;
color: #fff;
text-decoration: none;
border: 3px solid 
#3ce33c;
border-radius: 10px;

}

.sub {
  background-color: #04AA6D;
  color: white;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  opacity: 0.9;
}

.sub:hover {
  opacity:1;
}

.button[id="sub"]{
  width: 100%;
  display: inline-block;
  text-decoration: none;
  border: 3px solid 
  #683ce3;
  border-radius: 0px;
  color: #fff;

}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}

@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>
'''


securityManagmentHtml = """

<!DOCTYPE html>
<html>
  <head>
    <title>mzooz bot</title>
  </head>
  <body>
    <header>
      <hr/>
      <div class="switchs">
        {% if trust %}
        <button class="button" id="untrust" onclick="untrust()">إدارة الموثوقين</button>
        {% else %}
        <button class="button" id="trust" onclick="trust()">إدارة الموثوقين</button>
        {% endif %}
        {% if trusted %}
          <button class="button" id="active" onclick="activateActiveSystem()">مفعل</button>
          <label class="switch" for="active" ><h3>نظام التفعيل</h3></label>
          {% else %}
          <button class="button" id="deActive" onclick="deActivateActiveSystem()">غير مفعل</button>
          <label class="switch" for="active" ><h3>نظام التفعيل</h3></label>          
          {%endif %}
        {% if trust %}
        <hr/>
        <h3 id="trust" style="text-align: center;">الوثوق بعضو</h3>
        <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر العضو">اختر العضو</option>
              {% for member in members %}
              <option value={{member}}>{{member}}</option>
              {% endfor %}
            </section>
          </select>
        </div>
        <hr/>
        <h3 id="untrust" style="text-align: center;">عدم الوثوق بعضو</h3>
        <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر العضو">اختر العضو</option>
              {% for member in trustedMembers %}
              <option value={{member}}>{{member}}</option>
              {% endfor %}
            </section>
          </select>
        </div>
        {% endif %}
        {% if trusted %}
        <hr/>
        <h3 style="text-align: center;">اختر رتبة التفعيل</h3>
        <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر الرتبة">اختر الرتبة</option>
              {% for role in roles %}
              <option value={{role}}>{{role}}</option>
              {% endfor %}
            </section>
          </select>
        </div>
        {% endif %}
          <hr/>
          <h3 style="text-align: center;"> log اختر قناة الـ</h3>
          <hr/>
          <div class="custom-select" style="width:100%;text-align: center;">
            <select>
              <section class="cards">
                <option value="اختر القناة">اختر القناة</option>
                {% for channel in channels %}
                <option value={{channel}}>{{channel}}</option>
                {% endfor %}
              </section>
            </select>
          </div>
      </div>
      <hr/>
    </header>
    <h1>mzooz bot</h1>
    <div class="picker">
      <h2>ادارة الحماية</h2>
      <hr />
      <section class="cards">
        <div class="card">
          <button class="button" id="save" onclick="save()">حفظ التغييرات</button>
          <a href="/server" class="button" id="back">العودة</a>
          <br />
        </div>
      </section>
    </div>
  </body>
  <script>


    var x, i, j, l, ll, selElmnt, a, b, c;
    /* Look for any elements with the class "custom-select": */
    x = document.getElementsByClassName("custom-select");
    l = x.length;
    for (i = 0; i < l; i++) {
      selElmnt = x[i].getElementsByTagName("select")[0];
      ll = selElmnt.length;
      a = document.createElement("DIV");
      a.setAttribute("class", "select-selected");
      a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
      x[i].appendChild(a);
      b = document.createElement("DIV");
      b.setAttribute("class", "select-items select-hide");
      for (j = 1; j < ll; j++) {
        c = document.createElement("DIV");
        c.innerHTML = selElmnt.options[j].innerHTML;
        c.addEventListener("click", function(e) {
          var y, i, k, s, h, sl, yl;
          s = this.parentNode.parentNode.getElementsByTagName("select")[0];
          sl = s.length;
          h = this.parentNode.previousSibling;
          for (i = 0; i < sl; i++) {
            if (s.options[i].innerHTML == this.innerHTML) {
              s.selectedIndex = i;
              h.innerHTML = this.innerHTML;
                y = this.parentNode.getElementsByClassName("same-as-selected");
                yl = y.length;
                for (k = 0; k < yl; k++) {
                  y[k].removeAttribute("class");
                }
                this.setAttribute("class", "same-as-selected");
                break;
              }
            }
    
            h.click();
    
        });
        b.appendChild(c);
      }
      x[i].appendChild(b);
      a.addEventListener("click", function(e) {
        e.stopPropagation();
        closeAllSelect(this);
        this.nextSibling.classList.toggle("select-hide");
        this.classList.toggle("select-arrow-active");
      });
    }
    
    function closeAllSelect(elmnt) {
      var x, y, i, xl, yl, arrNo = [];
      x = document.getElementsByClassName("select-items");
      y = document.getElementsByClassName("select-selected");
      xl = x.length;
      yl = y.length;
      for (i = 0; i < yl; i++) {
        if (elmnt == y[i]) {
          arrNo.push(i)
        } else {
          y[i].classList.remove("select-arrow-active");
        }
      }
      for (i = 0; i < xl; i++) {
        if (arrNo.indexOf(i)) {
          x[i].classList.add("select-hide");
        }
      }
    }
    
    document.addEventListener("click", closeAllSelect);
    
    function deActivateActiveSystem(){
      location.replace("/securityManagment/activeRole/on/0/0/0");
      };

      function activateActiveSystem(){
      location.replace("/securityManagment/activeRole/off/0/0/0");
      };

      function trust(){
        location.replace("/securityManagment/trust/on/0/0/0");
      };

      function untrust(){
        location.replace("/securityManagment/trust/off/0/0/0");
      };
      function save(){

        if ("{{trusted}}" == "True" && "{{trust}}" == "True"){
          location.replace("/securityManagment/all/trustMember:"+document.getElementsByClassName("select-selected")[0].innerHTML + '/unTrustMember:' + document.getElementsByClassName("select-selected")[1].innerHTML + '/activeRole:' + document.getElementsByClassName("select-selected")[2].innerHTML + '/logChannel:' + document.getElementsByClassName("select-selected")[3].innerHTML);
        
        }else if ("{{trusted}}" == "False" && "{{trust}}" == "False"){
          location.replace("/securityManagment/logChannel/0/0/0/" + document.getElementsByClassName("select-selected")[0].innerHTML);

        }else if ("{{trusted}}" == "True" && "{{trust}}" == "False"){
          location.replace("/securityManagment/roleAndLog/0/activeRole:" + document.getElementsByClassName("select-selected")[0].innerHTML + "/logChannel:" + document.getElementsByClassName("select-selected")[1].innerHTML +"/0");
  
        }else if ("{{trusted}}" == "False" && "{{trust}}" == "True"){
          location.replace("/securityManagment/trustAndLog/0/trustedMember:" + document.getElementsByClassName("select-selected")[0].innerHTML + "/unTrustedMember:" + document.getElementsByClassName("select-selected")[1].innerHTML +"/logChannel:" + document.getElementsByClassName("select-selected")[2].innerHTML);
        }

      }
      
    </script>


<style>

.custom-select {
  position: relative;
  font-family: Arial;
}

.custom-select select {
  display: none; /*hide original SELECT element: */
}

.select-selected {
  background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
  position: absolute;
  content: "";
  top: 14px;
  right: 10px;
  width: 0;
  height: 0;
  border: 6px solid transparent;
  border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
  border-color: transparent transparent #fff transparent;
  top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
  color: #ffffff;
  padding: 8px 16px;
  border: 1px solid transparent;
  border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
  cursor: pointer;
}

/* Style items (options): */
.select-items {
  position: absolute;
  background-color: #3c5be3;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
  display: none;
}

.select-items div:hover, .same-as-selected {
  background-color: rgba(0, 0, 0, 0.1);
}


input {
  opacity:0;
  position:absolute;
  left:-99999px;
}
 
input:checked + label {
  order: 1;
  z-index:2;
  background: #5c59ff;
  border-top:none;
  position:relative;
  color: white;
}
 
input:checked + label:after {
  content:'';
  width: 0; 
 height: 0; 
 border-left: 5px solid transparent;
 border-right: 5px solid transparent;
 border-top: 5px solid white;
  position:absolute;
  right:10px;
  top:calc(50% - 2.5px);
  pointer-events:none;
  z-index:3;
}
 
input:checked + label:before {
  position:absolute;
  right:0;
  height: 40px;
  width: 40px;
  content: '';
  background: #050505;
}


/* The switch - the box around the slider */
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #f32133;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #21f34f;
}

input:focus + .slider {
  box-shadow: 0 0 1px #21f321;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

.switch h3{
  color: #00c292;

}

h3{
  color: #00c292;

}

h3[id="untrust"]{
  color: #c24e00;

}

h3[id="trust"]{
  color: #473ce3;

}


.button{
  background-color: #c22d0000;
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}

h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}
.button{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}

.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}

.button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button[id="untrust"]{
  display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #e3e03c;
    border-radius: 10px;

}

.button[id="active"]{
  display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3ce33c;
    border-radius: 10px;
  background-color: #4caf4f00;
}

.button[id="deActive"]{
  display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
  background-color: #4caf4f00;
}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}

@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>
"""



setGamesChannelHtml = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
	<meta charset="utf-8">
	<title> mzooz bot </title>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>
</head>

<body>      
  <hr/>
  <h2>اختر القناة المراد إضافتها الى قنوات الالعاب</h2>
  <div class="picker">
    <hr/>
      <div class="custom-select" style="width:200px;">
        <select>
          <section class="cards">
            <option value="اختر القناة">اختر القناة</option>
            {% for channel in channels %}
            <option value={{channel}}>{{channel}}</option>
            {% endfor %}
          </section>
        </select>
      </div>
      <button class="button" id="save" onclick="add()">إضافة</button>
  </div>

  <hr/>
  <h2>اختر القناة المراد إزالتها من قنوات الالعاب</h2>
  <div class="picker">
    <hr/>
      <div class="custom-select" style="width:200px;">
        <select>
          <section class="cards">
            <option value="اختر القناة">اختر القناة</option>
            {% for channel in addedChannels %}
            <option value={{channel}}>{{channel}}</option>
            {% endfor %}
          </section>
        </select>
      </div>
      <button class="button" id="save" onclick="del()">حذف</button>
      <a href="/gamesManagment" class="button" id="back" >العودة</a>
  </div>

    </body>


<script>


var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }

        h.click();

    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);


function add(){
  location.replace("/setGamesChannel/add/"+document.getElementsByClassName("select-selected")[0].innerHTML);

}

function del(){
  location.replace("/setGamesChannel/delete/"+document.getElementsByClassName("select-selected")[1].innerHTML);

}

</script>

<style>



.custom-select {
  position: relative;
  font-family: Arial;
}

.custom-select select {
  display: none; /*hide original SELECT element: */
}

.select-selected {
  background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
  position: absolute;
  content: "";
  top: 14px;
  right: 10px;
  width: 0;
  height: 0;
  border: 6px solid transparent;
  border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
  border-color: transparent transparent #fff transparent;
  top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
  color: #ffffff;
  padding: 8px 16px;
  border: 1px solid transparent;
  border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
  cursor: pointer;
}

/* Style items (options): */
.select-items {
  position: absolute;
  background-color: #3c5be3;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
  display: none;
}

.select-items div:hover, .same-as-selected {
  background-color: rgba(0, 0, 0, 0.1);
}


input {
  opacity:0;
  position:absolute;
  left:-99999px;
}
 
input:checked + label {
  order: 1;
  z-index:2;
  background: #5c59ff;
  border-top:none;
  position:relative;
  color: white;
}
 
input:checked + label:after {
  content:'';
  width: 0; 
 height: 0; 
 border-left: 5px solid transparent;
 border-right: 5px solid transparent;
 border-top: 5px solid white;
  position:absolute;
  right:10px;
  top:calc(50% - 2.5px);
  pointer-events:none;
  z-index:3;
}
 
input:checked + label:before {
  position:absolute;
  right:0;
  height: 40px;
  width: 40px;
  content: '';
  background: #050505;
}
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  justify-items: center;
}

.card {
  margin: 0.5em;
  display: grid;
  grid-template-rows: 1fr 0.2fr;
  justify-items: center;
}

.card:hover {
  box-shadow: rgba(2, 8, 20, 0.1) 0px 0.35em 1.175em,
    rgba(2, 8, 20, 0.08) 0px 0.175em 0.5em;
  transform: scale(1.1);
}

.card img {
  border-radius: 50%;
  width: 7em;
  height: 7em;
}

h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}
h3 {
  text-align: center;
  color:#e33c3c;
}



@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}

.button{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}


  .button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button[id="save"]{
  background-color: #4caf4f00;
      display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3ce344;
    border-radius: 10px;
}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}




@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>


"""

setGamesCategoryHtml = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
	<meta charset="utf-8">
	<title> mzooz bot </title>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>
</head>

<body>
  <hr/>
    <h2>اختر المجموعة المراد تعيينها</h2>
    <div class="picker">
      <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر المجموعة المراد تعيينها">اختر المجموعة المراد تعيينها</option>
              <option value="None">عدم تعيين مجموعة</option>
              {% for category in categorys %}
              <option value={{category}}>{{category}}</option>
              {% endfor %}
            </section>
            </select>
        </div>
        <button class="button" id="save" onclick="save()">تعيين</button>
        <a href="/gamesManagment" class="button" id="back" >العودة</a>  
    </body>


<script>


var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }

        h.click();

    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);

function save(){
  var selectedOption = document.querySelector('select').value;
  location.replace("/setGamesCategory/"+selectedOption);
  };
</script>

<style>



.custom-select {
  position: relative;
  font-family: Arial;
}

.custom-select select {
  display: none; /*hide original SELECT element: */
}

.select-selected {
  background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
  position: absolute;
  content: "";
  top: 14px;
  right: 10px;
  width: 0;
  height: 0;
  border: 6px solid transparent;
  border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
  border-color: transparent transparent #fff transparent;
  top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
  color: #ffffff;
  padding: 8px 16px;
  border: 1px solid transparent;
  border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
  cursor: pointer;
}

/* Style items (options): */
.select-items {
  position: absolute;
  background-color: #3c5be3;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
  display: none;
}

.select-items div:hover, .same-as-selected {
  background-color: rgba(0, 0, 0, 0.1);
}


input {
  opacity:0;
  position:absolute;
  left:-99999px;
}
 
input:checked + label {
  order: 1;
  z-index:2;
  background: #5c59ff;
  border-top:none;
  position:relative;
  color: white;
}
 
input:checked + label:after {
  content:'';
  width: 0; 
 height: 0; 
 border-left: 5px solid transparent;
 border-right: 5px solid transparent;
 border-top: 5px solid white;
  position:absolute;
  right:10px;
  top:calc(50% - 2.5px);
  pointer-events:none;
  z-index:3;
}
 
input:checked + label:before {
  position:absolute;
  right:0;
  height: 40px;
  width: 40px;
  content: '';
  background: #050505;
}
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  justify-items: center;
}

.card {
  margin: 0.5em;
  display: grid;
  grid-template-rows: 1fr 0.2fr;
  justify-items: center;
}

.card:hover {
  box-shadow: rgba(2, 8, 20, 0.1) 0px 0.35em 1.175em,
    rgba(2, 8, 20, 0.08) 0px 0.175em 0.5em;
  transform: scale(1.1);
}

.card img {
  border-radius: 50%;
  width: 7em;
  height: 7em;
}

h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}


@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}

.button{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}


  .button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button[id="save"]{
  background-color: #4caf4f00;
      display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3ce344;
    border-radius: 10px;
}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}




@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>

"""

gamesManagmentHtml = """
<!DOCTYPE html>
<html>
  <head>
    <title>Dashboard</title>
  </head>
  <body>
    <h1>mzooz bot</h1>
    <div class="picker">
      <h2>ادارة الالعاب</h2>
      <hr />
      <section class="cards">
        <div class="card">
            <a href="/setGamesCategory/0" class="button">تعيين مجموعة</a>
            <a href="/setGamesChannel/0/0" class="button">ادارة القنوات</a>
          <a href="/server" class="button" id="back">العودة</a>
          <br />
        </div>
      </section>
    </div>
  </body>


<style>

h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}
.button{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}

.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}

.button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}

@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>
"""


systemManagmentHtml = """
<!DOCTYPE html>
<html>
  <head>
    <title>Dashboard</title>
  </head>
  <body>
    <h1>mzooz bot</h1>
    <div class="picker">
      <h2>ادارة النظام</h2>
      <hr />
      <div class="switch">
        <button class="button" id ="welcomming" onclick="wlcbyeManagment()">ترحيب - توديع</button>
        <button class="button" id ="suggstions" onclick="suggs()">الاقتراحات</button>
        <button class="button" id ="setLine" onclick="setLine()">تعيين خط</button>
      </div>

      <div class="switch">
        <button class="button" id ="robot" onclick="robot()">الرقابة</button>
        <button class="button" id ="customCommnads" onclick="customCommands()">اوامر خاصة</button>
        <button class="button" id ="back" onclick="back()">رجوع</button>
      </div>

    </div>
  </body>


<script>
  function customCommands(){
    location.replace("/cmdsManagment/0/0");
  };
  function wlcbyeManagment(){
    location.replace("/wlcbyeManagment/0/0/0/0");
  };
  function robot(){
    location.replace("/robotManagment");
  };
  function suggs(){
    location.replace("/suggestionsManagment/0/0");
  };
  function setLine(){
    location.replace("/setLine/0/0/0");
  };
  function back(){
    location.replace("/server");
  };

</script>

<style>

h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}
.button{
  background-color: #21253400;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}

.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}


.button[id="welcomming"]{
  background-color: #21253400;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 33px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;

}


.button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}

@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>
"""









cmdsManagmentHtml   = """
<!DOCTYPE html>
<html>
  <head>
    <title>mzooz bot</title>
  </head>
  <body>
      <h1>mzooz bot</h1>
      <h2>اوامر خاصة</h2>
      <form class="picker" method="POST">
        {% if not CMD %}
        <hr/>
        <h3>اختر الامر المراد تعديله</h3>
        <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر الامر">اختر الامر</option>
              {% for cmd in cmds %}
              <option value={{cmd}}>{{cmd}}</option>
              {% endfor %}
            </section>
          </select>
        </div>
        {%else%}
        <hr/>
        <h4 id="warnning">لاتكتب البادئة</h4>
        <hr/>
        <input type="text" id="url" name="url" placeholder="أضف امر بديل">
        <input type="submit" class="button" id="sub" value="أضف">
        <hr/>
        <h3>{{oldCmd}} هذه الاوامر البديله لـ</h3>
        <h4>اختر الامر المراد ازالته</h4>
        <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر الامر">اختر الامر</option>
              {% for cmd in cmds %}
              <option value={{cmd}}>{{cmd}}</option>
              {% endfor %}
            </section>
          </select>
        </div>
        {%endif%}
      </form>
      {% if not CMD %}
      <button class="button" id="sub" onclick="save()">تعديل</button>
      <button class="button" id="back" onclick="back()">رجوع</button>
      {%else%}
      <button class="button" id="sub" onclick="save()">حذف الامر</button>
      <a href="/cmdsManagment/0/0" class="button" id="back">رجوع</a>
      {%endif%}
  </body>
  
  
  <script>
var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }

        h.click();

    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);

function save(){
  if ("{{CMD}}" == "False"){
    if (document.getElementsByClassName("select-selected")[0].innerHTML != 'اختر الامر') {
      location.replace("/cmdsManagment/" + document.getElementsByClassName("select-selected")[0].innerHTML + '/0')}
}else if ("{{CMD}}" == "True"){
  if (document.getElementsByClassName("select-selected")[0].innerHTML != 'اختر الامر') {
      location.replace("/cmdsManagment/0/" + document.getElementsByClassName("select-selected")[0].innerHTML)}
}
}

function back(){
    location.replace("/systemManagment");
}


</script>


<style>



textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */ 
  border: 1px solid rgb(190, 190, 190); /* Gray border */
  border-radius: 2px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 0px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
}

.custom-select {
position: relative;
font-family: Arial;
}

.custom-select select {
display: none; /*hide original SELECT element: */
}

.select-selected {
background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
position: absolute;
content: "";
top: 14px;
right: 10px;
width: 0;
height: 0;
border: 6px solid transparent;
border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
border-color: transparent transparent #fff transparent;
top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
color: #ffffff;
padding: 8px 16px;
border: 1px solid transparent;
border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
cursor: pointer;
}

/* Style items (options): */
.select-items {
position: absolute;
background-color: #3c5be3;
top: 100%;
left: 0;
right: 0;
z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
display: none;
}

.select-items div:hover, .same-as-selected {
background-color: rgba(0, 0, 0, 0.1);
}



input:checked + label {
order: 1;
z-index:2;
background: #5c59ff;
border-top:none;
position:relative;
color: white;
}

input:checked + label:after {
content:'';
width: 0; 
height: 0; 
border-left: 5px solid transparent;
border-right: 5px solid transparent;
border-top: 5px solid white;
position:absolute;
right:10px;
top:calc(50% - 2.5px);
pointer-events:none;
z-index:3;
}

input:checked + label:before {
position:absolute;
right:0;
height: 40px;
width: 40px;
content: '';
background: #050505;
}


/* The switch - the box around the slider */
.switch {
position: relative;
display: inline-block;
width: 60px;
height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
opacity: 0;
width: 0;
height: 0;
}

/* The slider */
.slider {
position: absolute;
cursor: pointer;
top: 0;
left: 0;
right: 0;
bottom: 0;
background-color: #f32133;
-webkit-transition: .4s;
transition: .4s;
}

.slider:before {
position: absolute;
content: "";
height: 26px;
width: 26px;
left: 4px;
bottom: 4px;
background-color: white;
-webkit-transition: .4s;
transition: .4s;
}

input:checked + .slider {
background-color: #21f34f;
}

input:focus + .slider {
box-shadow: 0 0 1px #21f321;
}

input:checked + .slider:before {
-webkit-transform: translateX(26px);
-ms-transform: translateX(26px);
transform: translateX(26px);
}

.switch h3{
color: #00c292;

}

h3{
color: #00c292;

}

h4{
color: #3c98e3;
text-align: center;

}

h4[id="warnning"]{
  color: #e33c3c;
text-align: center;
}



.button{
  text-align: center;
background-color: #c22d0000;
}

/* Rounded sliders */
.slider.round {
border-radius: 34px;
}

.slider.round:before {
border-radius: 50%;
}

h1{
text-align: center;
color:#3c67e3;
}
h2 {
text-align: center;
color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
margin: 0;
padding: 0;
box-sizing: border-box;
}
body{
font-family: 'Poppins', sans-serif;
background-color: #212534;
display: grid;
place-content: center;
height: 100vh;
}
.button{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 10px 10px;
border: 3px solid 
#3c67e3;
border-radius: 10px;
}

.picker h3 {
text-align: center;
padding-top: 2%;
font-family: Georgia, "Times New Roman", Times, serif;
font-size: 1.5em;
}

.button:hover{
animation: pulsate 1s 
ease-in-out;
}

@keyframes pulsate {
0%{
    box-shadow: 
    0 0 25px #5ddcff,
    0 0 50px #4e00c2;
}
}

.picker input[type="text"] {
	border: 0;
	background: none;
	border: 2px solid #3498bd;
  width: 100%; 
  padding: 12px; 
	text-align: center;
  border-radius: 2px; 
  box-sizing: border-box; 
  margin-top: 0px; 
  margin-bottom: 16px; 
	outline: none;
	color: white;
	transform: 0.25s;
}



h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}
.button{
  background-color: #21253400;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}

.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}



.button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    border: 3px solid 
    #e33c3c;
    border-radius: 0px;
}

.button[id="yellow"]{
display: inline-block;
color: #fff;
text-decoration: none;
border: 3px solid 
#3ce33c;
border-radius: 10px;

}

.sub {
  background-color: #04AA6D;
  color: white;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  opacity: 0.9;
}

.sub:hover {
  opacity:1;
}

.button[id="sub"]{
  width: 100%;
  display: inline-block;
  text-decoration: none;
  border: 3px solid 
  #683ce3;
  border-radius: 0px;
  color: #fff;

}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}

@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>
"""








wlcbyeManagmentHtml = """

<!DOCTYPE html>
<html>
  <head>
    <title>mzooz bot</title>
  </head>
  <body>
      <h1>mzooz bot</h1>
      <h2>ترحيب - توديع</h2>
      <h4>منشن العضو [user]</h4>
      <h4>اسم السيرفر [server]</h4>
      <h4>عدد الاعضاء [membersCount]</h4>
      <h4>منشن الداعي [inviter]</h4>
      <h4>عدد المدعويين من هذا الشخص [inviters]</h4>
      <hr/>
      <form class="picker" method="POST">
        <textarea id="url" name="subject" placeholder="رسالة الترحيب" style="height:100px">{{message}}</textarea>
        <input type="submit" class="button" id="sub" value="تحديث الرسالة">
        <hr/>
        <h3>اختر قناة الترحيب</h3>
        <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر القناة">اختر القناة</option>
              <option value="لاتعيين">لاتعيين</option>
              {% for channel in channels %}
              <option value={{channel}}>{{channel}}</option>
              {% endfor %}
            </section>
          </select>
        </div>
        <hr/>
        <h3>اختر قناة التوديع</h3>
        <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر القناة">اختر القناة</option>
              <option value="لاتعيين">لاتعيين</option>
              {% for c in channels %}
              <option value={{c}}>{{c}}</option>
              {% endfor %}
            </section>
          </select>
        </div>
        <hr/>
        {% if activeRole%}
          <h3>اختر رولات الترحيب</h3>
          <hr/>
          <div class="custom-select" style="width:100%;text-align: center;">
            <select>
              <section class="cards">
                <option value="اختر الرتبة">اختر الرتبة</option>
                {% for role in roles %}
                <option value={{role}}>{{role}}</option>
                {% endfor %}
              </section>
            </select>
          </div>
          <hr/>
          <h3>ازل رولات الترحيب</h3>
          <hr/>
          <div class="custom-select" style="width:100%;text-align: center;">
            <select>
              <section class="cards">
                <option value="ازل الرتبة">ازل الرتبة</option>
                {% for r in onRoles %}
                <option value={{r}}>{{r}}</option>
                {% endfor %}
              </section>
            </select>
          </div>
          <hr/>
        {% endif %}
    </form>
    {% if activeRole%}
    <a href="/autoRoles/off" class="button" id="back">الغاء تفعيل رولات تلقائية</a>
    {% else %}
    <a href="/autoRoles/on" class="button" id="yellow">تفعيل رولات تلقائية</a>
    {% endif %}
    <button class="button" id="yellow" onclick="save()">حفظ</button>
    <button class="button" id="back" onclick="back()">رجوع</button>
  </body>
  
  
  <script>
var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }

        h.click();

    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);

function save(){
  if ("{{activeRole}}" == "True"){
    location.replace("/wlcbyeManagment/" + document.getElementsByClassName("select-selected")[0].innerHTML + "/" + document.getElementsByClassName("select-selected")[1].innerHTML+'/'+document.getElementsByClassName("select-selected")[2].innerHTML + '/' + document.getElementsByClassName("select-selected")[3].innerHTML);
  }else if ("{{activeRole}}" == "False"){
  location.replace("/wlcbyeManagment/" + document.getElementsByClassName("select-selected")[0].innerHTML + "/" + document.getElementsByClassName("select-selected")[1].innerHTML+'/0/0');
}
}

function back(){
    location.replace("/systemManagment")
}

</script>


<style>



textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */ 
  border: 1px solid rgb(190, 190, 190); /* Gray border */
  border-radius: 2px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 0px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
}

.custom-select {
position: relative;
font-family: Arial;
}

.custom-select select {
display: none; /*hide original SELECT element: */
}

.select-selected {
background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
position: absolute;
content: "";
top: 14px;
right: 10px;
width: 0;
height: 0;
border: 6px solid transparent;
border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
border-color: transparent transparent #fff transparent;
top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
color: #ffffff;
padding: 8px 16px;
border: 1px solid transparent;
border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
cursor: pointer;
}

/* Style items (options): */
.select-items {
position: absolute;
background-color: #3c5be3;
top: 100%;
left: 0;
right: 0;
z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
display: none;
}

.select-items div:hover, .same-as-selected {
background-color: rgba(0, 0, 0, 0.1);
}



input:checked + label {
order: 1;
z-index:2;
background: #5c59ff;
border-top:none;
position:relative;
color: white;
}

input:checked + label:after {
content:'';
width: 0; 
height: 0; 
border-left: 5px solid transparent;
border-right: 5px solid transparent;
border-top: 5px solid white;
position:absolute;
right:10px;
top:calc(50% - 2.5px);
pointer-events:none;
z-index:3;
}

input:checked + label:before {
position:absolute;
right:0;
height: 40px;
width: 40px;
content: '';
background: #050505;
}


/* The switch - the box around the slider */
.switch {
position: relative;
display: inline-block;
width: 60px;
height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
opacity: 0;
width: 0;
height: 0;
}

/* The slider */
.slider {
position: absolute;
cursor: pointer;
top: 0;
left: 0;
right: 0;
bottom: 0;
background-color: #f32133;
-webkit-transition: .4s;
transition: .4s;
}

.slider:before {
position: absolute;
content: "";
height: 26px;
width: 26px;
left: 4px;
bottom: 4px;
background-color: white;
-webkit-transition: .4s;
transition: .4s;
}

input:checked + .slider {
background-color: #21f34f;
}

input:focus + .slider {
box-shadow: 0 0 1px #21f321;
}

input:checked + .slider:before {
-webkit-transform: translateX(26px);
-ms-transform: translateX(26px);
transform: translateX(26px);
}

.switch h3{
color: #00c292;

}

h3{
color: #00c292;

}

h3[id="untrust"]{
color: #c24e00;

}

h4{
color: #3ce38f;

}

h3[id="trust"]{
color: #473ce3;

}


.button{
  text-align: center;
background-color: #c22d0000;
}

/* Rounded sliders */
.slider.round {
border-radius: 34px;
}

.slider.round:before {
border-radius: 50%;
}

h1{
text-align: center;
color:#3c67e3;
}
h2 {
text-align: center;
color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
margin: 0;
padding: 0;
box-sizing: border-box;
}
body{
font-family: 'Poppins', sans-serif;
background-color: #212534;
display: grid;
place-content: center;
height: 100vh;
}
.button{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 10px 10px;
border: 3px solid 
#3c67e3;
border-radius: 10px;
}

.picker h3 {
text-align: center;
padding-top: 2%;
font-family: Georgia, "Times New Roman", Times, serif;
font-size: 1.5em;
}

.button:hover{
animation: pulsate 1s 
ease-in-out;
}

@keyframes pulsate {
0%{
    box-shadow: 
    0 0 25px #5ddcff,
    0 0 50px #4e00c2;
}
}


.picker input[type="text"]{
	border: 0;
	background: none;
	display: block;
	margin: 20px auto;
	text-align: center;
	border: 2px solid #3498bd;
	width: 200px;
	outline: none;
	color: white;
	border-radius: 24px;
	transform: 0.25s;

}
.picker input[type="text"]:focus{
	width: 220px;
	border-color: #2ecc71;
}



h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}
.button{
  background-color: #21253400;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}

.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}



.button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button[id="yellow"]{
display: inline-block;
color: #fff;
text-decoration: none;
border: 3px solid 
#3ce33c;
border-radius: 10px;

}

.sub {
  background-color: #04AA6D;
  color: white;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  opacity: 0.9;
}

.sub:hover {
  opacity:1;
}

.button[id="sub"]{
  width: 100%;
  display: inline-block;
  text-decoration: none;
  border: 3px solid 
  #683ce3;
  border-radius: 0px;
  color: #fff;

}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}

@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>
"""


addAntiWordHtml     = """


<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
	<meta charset="utf-8">
	<title> mzooz bot </title>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>
</head>

<body>      
  <h1>mzooz bot</h1>
  <h2>إدارة الكلمات البذيئة</h2>
  <h3>لاتضغط زر عشان يضبط enter</h3>
  <hr/>
  <div class="picker">
    <form class="picker">
      <input type="text" id="w" name="w" placeholder="الكلمة" >
    </form>
    <hr/>
    <div class="custom-select" style="width:200px;">          
        <select>
        <section class="cards">
          <option value="اختر الكلمة المراد السماح لها">اختر الكلمة المراد السماح لها</option>
          {% for word in words %}
          <option value={{word}}>{{word}}</option>
          {% endfor %}
        </section>
      </select>
    </div>
    <input type="submit" hidden="True">
  </div>
    <button class="button" id="save" onclick="save()">حفظ التغييرات</button>
    <a href="/robotManagment" class="button" id="back" >رجوع</a>

</body>


<script>


var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }

        h.click();

    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);

function save(){
  var w = document.getElementById("w").value
  if (w==""){
    w = "0"
  }
  for (i in w){
    if (w[i] == "/"){
      w = w.replace("/","");
    }
  };  location.replace("/addAntiWord/"+w + "/" + document.getElementsByClassName("select-selected")[0].innerHTML);
  }
</script>

<style>



.custom-select {
  position: relative;
  font-family: Arial;
}

.custom-select select {
  display: none; /*hide original SELECT element: */
}

.select-selected {
  background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
  position: absolute;
  content: "";
  top: 14px;
  right: 10px;
  width: 0;
  height: 0;
  border: 6px solid transparent;
  border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
  border-color: transparent transparent #fff transparent;
  top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
  color: #ffffff;
  padding: 8px 16px;
  border: 1px solid transparent;
  border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
  cursor: pointer;
}

/* Style items (options): */
.select-items {
  position: absolute;
  background-color: #3c5be3;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
  display: none;
}

.select-items div:hover, .same-as-selected {
  background-color: rgba(0, 0, 0, 0.1);
}


input:checked + label {
order: 1;
z-index:2;
background: #5c59ff;
border-top:none;
position:relative;
color: white;
}

input:checked + label:after {
content:'';
width: 0; 
height: 0; 
border-left: 5px solid transparent;
border-right: 5px solid transparent;
border-top: 5px solid white;
position:absolute;
right:10px;
top:calc(50% - 2.5px);
pointer-events:none;
z-index:3;
}

input:checked + label:before {
position:absolute;
right:0;
height: 40px;
width: 40px;
content: '';
background: #050505;
}

input:checked + .slider {
background-color: #21f34f;
}

input:focus + .slider {
box-shadow: 0 0 1px #21f321;
}

input:checked + .slider:before {
-webkit-transform: translateX(26px);
-ms-transform: translateX(26px);
transform: translateX(26px);
}

.picker input[type="text"]{
	border: 0;
	background: none;
	display: block;
	margin: 20px auto;
	text-align: center;
	border: 2px solid #3498bd;
	padding: 14px 10px;
	width: 200px;
	outline: none;
	color: white;
	border-radius: 24px;
	transform: 0.25s;

}
.picker input[type="text"]:focus{
	width: 220px;
	border-color: #2ecc71;
}

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  justify-items: center;
}

.card {
  margin: 0.5em;
  display: grid;
  grid-template-rows: 1fr 0.2fr;
  justify-items: center;
}

.card:hover {
  box-shadow: rgba(2, 8, 20, 0.1) 0px 0.35em 1.175em,
    rgba(2, 8, 20, 0.08) 0px 0.175em 0.5em;
  transform: scale(1.1);
}

.card img {
  border-radius: 50%;
  width: 7em;
  height: 7em;
}

h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}
h3{
  text-align: center;
  color:#e33c3c;
 
}


@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}

.button{
  text-align: center;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}


  .button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button[id="save"]{
  background-color: #4caf4f00;
      display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3ce344;
    border-radius: 10px;
}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}




@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>


"""



robotManagmentHtml  = """

<!DOCTYPE html>
<html>
  <head>
    <title>mzooz bot</title>
  </head>
  <body>
    <h1>mzooz bot</h1>
    <h2>ادارة الرقابة</h2>
    <hr/>
      {% if activeAuto %}
      <a href="/robotAutoActive/off" class="button" id="back">الغاء تفعيل الرقابة التلقائية</a>
      <a href="/addAutoResponse" class="button">أضف رد تلقائي</a>
      <a href="/addAntiWord/0/0" class="button">أضف كلمات بذيئة</a>
      
      {% else %}
      <a href="/robotAutoActive/on" class="button" id="active">تفعيل الرقابة التلقائية</a>
      {% endif %}

      {% if antiUrls %}
      <a href="/antiUrls/off" class="button" id="unActive">تعطيل مانع الروابط</a>
      {% else %}
      <a href="/antiUrls/on" class="button" id="yellow">تفعيل مانع الروابط</a>
      {% endif %}

      {% if antiSpam %}
      <a href="/antiSpam/off" class="button" id="unActive">تعطيل مانع السبام</a>
      {% else %}
      <a href="/antiSpam/on" class="button" id="yellow">تفعيل مانع السبام</a>
      {% endif %}

      <button class="button" id="back" onclick="back()">رجوع</button>
      <hr/>
</body>
  
  
  <script>
var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }

        h.click();

    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);

function save(){
  if ("{{activeAuto}}" == "True"){
    location.replace("/robot");
  }else if ("{{activeAuto}}" == "False"){
    location.replace("/robot");
  }
}

function back(){
    location.replace("/systemManagment")
}

</script>


<style>

.custom-select {
position: relative;
font-family: Arial;
}

.custom-select select {
display: none; /*hide original SELECT element: */
}

.select-selected {
background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
position: absolute;
content: "";
top: 14px;
right: 10px;
width: 0;
height: 0;
border: 6px solid transparent;
border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
border-color: transparent transparent #fff transparent;
top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
color: #ffffff;
padding: 8px 16px;
border: 1px solid transparent;
border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
cursor: pointer;
}

/* Style items (options): */
.select-items {
position: absolute;
background-color: #3c5be3;
top: 100%;
left: 0;
right: 0;
z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
display: none;
}

.select-items div:hover, .same-as-selected {
background-color: rgba(0, 0, 0, 0.1);
}



input:checked + label {
order: 1;
z-index:2;
background: #5c59ff;
border-top:none;
position:relative;
color: white;
}

input:checked + label:after {
content:'';
width: 0; 
height: 0; 
border-left: 5px solid transparent;
border-right: 5px solid transparent;
border-top: 5px solid white;
position:absolute;
right:10px;
top:calc(50% - 2.5px);
pointer-events:none;
z-index:3;
}

input:checked + label:before {
position:absolute;
right:0;
height: 40px;
width: 40px;
content: '';
background: #050505;
}


/* The switch - the box around the slider */
.switch {
position: relative;
display: inline-block;
width: 60px;
height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
opacity: 0;
width: 0;
height: 0;
}

/* The slider */
.slider {
position: absolute;
cursor: pointer;
top: 0;
left: 0;
right: 0;
bottom: 0;
background-color: #f32133;
-webkit-transition: .4s;
transition: .4s;
}

.slider:before {
position: absolute;
content: "";
height: 26px;
width: 26px;
left: 4px;
bottom: 4px;
background-color: white;
-webkit-transition: .4s;
transition: .4s;
}

input:checked + .slider {
background-color: #21f34f;
}

input:focus + .slider {
box-shadow: 0 0 1px #21f321;
}

input:checked + .slider:before {
-webkit-transform: translateX(26px);
-ms-transform: translateX(26px);
transform: translateX(26px);
}

.switch h3{
color: #00c292;

}

h3{
color: #c02222;

}

h3[id="untrust"]{
color: #c24e00;

}

h3[id="trust"]{
color: #473ce3;

}


.button{
  text-align: center;
background-color: #c22d0000;
}

/* Rounded sliders */
.slider.round {
border-radius: 34px;
}

.slider.round:before {
border-radius: 50%;
}

h1{
text-align: center;
color:#3c67e3;
}
h2 {
text-align: center;
color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
margin: 0;
padding: 0;
box-sizing: border-box;
}
body{
font-family: 'Poppins', sans-serif;
background-color: #212534;
display: grid;
place-content: center;
height: 100vh;
}
.button{
  position: center;
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#3c67e3;
border-radius: 10px;
}

.picker h3 {
text-align: center;
padding-top: 2%;
font-family: Georgia, "Times New Roman", Times, serif;
font-size: 1.5em;
}

.button[id="unActive"]{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#e3e03c;
border-radius: 10px;

}

.button[id="active"]{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#3ce33c;
border-radius: 10px;
background-color: #4caf4f00;
}

.button[id="yellow"]{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#e3713c;
border-radius: 10px;
background-color: #4caf4f00;
}

.button:hover{
animation: pulsate 1s 
ease-in-out;
}

@keyframes pulsate {
0%{
    box-shadow: 
    0 0 25px #5ddcff,
    0 0 50px #4e00c2;
}
}


.picker input[type="text"]{
	border: 0;
	background: none;
	display: block;
	margin: 20px auto;
	text-align: center;
	border: 2px solid #3498bd;
	padding: 14px 10px;
	width: 200px;
	outline: none;
	color: white;
	border-radius: 24px;
	transform: 0.25s;

}
.picker input[type="text"]:focus{
	width: 220px;
	border-color: #2ecc71;
}



h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}
.button{
  background-color: #21253400;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}

.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}


.button[id="welcomming"]{
  background-color: #21253400;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 33px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;

}


.button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 45px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button[id="save"]{
  display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 45px;
    border: 3px solid 
    #3ce33c;
    border-radius: 10px;

}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}

@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>
"""



addAutoResponseHtml = """


<!DOCTYPE html>
<html>
  <head>
    <title>mzooz bot</title>
  </head>
  <body>
    <div class="picker">
      <h1>mzooz bot</h1>
      <h2>إضافة رد تلقائي</h2>
      <hr/>
      <form class="picker">
        <input type="text" id="word" name="word" placeholder="الكلمة">
        <input type="text" id="response" name="response" placeholder="ردها">
        <hr/>
      </form>
    </div>
    <button class="button" id="save" onclick="save()">حفظ</button>
    <button class="button" id="back" onclick="back()">رجوع</button>
  </body>



  <script>
function save(){
  var word = document.getElementById("word").value;
  var response = document.getElementById("response").value;
  location.replace("/addAntiBad/"+word+"/"+response);
}

function back(){
    location.replace("/robotManagment")
}

</script>


<style>

.custom-select {
position: relative;
font-family: Arial;
}

.custom-select select {
display: none; /*hide original SELECT element: */
}

.select-selected {
background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
position: absolute;
content: "";
top: 14px;
right: 10px;
width: 0;
height: 0;
border: 6px solid transparent;
border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
border-color: transparent transparent #fff transparent;
top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
color: #ffffff;
padding: 8px 16px;
border: 1px solid transparent;
border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
cursor: pointer;
}

/* Style items (options): */
.select-items {
position: absolute;
background-color: #3c5be3;
top: 100%;
left: 0;
right: 0;
z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
display: none;
}

.select-items div:hover, .same-as-selected {
background-color: rgba(0, 0, 0, 0.1);
}



input:checked + label {
order: 1;
z-index:2;
background: #5c59ff;
border-top:none;
position:relative;
color: white;
}

input:checked + label:after {
content:'';
width: 0; 
height: 0; 
border-left: 5px solid transparent;
border-right: 5px solid transparent;
border-top: 5px solid white;
position:absolute;
right:10px;
top:calc(50% - 2.5px);
pointer-events:none;
z-index:3;
}

input:checked + label:before {
position:absolute;
right:0;
height: 40px;
width: 40px;
content: '';
background: #050505;
}


/* The switch - the box around the slider */
.switch {
position: relative;
display: inline-block;
width: 60px;
height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
opacity: 0;
width: 0;
height: 0;
}

/* The slider */
.slider {
position: absolute;
cursor: pointer;
top: 0;
left: 0;
right: 0;
bottom: 0;
background-color: #f32133;
-webkit-transition: .4s;
transition: .4s;
}

.slider:before {
position: absolute;
content: "";
height: 26px;
width: 26px;
left: 4px;
bottom: 4px;
background-color: white;
-webkit-transition: .4s;
transition: .4s;
}

input:checked + .slider {
background-color: #21f34f;
}

input:focus + .slider {
box-shadow: 0 0 1px #21f321;
}

input:checked + .slider:before {
-webkit-transform: translateX(26px);
-ms-transform: translateX(26px);
transform: translateX(26px);
}

.switch h3{
color: #00c292;

}

h3{
color: #00c292;

}

h3[id="untrust"]{
color: #c24e00;

}

h3[id="trust"]{
color: #473ce3;

}


.button{
background-color: #c22d0000;
}

/* Rounded sliders */
.slider.round {
border-radius: 34px;
}

.slider.round:before {
border-radius: 50%;
}

h1{
text-align: center;
color:#3c67e3;
}
h2 {
text-align: center;
color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
margin: 0;
padding: 0;
box-sizing: border-box;
}
body{
font-family: 'Poppins', sans-serif;
background-color: #212534;
display: grid;
place-content: center;
height: 100vh;
}
.button{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#3c67e3;
border-radius: 10px;
}

.picker h3 {
text-align: center;
padding-top: 2%;
font-family: Georgia, "Times New Roman", Times, serif;
font-size: 1.5em;
}

.button[id="untrust"]{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#e3e03c;
border-radius: 10px;

}

.button[id="active"]{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#3ce33c;
border-radius: 10px;
background-color: #4caf4f00;
}

.button[id="deActive"]{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#e33c3c;
border-radius: 10px;
background-color: #4caf4f00;
}

.button:hover{
animation: pulsate 1s 
ease-in-out;
}

@keyframes pulsate {
0%{
    box-shadow: 
    0 0 25px #5ddcff,
    0 0 50px #4e00c2;
}
}


.picker input[type="text"]{
	border: 0;
	background: none;
	display: block;
	margin: 20px auto;
	text-align: center;
	border: 2px solid #3498bd;
	padding: 14px 10px;
	width: 200px;
	outline: none;
	color: white;
	border-radius: 24px;
	transform: 0.25s;

}
.picker input[type="text"]:focus{
	width: 220px;
	border-color: #2ecc71;
}



h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}
.button{
  background-color: #21253400;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}

.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}


.button[id="welcomming"]{
  background-color: #21253400;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 33px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;

}


.button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 45px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button[id="save"]{
  display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 45px;
    border: 3px solid 
    #3ce33c;
    border-radius: 10px;

}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}

@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>
"""


setSuggstionsHtml   = """

<!DOCTYPE html>
<html>
  <head>
    <title>mzooz bot</title>
  </head>
  <body>
    <div class="picker">
      <h1>mzooz bot</h1>
      <h2>ادارة الاقتراحات</h2>
      <hr/>
        {% if activeSuggstions %}
        <a href="/activeSuggstions/off" class="button" id="back">الغاء التفعيل</a>
        <label class="switch" for="active" ><h3>نظام الاقتراحات</h3></label>
        <hr/>
        <h3>أضف قناة الى قائمة الاقتراحات</h3>
        <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر القناة">اختر القناة</option>
              {% for channel in channels %}
              <option value={{channel}}>{{channel}}</option>
              {% endfor %}
            </section>
          </select>
        </div>
        <hr/>
        <h3>اختر قناة لإزالتها من قائمة الاقتراحات</h3>
        <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر القناة">اختر القناة</option>
              {% for channel in onChannels %}
              <option value={{channel}}>{{channel}}</option>
              {% endfor %}
            </section>
          </select>
        </div>
        {% else %}
        <a href="/activeSuggstions/on" class="button" id="active">تفعيل</a>
        <label class="switch" for="active" ><h3>نظام الاقتراحات</h3></label>
        {% endif %}
        <hr/>
      </div>
      <button class="button" id="save" onclick="save()">حفظ</button>
      <button class="button" id="back" onclick="back()">رجوع</button>
  </body>
  
  
  <script>
var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }

        h.click();

    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);

function save(){
  if ("{{activeSuggstions}}" == "True"){
    location.replace("/suggestionsManagment/" + document.getElementsByClassName("select-selected")[0].innerHTML + "/" + document.getElementsByClassName("select-selected")[1].innerHTML);
  }else if ("{{activeSuggstions}}" == "False"){
    location.replace("/suggestionsManagment/0/0");
  }
}

function back(){
    location.replace("/systemManagment")
}

</script>


<style>

.custom-select {
position: relative;
font-family: Arial;
}

.custom-select select {
display: none; /*hide original SELECT element: */
}

.select-selected {
background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
position: absolute;
content: "";
top: 14px;
right: 10px;
width: 0;
height: 0;
border: 6px solid transparent;
border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
border-color: transparent transparent #fff transparent;
top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
color: #ffffff;
padding: 8px 16px;
border: 1px solid transparent;
border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
cursor: pointer;
}

/* Style items (options): */
.select-items {
position: absolute;
background-color: #3c5be3;
top: 100%;
left: 0;
right: 0;
z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
display: none;
}

.select-items div:hover, .same-as-selected {
background-color: rgba(0, 0, 0, 0.1);
}



input:checked + label {
order: 1;
z-index:2;
background: #5c59ff;
border-top:none;
position:relative;
color: white;
}

input:checked + label:after {
content:'';
width: 0; 
height: 0; 
border-left: 5px solid transparent;
border-right: 5px solid transparent;
border-top: 5px solid white;
position:absolute;
right:10px;
top:calc(50% - 2.5px);
pointer-events:none;
z-index:3;
}

input:checked + label:before {
position:absolute;
right:0;
height: 40px;
width: 40px;
content: '';
background: #050505;
}


/* The switch - the box around the slider */
.switch {
position: relative;
display: inline-block;
width: 60px;
height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
opacity: 0;
width: 0;
height: 0;
}

/* The slider */
.slider {
position: absolute;
cursor: pointer;
top: 0;
left: 0;
right: 0;
bottom: 0;
background-color: #f32133;
-webkit-transition: .4s;
transition: .4s;
}

.slider:before {
position: absolute;
content: "";
height: 26px;
width: 26px;
left: 4px;
bottom: 4px;
background-color: white;
-webkit-transition: .4s;
transition: .4s;
}

input:checked + .slider {
background-color: #21f34f;
}

input:focus + .slider {
box-shadow: 0 0 1px #21f321;
}

input:checked + .slider:before {
-webkit-transform: translateX(26px);
-ms-transform: translateX(26px);
transform: translateX(26px);
}

.switch h3{
color: #00c292;

}

h3{
color: #00c292;

}

h3[id="untrust"]{
color: #c24e00;

}

h3[id="trust"]{
color: #473ce3;

}


.button{
background-color: #c22d0000;
}

/* Rounded sliders */
.slider.round {
border-radius: 34px;
}

.slider.round:before {
border-radius: 50%;
}

h1{
text-align: center;
color:#3c67e3;
}
h2 {
text-align: center;
color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
margin: 0;
padding: 0;
box-sizing: border-box;
}
body{
font-family: 'Poppins', sans-serif;
background-color: #212534;
display: grid;
place-content: center;
height: 100vh;
}
.button{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#3c67e3;
border-radius: 10px;
}

.picker h3 {
text-align: center;
padding-top: 2%;
font-family: Georgia, "Times New Roman", Times, serif;
font-size: 1.5em;
}

.button[id="untrust"]{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#e3e03c;
border-radius: 10px;

}

.button[id="active"]{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#3ce33c;
border-radius: 10px;
background-color: #4caf4f00;
}

.button[id="deActive"]{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#e33c3c;
border-radius: 10px;
background-color: #4caf4f00;
}

.button:hover{
animation: pulsate 1s 
ease-in-out;
}

@keyframes pulsate {
0%{
    box-shadow: 
    0 0 25px #5ddcff,
    0 0 50px #4e00c2;
}
}


.picker input[type="text"]{
	border: 0;
	background: none;
	display: block;
	margin: 20px auto;
	text-align: center;
	border: 2px solid #3498bd;
	padding: 14px 10px;
	width: 200px;
	outline: none;
	color: white;
	border-radius: 24px;
	transform: 0.25s;

}
.picker input[type="text"]:focus{
	width: 220px;
	border-color: #2ecc71;
}



h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}
.button{
  background-color: #21253400;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}

.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}


.button[id="welcomming"]{
  background-color: #21253400;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 33px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;

}


.button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 45px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button[id="save"]{
  display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 45px;
    border: 3px solid 
    #3ce33c;
    border-radius: 10px;

}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}

@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>
"""


setLineHtml         = """

<!DOCTYPE html>
<html>
  <head>
    <title>mzooz bot</title>
  </head>
  <body>
    <div class="picker">
      <h1>mzooz bot</h1>
      <h2>تعيين خط</h2>
      <hr/>
      <form class="picker">
        <input type="text" id="url" name="url" placeholder="رابط الصورة-خط" value="{{lineUrl}}">
        <hr/>
        {% if activeAutoLine %}
        <a href="/activeAutoLine/off" class="button" id="back">الغاء التفعيل</a>
        <label class="switch" for="active" ><h3>خط تلقائي</h3></label>
        <hr/>
        <h3>اختر قناة الخط التلقائي</h3>
        <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر القناة">اختر القناة</option>
              {% for channel in channels %}
              <option value={{channel}}>{{channel}}</option>
              {% endfor %}
            </section>
          </select>
        </div>
        <hr/>
        <h3>اختر قناة لإزالتها من الخط التلقائي</h3>
        <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر القناة">اختر القناة</option>
              {% for channel in onChannels %}
              <option value={{channel}}>{{channel}}</option>
              {% endfor %}
            </section>
          </select>
        </div>
        {% else %}
        <a href="/activeAutoLine/on" class="button" id="active">تفعيل</a>
        <label class="switch" for="active" ><h3>خط تلقائي</h3></label>
        {% endif %}
        <hr/>
      </form>
    </div>
    <button class="button" id="save" onclick="save()">حفظ</button>
    <button class="button" id="back" onclick="back()">رجوع</button>
  </body>
  
  
  <script>
var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }

        h.click();

    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);

function save(){
  "save the input value"
  var url = document.getElementById("url").value;
  for (i in url){
    if (url[i] == "/"){
      url = url.replace("/","`");
    }
  };
  if ("{{activeAutoLine}}" == "True"){
    location.replace("/setLine/" + document.getElementsByClassName("select-selected")[0].innerHTML + "/" + document.getElementsByClassName("select-selected")[1].innerHTML + '/' + url);
  }else if ("{{activeAutoLine}}" == "False"){
    location.replace("/setLine/0/"+ url);
  }
}

function back(){
    location.replace("/systemManagment")
}

</script>


<style>

.custom-select {
position: relative;
font-family: Arial;
}

.custom-select select {
display: none; /*hide original SELECT element: */
}

.select-selected {
background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
position: absolute;
content: "";
top: 14px;
right: 10px;
width: 0;
height: 0;
border: 6px solid transparent;
border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
border-color: transparent transparent #fff transparent;
top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
color: #ffffff;
padding: 8px 16px;
border: 1px solid transparent;
border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
cursor: pointer;
}

/* Style items (options): */
.select-items {
position: absolute;
background-color: #3c5be3;
top: 100%;
left: 0;
right: 0;
z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
display: none;
}

.select-items div:hover, .same-as-selected {
background-color: rgba(0, 0, 0, 0.1);
}



input:checked + label {
order: 1;
z-index:2;
background: #5c59ff;
border-top:none;
position:relative;
color: white;
}

input:checked + label:after {
content:'';
width: 0; 
height: 0; 
border-left: 5px solid transparent;
border-right: 5px solid transparent;
border-top: 5px solid white;
position:absolute;
right:10px;
top:calc(50% - 2.5px);
pointer-events:none;
z-index:3;
}

input:checked + label:before {
position:absolute;
right:0;
height: 40px;
width: 40px;
content: '';
background: #050505;
}


/* The switch - the box around the slider */
.switch {
position: relative;
display: inline-block;
width: 60px;
height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
opacity: 0;
width: 0;
height: 0;
}

/* The slider */
.slider {
position: absolute;
cursor: pointer;
top: 0;
left: 0;
right: 0;
bottom: 0;
background-color: #f32133;
-webkit-transition: .4s;
transition: .4s;
}

.slider:before {
position: absolute;
content: "";
height: 26px;
width: 26px;
left: 4px;
bottom: 4px;
background-color: white;
-webkit-transition: .4s;
transition: .4s;
}

input:checked + .slider {
background-color: #21f34f;
}

input:focus + .slider {
box-shadow: 0 0 1px #21f321;
}

input:checked + .slider:before {
-webkit-transform: translateX(26px);
-ms-transform: translateX(26px);
transform: translateX(26px);
}

.switch h3{
color: #00c292;

}

h3{
color: #00c292;

}

h3[id="untrust"]{
color: #c24e00;

}

h3[id="trust"]{
color: #473ce3;

}


.button{
background-color: #c22d0000;
}

/* Rounded sliders */
.slider.round {
border-radius: 34px;
}

.slider.round:before {
border-radius: 50%;
}

h1{
text-align: center;
color:#3c67e3;
}
h2 {
text-align: center;
color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
margin: 0;
padding: 0;
box-sizing: border-box;
}
body{
font-family: 'Poppins', sans-serif;
background-color: #212534;
display: grid;
place-content: center;
height: 100vh;
}
.button{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#3c67e3;
border-radius: 10px;
}

.picker h3 {
text-align: center;
padding-top: 2%;
font-family: Georgia, "Times New Roman", Times, serif;
font-size: 1.5em;
}

.button[id="untrust"]{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#e3e03c;
border-radius: 10px;

}

.button[id="active"]{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#3ce33c;
border-radius: 10px;
background-color: #4caf4f00;
}

.button[id="deActive"]{
display: inline-block;
color: #fff;
text-decoration: none;
padding: 20px 50px;
border: 3px solid 
#e33c3c;
border-radius: 10px;
background-color: #4caf4f00;
}

.button:hover{
animation: pulsate 1s 
ease-in-out;
}

@keyframes pulsate {
0%{
    box-shadow: 
    0 0 25px #5ddcff,
    0 0 50px #4e00c2;
}
}


.picker input[type="text"]{
	border: 0;
	background: none;
	display: block;
	margin: 20px auto;
	text-align: center;
	border: 2px solid #3498bd;
	padding: 14px 10px;
	width: 200px;
	outline: none;
	color: white;
	border-radius: 24px;
	transform: 0.25s;

}
.picker input[type="text"]:focus{
	width: 220px;
	border-color: #2ecc71;
}



h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}
.button{
  background-color: #21253400;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}

.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}


.button[id="welcomming"]{
  background-color: #21253400;
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 33px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;

}


.button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 45px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button[id="save"]{
  display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 45px;
    border: 3px solid 
    #3ce33c;
    border-radius: 10px;

}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}

@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>
"""



ticketManagmentHtml = """
<!DOCTYPE html>
<html>
  <head>
    <title>Dashboard</title>
  </head>
  <body>
    <h1>mzooz bot</h1>
    <div class="picker">
      <h2>ادارة التيكت</h2>
      <hr />
      <section class="cards">
        <div class="card">          
          <a href="/tickets" class="button">حذف تيكت</a>
          <a href="/moveTicket/0/0" class="button">نقل تيكت</a>
          <a href="/createCategory/0" class="button">تعيين مجموعه</a>
<!--          <a href="/transcripts" class="button">transcripts</a> -->
          <a href="/server" class="button" id="back">العودة</a>
          <br />
        </div>
      </section>
    </div>
  </body>


<style>

h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}
.button{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}

.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}

.button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}

@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>





"""


transcripthtml = '''


<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
	<meta charset="utf-8">
	<title> mzooz bot </title>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>
</head>

<body>      
      <hr/>
      <h2>اختر النسخة</h2>
      <div class="picker">
        <hr/>
          <div class="custom-select" style="width:100%;text-align: center;">
            <select>
              <section class="cards">
                <option value="اختر النسخة">اختر النسخة</option>
                {% for transcript in transcripts %}
                <option value={{transcript}}>{{transcript[:-5]}}</option>
                {% endfor %}
              </section>
            </select>
          </div>
          <button class="button" id="save" onclick="save()">فتح</button>
          <a href="/ticketsManagment" class="button" id="back" >العودة</a>

      </div>
    </body>


<script>


var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }

        h.click();

    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);

function save(){
  var selectedOption = document.querySelector('select').value;
  location.replace("/openTranscript/"+selectedOption);
  };
</script>

<style>



.custom-select {
  position: relative;
  font-family: Arial;
}

.custom-select select {
  display: none; /*hide original SELECT element: */
}

.select-selected {
  background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
  position: absolute;
  content: "";
  top: 14px;
  right: 10px;
  width: 0;
  height: 0;
  border: 6px solid transparent;
  border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
  border-color: transparent transparent #fff transparent;
  top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
  color: #ffffff;
  padding: 8px 16px;
  border: 1px solid transparent;
  border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
  cursor: pointer;
}

/* Style items (options): */
.select-items {
  position: absolute;
  background-color: #3c5be3;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
  display: none;
}

.select-items div:hover, .same-as-selected {
  background-color: rgba(0, 0, 0, 0.1);
}


input {
  opacity:0;
  position:absolute;
  left:-99999px;
}
 
input:checked + label {
  order: 1;
  z-index:2;
  background: #5c59ff;
  border-top:none;
  position:relative;
  color: white;
}
 
input:checked + label:after {
  content:'';
  width: 0; 
 height: 0; 
 border-left: 5px solid transparent;
 border-right: 5px solid transparent;
 border-top: 5px solid white;
  position:absolute;
  right:10px;
  top:calc(50% - 2.5px);
  pointer-events:none;
  z-index:3;
}
 
input:checked + label:before {
  position:absolute;
  right:0;
  height: 40px;
  width: 40px;
  content: '';
  background: #050505;
}
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  justify-items: center;
}

.card {
  margin: 0.5em;
  display: grid;
  grid-template-rows: 1fr 0.2fr;
  justify-items: center;
}

.card:hover {
  box-shadow: rgba(2, 8, 20, 0.1) 0px 0.35em 1.175em,
    rgba(2, 8, 20, 0.08) 0px 0.175em 0.5em;
  transform: scale(1.1);
}

.card img {
  border-radius: 50%;
  width: 7em;
  height: 7em;
}

h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}



@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}

.button{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}


  .button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button[id="save"]{
  background-color: #4caf4f00;
      display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3ce344;
    border-radius: 10px;
}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}




@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>

'''

dashboardHtml = '''

<!DOCTYPE html>
<html>
  <head>
    <title>Dashboard</title>
  </head>
  <body>
    <h1>mzooz bot</h1>

    <h2>البوت موجود بـ: {{guild_count}} سيرفرات</h2>
    <div class="picker">
      <h3>رجاءً اختر السيرفر للبدأ</h3>
      <hr />
      <section class="cards">
        {% for guild in guilds %}
        <div class="card">
          <a href="/dashboard/{{guild.id}}">
            {% if guild.icon_url is not none %}
            <img src="{{guild.icon_url}}" class="{{guild.class_color}}" />
            {% else %}
            <img
              src="https://discordapp.com/assets/322c936a8c8be1b803cd94861bdfa868.png"
              class="{{guild.class_color}}"
            />
            {% endif %}
          </a>
          <br />
          {{ guild.name }}
        </div>
        {% endfor %}
      </section>
    </div>
  </body>


<style>

body {
    background-color:cornflowerblue;
    background-size: 40%;
    color: #fff;
}

h1,
h2 {
  text-align: center;
  color:slateblue;
}

.picker {
  margin: 2em;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  background-color: #23272a;
  border-radius: 3px;
}

.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  justify-items: center;
}

.card {
  margin: 0.5em;
  display: grid;
  grid-template-rows: 1fr 0.2fr;
  justify-items: center;
}

.card:hover {
  box-shadow: rgba(2, 8, 20, 0.1) 0px 0.35em 1.175em,
    rgba(2, 8, 20, 0.08) 0px 0.175em 0.5em;
  transform: scale(1.1);
}

.card img {
  border-radius: 50%;
  width: 7em;
  height: 7em;
}

.green-border {
  border: 4px solid rgb(106, 255, 170);
}

.red-border {
  border: 4px solid rgb(255, 103, 90);
}


</style>

  </html>


'''


indexHtml = '''

<!DOCTYPE html>
<html>
  <head>
    <title>Home Page</title>
    <style>
      button {
        background-color: #4caf50; /* Green */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 12px;
      }
      button:hover {
        transform: scale(1.1);
        cursor: pointer;
      }
    </style>
  </head>
  <body>
    <h1>اهلا بك في لوحة القيادة</h1>
    <p align="center">
      {% if not authorized %}
      <a href="/login"><button>Login with discord</button></a>
      {% else %}
      <a href="/dashboard"><button>Open Dashboard</button></a>
      {%endif %}
      <a href="https://discord.gg/7gzWBSCbY6"><button>mzooz server</button></a>
      <a href="https://instagram.com/mzo0z"><button>coded by</button></a>
    </p>
  </body>

<style>

body {
  background-color: #23272a;
  background-size: 40%;
  color: #fff;
}

h1,
h2 {
  text-align: center;
}

.picker {
  margin: 2em;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  background-color: #23272a;
  border-radius: 3px;
}

.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  justify-items: center;
}

.card {
  margin: 0.5em;
  display: grid;
  grid-template-rows: 1fr 0.2fr;
  justify-items: center;
}

.card:hover {
  box-shadow: rgba(2, 8, 20, 0.1) 0px 0.35em 1.175em,
    rgba(2, 8, 20, 0.08) 0px 0.175em 0.5em;
  transform: scale(1.1);
}

.card img {
  border-radius: 50%;
  width: 7em;
  height: 7em;
}

.green-border {
  border: 4px solid rgb(106, 255, 170);
}

.red-border {
  border: 4px solid rgb(255, 103, 90);
}

</style>

  </html>


'''
serverHtml = '''

<!DOCTYPE html>
<html>
  <head>
    <title>Dashboard</title>
  </head>
  <body>
    <h1>mzooz bot</h1>
    <div class="picker">
      <h2>الادارة</h2>
      <hr />
      <section class="cards">
        <div class="card">
          <a href="/serverStatusManagement" class="button">ادارة نظام بيانات السيرفر</a>
          <a href="/securityManagment/0/0/0/0/0" class="button">ادارة الحماية</a>
          <a href="/gamesManagment" class="button">ادارة الالعاب</a>
          <a href="/systemManagment" class="button">ادارة السيستم</a>
          <a href="/bot/0" class="button">ادارة البوت</a>
          <a href="/ticketsManagment" class="button">ادارة التيكت</a>
          <a href="/islam/0" class="button">ادارة نظام الاجر</a>
          <br />
        </div>
      </section>
    </div>
  </body>


<style>

h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}
.button{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}

.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}

.button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}

@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>
'''



moveTicketHtml = """


<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
	<meta charset="utf-8">
	<title> mzooz bot </title>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>
</head>

<body>
  <hr/>
    <h2>اختر التيكت المراد نقله</h2>
    <div class="picker">
      <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر التيكت المراد نقله">اختر التيكت المراد نقله</option>
              {% for ticket in tickets %}
              <option value={{ticket}}>{{ticket[:ticket.find("_")].replace("[SPACE]", ' ')}}</option>
              {% endfor %}
            </section>
            </select>
      </div>

      
      <hr/>
      <h2>اختر القناة المراد نقله اليها</h2>
      <div class="picker">
        <hr/>
          <div class="custom-select" style="width:100%;text-align: center;">
            <select>
              <section class="cards">
                <option value="اختر القناة المراد نقله اليها">اختر القناة المراد نقله اليها</option>
                {% for channel in channels %}
                <option value={{channel}}>{{channel}}</option>
                {% endfor %}
              </section>
            </select>
          </div>
          <button class="button" id="save" onclick="save()">نقل</button>
          <a href="/ticketsManagment" class="button" id="back" >العودة</a>

      </div>
    </body>


<script>


var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }

        h.click();

    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);

function save(){
  var selectedOption = document.querySelector('select').value;
  location.replace("/moveTicket/"+selectedOption+"/"+document.getElementsByClassName("select-selected")[1].innerHTML);
  };
</script>

<style>



.custom-select {
  position: relative;
  font-family: Arial;
}

.custom-select select {
  display: none; /*hide original SELECT element: */
}

.select-selected {
  background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
  position: absolute;
  content: "";
  top: 14px;
  right: 10px;
  width: 0;
  height: 0;
  border: 6px solid transparent;
  border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
  border-color: transparent transparent #fff transparent;
  top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
  color: #ffffff;
  padding: 8px 16px;
  border: 1px solid transparent;
  border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
  cursor: pointer;
}

/* Style items (options): */
.select-items {
  position: absolute;
  background-color: #3c5be3;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
  display: none;
}

.select-items div:hover, .same-as-selected {
  background-color: rgba(0, 0, 0, 0.1);
}


input {
  opacity:0;
  position:absolute;
  left:-99999px;
}
 
input:checked + label {
  order: 1;
  z-index:2;
  background: #5c59ff;
  border-top:none;
  position:relative;
  color: white;
}
 
input:checked + label:after {
  content:'';
  width: 0; 
 height: 0; 
 border-left: 5px solid transparent;
 border-right: 5px solid transparent;
 border-top: 5px solid white;
  position:absolute;
  right:10px;
  top:calc(50% - 2.5px);
  pointer-events:none;
  z-index:3;
}
 
input:checked + label:before {
  position:absolute;
  right:0;
  height: 40px;
  width: 40px;
  content: '';
  background: #050505;
}
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  justify-items: center;
}

.card {
  margin: 0.5em;
  display: grid;
  grid-template-rows: 1fr 0.2fr;
  justify-items: center;
}

.card:hover {
  box-shadow: rgba(2, 8, 20, 0.1) 0px 0.35em 1.175em,
    rgba(2, 8, 20, 0.08) 0px 0.175em 0.5em;
  transform: scale(1.1);
}

.card img {
  border-radius: 50%;
  width: 7em;
  height: 7em;
}

h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}


@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}

.button{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}


  .button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button[id="save"]{
  background-color: #4caf4f00;
      display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3ce344;
    border-radius: 10px;
}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}




@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>
"""

setCategoryHtml = """


<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
	<meta charset="utf-8">
	<title> mzooz bot </title>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>
</head>

<body>
  <hr/>
    <h2>اختر المجموعة المراد تعيينها</h2>
    <div class="picker">
      <hr/>
        <div class="custom-select" style="width:100%;text-align: center;">
          <select>
            <section class="cards">
              <option value="اختر المجموعة المراد تعيينها">اختر المجموعة المراد تعيينها</option>
              <option value="None">عدم تعيين مجموعة</option>
              {% for category in categorys %}
              <option value={{category}}>{{category}}</option>
              {% endfor %}
            </section>
            </select>
        </div>
        <button class="button" id="save" onclick="save()">تعيين</button>
        <a href="/ticketsManagment" class="button" id="back" >العودة</a>  
    </body>


<script>


var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
      var y, i, k, s, h, sl, yl;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      sl = s.length;
      h = this.parentNode.previousSibling;
      for (i = 0; i < sl; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }

        h.click();

    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);

function save(){
  var selectedOption = document.querySelector('select').value;
  location.replace("/createCategory/"+selectedOption);
  };
</script>

<style>



.custom-select {
  position: relative;
  font-family: Arial;
}

.custom-select select {
  display: none; /*hide original SELECT element: */
}

.select-selected {
  background-color: #171431;
}

/* Style the arrow inside the select element: */
.select-selected:after {
  position: absolute;
  content: "";
  top: 14px;
  right: 10px;
  width: 0;
  height: 0;
  border: 6px solid transparent;
  border-color: #fff transparent transparent transparent;
}

/* Point the arrow upwards when the select box is open (active): */
.select-selected.select-arrow-active:after {
  border-color: transparent transparent #fff transparent;
  top: 7px;
}

/* style the items (options), including the selected item: */
.select-items div,.select-selected {
  color: #ffffff;
  padding: 8px 16px;
  border: 1px solid transparent;
  border-color: transparent transparent rgba(0, 0, 0, 0.1) transparent;
  cursor: pointer;
}

/* Style items (options): */
.select-items {
  position: absolute;
  background-color: #3c5be3;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 99;
}

/* Hide the items when the select box is closed: */
.select-hide {
  display: none;
}

.select-items div:hover, .same-as-selected {
  background-color: rgba(0, 0, 0, 0.1);
}


input {
  opacity:0;
  position:absolute;
  left:-99999px;
}
 
input:checked + label {
  order: 1;
  z-index:2;
  background: #5c59ff;
  border-top:none;
  position:relative;
  color: white;
}
 
input:checked + label:after {
  content:'';
  width: 0; 
 height: 0; 
 border-left: 5px solid transparent;
 border-right: 5px solid transparent;
 border-top: 5px solid white;
  position:absolute;
  right:10px;
  top:calc(50% - 2.5px);
  pointer-events:none;
  z-index:3;
}
 
input:checked + label:before {
  position:absolute;
  right:0;
  height: 40px;
  width: 40px;
  content: '';
  background: #050505;
}
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  justify-items: center;
}

.card {
  margin: 0.5em;
  display: grid;
  grid-template-rows: 1fr 0.2fr;
  justify-items: center;
}

.card:hover {
  box-shadow: rgba(2, 8, 20, 0.1) 0px 0.35em 1.175em,
    rgba(2, 8, 20, 0.08) 0px 0.175em 0.5em;
  transform: scale(1.1);
}

.card img {
  border-radius: 50%;
  width: 7em;
  height: 7em;
}

h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}


@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}

.button{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3c67e3;
    border-radius: 10px;
}


  .button[id="back"]{
    display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #e33c3c;
    border-radius: 10px;
}

.button[id="save"]{
  background-color: #4caf4f00;
      display: inline-block;
    color: #fff;
    text-decoration: none;
    padding: 20px 50px;
    border: 3px solid 
    #3ce344;
    border-radius: 10px;
}

.button:hover{
    animation: pulsate 1s 
    ease-in-out;
}




@keyframes pulsate {
    0%{
        box-shadow: 
        0 0 25px #5ddcff,
        0 0 50px #4e00c2;
    }
}

</style>

  </html>
"""
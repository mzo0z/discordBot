import os
import assist

privateFiles  = assist.privateFiles + "web\\"
transcripts   = privateFiles + 'transcripts\\'
jsonFile      = assist.privateFiles + 'system\\ticket.json'

dashboard     = privateFiles + 'dashboard.html'
index         = privateFiles + 'index.html'
server        = privateFiles + 'server.html'
settings      = privateFiles + 'Settings.html'
ticket        = privateFiles + 'ticket.html'
transcript    = privateFiles + 'transcript.html'

transcripthtml = '''

<!DOCTYPE html>
<html>
  <head>
    <title>Dashboard</title>
  </head>
  <body>
    <h1>mzooz bot</h1>
    <div class="picker">
      <h2>هذه جميع النسخ المحفوظة</h2>
      <h3>ملحوظة: اسم النسخة هو اسم الروم الذي تم فتحه</h3>
      <hr />
      <section class="cards">
        {% for transcript in transcripts %}
        <div class="card">          
          <a href="/openTranscript/{{transcript}}"><button id="transcript">{{ transcript }}</button></a>
          <br />
        </div>
        {% endfor %}
      </section>
      <a href="/server"><button>العودة</button></a>
    </div>
  </body>


<style>

body {
    background-color:cornflowerblue;
    background-size: 40%;
    color: #fff;
}

h1 {
  text-align: center;
  color:slateblue;
}

h2 {
  text-align: center;
  color:rgb(90, 205, 90);
}

.picker {
  margin: 2em;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  background-color: #23272a;
  border-radius: 3px;
}

.picker button{
		border: 0;
	background: none;
	display: block;
	margin: 20px auto;
	text-align: center;
	border: 2px solid #2ecc71;
	padding: 14px 40px;
	outline: none;
	color: white;
	border-radius: 24px;
	transform: 0.25s;
	cursor: pointer;
}

.picker button[id="transcript"]{
		border: 0;
	background: none;
	display: block;
	margin: 20px auto;
	text-align: center;
	border: 2px solid #2e31cc;
	padding: 14px 40px;
	outline: none;
	color: white;
	border-radius: 24px;
	transform: 0.25s;
	cursor: pointer;
}

.picker button[id="transcript"]:hover{
	background: #2e31cc;
}


.picker button:focus{
box-shadow: rgba(2, 8, 20, 0.1) 0px 0.35em 1.175em,
rgba(2, 8, 20, 0.08) 0px 0.175em 0.5em;
transform: scale(1.1);
}


.picker button:hover{
	background: #2ecc71;
}


.picker h3 {
  text-align: center;
  padding-top: 2%;
  font-family: Georgia, "Times New Roman", Times, serif;
  font-size: 1.5em;
}

.picker h3{
	color:tomato;
	text-transform: uppercase;
	font-weight: 500px;
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

dashboardhtml = '''
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


indexhtml = '''
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
serverhtml = '''
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
    <p align="center">
      <a href="/bot"><button>اعدادات البوت</button></a>
      <a href="/tickets"><button>حذف تيكت</button></a>
      <!--<a href="/transcripts"><button>رؤية النسخ</button></a> -->
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

settingshtml = '''
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
	<meta charset="utf-8">
	<title> mzooz bot </title>
</head>
<body>
    <form class="box" action="/update" method="POST">
        <h1>اعدادات البوت</h1>
        <h2>اذا في خيار ماتبي تعدله خله فاضي
            اذا تبي تطلع بدون لاتعدل شي , لاتكتب ولاشي واضغط تحديث</h2>

        <input type="text" name="prefix" placeholder="بادئة البوت"/>
        <input type="text" name="ownerId" placeholder="اي دي المالك"/>
        <input type="text" name="serverId" placeholder="اي دي السيرفر"/>
        <input type="submit" name="" value="تحديث" id="save"/>
    </form>

</body>
<style type="text/css">
body{
	margin: 0;
	padding: 0;
	font-family: sans-serif;
	background: #34495e;
}

.box{  margin: 0.5em;
  display: grid;
  grid-template-rows: 1fr 0.2fr;
  justify-items: center;
}

.box{
	width: 300px;
	padding: 40px;
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	background: #191919;
	text-align: center;
}
.box h1{
	color: white;
	text-transform: uppercase;
	font-weight: 500px;
}

.box h2{
	color:tomato;
	text-transform: uppercase;
	font-weight: 500px;
}


.box input[type = "text"],.box input[type = "password"]{
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
.box input[type = "text"]:focus,.box input[type = "password"]:focus{
	width: 280px;
	border-color: #2ecc71;
}
.box input[type = "submit"]{
		border: 0;
	background: none;
	display: block;
	margin: 20px auto;
	text-align: center;
	border: 2px solid #2ecc71;
	padding: 14px 40px;
	outline: none;
	color: white;
	border-radius: 24px;
	transform: 0.25s;
	cursor: pointer;
}

.box input[id = "back"]{
    border: 0;
	background: none;
	display: block;
	margin: 20px auto;
	text-align: center;
	border: 2px solid #cc2e2e;
	padding: 14px 40px;
	outline: none;
	color: white;
	border-radius: 24px;
	transform: 0.25s;
	cursor: pointer;
}



.box input[id = "save"]:focus{
box-shadow: rgba(2, 8, 20, 0.1) 0px 0.35em 1.175em,
rgba(2, 8, 20, 0.08) 0px 0.175em 0.5em;
transform: scale(1.1);
}


.box input[id = "save"]:hover{
	background: #2ecc71;
}




</style>
</html>'''

tickethtml = '''

<!DOCTYPE html>
<html>
  <head>
    <title>Dashboard</title>
  </head>
  <body>
    <h1>mzooz bot</h1>
    <div class="picker">
      <h2>اختر التيكت المراد حذفه</h2>
      <hr />
      <section class="cards">
        {% for ticket in tickets %}
        <div class="card">          
          <a href="/delete/{{ticket}}"><button id="ticket">{{ ticket[:ticket.find("_")] }}</button></a>
          <br />
        </div>
        {% endfor %}
      </section>
      <a href="/server"><button>العودة</button></a>
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

.picker button{
		border: 0;
	background: none;
	display: block;
	margin: 20px auto;
	text-align: center;
	border: 2px solid #2ecc71;
	padding: 14px 40px;
	outline: none;
	color: white;
	border-radius: 24px;
	transform: 0.25s;
	cursor: pointer;
}

.picker button[id="ticket"]{
		border: 0;
	background: none;
	display: block;
	margin: 20px auto;
	text-align: center;
	border: 2px solid #2e31cc;
	padding: 14px 40px;
	outline: none;
	color: white;
	border-radius: 24px;
	transform: 0.25s;
	cursor: pointer;
}

.picker button[id="ticket"]:hover{
	background: #2e31cc;
}


.picker button:focus{
box-shadow: rgba(2, 8, 20, 0.1) 0px 0.35em 1.175em,
rgba(2, 8, 20, 0.08) 0px 0.175em 0.5em;
transform: scale(1.1);
}


.picker button:hover{
	background: #2ecc71;
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

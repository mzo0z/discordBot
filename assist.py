import os
import mzo0z

LIT           = os.getcwd()  + '/'
privateFiles  = LIT          + "templates/"
web           = privateFiles + 'web/'
sstm          = privateFiles + "system/"
scrpt         = privateFiles + "transcript/"
logFile       = privateFiles + "Log/"
jsonFile      = privateFiles + 'system/data.json'
safejson      = privateFiles + 'system/security.json'
tickjson      = privateFiles + 'system/ticket.json'
gamesjson     = privateFiles + 'system/game.json'

dashboard     = privateFiles + 'web/dashboard.html'
index         = privateFiles + 'web/index.html'
server        = privateFiles + 'web/server.html'
settings      = privateFiles + 'web/Settings.html'
ticket        = privateFiles + 'web/ticket.html'

token = "[token]"
redurl = "[secret key]"
botId = 1234567890 #bot id




helpHtml = """


<!DOCTYPE html>
<html lang="ar">
  <head>
    <title>mzooz bot</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

  <header>
    <a href="https://instagram.com/mzo0z"><h3>insta</h3></a>
    <h3>coded by <a href="https://github.com/mzo0z">@mzo0z</a></h3>
    <a href="https://discord.gg/7gzWBSCbY6"><h3>discord</h3></a>
  </header>


  <section class="main">
    <div>
      <!--رسالة الى الملقوف الي يبي يقرا الكود, اذا كنت مبرمج لاتضحك ع الكود ترا بالغصب سويته وموراضي 
      يطلع الموقع كامل المهم ف بحثت وبحثت مالقيت ف قلت ماكو الا حل واحد واهو انسخ كود جاهز المهم
      بعد مانسخت الكود وعدلت عليه المشكلة ماراحت ف قلت مالها الا الذيب
      كودزلا المهم شفت مقطعه واهو يسوي له موقع ونسخت جم سطر منه المهم قال الـ سكشنز راح تفيد وصج 
      فادت بشكل جدا مفيد عالعموم مرة ثانية لاتتليقف ياقليل الادب  -->
    </div>
  </section>


  <section class="public">
    <div>
      <table id="customers">
        <tr>
          <th>الصلاحيات المطلوبة</th>
          <th>الاوامر العامة</th>
          <th>الشرح</th>
        </tr>
        <tr>
          <td>None</td>
          <td>ping - بنق</td>
          <td>تظهر لك سرعة الاتصال</td>
        </tr>
        <tr>
          <td>None</td>
          <td>roll - نرد</td>
          <td>رمي نرد</td>
        </tr>
        <tr>
          <td>None</td>
          <td>roles - رولات</td>
          <td>يظهر جميع الرولات في السيرفر</td>
        </tr>
        <tr>
          <td>None</td>
          <td>rooms - رومات</td>
          <td>يظهر جميع الرومات في السيرفر</td>
        </tr>
        <tr>
          <td>None</td>
          <td>server - سيرفر</td>
          <td>يظهر معلومات عن السيرفر</td>
        </tr>
        <tr>
          <td>None</td>
          <td>avatar - افتار</td>
          <td>يظهر افتارك او افتار الشخص الي بالمنشن</td>
        </tr>
        <tr>
          <td>None</td>
          <td>user - عضو</td>
          <td>يعطيك معلومات عنك او عن العضو الي بالمنشن</td>
        </tr>
        <tr>
          <td>None</td>
          <td>line - خط</td>
          <td>يرسل خط</td>
        </tr>
        <tr>
          <td>None</td>
          <td>meme - memes - ميم - ميمز</td>
          <td>يرسل ميمز</td>
        </tr>
        <tr>
          <td>None</td>
          <td>add_meme</td>
          <td>اذا كنت حاب تضيف ميمز تكتب هالامر ورابط الصورة</td>
        </tr>
        <tr>
          <td>None</td>
          <td>tax - ضريبة</td>
          <td>لحساب ضريبة البوت</td>
        </tr>
        <tr>
          <td>manage_event</td>
          <td>gstart - givaway - give - قيف</td>
          <td>لبدأ قيف اواي</td>
        </tr>
    </table>
  </div>
  </section>
  <section>
    <div>
      <table id="customers">
        <tr>
          <th>الصلاحيات المطلوبة</th>
          <th>الاوامر الادارية</th>
          <th>الشرح</th>
        </tr>
        <tr>
          <td>kick members</td>
          <td>{{kickCommands}}</td>
          <td>لطرد عضو</td>
        </tr>
        <tr>
          <td>ban members</td>
          <td>{{banCommands}}</td>
          <td>لتبنيد عضو</td>
        </tr>
        <tr>
          <td>ban members</td>
          <td>{{unBanCommands}}</td>
          <td>لفك تبنيد عضو</td>
        </tr>
        <tr>
          <td>manage messages</td>
          <td>{{clearCommands}}</td>
          <td>مادري شلون اشرحها بس يسوي كلير حق القناة</td>
        </tr>
        <tr>
          <td>manage roles</td>
          <td>{{rolesCommands}}</td>
          <td>لإعطاء عضو رتبة</td>
        </tr>
        <tr>
          <td>manage roles</td>
          <td>{{unRolesCommands}}</td>
          <td>لإزالة رتبة من عضو</td>
        </tr>
        <tr>
          <td>manage channels</td>
          <td>{{lockCommands}}</td>
          <td>لقفل قناة</td>
        </tr>
        <tr>
          <td>manage channels</td>
          <td>{{unLockCommands}}</td>
          <td>لفك قفل قناة</td>
        </tr>
        <tr>
          <td>manage roles</td>
          <td>{{muteCommands}}</td>
          <td>لإعطاء عضو ميوت</td>
        </tr>
        <tr>
          <td>manage roles</td>
          <td>{{unMuteCommands}}</td>
          <td>لإزالة الميوت من عضو</td>
        </tr>
      </table>
      </div>
      </section>

    <section>
      <div>
      <table id="customers">
        <tr>
          <th>اللعبة</th>
          <th>اوامر الالعاب</th>
          <th>الشرح</th>
        </tr>
        <tr>
          <td>لعبة الاسألة</td>
          <td>q - ask - س - سؤال</td>
          <td>لعبة اسألة وتغذية المخ</td>
        </tr>
        <tr>
          <td>لعبة الاعلام</td>
          <td>flag - اعلام - علم</td>
          <td>يرسل علم دولة ولازم تعرق اسم الدولة</td>
        </tr>
        <tr>
          <td>لعبة رتب</td>
          <td>sort - رتب</td>
          <td>يرسل كلمة غير مرتبة ولازم ترتبها</td>
        </tr>
        <tr>
          <td>لعبة ماهي الكلمة</td>
          <td>word - كلمة - w</td>
          <td>يرسل كلمة ناقص منها حروف ولازم تعرف الكلمة</td>
        </tr>
        <tr>
          <td>لعبة اعكس</td>
          <td>reverse - r عكس - اعكس - ع</td>
          <td>يرسل كلمة معكوسه ولازم تكتبها بشكل صحيح</td>
        </tr>
      </table>
      </div>
      </section>
  </body>

<style>

*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  scroll-behavior: smooth;
}

h1{
  text-align: center;
  color:#3c67e3;
}
h2 {
  text-align: center;
  color:#3ccfe3;
}

body{
    font-family: 'Poppins', sans-serif;
    background-color: #212534;
    display: grid;
    place-content: center;
    height: 100vh;
}

h3{
  color: #3c67e3;
}

a {
  color: #3c67e3;
  text-decoration: none;
}

#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
  color: rgb(164, 184, 53);
  background-color: #212534;

}

#customers tr:nth-child(even){
  background-color: #212534;
}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #256aa3;
  color: #4b25a3;
}

header{
  background-color: #2f3136;
  width: 100%;
  position: fixed;
  z-index: 999;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  padding: 10px 200px;


}

.main{
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

</style>

  </html>
"""



mzo0zServer = 'https://discord.gg/3psKD4pH4G'

def setupCommand(prefix):
    return f"""
-------------- set up bot --------------
{prefix}setqran لتعيين هذا الروم على انه روم الادعيه
{prefix}setgames لإعطاء هذا الروم صلاحية تشغيل الالعاب
{prefix}setsug لإضافة هذا الروم الى رومات الاقتراحات
{prefix}setsupport لجعل هذا الروم هو روم الدعم الفني
{prefix}setlog لجعل هذا الروم هو روم اللوق 
{prefix}setprefix بادئة البوت
{prefix}unsetsug لإزالة صلاحية الاقتراحات من هذالروم
{prefix}unsetgames لإزالة صلاحية تشغيل الالعاب من هذالروم

-------------- اذا تبي البوت يطرد الشخص اذا مافعل نقسه --------------
{prefix}setActiveRole منشن رتبة التفعيل الي لازم تكون عند الشخص عشان لاينطرد
{prefix}roleOn عشان تشغل الميزة
{prefix}roleOff عشان تطفي الميزة
(اذا فعلتها لازم تضيف الرتبة ولا ماراح تشتغل)
    """



def gamesHelp(prefix):
    return f'''```css
▣════["الالعاب"]════▣
[اسألة]
['{prefix}س & {prefix}q']
[اعلام]
['{prefix}اعلام {prefix}flag']
[رتب]
['{prefix}رتب {prefix}sort']
[ماهي الكلمة]
['{prefix}كلمة & {prefix}word']
[اعكس]
['{prefix}ع & {prefix}r']
[xo]
['{prefix}xo']
```'''
#soon
#[ترجم]
#['{prefix}ترجم']
#####

def publicHelpCommands(prefix):
    return f"""```css
#=<<"الاوامر العامة">>=#
▣══════["النظام"]══════▣
╠═[{prefix}ping]
╠═[{prefix}roll]
╠═[{prefix}roles]
╠═[{prefix}rooms]
╠═[{prefix}server]
╠═[{prefix}avatar]
╠═[{prefix}user]
╠═[{prefix}line]
╠═[{prefix}memes]
╠═[{prefix}add_meme]
╠═[{prefix}tax]
╚═[{prefix}gstart]
```
"""
def adminsHelpCommand(prefix):
    return f"""```css
#=<<"الاوامر الادارية">>=#
▣══════["النظام"]══════▣
╠═[{prefix}kick]
╠═[{prefix}ban]
╠═[{prefix}unban]
╠═[{prefix}clear]
╠═[{prefix}mute]
╠═[{prefix}unmute]
╠═[{prefix}role]
╠═[{prefix}unrole]
╠═[{prefix}lock]
┗═[{prefix}unlock]```"""


def publicHelp(prefix):
    return f"""```css
▣══════["البوت"]══════▣
["الصفحة"][الشرح]
["1"]═[تعليمات]
["2"]═[الاوامر العامة]
["3"]═[الاوامر الادرية]
["4"]═[الالعاب]
["بادئة البوت"]═[{prefix}]```"""



class embedColors:
    default = 0
    teal = 0x1abc9c
    dark_teal = 0x11806a
    green = 0x2ecc71
    ligh_green = 0x44ff44
    dark_green = 0x1f8b4c
    blue = 0x3498db
    dark_blue = 0x206694
    purple = 0x9b59b6
    dark_purple = 0x71368a
    magenta = 0xe91e63
    dark_magenta = 0xad1457
    yellow = 0xffd000
    gold = 0xf1c40f
    dark_gold = 0xc27c0e
    orange = 0xe67e22
    dark_orange = 0xa84300
    light_orange = 0xff6600
    light_red = 0xe74c3c
    dark_red = 0x992d22
    red = 0x990000
    lighter_grey = 0x95a5a6
    dark_grey = 0x607d8b
    light_grey = 0x979c9f
    darker_grey = 0x546e7a
    blurple = 0x7289da
    greyple = 0x99aab5


class colors():
    def coloring(msg, color):
        black=f'\033[30m{msg}\033[0;0m'
        red=f'\033[31m{msg}\033[0;0m'
        green=f'\033[32m{msg}\033[0;0m'
        orange=f'\033[33m{msg}\033[0;0m'
        blue=f'\033[34m{msg}\033[0;0m'
        purple=f'\033[35m{msg}\033[0;0m'
        cyan=f'\033[36m{msg}\033[0;0m'
        lightgrey=f'\033[37m{msg}\033[0;0m'
        darkgrey=f'\033[90m{msg}\033[0;0m'
        lightred=f'\033[91m{msg}\033[0;0m'
        lightgreen=f'\033[92m{msg}\033[0;0m'
        yellow=f'\033[93m{msg}\033[0;0m'
        lightblue=f'\033[94m{msg}\033[0;0m'
        pink=f'\033[95m{msg}\033[0;0m'
        lightcyan=f'\033[96m{msg}\033[0;0m'
        toReturn = {
            'black'      : black,
            'red'        : red,
            'green'      : green,
            'orange'     : orange,
            'blue'       : blue,
            'cyan'       : cyan,
            'purple'     : purple,
            'lightgrey'  : lightgrey,
            'darkgrey'   : darkgrey,
            'lightred'   : lightred,
            'lightgreen' : lightgreen,
            'yellow'     : yellow,
            'lightblue'  :lightblue,
            'pink'       :pink,
            'lightcyan'  :lightcyan}
        return toReturn[color]



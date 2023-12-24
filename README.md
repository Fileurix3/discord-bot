<h1>Discord bot</h1>

<h4>python version - 3.12</h4>
<h4>sqlite3</h4>
<h4>using the discord.py library</h4>
<h2>about</h2>
Discord bot for issuing roles by user level:
<ul>
    <li>0 level</li>
    <li>10 level</li>
    <li>50 level</li>
    <li>100 level</li>
    <li>200 level</li>
    <li>500 level</li>
    <li>1000 level</li>
    </ul>
Level is given for activity in chat, one message 0.05 levels, the amount of level received can be changed in the level_message variable

<h3>bot command</h3>
<li><b>commands that can only be used by an administrator</b></li>
<ul type = "circle">
    <li>!add @user 0 - adds the specified number of levels</li>
    <li>!reduce @user 0 - takes a specified number of levels</li>
    <li>!change @user 0 - sets the level to the user</li>
    <li>!clear - clearing chat</li>
</ul>
<li><b>commands that everyone can use</b></li>
<ul type = "circle">
    <li>!level @user - shows user level</li>
    <li>!leaderboard - shows the top 10 users by level</li>
</ul>

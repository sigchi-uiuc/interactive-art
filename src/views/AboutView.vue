<template>
  <div class="wrapper">
  <div class="nav-bar">
            <div class="logo-container">
                <img :src="require('@/assets/icons/eyes.png')" class="logo">
                <h1>
                    Melodic Eyes
                </h1>
            </div>
            <button class="learn-button" @:click="this.$router.push('/')">
                Try Now
            </button>
  </div>
  <hr class="divider">

<div class="about">
    <div class="info-1">
        <h1>About SIGCHI @ UIUC</h1>
        <p> SIGCHI@UIUC is a Special Interest Group focused on Computer-Human Interaction within ACM (Association of Computing Machinery) at the University of Illinois at Urbana-Champaign. In weekly meetings, we learn about real-world examples of computer-human interaction in current technology, engage in discussions, and work on our main project for the year: Melodic Eyes. </p>
        <br>
    </div>

    <div class="border"></div>

    <div class="info-2">
        <img src="../assets/iart_demo.gif" alt="Art Demo">
        <div class="info-sub">
            <h1> About 'Melodic Eyes' </h1>
            <p> Experience art and music in a whole new way!  With 'Melodic Eyes', you can look at historic art pieces in a completely new light - or should we say, sound.  Using an eye tracker and an image-to-music algorithm, you control the music in this modern art exhibit! </p>
            <p> At its core, Melodic Eyes is a tool that produces sound/music from an art piece, depending on where a person is looking at the artwork. This project takes in user-interactive input via an eye tracker, uses the input to determine the portion of the image being looked at, and matches the average color of that area to a specific sound. </p>
            <p>To accomplish this, our SIG was divided into 2 sub-teams: UI and Infra. The UI team created this website and the logic behind the image-to-music algorithm.  The Infra team created a physical exhibit for Melodic Eyes that combines a monitor, eyetracker, and soundbar in an art frame.</p>
            <!--<ul>
                <li>Eye tracker functionality</li>
                <li>User interface</li>
                <li>Infra</li>
                <li>Image-music conversion</li>
            </ul>-->
        </div>
        <br>
    </div>  

    <div class="border"></div>

    <div class="info-6">
        <div class="info-sub6">
            <h1> Engineering Open House </h1>
            <p> This project will be presented at the 2023 Engineering Open House (EOH) event at the University of Illinois at Urbana-Champaign. EOH takes place on March 31st and April 1st, with around 35,000 expected attendees. Click the 'EOH' link below to learn more!</p>
        </div>
        <img src="../assets/eoh_logo.png" alt="EOH Logo">
        <br>
    </div>

    <div class="border"></div>

    <div class="info-3">
        <h1>Links</h1>
        <div class="link"> 
            <div class="link1"> <div class="box"> <a href="https://acm.illinois.edu/"> ACM Website </a> </div> </div>
            <div class="link1"> <div class="box"> <a href="https://eohillinois.org/?utm_source=Google&utm_medium=Search&utm_campaign=EOH2023&gclid=CjwKCAjw_MqgBhAGEiwAnYOAeqjudnf1At9Ix4WJLyQj9p0yqzHRJVjDwXPbQkXoUjSJ2IBR4xf7jhoCZ-MQAvD_BwE"> EOH 2023 Website </a> </div> </div>
            <div class="link1"> <div class="box"> <a href="https://discord.gg/XRShsPCAQ3"> SIGCHI Discord </a> </div> </div>
        </div>
        <br>
    </div>
    
    <div class="border"></div>

    <div class="info-4">
        <h1>Members</h1>
        <h3> Project Lead </h3>
        <div class="leads"> 
            <div></div>
            <div class="lead1"> <div class="boxes"> Mitchell Bifeld </div> </div>
            <div></div>
        </div>
        <h3> UI Team </h3>
        <!-- <div class="ui"> -->
            <div class="members"> 
                <div class="lead1"> <div class="boxes"> Ethan Grinberg </div> </div>
                <div class="lead1"> <div class="boxes"> Aditi Shrivastava </div> </div>
                <div class="lead1"> <div class="boxes"> Karthik </div> </div>
            </div>
            <div class="members">
                <div class="lead1"> <div class="boxes"> Rohith </div> </div>
                <div class="lead1"> <div class="boxes"> Mari </div> </div>
                <div class="lead1"> <div class="boxes"> Will Schermer </div> </div>
            </div>
        <h3> Infrastructure Team </h3>
            <div class="members"> 
                <div class="lead1"> <div class="boxes"> Tyler Jurczyk </div> </div>
                <div class="lead1"> <div class="boxes"> Nathan Chung </div> </div>
            </div>
    </div>
  </div>
  <div class="info-5">
        <h4> Project designed by the SigCHI@UIUC 2023 team </h4>
    </div>
  </div>
</template>


<style scoped>

.wrapper {
    cursor: default;
}

template {
    margin: 0%;
    padding: 0%;
}

.desc {
    margin-top: 1%;
    opacity: 80%;
    font-size: 70%;
    font-family: 'Trebuchet MS', sans-serif;
}

h4 {
    margin: 0%;
    padding: 0%;
    opacity: 80%;
    font-size: 70%;
    padding-bottom: 0.8%;
}
.about {
    padding-bottom: 0%;
    font-family: 'Trebuchet MS', sans-serif;
}
.info-4 {
    padding-bottom: 4%;
}

.info-2 {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin-top: 3%;
    margin-bottom: 3%;
}

.info-6 {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 3%;
}

.info-6 img {
    width: 25%;
    height: 25%;
    border-radius: 10px;
    margin-left: 5%;
    margin-right: 5%;
    box-sizing: border-box;
    box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.4);
}

.info-sub6 {
    margin-left: 8%;
    text-align: right;
}

.info-1 {
    margin-top: 3%;
}

.info-sub {
    text-align: left;
    margin-right: 8%;
}


.info-2 img {
    width: 25%;
    height: 25%;
    border-radius: 10px;
    margin-left: 5%;
    margin-right: 5%;
    box-sizing: border-box;
    box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.4);
}

.info-1 {
    margin-left: 5%;
    margin-right: 5%;
}

.info-5 {
    margin: 0%;
    padding: 0%;
    width: 100%;
}
.nav-bar {
        display: flex;  
        align-items: center;
        justify-content: space-between;
    }

    .logo-container {
        display: flex;
        align-items: center;
        margin-left: var(--dl-space-space-unit);
        order: 1;
    }

    .logo {
        width: 100px;
        height: 100px;
    }

    .learn-button {
        order: 2;
        margin-right: var(--dl-space-space-unit);

        background-color: rgba(50, 168, 80, 0.6);
        font-size: 16px;
        width: 120px;
        height: var(--dl-size-size-small);
        border-width: 3px;
        border-color: var(--dl-color-gray-500);
        border-radius: var(--dl-radius-radius-radius8);
        box-shadow: 0px 4px 2px 0px #595959;
        position: relative;
        cursor: pointer;
    }

    .learn-button:hover {
        background-color: white;
    }

    .divider {
        margin-left: var(--dl-space-space-unit);
        margin-right: var(--dl-space-space-unit);
    }

    .border {
        border-bottom: rgba(50, 168, 80, 0.6) 2px;
        border-bottom-style: solid;
        width: 10%;
        justify-items: center;
        position: absolute;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    .info-3 {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 2.5%;
        margin-top: 3%;
    }

    .link {
        display: flex;
        flex-wrap: wrap;
        width: 100%;
        justify-content: center;
    }

    .link1 {
        flex: 1 1 10%; /* Adjust this value to change the width of each link card */
        margin-left: 10%;
        margin-right: 10%;
        border: 0.8px solid rgba(50, 168, 80, 0.6);
        border-radius: 10px;
        box-sizing: border-box;
        box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.4);
        cursor: pointer;
    }

    .box {
        padding-left: 2%;
        padding-top: 10%;
        padding-right: 2%;
        padding-bottom: 10%;
    }

    .link1:hover .box {
        box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.6);
        background-color: rgba(50, 168, 80, 0.6);
        border-radius: 10px;
    }

    .link1:hover .box a {
        color: white;
    }

    .link1 a {
        color: black;
        text-decoration: none;
    }

    .info-4 {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 3%;
    }

    .leads {
        display: flex;
        flex-wrap: wrap;
        width: 100%;
        justify-content: center;
        margin-top: 1%;
    }

    .members {
        margin-top: 2.5%;
        display: flex;
        flex-wrap: wrap;
        width: 100%;
        justify-content: center;
        margin-top: 1.5%;
    }

    .members:last-child {
        margin-top: 1.2%;
    }


    .boxes {
        padding-left: 2%;
        padding-top: 5%;
        padding-right: 2%;
        padding-bottom: 5%;
        font-size: 105%;
        font-family: 'Trebuchet MS', sans-serif;
    }

    .lead1 {
        flex: 1 1 8%; /* Adjust this value to change the width of each link card */
        border: 0.8px solid rgba(50, 168, 80, 0.6);
        border-radius: 10px;
        box-sizing: border-box;
        box-shadow: 0px 5px 6px rgba(0, 0, 0, 0.4);
        margin-left: 5%;
        margin-right: 5%;
        margin-bottom: 2%;
        max-width: 300px;
        
    }

</style>
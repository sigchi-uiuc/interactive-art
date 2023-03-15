<template>
  <div class="nav-bar">
            <div class="logo-container">
                <img :src="require('@/assets/icons/eyes.png')" class="logo">
                <h1>
                    Melodic Eyes
                </h1>
            </div>
            <button class="learn-button" @:click="this.$router.push('/')">
                Home Page
            </button>
  </div>
  <hr class="divider">

<div class="about">
    <h1>About SIGCHI</h1>
    <p> SIGCHI is a Special Interest Group within ACM (Association of Computing Machinery), which focuses on Computer-Human Interaction. In weekly meetings (Tuesdays at 6pm), we learn about real-world examples of computer-human interaction in current technology, and then engage in discussions and work on our main project for this year: a tool that produces sound/music from an art/picture, depending on where a person is looking at the artwork. </p>
    <br>

    <h1>Details About This Project </h1>
    <p> This project takes in human-interactive input via an eye tracker, uses the input to select an area of an image, and matches the average color of that area to a specific sound. To accomplish this, our SIG was divided into 4 sub-teams: one dedicated for the eye tracker functionality, one for the user interface, one for infra, and one for image-music conversion.</p>
    <br>

    <h1>Links</h1>
    <p> ACM Website: https://acm.illinois.edu/ </p>
    <p> SIGCHI Website: https://sigchi.acm.illinois.edu/ </p>
    <br>
    
    <h1> Info About Members</h1>
    <p>Lead: Abhimanyu Thosar, Mitchell Bifeld, Swathi Ram, Jeffrey Tsai</p>
    <p>UI Team: Aditi, Will, Rohith, Karthik, Mari, Ethan, Mitchell</p>
  </div>
</template>


<style scoped>

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
    }

    .divider {
        margin-left: var(--dl-space-space-unit);
        margin-right: var(--dl-space-space-unit);
    }
</style>
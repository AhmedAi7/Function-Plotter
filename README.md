<!-- PROJECT LOGO -->
<br />
<p align="center">
  
  <h2 align="center">Function-Plotter</h2>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
     <a href="#general-overview">General Overview</a>
    </li>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-architecture">Project Architecture</a></li>
        <li><a href="#apis-main-function">APIs Main function</a></li>
      </ul>
    </li>
    <li>
      <a href="#testing-screenshots">Testing Screenshots</a>
      <ul>
        <li><a href="#working-examples">Working Examples</a></li>
        <li><a href="#some-error-messages-for-any-not-vaild-input">Error Messages</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- GENERAL OVERVIEW -->
## General Overview
Simple GUI APP for Function Plotter using Python

<!-- ABOUT THE PROJECT -->
## About The Project

### Project Architecture
The project contains of main components:
* mainApplication: The main GUI Form which used to interact with the Application
* Parser: To validate user input and parse function equations
* graphPlotter : Plot a given equation using matplotlib.pyplot and numpy libraries 

### APIs Main Function
User enter the function equation, Minimum integer value for X and Maximum integer value of X, Application validate the inputs and then plot the function.
Equation should be a function of X only and separated by operators supported: + - / * ^ .
Min and Max X must be an integer number.

<!-- TESTING SCREENSHOTS -->
## Testing Screenshots


### Working Examples
![image](https://user-images.githubusercontent.com/36490859/145711837-968bbc7c-8b8c-4f99-94ea-c66aa14559d3.png)

![image](https://user-images.githubusercontent.com/36490859/145711843-7b45031d-ee3f-4075-a7b6-0feaac2d0c81.png)

![image](https://user-images.githubusercontent.com/36490859/145711849-eec84965-8762-41e9-b007-592436de675e.png)

![image](https://user-images.githubusercontent.com/36490859/145711853-63498660-737e-41a0-9a8c-3bc4d3b777f3.png)

#### Some Error Messages for any not vaild input
![image](https://user-images.githubusercontent.com/36490859/145711920-c289fa19-76d8-4acb-ae22-5d4e92874dcb.png)

![image](https://user-images.githubusercontent.com/36490859/145711869-5c30ba86-d839-49bc-b85c-14cb2bbb3ce2.png)

![image](https://user-images.githubusercontent.com/36490859/145711928-c0bca80d-6474-4feb-b935-a2265e1fd019.png)



<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/jacohein/Harmony">
    <img src="static/images/music.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Harmony</h3>

  <p align="center">
    Harmony is a real-time musical companion app that enriches musical experiences by allowing musicians to share active notes and learn from one another as they play. Our application revolves around the use of a Raspberry Pi, which serves as the driver of a 
    musical session. The Raspberry Pi is responsible for processing a stream of audio MIDI data output from a musical instrument, played by a host user—a musician whose device is connected directly to the Pi. As the Pi begins receiving MIDI data, it will 
    transmit notes across a web socket to a group of musicians. The musicians can use the received information to better inform their own playing, and harmonize with the group. Understanding the notes being played during a music session, can aid collaborative 
    play, and allow a musician to understand notes, melody, keys, and more.
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/jacohein/Harmony/issues">Report Bug</a>
    ·
    <a href="https://github.com/jacohein/Harmony/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#running">Getting to run</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The development of Harmony has been guided by our group's love for music and a commitment to creating an educational, user-friendly, platform. Accompanying this passion are years of trial and error in learning instruments. This is why Harmony was created—to offer an explorative tool for musicians. Throughout Harmony’s development, we always had the beginner musician in mind due to our own experiences learning instruments. One of the major difficulties for a beginner musician when learning to play is understanding the interface of an instrument. For example, a piano has 88 keys, and each key is distinguished by its position on a piano, and its color—black or white. The interesting part of a piano is that there are repeated octaves up and down the instrument. This means that the core of noteplaying is simpler than the interface suggests. How can a musician learn to understand the keys in front of them? Our focus was on addressing this fundamental question by translating the instrument's interface into a more intuitive format for humans: characters, or in the musical context, notes. If we were able to translate and display the notes a musician had been playing in real-time, we would be able to relay that information to them in a form they could understand, and subsequently to others they play with. This would not only give musicians the capability to know which notes they were playing, but allow them the language to articulate their musical expressions. This could mean explaining to a musical teacher what they played, or even hearing a chord, and demoing notes pressed, until they matched their desired output.
 <br />
 `jacohein`, `Harmony`, `jacob-heinrich149`, `jacobheinrich45@gmail.com`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
* [![Flask][flask]][Flask-url]
* [![Python][python]][Python-url]
* [![Javascript][javascript]][Javascript-url]
* [![Rtmidi][rtmidi]][Rtmidi-url]
* [![HTML][html]][HTML-url]
* [![CSS][css]][CSS-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
<ul>
  <li>MIDI Keyboard</li>
  <li>MIDI cable to connect keyboard</li>
</ul>

### Running


1. Clone the repo
   ```sh
   git clone https://github.com/jacohein/Harmony.git
   ```
2. Install Python packages
   ```sh
   pip install
   ```
3. Connect MIDI device
4. Get IPV4 local address in terminal
   ```sh
   ipconfig /all
   ```
5. Run server
   ```sh
   cd /directory
   python app.py
   ```
6. Connect to web socket through IPV4 address
   ```sh
   http://...
   ```
   

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Create private web rooms for musical play
- [ ] Add login functionality

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

Jacob Heinrich - jacobheinrich45@gmail.com

Project Link: [https://github.com/jacohein/Harmony](https://github.com/jacohein/Harmony)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[flask]: https://img.shields.io/badge/Flask-blue
[javascript]: https://img.shields.io/badge/Javascript-white
[html]: https://img.shields.io/badge/HTML-green
[css]: https://img.shields.io/badge/CSS-purple
[python]: https://img.shields.io/badge/Python-orange
[rtmidi]: https://img.shields.io/badge/Rtmidi-pink

[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[Javascript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[Python-url]: https://www.python.org/
[HTML-url]: https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics
[CSS-url]: https://developer.mozilla.org/en-US/docs/Web/CSS
[Rtmidi-url]: https://pypi.org/project/python-rtmidi/

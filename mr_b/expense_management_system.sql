{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
  <title>{{title}}</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="{% static 'index/animate.css' %}">
  <link rel="stylesheet" href="{% static 'index/flexslider.css' %}">
  <link rel="stylesheet" href="{% static 'index/fontstyle.css' %}">
  <link rel="stylesheet" href="{% static 'index/bootstrap.css' %}">
  <link rel="stylesheet" href="{% static 'index/stuff.css' %}">
  <link rel="stylesheet" href="{% static 'index/style.css' %}">
  <link rel="stylesheet" href="{% static 'index/slider.css' %}">
  <link href="https://fonts.googleapis.com/css?family=Nunito+Sans:200,300,400,700" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="shortcut icon" href="#">
</head>
<!--<div class="scrollbar" id="style-1">-->
<!--      <div class="force-overflow"></div>-->
<!--</div>-->
<body data-spy="scroll" data-target="#pb-navbar" data-offset="200">

  <div class="cursor"></div>
  <div class="cursor cursor2"></div>
  <nav class="navbar navbar-expand-lg site-navbar navbar-light bg-light" id="pb-navbar">
    <div class="container">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExample09"
        aria-controls="navbarsExample09" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-md-center" id="navbarsExample09">
        <ul class="navbar-nav">
          <li class="nav-item"><a class="nav-link" href="#section-home">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="#section-portfolio">My Apps</a></li>
          <li class="nav-item"><a class="nav-link" href="#section-resume">Resume</a></li>
          <li class="nav-item"><a class="nav-link" href="#section-about">About</a></li>
          <li class="nav-item"><a class="nav-link" href="#section-contact">Contact</a></li>
        </ul>
      </div>
    </div>
  </nav>
  <section class="site-hero" id="section-home">
    <div class="container">
      <div class="row intro-text align-items-center justify-content-left">
        <div class=" text-center pt-5">
          <h1 class="site-heading site-animate">Ola!! This is Mani SS<h1>
              <strong class="d-block text-white text-uppercase letter-spacing">and this is My Portfolio</strong>
        </div>
      </div>
    </div>
  </section>
  <section class="site-section " id="section-portfolio">
    <div class="container">
      <div class="row ">
        <div class="section-heading text-center ">
          <h2>My <strong>Apps</strong></h2>
        </div>
        <div class="row stuff">
          <div class="flip-card-container col-lg-4 " style="--hue: 220">
            <div class="flip-card">
              <div class="card-front">
                <figure>
                  <div class="img-bg"></div>
                  <div class="img-bg2"></div>
                  <div class="img-bg3"></div>
                  <div class="img-bg4"></div>
                  <div class="jumbotron">

                  </div>

                </figure>

              </div>

              <div class="card-back">
                <figure>
                  <div class="img-bg"></div>
                </figure>

                <ul>
                  <li> <button><a target="_blank" href="https://github.com/ManiSai18/Speaking-Lexicon">Speaking Lexicon</a></button></li>
                </ul>

                <div class="design-container">
                  <span class="design design--1"></span>
                  <span class="design design--2"></span>
                  <span class="design design--3"></span>
                  <span class="design design--4"></span>
                  <span class="design design--5"></span>
                  <span class="design design--6"></span>
                  <span class="design design--7"></span>
                  <span class="design design--8"></span>
                </div>
              </div>

            </div>
          </div>
          <div class="flip-card-container col-lg-4 " style="--hue: 170">
            <div class="flip-card">

              <div class="card-front">
                <figure>
                  <div class="img-bg"></div>
                  <div class="img-bg2"></div>
                  <div class="img-bg3"></div>
                  <div class="img-bg4"></div>
                  <div class="jumbotron">

                  </div>

                </figure>

              </div>

              <div class="card-back">
                <figure>
                  <div class="img-bg"></div>
                </figure>

                <ul>
                  <li> <button><a target="_blank" href="https://github.com/ManiSai18/Mr.Budget">Mr. Budget</a></button></li>
                </ul>

                <div class="design-container">
                  <span class="design design--1"></span>
                  <span class="design design--2"></span>
                  <span class="design design--3"></span>
                  <span class="design design--4"></span>
                  <span class="design design--5"></span>
                  <span class="design design--6"></span>
                  <span class="design design--7"></span>
                  <span class="design design--8"></span>
                </div>
              </div>

            </div>
          </div>

          <div class="flip-card-container col-lg-4 " style="--hue: 350">
            <div class="flip-card">

              <div class="card-front">
                <figure>
                  <div class="img-bg"></div>
                  <div class="img-bg2"></div>
                  <div class="img-bg3"></div>
                  <div class="img-bg4"></div>

                  <div class="jumbotron">

                  </div>

                </figure>

              </div>

              <div class="card-back">
                <figure>
                  <div class="img-bg"></div>
                </figure>

                <ul>
                  <li> <button><a target="_blank" href="https://manisai18.pythonanywhere.com/">My Portfolio</a></button></li>
                </ul>

                <div class="design-container">
                  <span class="design design--1"></span>
                  <span class="design design--2"></span>
                  <span class="design design--3"></span>
                  <span class="design design--4"></span>
                  <span class="design design--5"></span>
                  <span class="design design--6"></span>
                  <span class="design design--7"></span>
                  <span class="design design--8"></span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <section class="site-section " id="section-resume">
    <div class="container">
      <div class="row">
        <div class="section-heading text-center">
          <h2>My <strong>Resume</strong></h2>
        </div>
        <div class="carousel memo">
          {% for data1 in resume %}
          {% if data1.title == 'Masters' and data1.group == 'Education' %}
            <div class="carousel-item">
              <div class="carousel-box">
                <h2 style="color: #4bcef5;">{{ data1.title }}</h2>
                  <div class="info">
                    <p>Name       : {{ data1.Info.name }}</p>
                    <p>Course      : {{ data1.Info.Course }}</p>
                    <p>Location   : {{ data1.Info.loc }}</p>
                    <p>Estimated year of Passout  : {{ data1.Info.Passedout }}</p>
                    <p>Percentage/CGPA : {{ data1.Info.Percentage }}</p>
                  </div>
                <img src="{{ data1.image }}" />
              </div>
            </div>
            {% elif data1.group == 'Education' %}
            <div class="carousel-item">
              <div class="carousel-box">
                <h2 style="color: #4bcef5;">{{ data1.title }}</h2>
                  <div class="info">
                    <p>Name       : {{ data1.Info.name }}</p>
                    <p>Board      : {{ data1.Info.board }}</p>
                    <p>Location   : {{ data1.Info.loc }}</p>
                    <p>Passedout  : {{ data1.Info.Passedout }}</p>
                    <p>Percentage/CGPA : {{ data1.Info.Percentage }}</p>
                  </div>
                <img src="{{ data1.image }}" />
              </div>
            </div>
          {% elif data1.group == 'Experience' %}
            <div class="carousel-item">
              <div class="carousel-box">
                <h2 style="color: #4bcef5;">{{ data1.title }}</h2>
                  <div class="info2">
                    <p>MNC        : {{ data1.Info.name }}</p>
                    <p>Technology/Role : {{ data1.Info.tech }}</p>
                    <p>Period   : {{ data1.Info.period }}</p>
                    <p>Work  : {{ data1.Info.dev }}</p>
                  </div>
                <img src="{{ data1.image }}" />
              </div>
            </div>
          {% elif data1.group == 'Skills' %}
            <div class="carousel-item">
              <div class="carousel-box">
                <h2 style="color: #4bcef5;">{{ data1.title }}</h2>
                  <div class="info">
                    <p>Web Technologies        : {{ data1.Info.web }}</p>
                    <p>Web frame works : {{ data1.Info.webf }}</p>
                    <p>Languages : {{ data1.Info.lang }}</p>
                    <p>Technologies: {{ data1.Info.ot }}</p>
                    <p>Database: {{ data1.Info.db }}</p>
                  </div>
                <img src="{{ data1.image }}" />
              </div>
            </div>
          {% elif data1.group == 'Certification' %}
            <div class="carousel-item">
              <div class="carousel-box">
                <h2 style="color: #4bcef5;">{{ data1.title }}</h2>
                  <div class="info">
                    <p><b>*</b> {{ data1.Info.1 }}</p>
                    <p><b>*</b> {{ data1.Info.2}}</p>
                  </div>
                <img src="{{ data1.image }}" />
              </div>
            </div>
          {% elif data1.group == 'Intrst' %}
            <div class="carousel-item">
              <div class="carousel-box">
                <h2 style="color: #4bcef5;">{{ data1.title }}</h2>
                  <div class="info">
                    <b>*</b> {{ data1.Info.interests }}
                  </div>
                <img src="{{ data1.image }}" />
              </div>
            </div>
          {% endif %}

          {% endfor %}
        </div>
      </div>
    </div>
  </section>
  <section class="site-section" id="section-about">
    <div class="container abou">
      <div class="row mb-5 align-items-center">
        <div class="col-lg-5 pl-lg-5">
          <div class="section-heading">
            <h2>About <strong>Me</strong></h2>
          </div>
          <p class="lead">A Simple, Passionate, Blithe Smart-Worker </p>
          <p class="mb-5  ">Always be on hunger to chase down the unknown stuff. Master the challenges. Have an Elite Character</p>
        </div>
        <div class="col-lg-5 pr-lg-5 mb-5 mb-lg-0">
          <img src="{% static 'index/Msp.jpg' %}" alt="Image placeholder" class="img-fluid">
        </div>

      </div>
    </div>
  </section>
  <section class="site-section pb-0" id="section-services">
    <div class="container">
      <div class="row mb-4">
          <div class="section-heading text-center">
            <h2>My <strong>Projects</strong></h2>
          </div>
      </div>
      <div class="row">

  <div class="col-md-6 col-lg-4 text-center mb-5">
    <div class="site-service-item">
      <div class="card">
        <img src="https://uploads-ssl.webflow.com/5a9ee6416e90d20001b20038/62ee027b0c783a2ca5cbc0e5_Rectangle%201%20(38).svg" alt="Infosys" style="width:100%;">
      </div>
      <h3 class="mb-4">Infosys Experience</h3>
      <p>Joined Infosys in 2020, promoted to core development team within 5 months. Delivered SAP ABAP developments including reports, forms, enhancements, data dictionaries, IDOC handling, debugging, and client-specific implementations under tight delivery schedules.</p>
    </div>
  </div>

  <div class="col-md-6 col-lg-4 text-center mb-5">
    <div class="site-service-item">
      <div class="card">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1luWatPcWzDDmvi3JZJWZfWcpbFLPbWJpEA&usqp=CAU" alt="Mr. Budget" style="width:100%">
      </div>
      <h3 class="mb-4">Mr. Budget – Personal Finance Web App</h3>
      <p>Rebuilt a legacy budgeting app using Django & PostgreSQL. Implemented OTP-based secure login, multiple user plans, dynamic expense distribution, transactions tracking, and expense visualizations using Matplotlib & Seaborn libraries.</p>
    </div>
  </div>

  <div class="col-md-6 col-lg-4 text-center mb-5">
    <div class="site-service-item">
      <div class="card">
        <img src="https://media.gettyimages.com/id/1464751225/video/simulation-of-a-vehicles-rear-collision-with-a-truck.avif?s=640x640&k=20&c=Z96D50lUjAtRuUW-chiJAwe7uHdwokL7KgkRclIkEOs=" alt="Capstone" style="width:100%">
      </div>
      <h3 class="mb-4">Capstone – U.S Accident Data Analysis</h3>
      <p>Analyzed accident patterns, risk zones, and seasonal variations using Python, Regression models, and ANOVA. Delivered data-backed safety recommendations with interactive visualizations.</p>
    </div>
  </div>

</div>

    </div>
  </section>

  <section class="site-section" id="section-contact">
    <div class="container">
      <div class="row">
        <div class="section-heading text-center">
          <h2>My <strong>Contact</strong></h2>
        </div>
      </div>
      <div class="row">
        <ul class="site-contact-details">
          <li><span class="text-uppercase">Email</span> manisaisankarp@gmail.com</li>
          <li><span class="text-uppercase">Phone</span> +1 2676981836</li>
          <li><span class="text-uppercase">Present Address</span> Denton, Texas, United States</li>
        </ul>
      </div>
    </div>
  </section>
  <footer class="site-footer" style="margin-top: -10%;">
    <div class="container">
      <div class="row mb-5">
        <div class="col-md-12 text-center">
          <p>
            <a target="_blank" href="https://www.linkedin.com/in/mani-ss" class="social-item fa fa-linkedin"></a>
            <a target="_blank" href="https://www.instagram.com/the.mani.ss/" class="social-item fa fa-instagram"></a>
            <a target="_blank" href="mailto:  manisss180@gmail.com" class="social-item fa fa-google"></a>
            <a target="_blank" href="https://www.facebook.com/Mani.Sai.M.S.1/" class="social-item fa fa-facebook"></a>
          </p>
        </div>
      </div>
    </div>
  </footer>
  <script src="{% static 'index/jquery.min.js' %}"></script>
  <script src="{% static 'index/slider.js' %}"></script>
  <script src="{% static 'index/jquery-migrate-3.0.1.min.js' %}"></script>
  <script src="{% static 'index/popper.min.js' %}"></script>
  <script src="{% static 'index/bootstrap.min.js' %}"></script>
  <script src="{% static 'index/jquery.easing.1.3.js' %}"></script>
  <script src="{% static 'index/jquery.stellar.min.js' %}"></script>
  <script src="{% static 'index/jquery.waypoints.min.js' %}"></script>
  <script src="https://unpkg.com/isotope-layout@3/dist/isotope.pkgd.min.js"></script>
  <script src="https://unpkg.com/imagesloaded@4/imagesloaded.pkgd.min.js"></script>
  <script src="{% static 'index/custom.js' %}"></script>

</body>

</html>
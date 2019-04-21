<!DOCTYPE html>



<html lang="en" dir="ltr">
  <head>
    <meta name = "viewport" content = "width=device-width", initial-scale = 1.0">
    <title> Barcode Generator </title>
    <link rel="stylesheet" type = "text/css" href= "design.css">
  </head>
  <body>

    <div class = "container">
      <h1 id = "judul"> CHATBOT! </h1>
      <div id="wrap">
      
    </div>
      
    </div>

    <?php
      if(isset($_POST["submit"])){
      ?> 
        <h1> <?php print $_POST['input']; ?> </h1>
        <?php
      } else {
      }
    ?>

    <div class = "container2">
        <div id = "wrapper">
          <form  method = "post" action="" >
              <input type="text" name="output" placeholder ="Ketik pertanyaan..">
              <br>
              <input type="text" name="input" placeholder ="Ketik pertanyaan..">
              <br></br>
              <input type="submit" name = "submit" value="CHAT">
          </form> 
        </div>
  
    </div>

  </body>
</html>
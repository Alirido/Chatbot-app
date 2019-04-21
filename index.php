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

    <div class = "container4">
      <?php
        session_start() ;
        if(isset($_POST["submit"])){
          if ($_SESSION["msg"] != ""){
            $_SESSION["msg"] .=  "\n";
          }

          $_SESSION["msg"] .= "Anda: ".$_POST["input"];
          $in = $_POST["input"];
          $algo = $_POST["inputAlgo"];

          $hsl = shell_exec("C:\\Users\\arriendo\\AppData\\Local\\Programs\\Python\\Python37\\python.exe chat.py $algo ".escapeshellarg($in));

          $_SESSION["msg"] .= "\n Naruto: ".$hsl;

        } else {
          $_SESSION["msg"] = "" ;
        }
    
        $demo  = $_SESSION["msg"] == "" ? "Naruto: Selamat datang di Chatbot ini!" : $_SESSION["msg"];
        echo nl2br($demo);
      ?>
    </div>
    
    <div class = "container2">
        <div id = "wrapper">
          <form  method = "post" action="" >
              <input type="text" name="inputAlgo" placeholder ="Ketik Algo (KMP / BM / REGEX)">
              <br>
              <input type="text" name="input" placeholder ="Ketik pertanyaan..">
              <br></br>
              <input type="submit" name = "submit" value="CHAT">
          </form> 
        </div>
    </div>

  </body>
</html>
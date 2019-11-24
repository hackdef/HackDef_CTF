<?php
   error_reporting(0);
   include("config.php");
   session_start();
   
   if($_SERVER["REQUEST_METHOD"] == "POST") {
      
      $myusername = $_POST['username'];
      $mypassword = mysqli_real_escape_string($conn,$_POST['password']); 
      
      //$filter = array('union', 'or', 'load_file', 'from', 'where','substr','substring', 'select', 'ascii', 'and', 'like', 'rlike', 'database');
      $filter = array('substr','substring','and');

      foreach ($filter as $banned) {
         $myusername = preg_replace('/\b' . $banned . '\b/i', '[X]', $myusername);
      }
      if (strpos($myusername, '[X]') !== false){
         $error = $myusername;
         include('waf.html');
         die();
      }

      $sql = "SELECT * FROM users WHERE BINARY username = '$myusername' and password = '$mypassword'";
      $result = mysqli_query($conn,$sql);
      $row = mysqli_fetch_array($result,MYSQLI_ASSOC);
      $count = mysqli_num_rows($result);

      if($count > 0) {
         if($mypassword === $row['password']) {
            $_SESSION['login_user'] = $myusername;
            header("location: flag.html");
         }
      }else { 
         include('error.html');
         die();
      }
   }
?>
<!DOCTYPE html>
<html lang="es">
<!-- By @nogagmx -->
<head>
      <title>CaptureBANK</title>
      <meta charset="utf-8">
      <link rel="icon" href="img/logo.png">
      <link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet">
      <link rel="stylesheet" type="text/css" href="font-awesome-4.7.0/css/font-awesome.min.css">
      <link rel="stylesheet" href="css/styles.css">
      <meta name="viewport" content="width=device-width, initial-scale=1" />
</head>

<body>
<div class="main">
   <img src="img/logo1.png" align="middle">
   <form class="form2" action="" method="post">
         <input class="un" type="text" name="username" placeholder="Usuario" required="" autofocus=""/>
          <input class="pass" type="password" name="password" placeholder="Contraseña" required=""/>
          <button class="submit1" align="center">Ingresar</button>
   </form>
</div>
</body>
</html>

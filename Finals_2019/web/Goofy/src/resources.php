<?php
  include("config.php");
  session_start();
  error_reporting(0);
  function showPDF($url) {
      $ch = curl_init(); 
      curl_setopt($ch, CURLOPT_URL, $url);
      curl_setopt($ch, CURLOPT_RETURNTRANSFER,true);
      curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
      curl_setopt($ch, CURLOPT_TIMEOUT, 10); 
      curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, $timeout );
      curl_setopt($ch, CURLOPT_COOKIEJAR, $cookie);
      curl_setopt($ch, CURLOPT_COOKIEFILE, $cookie);
      curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Encoding: none','Content-Type: application/pdf')); 

      header('Content-type: application/pdf');
      $result = curl_exec($ch);
      curl_close($ch);
      echo $result;
  }

  if (!isset($_SESSION['login_user'])) {
    header('Location: index.html');
    exit();
  }
  $myusername = $_SESSION['login_user'];
  
	if(isset($_GET['url'])){ 
	$url = $_GET['url'];

  if ($url !== 'https://www.owasp.org/images/a/ae/Seguridad_en_entornos_financieros.pdf'){
     
     // Verificar si se ha ingresado 'localhost' o '127.0.0.1'
     $local_attack = '/(gopher|sftp|ftp|dict|http|https|ftp|ldap|tftp)?:\/\/(\blocalhost\b|\b127.0.0.1\b|\b127.1\b|\b127.0.1\b|\b0177.0.0.1\b|\b0\b)/';
     
     if (preg_match($local_attack, $url)){
          //Filtrar inputs
          $urlor = $url;
          $filter = array('127.0.0.1','file:\/\/','http:\/\/','dict:\/\/','sftp:\/\/','tftp:\/\/','ldap:\/\/','localhost','127.1', '127.0.1', '0177.0.0.1','ftp:\/\/','https:\/\/');
          foreach ($filter as $banned) {
              $url = preg_replace('/' . $banned . '/i', '[X]', $url);
          }
          //$local_attack_port2 = '/(gopher|sftp|ftp|dict|http|https|ftp|ldap|tftp)?:\/\/(\blocalhost\b|\b127.0.0.1\b|\b127.1\b|\b127.0.1\b|\b0177.0.0.1\b|\b0\b):(?:[0-9]+)$/';
          $local_attack_port = '/((?:))(?:[0-9]+)$/';
          preg_match($local_attack_port, $urlor, $port) ? $port[0] : 'no match';
          echo $port[1];
          if (strpos($url, '[X]') !== false){
            echo "Nope!". "\xA". "Se detectó el siguiente input : ";
            echo $url. "\xA";

          }
          if (preg_match($local_attack_port, $urlor)){
              echo "Hey hacker, lo que buscas está en alguno de los puertos en el rango 1500 -1515....¡Suerte!";
              if($port[0] == 1510){
                  showPDF($url);
              }else{
                  die();
              }
          } 
      }else{
          echo "Estimado usuario(a), No es posible incluir sitios o archivos externos. Por su comprensión, Gracias. El equipo de seguridad de CaptureBANK siempre en busca de proteger su información. Cualquier duda, comentario o aclaración favor de enviar un mail a: te_vamos_a_ignorar@capturebank.com.mx";
          die();
      }
  }else{
        showPDF($url);
    }
	}
?>
<!DOCTYPE html>
<html>
<head>
    <title>CaptureBANK</title>
    <meta charset="utf-8">
    <link rel="icon" href="img/logo.png">
    <link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" type="text/css" href="font-awesome-4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="css/style2.css">
</head>

<body>
<div class="topnav" id="myTopnav">
  <a href="profile.php"class="active">Mi Perfil</a>
  <a href="principal.php">Home</a>
  <a href="transfers.php">Transferencias</a>
  <a href="resources.php">Recursos Importantes</a>
  <a href="logout.php">Salir</a>
  <a href="javascript:void(0);" class="icon" onclick="myFunction()">
  <i class="fa fa-bars"></i>
  </a>
</div>

<div style="padding-left:16px">
  <h4 style="color:#ff0000;">Recursos importantes</h4>
  <ul>
  <a href="resources.php?url=https://www.owasp.org/images/a/ae/Seguridad_en_entornos_financieros.pdf" style="color:#ffffff;"><li>Consejos de Seguridad</li></a>
  <a href="#" style="color:#ffffff;"><li>Manual de Usuario</li></a>
  <a href="#" style="color:#ffffff;"><li>Comisiones</li></a>
  <a href="#" style="color:#ffffff;"><li>Tarjetas de Crédito</li></a>
  <a href="#" style="color:#ffffff;"><li>Préstamo para vivienda</li></a>
  <a href="#" style="color:#ffffff;"><li>Estrena tu auto</li></a>
</ul>
</div>

<script>
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}
</script>

<div class="footer">
  <p>CaptureBANK - Hackdef Finals 2019</p>
</div>
</body>
</html>

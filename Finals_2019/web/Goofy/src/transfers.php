<?php
  include("config.php");
  session_start();

  if (!isset($_SESSION['login_user'])) {
    header('Location: index.html');
    exit();
  }
  $myusername = $_SESSION['login_user'];
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
</div>
<div class="box">
  <br><br>
  <input class="un "name="cantidad" placeholder="Cantidad" required="" autofocus="" onkeypress="return isNumber(event)"/><br>
  <input class="un "name="tjorigen" placeholder="Cuenta / Tarjeta Origen" required="" autofocus="" onkeypress="return isNumberKey(this,event)"/><br>
  <input class="un "name="tjdestino" placeholder="Cuenta / Tarjeta Destino" required="" autofocus="" onkeypress="return isNumberKey(this,event)"/><br>
  <button class="submit" align="center">Transferir</button><br>
  <p class="text">Para transacciones mayores a $50,000.00<br>se requiere autorización del gerente.</p>
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

function isNumberKey(source,evt){
    var charCode = (evt.which) ? evt.which : evt.keyCode
    if (charCode > 31 && (charCode < 48 || charCode > 57)|| source.value.length === 16)
        return false;
    return true;
}
function isNumber(evt){
    var charCode = (evt.which) ? evt.which : evt.keyCode
    if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
    return true;
}
</script>

<div class="footer">
  <p>CaptureBANK - Hackdef Finals 2019</p>
</div>
</body>
</html>
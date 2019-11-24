<?php
include("config.php");
session_start();

if (!isset($_SESSION['login_user'])) {
	header('Location: login.php');
	exit();
}
$myusername = $_SESSION['login_user'];

$sql = "SELECT name, lastname, address, phone, age FROM users WHERE username = '$myusername'";
$result = mysqli_query($conn,$sql);
$row = mysqli_fetch_array($result,MYSQLI_ASSOC);

$sql2 = "SELECT cards.cardNum FROM users INNER JOIN cards ON users.userId = cards.userId WHERE users.username = '$myusername'";
$result2 = mysqli_query($conn,$sql2);
$array = array();
while($row2 = mysqli_fetch_assoc($result2)){
	$array[] = $row2;
}

$json = json_encode($array); 
$data=json_decode($json,true);
$cards="";

foreach($data as $key=>$v){ 
    $cards.=$data[$key]['cardNum'].", ";
}
$cards= trim($cards, ", ");
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
		<div class="content">
			<div>
				<h2>Información Personal</h2>
				<table>
					<tr>
						<td>Nombre Completo:</td>
						<td><?=$row["name"]?>&nbsp;<?=$row["lastname"]?></td>
					</tr>
					<tr>
						<td>Dirección:</td>
						<td><?=$row["address"]?></td>
					</tr>
					<tr>
						<td>Telefono:</td>
						<td><?=$row["phone"]?></td>
					</tr>
					<tr>
						<td>Edad:</td>
						<td><?=$row["age"]?></td>
					</tr>
					<tr>
						<td>Tarjetas Asociadas:</td>
						<td><?=$cards?></td>
					</tr>
				</table>
			</div>
		</div>
	<div class="footer">
  	<p>CaptureBANK - Hackdef Finals 2019</p>
	</div>
	</body>
</html>
<?php
   define('DB_SERVER', '172.18.0.2');
   define('DB_USERNAME', 'root');
   define('DB_PASSWORD', 'h4ckD3f_f1n4ls2olg');
   define('DB_DATABASE', 'CaptureBankHDF');
   $conn = mysqli_connect(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);

   if($conn === false){
    die("ERROR: Could not connect due to:  " . mysqli_connect_error());
   }
?>

<?php

class Download_Image {
    public $path;
    public $operation;
    function __wakeup() {
        $image_path=base64_decode($this->path);
        if(file_exists($image_path) && $this->operation == "Download") {
            header('Content-Description: File Transfer');
            header('Content-Type: image/jpeg');
            header('Content-Disposition: attachment; filename="'.basename($image_path).'"');
            header('Expires: 0');
            header('Cache-Control: must-revalidate');
            header('Pragma: public');
            header('Content-Length: ' . filesize($image_path));
            flush();
            readfile($image_path);
        } else {
        http_response_code(404);
        echo "<br>File not found!";
          }
    }
}

$obj_image=base64_decode($_POST['image_path']);
$get_image=unserialize($obj_image);
?>

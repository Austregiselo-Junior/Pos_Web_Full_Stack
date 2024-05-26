<?php

    require_once "vendor/autoload.php";

    use Mpdf\QrCode\QrCode;
    use Mpdf\QrCode\Output;
    
    $qrCode = new QrCode('MIQUEIAS - DEV');
    
    // Save black on white PNG image 100 px wide to filename.png. Colors are RGB arrays.
    $output = new Output\Png("mq.png");
    $data = $output->output($qrCode, 100, [255, 255, 255], [0, 0, 0]);
    file_put_contents('filename.png', $data);
    
    // Echo a SVG file, 100 px wide, black on white.
    // Colors can be specified in SVG-compatible formats
     $output = new Output\Svg();
     echo $output->output($qrCode, 100, 'white', 'black');
    
    // Echo an HTML table
    $output = new Output\Html();
    echo $output->output($qrCode);

?>
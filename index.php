<?php
    $command = escapeshellcmd('python F:\RK\Nextgenpixel\Mini-Project\odd.py');
    $output = shell_exec($command);
    echo $output;
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<a href="news.php">click me to run python via php</a>
</body>
</html>
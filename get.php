<?php
$str = 'Siapa nama koordas strategi algoritma?';
$algo = 'BM';
echo shell_exec("C:\\Users\\arriendo\\AppData\\Local\\Programs\\Python\\Python37\\python.exe chat.py $algo ".escapeshellarg($str));
?>
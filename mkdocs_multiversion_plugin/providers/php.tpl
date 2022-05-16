<?php
$list = scandir('.');
$dirs = array();
foreach ($list as $value){
    if ($value != '..' && $value != "." && !is_file($value)){
        $dirs[] = $value;
    }
}

usort($dirs, function($a, $b) {
    return version_compare($b, $a);
});

/*
{
  "stable":{
    "name":"stable",
    "latest":false
  },
  "1.1.0":{
    "name":"latest release (1.1.0)",
    "latest":trues
  },
  "1.0.0":{
    "name":"1.0.0",
    "latest":false
  }
}
*/

if (isset($_GET['version'])) {
    $versions = array();
    $latest = true;
    foreach ($dirs as $version) {
        $item = array();
        if ($latest) {
            $latest = false;
            $item['name'] = sprintf("{{ latest_version_name_format }}", $version);
        } else {
            $item['name'] = sprintf("{{ version_name_format }}", $version);
        }
        $item['latest'] = $latest;
        $versions[$version] = $item;
    }
    header('Content-Type: application/json');
    echo json_encode($versions);
} else if (count($dirs) > 0) {
    header('Location: ' . $dirs[0]);
} else {
    echo "404";
}
?>


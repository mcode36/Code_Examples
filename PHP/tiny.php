<?php

///// Database connection /////

  $host="localhost";
  $user="db_user";
  $pwd="Magic#!B11";
  $sys_dbname="test_db";

  $db_conn = mysqli_connect($host,$user,$pwd,$sys_dbname);
  // Check connection
  if (mysqli_connect_errno()) {
     echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }

  $page_root = "https://home.aviacomm.com/Avia_ERP/Vacation" ;
  $main_table = "cars" ;
?>

<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
    <ul>
    <li>
    <label for="F_brand">Brand</label>
    <input type="text" id="F_brand" name="F_brand">
    </li>
    <li>
    <label for="F_model">Model</label>
    <input type="text" id="F_model" name="F_model">
    </li>
    <li>
    <label for="F_year">Year</label>
    <input type="text" id="F_year" name="F_year">
    </li>
    </ul>
    <button type="submit">Submit</button>
  </form>
<hr>
<?php
  $main_table = 'cars';

  if ( $_SERVER['REQUEST_METHOD'] == 'POST') {
    $content['Brand'] = $_POST["F_brand"] ;
    $content['Model'] = $_POST["F_model"] ;
    $content['Year'] = $_POST["F_year"] ;

    echo ' <table border="1">' . "\n" ;
    foreach($content as $x_key => $x_value) {
      echo ' <tr>' . "\n" ;
      echo '   <td>' . $x_key . '</td><td>' . $x_value . '</td>' . "\n" ;
      echo ' </tr>' . "\n" ;
    }
    echo ' </table>' . "\n" ;

    // Insert to DB
    $sql ="insert into `" . $main_table . "` (`Brand`,`Model`,`Year`) values ('" ;
    $sql = $sql . $_POST["F_brand"] . "','" ;
    $sql = $sql . $_POST["F_model"] . "','" ;
    $sql = $sql . $_POST["F_year"]  . "')" ;

    if (!mysqli_query($db_conn,$sql)) {
      echo "Query String:" . $sql ;
      echo "<BR>";
      die('Error: ' . mysqli_error($db_conn));
    }
  }

  // Read back from DB
  $sql = "SELECT * FROM `" . $main_table . "` ORDER BY `ID` DESC" ;
  $result = mysqli_query($db_conn, $sql);
  if (!$result) {
    echo "Query String:" . $sql2 ;
    echo "<BR>";
    die('Error: ' . mysqli_error($db_conn));
 }

  echo ' <table border="1">' . "\n" ;
  while ($row = $result->fetch_assoc()) {
    echo ' <tr>' . "\n" ;
    echo '   <td>' . $row['ID'] . '</td>' . "\n" ;
    echo '   <td>' . $row['Brand'] . '</td>' . "\n" ;
    echo '   <td>' . $row['Model'] . '</td>' . "\n" ;
    echo '   <td>' . $row['Year'] . '</td>' . "\n" ;
    echo ' </tr>' . "\n" ;
  }
  echo ' </table>' . "\n" ;

?>
</body>
</html>

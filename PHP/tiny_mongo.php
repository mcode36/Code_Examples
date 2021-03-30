<?php
///// Database connection /////
  error_reporting(E_ALL & ~E_NOTICE);

  $mng = new MongoDB\Driver\Manager("mongodb://localhost:27017");
  $col = "test_db.cars" ;
  $bulk = new MongoDB\Driver\BulkWrite;
?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
  table, td {
    border: 1px solid grey;
    border-collapse: collapse;
  }
  </style>
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
  if ( $_SERVER['REQUEST_METHOD'] == 'POST') {
    $content['Brand'] = $_POST["F_brand"] ;
    $content['Model'] = $_POST["F_model"] ;
    $content['Year'] = $_POST["F_year"] ;

    // Verify form POST data
    echo ' <table border="1">' . "\n" ;
    foreach($content as $x_key => $x_value) {
      echo ' <tr>' . "\n" ;
      echo '   <td>' . $x_key . '</td><td>' . $x_value . '</td>' . "\n" ;
      echo ' </tr>' . "\n" ;
    }
    echo ' </table>' . "\n" ;

    // Insert to DB
    $doc = [
         'brand' => $content['Brand'],
         'model' => $content['Model'], 
         'year'  => $content['Year']
    ];
    $bulk->insert($doc);
    $result = $mng->executeBulkWrite($col, $bulk);
    echo "Number of record added: " . $result->getInsertedCount() . "<br>\n" ;
  }

  // Read back from DB
  $filter = [];
  $options = ['sort' => [ '_id' => -1]];
  $query = new MongoDB\Driver\Query($filter, $options);
  $rows = $mng->executeQuery($col, $query);

  echo ' <table>' . "\n" ;
  foreach ($rows as $row) {
    echo ' <tr>' . "\n" ;
    echo '   <td>' . $row->brand . '</td>' . "\n" ;
    echo '   <td>' . $row->model . '</td>' . "\n" ;
    echo '   <td>' . $row->year  . '</td>' . "\n" ;
    echo ' </tr>' . "\n" ;
  }
  echo ' </table>' . "\n" ;

?>
</body>
</html>

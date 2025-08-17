<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
       <h1>Fill up the form</h1>
       <form action="index.php" method="post">
        <input type="text" name="name" id="name" placeholder="Enter your name">
        <input type="email" name="email" id="email" placeholder="Enter your email">
        <input type="phone" name="phone" id="phone" placeholder="Enter your phone number">
        <button id="submit" type="submit">Submit</button>
       </form>
    </div>
    <script src="index.js"></script>
    <?php
        if(isset($_POST['name'])){
            $server="localhost";
            $username="root";
            $password="";
            
            $con=mysqli_connect($server, $username, $password);

            if(!$con) {
                die("failed" . mysqli_connect_error());
            }
            $name=$_POST['name'];
            $email=$_POST['email'];
            $phone=$_POST['phone'];
            $sql="INSERT INTO `form`.`form` (`name`, `email`, `phone`, `date`) VALUES ('$name', '$email', '$phone', current_timestamp());";

            if($con->query($sql)==false){
                echo "ERROR: $sql <br> $con->error";
            }
            
            $con->close();
        }
    ?>
</body>
</html>
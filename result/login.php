<?php
session_start();
$conn = new mysqli("localhost", "root", "praise1800", "student_results");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = hash('sha256', $_POST['password']);

    // Use a prepared statement
    $stmt = $conn->prepare("SELECT * FROM teachers WHERE username = ? AND password = ?");
    $stmt->bind_param("ss", $username, $password);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $_SESSION['teacher'] = $username;
        header("Location: upload.php");
        exit();
    } else {
        echo "<script>alert('Invalid Credentials');</script>";
    }

    $stmt->close();
    $conn->close();
}
?>
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="styles.css">
    <title>Teacher Login</title>
</head>
<body>
    <h2>Teacher Login</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
</body>
</html>
<?php
session_start();
if (!isset($_SESSION['teacher'])) {
    header("Location: login.php");
    exit();
}

$conn = new mysqli("localhost", "root", "", "student_results");

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES['result_pdf'])) {
    $student_id = $_POST['student_id'];
    $term = $_POST['term'];
    $file_name = $student_id . "_" . $term . ".pdf";
    $file_tmp = $_FILES['result_pdf']['tmp_name'];
    move_uploaded_file($file_tmp, "uploads/" . $file_name);

    $query = "INSERT INTO results (student_id, term, result_pdf) VALUES ('$student_id', '$term', '$file_name')";
    if ($conn->query($query)) {
        echo "<script>alert('Result uploaded successfully!');</script>";
    } else {
        echo "<script>alert('Error uploading result.');</script>";
    }
}
?>
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="styles.css">
    <title>Upload Student Results</title>
</head>
<body>
    <h2>Upload Student Result</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="text" name="student_id" placeholder="Enter Student ID" required>
        <select name="term">
            <option value="1st Term">1st Term</option>
            <option value="2nd Term">2nd Term</option>
        </select>
        <input type="file" name="result_pdf" accept=".pdf" required>
        <button type="submit">Upload</button>
    </form>
    <a href="logout.php">Logout</a>
</body>
</html>

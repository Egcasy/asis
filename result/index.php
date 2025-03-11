<?php
$conn = new mysqli("localhost", "root", "praise1800", "student_results");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $student_id = $_POST['student_id'];
    $term = $_POST['term'];

    $query = "SELECT * FROM results WHERE student_id = '$student_id' AND term = '$term'";
    $result = $conn->query($query);
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
<link rel="stylesheet" href="styles.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Result Portal</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        form { margin-top: 20px; }
        input, select, button { padding: 10px; margin: 5px; }
    </style>
</head>
<body>
    <h2>Check Your Result</h2>
    <form method="POST">
        <input type="text" name="student_id" placeholder="Enter Student ID" required>
        <select name="term">
            <option value="1st Term">1st Term</option>
            <option value="2nd Term">2nd Term</option>
        </select>
        <button type="submit">View Result</button>
    </form>

    <?php if (isset($result) && $result->num_rows > 0): ?>
        <h3>Your Result</h3>
        <?php while ($row = $result->fetch_assoc()): ?>
            <p><a href="uploads/<?php echo $row['result_pdf']; ?>" download>Download PDF</a></p>
        <?php endwhile; ?>
    <?php elseif (isset($result)): ?>
        <p>No results found!</p>
    <?php endif; ?>
</body>
</html>

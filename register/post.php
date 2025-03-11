<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'PHPMailer/PHPMailer.php';
require 'PHPMailer/SMTP.php';
require 'PHPMailer/Exception.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $surname = $_POST['surname'];
    $middle_name = $_POST['middle_name'];
    $last_name = $_POST['last_name'];
    $gender = $_POST['gender'];
    $dob = $_POST['dob'];
    $parent_phone = $_POST['parent_phone'];
    $guardian = $_POST['guardian'];
    $address = $_POST['address'];
    $email = $_POST['email'];
    $class = $_POST['class'];
    $subjects = isset($_POST['subject']) ? implode(", ", $_POST['subject']) : "None";

    // Handle uploaded files
    $student_photo = $_FILES['student_photo']['name'];
    $parent_photo = $_FILES['parents_photo']['name'];
    $upload_dir = "uploads/";

    move_uploaded_file($_FILES['student_photo']['tmp_name'], $upload_dir . $student_photo);
    move_uploaded_file($_FILES['parents_photo']['tmp_name'], $upload_dir . $parent_photo);

    // Create PHPMailer instance
    $mail = new PHPMailer(true);

    try {
        // SMTP Configuration
        $mail->isSMTP();
        $mail->Host = 'smtp.gmail.com'; // Change for Outlook, Yahoo, etc.
        $mail->SMTPAuth = true;
        $mail->Username = 'pikebuwa@gmail.com'; // Replace with your email
        $mail->Password = 'Praise1800@'; // Use an App Password if 2FA is enabled
        $mail->SMTPSecure = 'tls'; // Use 'ssl' for port 465
        $mail->Port = 587; // Port for TLS (use 465 for SSL)

        // Sender and Recipient
        $mail->setFrom('your-email@gmail.com', 'School Admin'); // Change sender email & name
        $mail->addAddress('your-email@gmail.com'); // Replace with your recipient email
        $mail->addReplyTo($email, "$surname $last_name");

        // Email Content
        $mail->isHTML(true);
        $mail->Subject = "New Student Registration";
        $mail->Body = "
            <h2>New Student Registration</h2>
            <p><strong>Name:</strong> $surname $middle_name $last_name</p>
            <p><strong>Gender:</strong> $gender</p>
            <p><strong>Date of Birth:</strong> $dob</p>
            <p><strong>Parent's Phone:</strong> $parent_phone</p>
            <p><strong>Guardian:</strong> $guardian</p>
            <p><strong>Address:</strong> $address</p>
            <p><strong>Email:</strong> $email</p>
            <p><strong>Class:</strong> $class</p>
            <p><strong>Subjects:</strong> $subjects</p>
            <p><strong>Student Photo:</strong> <a href='$upload_dir$student_photo'>View</a></p>
            <p><strong>Parent Photo:</strong> <a href='$upload_dir$parent_photo'>View</a></p>
        ";

        // Send email
        if ($mail->send()) {
            echo "<h2>Registration Successful</h2><p>Email Sent Successfully!</p>";
        } else {
            echo "<h2>Error!</h2><p>Email could not be sent.</p>";
        }
    } catch (Exception $e) {
        echo "<h2>Error!</h2><p>Message could not be sent. Mailer Error: {$mail->ErrorInfo}</p>";
    }
}
?>

<?php 
if ($_SERVER["REQUEST_METHOD"] == "POST") { 
    // Sanitize inputs using filter_input 
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING); 
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL); 
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING); 
    $age = filter_input(INPUT_POST, 'age', FILTER_SANITIZE_NUMBER_INT); 

 
    // Validate sanitized email 
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) { 
echo "<p>Invalid email format.</p>"; 
exit; 
} 
// Output the sanitized inputs 
echo "<h1>Submitted Data</h1>"; 
echo "<p><strong>Name:</strong> " . htmlspecialchars($name) . "</p>"; 
echo "<p><strong>Email:</strong> " . htmlspecialchars($email) . "</p>"; 
echo "<p><strong>Phone:</strong> " . htmlspecialchars($phone) . "</p>"; 
echo "<p><strong>Age:</strong> " . htmlspecialchars($age) . "</p>"; 
} 
?>
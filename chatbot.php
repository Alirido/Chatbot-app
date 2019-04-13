<!DOCTYPE html>
<html>
<head>
    <title>REGISTER</title>
    <link rel="stylesheet" type="text/css" href="chatbot.css" >
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">

</head>
<body>

    <div class="log_reg">

        <h1>REGISTER</h1>

        <form name="regis" method="POST" action="backend/_register.php">
            
            <table>
                <tr>
                    <td><label for="nm">Name</label></td>
                    <td><input type="text" name="nm" id="nm"></td>
                </tr>
                <tr id="show_nm_err" style="display: none">
                    <td></td>
                    <td id="nm_err" style="color:red"></td>
                </tr>
                <tr>
                    <td><label for="uname">Username</label></td>
                    <td><input type="text" name="uname" id="uname" style="width: 70%"><span id="unique_uname" style="display:none"></span></td>
                </tr>
                <tr id="show_uname_err">
                    <td></td>
                    <td id="uname_err" style="color:red"></td>
                </tr>
                <tr>
                    <td><label for="email">Email</label></td>
                    <td><input type="email" name="email" id="email" style="width: 70%"><span id="unique_email" style="display:none"></span></td>
                </tr>
                <tr id="show_email_err" style="display:none">
                    <td></td>
                    <td id="email_err" style="color:red"></td>
                </tr>
                <tr>
                    <td><label for="pwd1">Password</label></td>
                    <td><input type="Password" name="pwd1" id="pwd1"></td>
                </tr>
                <tr id="show_pwd1_err" style="display:none">
                    <td></td>
                    <td id="pwd1_err" style="color:red"></td>
                </tr>
                <tr>
                    <td><label for="pwd2">Confirm Password</label></td>
                    <td><input type="Password" name="pwd2" id="pwd2"></td>
                </tr>
                <tr id="show_pwd2_err" style="display:none">
                    <td></td>
                    <td id="pwd2_err" style="color:red"></td>
                </tr>
                <tr>
                    <td><label for="address">Address</label></td>
                    <td><textarea name="address" id="address"></textarea></td>
                </tr>
                <tr id="show_address_err" style="display:none">
                    <td></td>
                    <td id="address_err" style="color:red"></td>
                </tr>
                <tr>
                    <td><label for="p_num">Phone Number</label></td>
                    <td><input type="text" name="p_num" id="p_num"></td>
                </tr>
                <tr id="show_p_num_err" style="display:none">
                    <td></td>
                    <td id="p_num_err" style="color:red"></td>
                </tr>
                <tr>
                    <td><label for="c_num">Card Number</label></td>
                    <td><input type="text" name="c_num" id="c_num" style="width: 70%"><span id="valid_c_num" style="display:none"></span></td>
                </tr>
                <tr id="show_c_num_err">
                    <td></td>
                    <td id="c_num_err" style="color:red"></td>
                </tr>
            </table>
            <br>

            <a href="login.php">Already have an account?</a>
            <br><br>

            <input type="submit" name="register" value="REGISTER">
        
        </form>


       
    </div>
</body>
</html>
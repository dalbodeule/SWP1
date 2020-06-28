html = b"""
<!DOCTYPE HTML>
<html>
    <head>
        <title>11-1 Add/Mul of A and B</title>
    </head>
    <body>
        <form action="get">
            a = <input type="number" name="a" value="{valA}"><br>
            b = <input type="number" name="b" value="{valB}"><br>
            <input type="submit">Submit</input>
        </form>
        <hr>
        <div>
            A + B = <strong>{valAdd}</strong><br>
            A * B = <strong>{valMul}</strong>
        </div>
    </body>
</html>
"""

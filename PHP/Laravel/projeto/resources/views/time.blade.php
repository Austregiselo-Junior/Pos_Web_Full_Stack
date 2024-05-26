<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD</title>
</head>
<body>
     <h1>GET</h1>
         <form method='GET' action=/time>
        {{csrf_field() }}
         <p> 
            <p>Nome: {{ $nome}}</p>
            <p>Email: {{ $email}}</p>
        </p>
    </form>

    <h3>-----------------------------------------------------------</h3>
    <h1>POST</h1>
    <form method='POST' action=/time>
        {{csrf_field() }}
         <p>
            <p>
              <label for="nome">Nome do time:</label>
              <input type="text" id="nome" name="nome">
            </p>
            <p>
              <label for="email">E-mail:</label>
              <input type="text" id="email" name="email">
            </p>
        </p>
       <button type="submit">Enviar</button>
    </form>

      <h3>-----------------------------------------------------------</h3>
    <h1>PUT</h1>
    <form method='POST' action=/time>
        {{csrf_field() }}
         <p>
            <p>
                <label for="nome">Nome do time:</label>
                <input type="text" id="nome" name="nome">
            </p>
             <p>
                <label for="email">E-mail:</label>
                <input type="text" id="email" name="email">
            </p>
        </p>
            <button type="submit">Update</button>
    </form>

      <h3>-----------------------------------------------------------</h3>
    <h1>DELETE</h1>
    <form method='POST' action=/time>
        <button type="submit">Delete</button>
    </form>
</body>
</html>
<html>
    <body>
        <form method='POST' action=/contato>
           {{csrf_field() }}
            Nome: <input type='text'  name='nome' />
            email <input type='text' name='email' />
            <input type='submit' value='enviar'/>
        </form> 
    </body>
</html>
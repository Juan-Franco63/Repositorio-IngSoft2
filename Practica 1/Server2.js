const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Respuesta desde servidor 2 en puerto 3001');
});

app.listen(3001, () => {
    console.log('Servidor 2 corriendo en puerto 3001');
});

const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Respuesta desde servidor 1 en puerto 3000');
});

app.listen(3000, () => {
    console.log('Servidor 1 corriendo en puerto 3000');
});

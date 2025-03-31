//INTEGRANTES
// Juan Pablo Franco Herrera
// Santiago Collantes Nieto
// Fernando Salazar Serrano

const express = require('express');
const app = express();
const port = 3001;

app.get('/', (req, res) => {
    res.send('Hello from Server 1!');
});

app.listen(port, () => {
    console.log(`Server 1 listening at http://localhost:${port}`);
});

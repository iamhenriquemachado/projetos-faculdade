const express = require('express')
const app = express()

const PORT = process.env.PORT || 3000

app.get('/', (req, res) => {
    res.send(`API is running on port: ${PORT}`)
})

app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});
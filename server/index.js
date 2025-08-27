const express = require('express')
const bodyParser = require('body-parser')

const app = express()
const PORT = process.env.PORT || 3000
const HOST = process.env.HOST || 'localhost'

// Middleware
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))

// Routes
app.get('/', (req, res) => {
  res.json({ 
    message: 'Hello from Express server!',
    timestamp: new Date().toISOString(),
    host: HOST,
    port: PORT
  })
})

app.get('/health', (req, res) => {
  res.json({ status: 'OK', uptime: process.uptime() })
})

// Start server
app.listen(PORT, HOST, () => {
  console.log(`Server running at http://${HOST}:${PORT}`)
  console.log(`Environment: ${process.env.NODE_ENV || 'development'}`)
})

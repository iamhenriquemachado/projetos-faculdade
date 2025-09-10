require('dotenv').config()
const sql = require('mssql')


const databaseUser = process.env.DB_USER
const databasePassword = process.env.DB_PASSWORD
const databasesServer = process.env.DB_SERVER_HOST
const databaseSchema = process.env.DATABASE


const config = {
    user: databaseUser,
    password: databasePassword, 
    server: databasesServer, 
    database: databaseSchema, 
    options: {
        encrypt: false,
    }

}
async function connectToSqlServer() {
    try {
        await sql.connect(config)
        console.log("Connected to SQL server successfully!");

        const result = await sql.query`SELECT @@VERSION`;
        console.dir(result.recordset)

    } catch(err) {
        console.error('Error connecting to SQL Server:', err)
    } finally {
        if(sql.pool) {
            await sql.close()
            console.log("SQL connection successfully closed.")
        }
    }
}


connectToSqlServer();
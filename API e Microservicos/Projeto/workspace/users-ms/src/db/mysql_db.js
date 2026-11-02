import { sequelize } from "./instances/mysql.js";

export const connectDB = async() => {
    try{
        await sequelize.sync();
        console.log(`Connected in database: ${process.env.MYSQL_DB_NAME}`);
    }catch(error){
        console.log(`Error: ${error.message}`);
        process.exit(1);
    }
}
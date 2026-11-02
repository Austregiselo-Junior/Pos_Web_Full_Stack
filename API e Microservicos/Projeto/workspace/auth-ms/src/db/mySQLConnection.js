import { sequelize } from "./instance/mySQLModel.js";

export const connectDB = async() => {
    try{
        await sequelize.sync();
        console.log(`Connected in database: ${process.env.MYSQL_DB_NAME}`);
    }catch(error){
        console.log(`Error connected: ${error.message}`);
        process.exit(1);
    }
}
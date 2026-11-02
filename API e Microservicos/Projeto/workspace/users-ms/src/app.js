import express from 'express';
import { connectDB } from './db/mysql_db.js';
import UserRoutes from "./routes/UserRoutes.js";
import axios from 'axios';

const app = express();

app.use(express.json());

app.use(UserRoutes);

const registerService = async()=>{
    try{
        await axios.post(`${process.env.SERVICE_REGISTRY_URL}/register`, {
            name: process.env.APP_NAME,
            url: `http://localhost:${process.env.PORT}`
        });
        console.log("Service Registered Sucessfully");
    }catch(error){
        console.error(`Error - ${error.message}`);
    }
}

connectDB().then(()=>{
    app.listen(process.env.PORT, ()=>{
        console.log(`App running on ${process.env.PORT}`);
    });
    registerService();
});
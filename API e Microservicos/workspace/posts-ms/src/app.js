import express from 'express';
import { connectDB } from './db/mysql_db.js';
import PostRoutes from "./routes/PostRoutes.js"

const app = express();

app.use(express.json());
app.use(PostRoutes);

connectDB().then(()=>{
    app.listen(process.env.PORT, ()=>{
        console.log(`App running on ${process.env.PORT}`);
    });
});
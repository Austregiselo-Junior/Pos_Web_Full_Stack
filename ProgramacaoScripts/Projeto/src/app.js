import express from "express";
import connectDB from "./db/db.js";
import UserRoutes from "./routes/UserRoutes.js"
import ProductRoutes from "./routes/ProductRoutes.js"

const app = express();
app.use(express.json());

// Define que todas as rotas iniciadas com "/users" serão tratadas pelas rotas definidas em 'UserRoutes'
app.use("/users", UserRoutes);

// Define que todas as rotas iniciadas com "/products" serão tratadas pelas rotas definidas em 'ProductRoutes'
app.use("/products", ProductRoutes);


connectDB().then(()=>{
    app.listen(process.env.PORT, ()=>{
        console.log(`Server listen in port ${process.env.PORT}`);
    });
});


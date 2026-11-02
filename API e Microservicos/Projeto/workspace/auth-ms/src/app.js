import express from "express";
import authRoutes from "./routes/authRoute.js";
import axios from "axios";

const app = express();
app.use(express.json());

app.use(authRoutes);

const registerService = async () => {
    try {
        await axios.post(`${process.env.SERVICE_REGISTRY_URL}/register`, {
            name: process.env.APP_NAME,
            url: `http://localhost:${process.env.PORT}`
        });
        console.log("Registered Sucessfully");
    } catch(error) {
        console.log(`ERROR - ${error.message}`);
    }
}

app.listen(process.env.PORT, () => {
    console.log(`Server run in port: ${process.env.PORT}`);
});
registerService();

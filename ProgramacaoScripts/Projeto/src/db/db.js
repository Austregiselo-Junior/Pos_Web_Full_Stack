import mongoose from "mongoose";

const connectDB = async() => {
    try{
        const conn = await mongoose.connect(process.env.MONGO_URL);
        console.log(`MongoDB connected: ${conn.connection.db.namespace}`);
    }catch(error){
        console.log(error);
        process.exit(1);
    }
}

export default connectDB;
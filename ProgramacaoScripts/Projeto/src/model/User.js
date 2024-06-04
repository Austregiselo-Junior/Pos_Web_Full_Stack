import mongoose from "mongoose";
import { Schema } from "mongoose";

const User = mongoose.model(
    "User",
    new Schema({
       name:{
        type: String,
        required: true,
        maxlength: 80
       },
       email:{
        type: String,
        required: true
       },
       password:{
        type: String,
        required: true
       },
       phone:{
        type:String,
        required: true
       },
       image: String,
       address:{
        type:String,
        required: true
       }
    },{timestamps: true})
);

export default User;
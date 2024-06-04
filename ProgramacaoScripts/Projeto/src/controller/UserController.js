import { createUserToken } from "../helpers/manager-jwt.js";
import UserService from "../service/UserService.js";

export default class UserController{
    static async register(req, res){
        try{
            const {name, email, password, confirmPassword, phone, address} = req.body;

            const user = await UserService.register(name, email, password, confirmPassword, phone, address);

            const token = createUserToken(user);

            res.status(201).json({token: token, userId: user._id});
        }catch(error){
            error.statusCode = error.statusCode || 500;
            res.status(error.statusCode).json({error: error.message});
        }
    }

    static async login(req, res){
        try{
            const {email, password} = req.body;

            const user = await UserService.verifyLogin(email, password);

            const token = createUserToken(user);

            res.status(200).json({token, userId: user._id});
        }catch(error){
            error.statusCode = error.statusCode || 500;
            res.status(error.statusCode).json({error: error.message});
        }
    }

    //req.user
    static async getUser(req, res){
        try{
            const user = await UserService.getUser(req);

            res.status(200).json({user});
        }catch(error){
            error.statusCode = error.statusCode || 500;
            res.status(error.statusCode).json({error: error.message});
        }
    }

    static async updateUser(req, res){
        try{
            const {name, email, password, confirmPassword, phone, address} = req.body;

            const user = await UserService.updateUser(req, name, email, password, confirmPassword, phone, address);

            res.status(200).json({user});
        }catch(error){
            error.statusCode = error.statusCode || 500;
            res.status(error.statusCode).json({error: error.message});
        }
    }
}
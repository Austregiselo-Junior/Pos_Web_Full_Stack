import { PostModel } from "../model/PostModel.js";

export class PostController{
    static async findAll(req, res){
        try{
            const posts = await PostModel.findAll();
            res.status(200).json({posts});
        }catch(error){
            res.status(500).json({message: error.message});
        }
    }

    static async save(req, res){
        try{
            const {title, user_id} = req.body;
            const post = await PostModel.create({title, user_id});
            res.status(201).json({post});
        }catch(error){
            res.status(500).json({message: error.message});
        }
    }

    static async findByUserId(req, res){
        try{
            const {id} = req.params;
            const post = await PostModel.findAll({where:{user_id: id}});
            res.status(200).json({post});
        }catch(error){
            res.status(500).json({message: error.message});
        }
    }
}
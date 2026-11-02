import { where } from "sequelize";
import { Post } from "../model/post.js";

export class PostController{
    static async findAll(req, res){
        try {
            const post = await Post.findAll();
            res.status(200).json({post});
        } catch (error) {
            res.status(500).json({message: error.message});
        }
    }

    static async save(req, res){
          try {
            const {title, user_id} = req.body;
            const post = await Post.create({user_id, title});
            res.status(200).json({post});
        } catch (error) {
            res.status(500).json({message: error.message});
        }
    }

    static async findUserById(req, res){
          try {
            const {id} = req.params;
            const post = await Post.findAll({where:{user_id: id}})
            res.status(200).json({post});
            
        } catch (error) {
            res.status(500).json({message: error.message});
        }
    }
}
import { User } from "../model/user.js";
import bcrypt from 'bcrypt';
import axios from 'axios';

export class UserController{
    static async findAll(req, res){
        try {
            const users = await User.findAll({attributes:{exclude:['password']}});

            const userAndPosts = await Promise.all(
                users.map(async(user)=>{
                    try {
                          const response = await axios.get(`${process.env.POSTS_SERVICE_URL}/posts/user/${user.id}`);
                          const post = response.data.post;

                         return{
                              user,
                             posts: post
                         }
                    } catch (error) {
                         console.log(`Error: ${error.message}`);
                        return {
                            user,
                            posts: []
                        }
                    }
                })
            );
            res.status(200).json({users:userAndPosts});
        } catch (error) {
            res.status(500).json({message: error.message});
        }
    }

    static async save(req, res){
          try {
            const {username, password} = req.body;

            const hashPassword = await bcrypt.hash(password,10);
            const user = await User.create({username, password:hashPassword});

            const result = user.get({plain: true}); // plain serve pra pegar só o usuário
            delete result.password;

            res.status(200).json({user: result});
        } catch (error) {
            res.status(500).json({message: error.message});
        }
    }

    static async findUserByName(req, res){
          try {
            const {username} = req.params;
            const user = await User.findOne({where:{username}});

            res.status(200).json({user});
        } catch (error) {
            res.status(500).json({message: error.message});
        }
    }
}
import axios from 'axios';
import jwt from "jsonwebtoken";
import bcrypt from "bcrypt";


export class authController {

    static async login(req, res) {
        try{
            const {username, password} = req.body;

            userPasswordValidation(username, password);

            const user = await userValidation(username);

            await passwordValidation(password, user);

            const token = await getTokenByID(user);

            res.status(200).json({token});
        }catch(error){
            res.status(500).json({message: error.message});
        }

        async function getTokenByID(user) {
              return jwt.sign({ id: user.id }, process.env.PRIVATE_KEY, {
                  expiresIn: '1h'
              });
        }
      
        async function passwordValidation(password, user) {
            const isPasswordHash = await bcrypt.compare(password, user.password);
            if (!isPasswordHash) {
                res.status(401).json({ message: "Invalid login or password." });
            }
        }

        async function userValidation(username) {
            try {
                const response = await axios.get(`${process.env.SERVICE_GATEWAY_URL}/${process.env.USER_SERVICE_NAME}/users/${username}`);
                const user = response.data.user;
                if (!user) {
                    res.status(404).json({ message: "User nor found" });
                }
                return user;
            } catch (error) {
                 throw error;
            }
        }

        function userPasswordValidation(username, password) {
            if (!username && !password) {
                res.status(422).json({ message: "The login and password fields are mandatory." });
            }
        }
    }
    
}
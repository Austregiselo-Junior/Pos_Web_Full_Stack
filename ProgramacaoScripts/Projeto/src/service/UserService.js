import User from "../model/User.js";
import bcrypt from "bcrypt";

export default class UserService{
    static async register(name, email, password, confirmPassword, phone, address){
        if(!name){
            const error = new Error("O nome é obrigatório");
            error.statusCode = 422;
            throw error;
        }

        if(!email){
            const error = new Error("O email é obrigatório");
            error.statusCode = 422;
            throw error;
        }

        if(!password){
            const error = new Error("A senha é obrigatória");
            error.statusCode = 422;
            throw error;
        }

        if(!phone){
            const error = new Error("O telefone é obrigatório");
            error.statusCode = 422;
            throw error;
        }

        if(!address){
            const error = new Error("O endereço é obrigatório");
            error.statusCode = 422;
            throw error;
        }

        if(!confirmPassword){
            const error = new Error("A confirmação de senha é obrigatório");
            error.statusCode = 422;
            throw error;
        }

        if(password !== confirmPassword){
            const error = new Error("A senha e confirmação de senha devem ser iguais");
            error.statusCode = 422;
            throw error;
        }

        const userExists = await User.findOne({email});

        if(userExists){
            const error = new Error("Por favor, utilize outro e-mail");
            error.statusCode = 422;
            throw error;
        }

        const salt = await bcrypt.genSalt(12);
        const passwordHash = await bcrypt.hash(password, salt);

        const user = new User({name, email, password: passwordHash, address, phone});
        const userSaved = await user.save();

        return userSaved;
    }

    static async verifyLogin(email, password){
        this.verify_field(email, "O email é obrigatório.", 422);
        this.verify_field(password, "A senha é obrigatoria.", 422);

        const user = await User.findOne({email});

        this.verify_field(user, "Login ou senha inválida", 401);

        const passwordHash = await bcrypt.compare(password, user.password);

        this.verify_field(passwordHash, "Login ou senha inválida", 401);

        return user;
    }

    static async getUser(req){
        const user = await User.findById(req.user.id).select("-password");

        if(!user){
            const error = new Error("Token inválido.");
            error.statusCode = 498;
            throw error;
        }

        return user;
    }

    static async updateUser(req, name, email, password, confirmPassword, phone, address){
        const user = await this.getUser(req);
    
        if(req.file){
            user.image = req.file.filename;
        }

        if(!name){
            const error = new Error("O nome é obrigatório.");
            error.statusCode = 422;
            throw error;
        }

        user.name = name;

        if(!phone){
            const error = new Error("O telefone é obrigatório.");
            error.statusCode = 422;
            throw error;
        }

        user.phone = phone;

        if(!address){
            const error = new Error("O endereço é obrigatório.");
            error.statusCode = 422;
            throw error;
        }

        user.address = address;

        if(!email){
            const error = new Error("O email é obrigatório.");
            error.statusCode = 422;
            throw error;
        }

        const userExists = await User.findOne({email});

        if(user.email !== email && userExists){
            const error = new Error("Por favor, informe outro e-mail");
            error.statusCode = 422;
            throw error;
        }

        user.email = email;

        if(!password){
            const error = new Error("A senha é obrigatória.");
            error.statusCode = 422;
            throw error;
        }

        if(!confirmPassword){
            const error = new Error("A confirmação de senha é obrigatória.");
            error.statusCode = 422;
            throw error;
        }

        if(password !== confirmPassword){
            const error = new Error("A senha precisa ser igual a confirmação de senha.");
            error.statusCode = 422;
            throw error;
        }else if(password === confirmPassword && password != null){
            const salt = await bcrypt.genSalt(12);
            const passwordHash = await bcrypt.hash(password, salt);

            user.password = passwordHash;
        }

        const updatedUser = await User.findByIdAndUpdate(user._id, user, {new:true}).select("-password");

        return updatedUser;
    }

    static verify_field(field, message, statusCode){
        if(!field){
            const error = new Error(message);
            error.statusCode = statusCode;
            throw error;
        }
    }
    
}
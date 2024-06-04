import jwt from "jsonwebtoken";

export const createUserToken = (user) => {
    const token = jwt.sign({
        name: user.name,
        id: user._id
    }, process.env.PRIVATE_KEY);

    return token;
}

export const verifyJwt = (req, res, next) => {
    const authHeader = req.headers.authorization;
    const token = authHeader?.split(" ")[1];

    if(!token){
        res.status(401).json({error: "Não Autorizado."});
        return;
    }

    try{
        const payload = jwt.verify(token, process.env.PRIVATE_KEY);
        req.user = payload;

        next();
    }catch(error){
        res.status(498).json({error: "Token inválido."});
        return;
    }
}
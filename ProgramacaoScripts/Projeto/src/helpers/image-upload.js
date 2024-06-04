import multer from "multer";
import path from "path";

const imageStore = multer.diskStorage({
    destination: (req, file, cb) => {
        let folder = "";

        if(req.baseUrl.includes("users")){
            folder = "users";
        }else if(req.baseUrl.includes("products")){
            folder = "products";
        }

        cb(null, `src/public/images/${folder}`);
    },
    filename: (req, file, cb) => {
        cb(null, Date.now()+Math.floor(Math.random() * 1000) + path.extname(file.originalname));
    }
});

const imageUpload = multer({
    storage:imageStore,
    fileFilter(req, file, cb){
        if(!file.originalname.match(/\.(png|jpg)$/)){
            return cb(new Error("Por favor, envie uma imagem jpg ou png"));
        }
        cb(undefined, true);
    }
});

export default imageUpload;
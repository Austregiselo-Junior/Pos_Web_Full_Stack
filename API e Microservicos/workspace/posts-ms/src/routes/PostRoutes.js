import {Router} from 'express';
import { PostController } from '../Controller/PostController.js';

// Rotas para users
const router = Router();
router.get("/posts", PostController.findAll);
router.post("/posts", PostController.save);
router.get("/posts/user/:id", PostController.findUserById);

export default router;
import { Router } from "express";
import { PostController } from "../controller/PostController.js";
import { authentication } from "../middleware/authentication.js";

const router = Router();

router.get("/posts", authentication, PostController.findAll);
router.get("/posts/user/:id", authentication, PostController.findByUserId);
router.post("/posts", authentication, PostController.save);

export default router;